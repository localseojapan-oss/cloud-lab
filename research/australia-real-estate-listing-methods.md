# オーストラリア不動産サイトの物件紹介手法 調査レポート

調査日: 2026-09-18
調査対象: 大手ポータル（realestate.com.au / Domain）、大手エージェント（Ray White、McGrath、Belle Property、LJ Hooker、The Agency など）、業界メディア・州政府の広告規制。
注記: 調査環境のネットワーク制限により、エージェント各社サイトの直接取得はできず、検索結果・業界記事・ポータルのヘルプ記事・各州の規制文書をもとに整理した。

---

## 1. 全体像: 「エージェントサイト」より「2大ポータル」が主戦場

- オーストラリアでは物件探しの起点が **realestate.com.au（REA Group）** と **Domain** の2大ポータルにほぼ集約されている。エージェント（不動産屋）の自社サイトは、ポータルに載せた物件を CRM から自動連携して表示する構造が基本。
- 業界標準のデータ形式 **REAXML** で CRM → ポータル → 自社サイトへ配信するため、物件情報の項目・構造（価格表示、販売方式、内見時間、写真、間取り図、エージェント情報）はサイトをまたいでほぼ共通化されている。
- したがって「物件紹介の手法」は、(a) ポータルの掲載枠と表示ルール、(b) 州ごとの価格広告規制、(c) エージェントが用意するメディア・キャンペーン、の3層で理解すると分かりやすい。

---

## 2. 販売方式（Method of Sale）が物件ページの「顔」になる

日本の「売買価格を提示して交渉」と違い、オーストラリアでは販売方式そのものが見出し級の情報として掲載される。主に4種類。

| 方式 | 概要 | 物件ページでの見せ方 |
|---|---|---|
| **Auction（オークション）** | 3〜4週間のキャンペーン後、指定日時に公開競売。落札即成立、クーリングオフなし、頭金（通常10%）即日 | 「Auction Sat 10 Oct 11:00am」「Auction unless sold prior」「Forthcoming Auction」など日時を前面に。オンライン/ライブ配信のリンクを併記 |
| **Private Treaty（一般売買）** | 最も一般的。希望価格を提示し、書面オファーで交渉 | 「$1,250,000」「$1.2M–$1.3M」「Price Guide $950,000」など |
| **Expressions of Interest / Tender（EOI・入札）** | 高級物件・開発用地など値付けが難しい物件向け。締切日までに「最良かつ最終」のオファーを提出 | 「Expressions of Interest closing Tue 6 Oct 5pm」「Offers closing」 |
| **Off-market（非公開）** | 正式掲載前に自社データベースの登録買主だけに案内 | 自社サイト・メールで「Coming Soon」「Off-market」。Domain の off-market alert、Listing Loop / Quiet Listings などの専用サービスも存在 |

- 「Deadline Sale / Fixed Date Sale」（締切付き一般売買）や、Openn Negotiation（一般売買の柔軟性とオークションの価格透明性を組み合わせたオンライン入札）など、ハイブリッド方式も広がっている。
- **オークション文化が紹介手法に直結**: Ray White はオークションを中核に据え、「上限のない価格が狙える」という訴求をサイト上で展開。ライブ配信（Gavl、AuctionNow）や自社の Online Auctions ページで、週末のオークションを「イベント」として見せる。TikTok 等で「Ray White Auction Live」的なコンテンツも流通。
- Domain は都市別の **Auction Results**（落札・事前売却・流札(Passed in)・延期・取下げ）を毎週公開しており、これが買主・売主双方の相場感形成に使われている。

---

## 3. 価格表示は「州の規制」で決まる（最重要ポイント）

物件ページの価格欄は自由ではなく、州法と Underquoting（過少見積り広告）規制に縛られる。同じポータルでも州によって表示が変わる。

### ポータルで選べる価格表示形式
- 固定価格（例: `$1,250,000`）
- 価格帯（例: `$1,200,000 – $1,300,000`）
- Price Guide（例: `Price Guide $950,000`）
- Offers Over / `$900,000+`（州によって禁止）
- オークション日時のみ（価格なし）
- `Contact Agent`（価格非公開。買主から不評で「Contact Agent の罠」と批判する記事も多い）

