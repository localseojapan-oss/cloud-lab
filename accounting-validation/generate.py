"""弥生会計と自社開発会計システム（ちょうざいむ）の並行入力テスト用仕訳データ生成スクリプト。

同じ仕訳定義 (VOUCHERS) から以下を出力する。
  output/journal_canonical.csv        ちょうざいむ投入用（1明細1行、UTF-8 BOM付き）
  output/yayoi_import.csv             弥生会計インポート用（仕訳日記帳形式、Shift_JIS、ヘッダーなし）
  output/expected_trial_balance.csv   期待値: 勘定科目別の試算表
  output/expected_sub_accounts.csv    期待値: 補助科目別残高
  output/expected_tax_summary.csv     期待値: 税区分別集計

前提: 税込経理方式、期首残高ゼロ（設立初月）、消費税額は税込金額から逆算し1円未満切り捨て。
"""

import csv
from collections import defaultdict
from pathlib import Path

OUT = Path(__file__).parent / "output"

# 勘定科目マスタ: 科目名 -> 区分（資産/負債/純資産 は B/S、収益/費用 は P/L）
ACCOUNTS = {
    "現金": "資産",
    "普通預金": "資産",
    "売掛金": "資産",
    "工具器具備品": "資産",
    "買掛金": "負債",
    "未払金": "負債",
    "預り金": "負債",
    "長期借入金": "負債",
    "資本金": "純資産",
    "売上高": "収益",
    "受取利息": "収益",
    "仕入高": "費用",
    "給料手当": "費用",
    "法定福利費": "費用",
    "地代家賃": "費用",
    "消耗品費": "費用",
    "旅費交通費": "費用",
    "交際費": "費用",
    "会議費": "費用",
    "通信費": "費用",
    "支払手数料": "費用",
    "租税公課": "費用",
    "保険料": "費用",
    "減価償却費": "費用",
    "支払利息": "費用",
}
DEBIT_NORMAL = {"資産", "費用"}

# 税区分: 汎用コード -> (弥生の税区分名, 税率%)
# 弥生の税区分名はバージョンやインボイス設定で異なる場合がある（例: 「課対仕入込10%適格」）。
# 取込エラーになる場合はここの名称を自社の弥生の設定に合わせて変更する。
TAX = {
    "SALES_10": ("課税売上込10%", 10),
    "SALES_8R": ("課税売上込軽減8%", 8),
    "SALES_RETURN_10": ("課税売返込10%", 10),
    "EXPORT": ("輸出売上", 0),
    "NONTAX_SALES": ("非課売上", 0),
    "PURCHASE_10": ("課対仕入込10%", 10),
    "PURCHASE_8R": ("課対仕入込軽減8%", 8),
    "NONTAX_PURCHASE": ("非課仕入", 0),
    "OUT_OF_SCOPE": ("対象外", 0),
}


def tax_amount(amount, code):
    rate = TAX[code][1]
    return amount * rate // (100 + rate) if rate else 0


def side(account, amount, tax="OUT_OF_SCOPE", sub="", dept=""):
    return {"account": account, "sub": sub, "dept": dept, "tax": tax, "amount": amount}


