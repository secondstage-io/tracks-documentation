# Wishlist Insights

<p class="docs-audience">For: UA and marketing leads, Steam marketing admin</p>

Wishlist Insights connects your campaigns to the wishlists Steam actually recorded. When Financial Data access is granted, every wishlist total TRACKS shows comes from Steam's own numbers. TRACKS then works out how much of that total each channel, campaign and ad drove, so you can make decisions based on cost per wishlist.

## Why wishlists need a model

No single source tells you which campaign drove which wishlist:

| Source | What it knows | What it can't tell you |
|---|---|---|
| **Steamworks wishlist report** | The exact number of wishlists added per day and per country | Which campaign drove them |
| **Steamworks UTM report** | For visits that reach Steam with UTM tags, which campaign they came from and whether the visitor wishlisted | Only a small, sampled share of the traffic you send |
| **Your landing page (GA4 + TRACKS snippet)** | How many visitors clicked through to Steam, per campaign, ad and country | Whether they wishlisted once on Steam |

TRACKS combines all three. Steam is the source of truth for **how many** wishlists happened. Your landing page is the source of truth for **how much traffic** each campaign sent to Steam. The UTM sample shows **how well** each channel's traffic turns into wishlists.

## How TRACKS attributes wishlists

The model runs every time your pipeline refreshes, for each day and each country separately.

<ol class="setup-steps" markdown="1">

<li markdown="block">

### Measure each channel's wishlist rate

From the Steamworks UTM report, TRACKS calculates what share of each channel's Steam visits turned into wishlists over the last 28 days. If a channel has too few tracked visits to be reliable, it borrows the pooled rate of similar channels (paid or organic), and failing that, the average of all tracked channels.

</li>

<li markdown="block">

### Estimate wishlists per campaign

Each campaign's Steam clicks from your landing page are multiplied by its channel's rate. Steam's UTM sample misses part of every campaign's effect, such as players who come back later through the Steam app or Steam search. To account for this, a per-channel calibration agreed for your game can be added on top of the measured rate.

</li>

<li markdown="block">

### Never exceed Steam

If the estimates for a day and country add up to more than Steam recorded, all of them are scaled down proportionally to Steam's number.

</li>

<li markdown="block">

### Give the rest to Organic

Wishlists that no campaign accounts for are credited to **Direct / Organic**. These come from Steam's own discovery surfaces (search, recommendations, sales pages, followers) and from word of mouth.

</li>

<li markdown="block">

### Leave unreported days blank

Steam publishes a day's wishlists only after that day ends. Until it does, wishlists for that day stay empty rather than showing an estimate.

</li>

</ol>

### Example

Steam reports **1,000** wishlists in the United States yesterday. Your landing page sent:

| Campaign | Steam clicks | Channel wishlist rate | Estimated wishlists |
|---|---|---|---|
| Meta – Trailer | 2,000 | 6% | 120 |
| Reddit – Gameplay | 1,000 | 9% | 90 |
| **Paid total** | | | **210** |
| **Direct / Organic** | | | **1,000 − 210 = 790** |

If the campaigns had added up to more than 1,000, every estimate would have been scaled down until the total was exactly 1,000.

## Reading the dashboard

### Wishlist Insights

The KPI cards, the daily table, the market and channel breakdowns, and the charts all use the definitions below.

| Metric | Definition |
|---|---|
| **Total Wishlists** | Wishlists added on Steam (gross additions), matching your Steamworks report |
| **Paid Wishlists** | The part of Total Wishlists credited to paid channels |
| **CPWL** (Cost per Wishlist) | Cost ÷ Paid Wishlists. What a paid wishlist costs you |
| **eCPWL** (Effective CPWL) | Cost ÷ Total Wishlists. Spend measured against all wishlists, including organic ones that campaigns may have influenced indirectly |
| **Wishlist CR %** | Paid Wishlists ÷ Clicks. The share of ad clicks that ended in a wishlist |
| **Landing Page Visits** | Sessions on your landing page or website |
| **Tracked Steam Visits** | Clicks from your landing page through to the Steam store page |
| **Web Conversions CVR %** | Tracked Steam Visits ÷ Landing Page Visits |
| **WL Share of Organic %** | (Total Wishlists − Paid Wishlists) ÷ Total Wishlists |
| **Cost, Impressions, Clicks, CPM, CTR %, CPC** | Media delivery and spend from your connected ad platforms |