### 州ごとの主な違い

| 州 | ルールの要点 |
|---|---|
| **VIC（ビクトリア）** | **Statement of Information（SOI）** の掲示が必須。売出価格の根拠として、直近の比較売買3件（住所・日付・価格）と郊外中央値を記載。価格帯を出す場合、上限は下限の **10%以内**。realestate.com.au では「view agent price guide」のリンクから SOI を閲覧できる。内見（Open for Inspection）時も掲示義務 |
| **NSW（ニューサウスウェールズ）** | 2026年の改正で **全広告に価格または価格ガイドの掲載を義務化**、違反には6桁の罰金。「offers over $900,000」「$900,000+」型の表現は禁止 |
| **QLD（クイーンズランド）** | Property Occupations Act 2014 により **オークション物件では価格ガイドの提示自体が禁止**（リザーブ価格や「落札しそうな額」を口頭でも言えない）。代わりに Comparative Market Analysis（CMA）を渡す。QLD のオークション物件ページに価格が出ないのはこのため |

- 売却後の価格表示: Domain では公的記録が届くまで「Price Withheld」、エージェントが非公開を選んだ場合は非表示。売却済み物件のページも残し、ブランド露出と相場データとして活用。

---

## 4. 物件ページの構成要素（ポータルとエージェント共通）

購入者の意思決定順に「感情 → 条件確認 → 行動」と並ぶのが定番構成。

1. **ヒーロー写真＋ギャラリー**（10〜16枚、スマホはスワイプ）
2. **主要スペック**: ベッド／バス／駐車台数のアイコン、土地面積、物件種別
3. **価格 or 販売方式**（上記3章の形式）
4. **見出し（最大150字程度）＋説明文**: 「フック → 本文 → 行動喚起」の3部構成。短い段落と箇条書き、二人称（you）で生活シーンを描く。「gorgeous」「luxury」などの使い古された形容詞は避ける、というのが業界のコピーライティング指針
5. **Key Features の箇条書き**
6. **間取り図（Floor plan）**: 2026年の調査では売主の81%が「必須」と回答、間取り図ありでクリック率が最大52%向上、買主の5人に1人は間取り図がないと無視、という数字が引用されている。LiDAR 計測の間取り図で面積トラブルを防ぐ動きも
7. **動画・3Dツアー**: Matterport 型の「ドールハウス表示」、Ray White は「全物件にバーチャルツアー」を掲げる
8. **Inspection times（内見時間）**: 土曜 11時〜14時の30分枠が定番。ポータル側に「今週の内見一覧」ページがあり、予約システム（Inspect Real Estate など）と連携
9. **Statement of Information / 契約書ダウンロード / 価格ガイド請求** などの資料リンク
10. **地図・郊外情報（Suburb insights: 中央値、人口動態、学校）**
11. **エージェントカード**（顔写真、電話、レビュー、担当物件数）と問い合わせフォーム
12. **売却済み・オークション結果へのリンク**

---

## 5. ポータルの「掲載枠（Depth product）」が見え方を決める

物件紹介の差は、写真の質だけでなく **売主負担広告費（VPA: Vendor Paid Advertising）** で買う掲載ランクで大きく変わる。

### realestate.com.au
- Standard → Feature → Highlight → **Premiere / Premiere+** の階層。
- 上位ほど検索結果で上に固定・写真が大きい。Premiere は約2週間後に自動で再浮上し、30日単位で購入。
- 料金は郊外ごとに変動（競争が激しいエリアほど高い）。

### Domain
- Branded → Silver → Gold → **Platinum → Platinum Edge** の階層。
- Platinum は検索1位固定・特大表示・大きなエージェント写真とエージェンシーロゴ。Google/Facebook/Instagram へ4日間自動配信。
- Gold は2位固定・検索結果でも画像カルーセル・90日掲載。
- Platinum Edge ではオークション結果ページにも社名ブランドが表示される。

→ エージェントは「物件を売る」と同時に「自社ブランドを郊外内で刷り込む」設計になっている。

---

## 6. マーケティングキャンペーンの標準パッケージ

オーストラリアでは売主が広告費を前払いする慣行があり、エージェントは「キャンペーン」として4〜6週間のパッケージを提案する。