# 伝票定義。rows は弥生の1行（借方, 貸方）単位。複合仕訳で片側が空の行は None。
# check は「何を確認するための仕訳か」。
VOUCHERS = [
    dict(no=1, date="2026/04/01", memo="資本金払込", check="対象外取引・補助科目付き預金",
         rows=[(side("普通預金", 10_000_000, sub="みずほ銀行"), side("資本金", 10_000_000))]),
    dict(no=2, date="2026/04/01", memo="事務所家賃 4月分", check="課税仕入10%・部門",
         rows=[(side("地代家賃", 220_000, "PURCHASE_10", dept="本社"), side("普通預金", 220_000, sub="みずほ銀行"))]),
    dict(no=3, date="2026/04/01", memo="損害保険料 4月分", check="非課税仕入",
         rows=[(side("保険料", 12_000, "NONTAX_PURCHASE", dept="本社"), side("普通預金", 12_000, sub="みずほ銀行"))]),
    dict(no=4, date="2026/04/03", memo="小口現金引出", check="資金移動（損益・税に影響しない）",
         rows=[(side("現金", 300_000), side("普通預金", 300_000, sub="みずほ銀行"))]),
    dict(no=5, date="2026/04/05", memo="文具購入", check="消費税の端数処理（1,099円→税99.9円）",
         rows=[(side("消耗品費", 1_099, "PURCHASE_10", dept="本社"), side("現金", 1_099))]),
    dict(no=6, date="2026/04/05", memo="来客用飲料", check="軽減税率8%仕入・同日複数伝票",
         rows=[(side("会議費", 1_079, "PURCHASE_8R", dept="営業部"), side("現金", 1_079))]),
    dict(no=7, date="2026/04/08", memo="商品仕入 D卸", check="掛仕入・補助科目",
         rows=[(side("仕入高", 550_000, "PURCHASE_10"), side("買掛金", 550_000, sub="D卸"))]),
    dict(no=8, date="2026/04/10", memo="商品売上 A商事", check="課税売上10%・掛売",
         rows=[(side("売掛金", 1_100_000, sub="A商事"), side("売上高", 1_100_000, "SALES_10", dept="営業部"))]),
    dict(no=9, date="2026/04/10", memo="食品売上 B物産", check="軽減税率8%売上",
         rows=[(side("売掛金", 324_000, sub="B物産"), side("売上高", 324_000, "SALES_8R", dept="営業部"))]),
    dict(no=10, date="2026/04/12", memo="仕入 D卸（10%・8%混在請求書）", check="1伝票内で税率混在の複合仕訳",
         rows=[(side("仕入高", 110_000, "PURCHASE_10"), side("買掛金", 164_000, sub="D卸")),
               (side("仕入高", 54_000, "PURCHASE_8R"), None)]),
    dict(no=11, date="2026/04/15", memo="輸出売上 C社", check="輸出免税売上",
         rows=[(side("売掛金", 2_000_000, sub="海外C社"), side("売上高", 2_000_000, "EXPORT", dept="営業部"))]),
    dict(no=12, date="2026/04/15", memo="収入印紙", check="不課税（対象外）経費",
         rows=[(side("租税公課", 200, dept="本社"), side("現金", 200))]),
    dict(no=13, date="2026/04/18", memo="手土産,株式会社E様訪問", check="摘要内のカンマ（CSVエスケープ）・軽減8%",
         rows=[(side("交際費", 5_400, "PURCHASE_8R", dept="営業部"), side("現金", 5_400))]),
    dict(no=14, date="2026/04/20", memo="売上値引 A商事", check="売上返還（借方の売上高）",
         rows=[(side("売上高", 33_000, "SALES_RETURN_10", dept="営業部"), side("売掛金", 33_000, sub="A商事"))]),
    dict(no=15, date="2026/04/22", memo="出張交通費", check="端数処理（12,345円→税1,122.27円）",
         rows=[(side("旅費交通費", 12_345, "PURCHASE_10", dept="営業部"), side("現金", 12_345))]),
    dict(no=16, date="2026/04/25", memo="4月分給与", check="1対多の複合仕訳・預り金の補助科目",
         rows=[(side("給料手当", 400_000, dept="本社"), side("預り金", 10_000, sub="源泉所得税")),
               (None, side("預り金", 15_000, sub="住民税")),
               (None, side("預り金", 57_000, sub="社会保険料")),
               (None, side("普通預金", 318_000, sub="みずほ銀行"))]),
    dict(no=17, date="2026/04/25", memo="社会保険料 会社負担分", check="未払計上",
         rows=[(side("法定福利費", 57_000, dept="本社"), side("未払金", 57_000))]),
    dict(no=18, date="2026/04/28", memo="A商事 入金（振込手数料差引）", check="多対1の複合仕訳・手数料の税区分",
         rows=[(side("普通預金", 1_066_340, sub="三井住友銀行"), side("売掛金", 1_067_000, sub="A商事")),
               (side("支払手数料", 660, "PURCHASE_10", dept="営業部"), None)]),
    dict(no=19, date="2026/04/28", memo="ノートPC購入", check="資産計上の課税仕入",
         rows=[(side("工具器具備品", 198_000, "PURCHASE_10"), side("未払金", 198_000))]),
    dict(no=20, date="2026/04/30", memo="D卸 買掛金支払（4/8分）", check="買掛金の消込",
         rows=[(side("買掛金", 550_000, sub="D卸"), side("普通預金", 550_000, sub="みずほ銀行"))]),
    dict(no=21, date="2026/04/30", memo="預金利息", check="1円の取引・非課税売上",
         rows=[(side("普通預金", 1, sub="みずほ銀行"), side("受取利息", 1, "NONTAX_SALES"))]),
    dict(no=22, date="2026/04/30", memo="借入金利息", check="非課税仕入（利息）",
         rows=[(side("支払利息", 3_456, "NONTAX_PURCHASE"), side("普通預金", 3_456, sub="三井住友銀行"))]),
    dict(no=23, date="2026/04/30", memo="減価償却費 4月分", check="直接法の償却・対象外",
         rows=[(side("減価償却費", 5_500, dept="本社"), side("工具器具備品", 5_500))]),
    dict(no=24, date="2026/04/30", memo="通信費 4月分", check="端数処理（99,999円→税9,090.81円）",
         rows=[(side("通信費", 99_999, "PURCHASE_10", dept="本社"), side("未払金", 99_999))]),
    dict(no=25, date="2026/04/30", memo="事務用品一式購入（コピー用紙・トナー・ファイル・封筒等）本社総務", check="摘要の文字数上限（全角32文字）",
         rows=[(side("消耗品費", 3_300, "PURCHASE_10", dept="本社"), side("現金", 3_300))]),
    dict(no=26, date="2026/04/30", memo="長期借入金 実行", check="8桁の大口金額",
         rows=[(side("普通預金", 99_999_999, sub="三井住友銀行"), side("長期借入金", 99_999_999))]),
]