**Breakdowns.** Every wishlist metric can be split by date, country (GEO), channel, channel grouping, campaign, ad group, ad and Beat. Because the model runs separately per country, the market breakdown also shows countries where you didn't spend. Their wishlists are organic, and they often reveal where your game has natural demand.

### Steam Store Traffic & Visibility

This section comes from Steamworks' **store traffic report**. It shows how players reached your Steam store page, whether or not you advertised.

| Metric | Definition |
|---|---|
| **Total Non-Owner Impressions** | How often your game was shown on Steam to people who don't own it |
| **Total New Visits** | Store page visits from people who don't own the game |
| **Click Through Rate %** | New Visits ÷ Non-Owner Impressions |
| **Steam New Visits (Last 6 Months)** | Total new visits over the period of the latest Steamworks traffic export. This card ignores the dashboard's date filter |

The traffic is shown in four ways:

- **By category** (Page / Category). Shows where on Steam visitors came from. **Search Suggestions** (the search bar's auto-complete) usually means players searching for your game by name, which is a strong brand-awareness signal. **Wishlist** means visits from players' own wishlists, **Sales Page** means event and sale pages, **Discovery Queue** means Steam's recommendation queue, and so on.
- **By source** (Page / Feature). The same data one level deeper, for example *Search Auto-complete*, *Personal Calendar* or *Main Cluster (Top Seller)*.
- **By market.** New visits and impressions per country.
- **From external websites.** Visits that arrived from outside Steam, by referring site (Google, YouTube, Reddit, and so on). Most paid traffic arrives here, or under *Direct Navigation*.

!!! tip "Good to know"

    *External Website* and *Direct Navigation* have no impressions, because the visitor wasn't shown the game on Steam first. *(other pages)* can show a click-through rate above 100% for the same reason. Steam flags part of the traffic as *Bot Traffic*, and it is not counted as real visits.

## Things to keep in mind

- **Steam days are Pacific Time.** Steam reports wishlists per day in US Pacific Time, so a Steam "day" starts at 07:00 or 08:00 UTC.
- **Recent days fill in later.** Steam data is refreshed several times a day, and the most recent day appears once Steam has published it. Until then, wishlist columns for that day show `–`.
- **Additions, not net change.** Total Wishlists counts wishlists **added**. Deletions and wishlists converted into purchases are not subtracted, so after launch the total is higher than the change in your outstanding wishlist balance.
- **Paid is usually a small share.** Most wishlists on Steam come from Steam's own discovery, so a 90–98% organic share is normal. Paid campaigns often lift organic wishlists too, which is what eCPWL is meant to capture.
- **The landing page is the bridge.** Paid wishlists can only be credited to campaigns whose traffic goes through a page with the TRACKS snippet, or whose links carry TRACKS UTM tags. Traffic sent straight to Steam without tags ends up in Organic.

## Requirements

- **Steamworks access** for `analytics@secondstage.io` with both **View Marketing Traffic Data** and **View Financial Data**. Financial data is what lets TRACKS match Steam's exact wishlist totals. See [Steamworks Integration](../platform/steamworks.md).
- **The TRACKS landing page snippet** or **TRACKS tracking links**, so that campaign tags reach Steam. See [Landing Page Integration](../platform/landingpages.md) and [Tracking Links](../support/trackinglinks.md).
- **Connected media channels**, so that cost, CPWL and eCPWL can be calculated. See [Media Platform Access](../platform/mediachannels/index.md).

## Related

- [ROAS %](roas.md): the return on spend once wishlists turn into purchases.
- [Ad Ops Guide](../support/adopshelper.md): link and naming conventions that keep campaign tags intact on the way to Steam.