| 項目 | 相場感（記事引用） |
|---|---|
| プロ写真＋間取り図 | $300〜800（10〜16枚＋実測図） |
| 夕景（Twilight）／ドローン撮影 | +$150〜300 |
| 看板（Signboard）・チラシ | $150〜600 |
| ホームステージング（家具設置） | $1,500〜5,000／4〜6週間 |
| パッケージ合計（パース例） | 中級 $3,000〜5,500、上級 $10,000超 |

- 定番の流れ: オフマーケット／Coming Soon で既存データベースに先出し → ポータル掲載（上位枠）＋看板 → 土曜の Open Home を複数回 → オークション or 締切日。
- 2026年トレンド: 近隣ライフスタイル写真（カフェ・ビーチ・公園）、縦型15〜30秒動画（SNSで写真のみ比80%増のエンゲージメントという引用）、エージェント本人が出演するウォークスルー動画。Instagram はエージェント利用率57%、TikTok は16%で「まだ空いている」チャネルとして語られる。

---

## 7. 写真・画像の「盛り方」の境界線

- バーチャルステージング（空室に家具を合成）は **明示すれば可**。一方、壁を明るく塗り替える、部屋を広く見せる、未改装のキッチンを改装済みに見せる、といった加工は Australian Consumer Law 上の誤認誘導（法人は最大$5,000万の罰金）。
- REIA（全国不動産協会）は「加工画像の明示ラベル」を推奨。実サイズと異なる家具合成もNG。
- 業界の目安: 「露出補正とレンズ歪み補正はOK。ひび割れを消す、植栽を足す、欠陥を隠すはNG。バーチャルステージングは開示付きで可」。

---

## 8. エージェント自社サイトに共通する構成

自社サイトはポータルから流入した買主・売主への「信頼構築」に寄っている。

- **郊外ランディングページ（Suburb profiles）**: 「〇〇 real estate agent」のSEO対策と、売主向けの地域実績訴求
- **エージェントプロフィール**: 顔写真、売却件数、平均売却日数、RateMyAgent の検証済みレビュー（実際の取引に紐づく）
- **Recent Sales / Sold ページ**: 売却実績を価格付きで並べ、社会的証明として使う
- **Just Listed / Just Sold** のメール・SNS自動配信
- **Off-market / Coming Soon** 一覧と会員登録フォーム（データベース構築が目的）
- **オークションカレンダーとライブ配信リンク**
- **無料査定（Appraisal）CTA**: 売主獲得が最終目的なので、買主向けページにも常設
- **市況レポート**（Ray White Now など週次の自社レポート）

---

## 9. 日本の不動産サイトとの主な違い（要点）

| 観点 | オーストラリア | 日本（一般的な傾向） |
|---|---|---|
| 主要導線 | 2大ポータル＋REAXML 連携 | 複数ポータル＋自社サイト、レインズは非公開 |
| 価格表示 | 州規制で形式が制限。オークションは価格なしも普通 | 原則固定価格を表示 |
| 販売方式 | オークション／EOI が日常的、見出しに出る | ほぼ一般売買 |
| 内見 | 決まった時間の公開 Open Home に多数が同時来場 | 個別予約が中心 |
| メディア | プロ写真・間取り図・動画・3Dは標準、ステージング一般的 | 写真中心、間取り図は標準、ステージングは少ない |
| 広告費 | 売主が前払い（VPA） | 仲介手数料に内包 |
| 情報開示 | VIC の SOI など「価格根拠」の開示義務 | 重要事項説明は契約直前 |
| エージェント表示 | 個人名・顔・実績・レビューを前面に | 会社名中心 |

---

## 10. 参考にできる具体的な施策（自社サイト設計への示唆）

1. 価格欄に「表示形式の選択肢」を持たせる（固定／レンジ／ガイド／方式のみ）。
2. 販売方式と締切・オークション日時を物件カードの一等地に置く。
3. 間取り図・動画・3Dツアーをギャラリーと同列のタブにする。
4. 内見時間を物件ページと「今週の内見一覧」の両方で出し、予約導線を付ける。
5. 売却済み物件ページを消さずに「実績」として残す。
6. エージェント個人のプロフィール＋レビュー＋売却データを標準装備にする。
7. Coming Soon / Off-market 会員登録で買主データベースを作る。
8. 加工画像には開示ラベルを付ける運用ルールを持つ。