def lines():
    """伝票を借方・貸方の明細単位に展開する。"""
    for v in VOUCHERS:
        n = 0
        for dr, cr in v["rows"]:
            for label, s in (("借方", dr), ("貸方", cr)):
                if s is None:
                    continue
                n += 1
                yield v, n, label, s


def validate():
    for v in VOUCHERS:
        dr = sum(r[0]["amount"] for r in v["rows"] if r[0])
        cr = sum(r[1]["amount"] for r in v["rows"] if r[1])
        assert dr == cr, f"伝票{v['no']} 貸借不一致: {dr} != {cr}"
        for pair in v["rows"]:
            for s in pair:
                if s:
                    assert s["account"] in ACCOUNTS, f"伝票{v['no']} 未登録科目: {s['account']}"
                    assert s["tax"] in TAX
        assert len(v["memo"]) <= 32, f"伝票{v['no']} 摘要が32文字超"


def write_canonical():
    with open(OUT / "journal_canonical.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["伝票番号", "明細番号", "日付", "貸借", "勘定科目", "補助科目", "部門",
                    "税区分コード", "税区分(弥生名)", "税率", "金額(税込)", "消費税額", "摘要", "確認観点"])
        for v, n, label, s in lines():
            name, rate = TAX[s["tax"]]
            w.writerow([v["no"], n, v["date"], label, s["account"], s["sub"], s["dept"],
                        s["tax"], name, rate, s["amount"], tax_amount(s["amount"], s["tax"]),
                        v["memo"], v["check"]])


def yayoi_side(s):
    if s is None:
        return ["", "", "", "", "", ""]
    return [s["account"], s["sub"], s["dept"], TAX[s["tax"]][0], s["amount"], tax_amount(s["amount"], s["tax"])]


def write_yayoi():
    # 弥生インポート形式（25項目）。識別フラグ: 2000=単一行, 2110=複数行の先頭, 2100=中間, 2101=最終。
    with open(OUT / "yayoi_import.csv", "w", encoding="cp932", newline="") as f:
        w = csv.writer(f, lineterminator="\r\n")
        for v in VOUCHERS:
            rows = v["rows"]
            for i, (dr, cr) in enumerate(rows):
                if len(rows) == 1:
                    flag = "2000"
                elif i == 0:
                    flag = "2110"
                elif i == len(rows) - 1:
                    flag = "2101"
                else:
                    flag = "2100"
                w.writerow([flag, v["no"], "", v["date"], *yayoi_side(dr), *yayoi_side(cr),
                            v["memo"], "", "", "0", "", "", "0", "0", "no"])


def write_expected():
    dr_total, cr_total = defaultdict(int), defaultdict(int)
    sub_dr, sub_cr = defaultdict(int), defaultdict(int)
    tax_amt, tax_tax, tax_cnt = defaultdict(int), defaultdict(int), defaultdict(int)
    for v, n, label, s in lines():
        key = s["account"]
        (dr_total if label == "借方" else cr_total)[key] += s["amount"]
        if s["sub"]:
            (sub_dr if label == "借方" else sub_cr)[(key, s["sub"])] += s["amount"]
        if s["tax"] != "OUT_OF_SCOPE":
            tax_amt[s["tax"]] += s["amount"]
            tax_tax[s["tax"]] += tax_amount(s["amount"], s["tax"])
            tax_cnt[s["tax"]] += 1

    def balance(account, dr, cr):
        return dr - cr if ACCOUNTS[account] in DEBIT_NORMAL else cr - dr

    with open(OUT / "expected_trial_balance.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["区分", "勘定科目", "借方合計", "貸方合計", "残高"])
        for account, kind in ACCOUNTS.items():
            dr, cr = dr_total[account], cr_total[account]
            if dr or cr:
                w.writerow([kind, account, dr, cr, balance(account, dr, cr)])
        w.writerow(["", "合計", sum(dr_total.values()), sum(cr_total.values()), ""])
        revenue = sum(balance(a, dr_total[a], cr_total[a]) for a, k in ACCOUNTS.items() if k == "収益")
        expense = sum(balance(a, dr_total[a], cr_total[a]) for a, k in ACCOUNTS.items() if k == "費用")
        w.writerow(["", "当期純損益(収益-費用)", "", "", revenue - expense])

    with open(OUT / "expected_sub_accounts.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["勘定科目", "補助科目", "借方合計", "貸方合計", "残高"])
        for key in sorted(set(sub_dr) | set(sub_cr), key=lambda k: (list(ACCOUNTS).index(k[0]), k[1])):
            dr, cr = sub_dr[key], sub_cr[key]
            w.writerow([*key, dr, cr, balance(key[0], dr, cr)])

    with open(OUT / "expected_tax_summary.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["税区分コード", "税区分(弥生名)", "明細件数", "金額(税込)合計", "消費税額合計"])
        for code, (name, _) in TAX.items():
            if tax_cnt[code]:
                w.writerow([code, name, tax_cnt[code], tax_amt[code], tax_tax[code]])

    assert sum(dr_total.values()) == sum(cr_total.values())


if __name__ == "__main__":
    validate()
    OUT.mkdir(exist_ok=True)
    write_canonical()
    write_yayoi()
    write_expected()
    print(f"{len(VOUCHERS)}伝票 / {sum(1 for _ in lines())}明細を出力しました: {OUT}")