---

## 参考ソース

### 販売方式
- Belle Property「The 4 main ways to sell property」 https://www.belleproperty.com/blog/the-4-main-ways-to-sell-property
- LJ Hooker「Understanding the Different Ways to Sell Real Estate」 https://www.ljhooker.com.au/blog/understanding-the-different-ways-to-sell-real-estate
- Nelson Alexander「Auction, private sale and expressions of interest explained」 https://www.nelsonalexander.com.au/news/auction-private-sale-and-expressions-interest-explained/
- Domain「Auction, private treaty or expression of interest」 https://www.domain.com.au/advice/auction-private-treaty-or-expression-of-interest-which-is-the-best-strategy-for-selling-your-home-20180329-h0y4q8/
- Ray White「Online Auctions」 https://www.raywhite.com/online-auctions/
- Ray White Surry Hills「Online auctions and virtual tours change the game」 https://www.raywhite.com/blog/virtual-tours-and-online-auctions-change-the-game-for-ray-white-surry-hills/
- Gavl https://www.gavl.com/ ／ Openn Negotiation https://en.wikipedia.org/wiki/Openn_Negotiation ／ OpenAgent「How do online property auctions work?」 https://www.openagent.com.au/blog/how-do-online-property-auctions-work
- Domain Auction Results（Sydney） https://www.domain.com.au/auction-results/sydney/
- Ray White Phillip Island「Fixed Date Sale」 https://raywhitephillipisland.com.au/buy/offer-process-and-tips-fixed-date-sale

### 価格表示・規制
- NSW Fair Trading「Underquoting guidance」 https://www.fairtrading.nsw.gov.au/housing-and-property/property-professionals/working-as-a-property-agent/underquoting
- Real Estate Business「NSW targets underquoting with 6-figure penalties and price guide disclosure」 https://www.realestatebusiness.com.au/sales/31528-nsw-target-underquoting-with-six-figure-penalties-and-price-guide-disclosure
- Consumer Affairs Victoria「Underquoting information for real estate agents」 https://www.consumer.vic.gov.au/licensing-and-registration/estate-agents/running-your-business/underquoting-information-for-real-estate-agents
- Titlespace「Underquoting in NSW, VIC & QLD explained」 https://titlespace.com.au/blog/buying-property/underquoting-nsw-vic-qld/
- Property Occupations Act 2014 (Qld) s216 https://classic.austlii.edu.au/au/legis/qld/consol_act/poa2014271/s216.html
- Max Property「Why you won't see a price guide on a Queensland auction」 https://maxproperty.au/insights/why-queensland-auctions-no-price-guide
- Sale by Home Owner「Statement of information」 https://www.salebyhomeowner.com.au/statement-of-information/
- re4u「What Does "Contact Agent" Really Mean?」 https://www.re4u.com.au/p/what-does-contact-agent-really-mean
- Domain Help「Sold price displayed on 'undisclosed' sold listings」 https://help.domain.com.au/hc/en-us/articles/360017399394-Sold-price-displayed-on-undisclosed-sold-listings
- Domain Help「Exclude 'Under Offer' & 'Deposit Taken' listings」 https://help.domain.com.au/hc/en-us/articles/360016961273-Exclude-Under-Offer-Deposit-Taken-listings-from-search-results

### 掲載枠・広告費
- PropertyNow「Realestate.com.au Listing Upgrades」 https://www.propertynow.com.au/what-we-offer/optional-inclusions/realestate-com-au-listing-upgrades/
- Unreserved Real Estate「realestate.com.au Advertising Costs 2026」 https://www.unreservedrealestate.com.au/articles/real-estate-advertising-costs/
- Domain Help「Domain upgrades, depth products and display advertising」 https://help.domain.com.au/hc/en-us/articles/360012210273-Domain-upgrades-depth-products-and-display-advertising
- Domain Marketing Hub「Platinum Listing」 https://agent.domain.com.au/property-marketing/platinum-listing/ ／「Gold Listing」 https://agent.domain.com.au/property-marketing/gold-listing/ ／「Platinum Edge」 https://help.domain.com.au/hc/en-us/articles/22347641727385-Platinum-Edge
- OpenAgent「How much does it cost to advertise and market a property?」 https://www.openagent.com.au/blog/much-cost-advertise-market-property
- KeyHive「Real Estate Advertising Fees Perth」 https://keyhive.com.au/learn/vendor-paid-advertising-perth
- Agents Brand「Marketing for Real Estate: What Sydney Agents Actually Spend in 2026」 https://www.agentsbrand.com.au/marketing-for-real-estate/
- Homenly「Property Advertising Australia 2026」 https://homenly.com/news/property-advertising-australia-the-complete-guide-to-promoting-real-estate-in-2026

### メディア（写真・間取り図・動画・3D）
- UberRE「Professional Real Estate Photography and Floor Plans Australia: the 2026 marketing standard」 https://www.uberre.com.au/post/professional-real-estate-photography-and-floor-plans-australia-the-2026-marketing-standard
- Upload Media「10 Best Real Estate Photography Trends Shaping the Sydney Market in 2026」 https://uploadit.com.au/10-best-real-estate-photography-trends-shaping-the-sydney-market-in-2026/
- iGUIDE「Immersive media in realestate.com.au property listings」 https://goiguide.com/blogs/realestate-com-au-property-listings-immersive-media
- CloudPano「Do Virtual Tours Help Sell realestate.com.au Listings?」 https://www.cloudpano.com/blog/virtual-tours-listing-performance-realestate-com-au
- Property Update「What Property Sellers Can Learn From Better Visual Marketing」 https://propertyupdate.com.au/what-property-sellers-can-learn-from-better-visual-marketing/
- Money magazine「AI real estate photos: what's legal」 https://www.moneymag.com.au/ai-edited-real-estate-photos-misleading-buyers
- ListingAI「Virtual Staging Rules in Australia」 https://www.listingai.co/blog/virtual-staging-compliance-guide/australia

### コピーライティング・SNS
- PropertyMe「5 real estate copywriting tips」 https://www.propertyme.com.au/blog/property-management/real-estate-copywriting-tips
- Professional Property Copy「How to Structure Your Real Estate Listing」 https://www.professionalpropertycopy.com.au/bullet-points-or-editorial/
- Openn「Creative Listing Description Examples」 https://www.openn.com/en-au/blogs/creative-listing-description-examples-for-real-estate-agents
- Entry Education「8 real estate marketing trends we're seeing in 2026」 https://entryeducation.edu.au/blog/real-estate-marketing-trends/
- Property Manager Australia「How Australian agents are embracing TikTok」 https://propertymanageraustraliamedia.com.au/revolutionising-real-estate-how-australian-agents-are-embracing-tiktok-for-a-market-edge/

### 自社サイト構成・データ連携
- WebRealty「What is REAXML」 https://webrealty.com.au/now-what-is-real-estate-agent-xml-reaxml-and-do-i-need-it/
- Themepress「Real Estate Agent Websites」 https://www.themepress.com.au/industry/real-estate-agent-websites/
- RateMyAgent https://www.ratemyagent.com.au/
- Marriott Lane「The art of Saturday open-for-inspection times」 https://marriottlane.com.au/selling/the-art-of-saturday-open-for-inspection-times/
- Inspect Real Estate https://www.inspectrealestate.com.au/
- Domain「Open for inspection times」 https://www.domain.com.au/sale/adelaide-sa/inspection-times/
- Which Real Estate Agent「The Best Off-Market Property Websites」 https://whichrealestateagent.com.au/sell-property/off-market-property-websites/
- Quiet Listings https://www.quietlistings.com.au/

### 日本語資料
- JAMS.TV「【2026年版】オーストラリアで一軒家を購入する完全ガイド」 https://www.jams.tv/real-estate/279423
- Wise「オーストラリア不動産・マンションを買う前に知っておきたい全知識」 https://wise.com/jp/blog/buying-property-in-australia
- オリオンスタープロパティ「日本とオーストラリアの不動産の違い」 https://australia-fudosan.com/
- Kookaburra Family「メルボルンで家を買う！人生初のオークションに参加！」 https://kookaburrafamily.com/first-house-auction/
