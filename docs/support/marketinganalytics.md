# Marketing Analytics

Marketing analytics covers the wider performance picture beyond attribution: awareness, acquisition, retention, and lifetime value. Where attribution answers *which campaign drove this install*, marketing analytics answers *which campaigns build profitable players over time*. TRACKS combines media, web, and attribution data into a single reporting surface so the same dashboards cover both questions.

## Why marketing analytics is different in gaming

Games rely on a longer consideration window than most consumer products — players research, watch streams, wishlist, and let reviews settle before buying. Awareness and brand health are leading indicators of sell-through, not vanity metrics. Acquisition cost is only part of the picture: a "cheap" channel with poor D30 retention often loses to an "expensive" one with loyal players. And the funnel spans web, storefront, and game — three places attribution and analytics tools have to stitch together.

For a deeper conceptual primer, see the Academy's [How game marketing differs](https://secondstage.io/academy/fundamentals/how-game-marketing-differs){:target="_blank"} and [The marketing funnel](https://secondstage.io/academy/fundamentals/the-marketing-funnel){:target="_blank"} modules.

## Key KPIs

Because games span a long funnel, it pays to think of metrics in three buckets: **awareness**, **acquisition**, and **post-launch**.

### Awareness metrics

For PC and console games, awareness is a first-class KPI — not a vanity metric. Players who never hear about your game can't convert later, and discoverability on storefronts compounds with off-storefront awareness.

- [**Cost Per Mille (CPM)**](../glossary.md#c)**:** Cost per 1,000 ad impressions — the baseline efficiency metric for awareness campaigns.
- **View Rate:** Percentage of video ad impressions that meet the platform's viewability threshold.
- [**Cost Per Qualified View (CPQ)**](../glossary.md#c)**:** A modeled refinement of CPM that counts only views with sustained engagement or downstream action — closer to "real" awareness than raw impressions.
- **Wishlist additions** *(Steam)* — wishlist activity is a strong leading indicator for sell-through, and TRACKS attributes wishlists back to the campaigns that drove them. See [Steamworks Integration](../platform/steamworks.md).
- **Brand health signals** — search volume, social mentions, and sentiment, when available.

For more on why awareness is foundational for PC/console marketing, see the Academy's [Brand Health module](https://secondstage.io/academy/fundamentals/brand-health){:target="_blank"} or the blog post [The Hidden Power of Awareness in Video Game Marketing](https://secondstage.io/2025/01/awareness-funnel-in-video-game-marketing/){:target="_blank"}.

### Acquisition metrics

Once a campaign moves from awareness to conversion-focused, attribution unlocks the full set of acquisition KPIs.

- **Installs:** Total new players acquired from marketing efforts (first game launch, not purchase).
- [**Cost Per Install (CPI)**](../glossary.md#c)**:** Average cost to acquire one new player.
- **Click-Through Rate (CTR):** Percentage of impressions that resulted in a click.
- [**Conversion Rate (CR%)**](../glossary.md#c)**:** Percentage of users who took a desired action (install, purchase) after clicking or viewing an ad.
- [**Effective CPI (eCPI)**](../glossary.md#e)**:** CPI adjusted to reflect modeled installs in addition to measured ones — useful when probabilistic attribution fills gaps left by deterministic tracking.

For how to read acquisition data when planning campaigns, see the Academy's [Measuring what matters](https://secondstage.io/academy/fundamentals/measuring-what-matters){:target="_blank"} module.

### Post-launch & lifetime value

Acquisition metrics tell you who came in. Post-launch metrics tell you whether they were *worth* acquiring — and they often reshuffle which channels look profitable.

- [**Return on Ad Spend (ROAS)**](../glossary.md#r)**:** Revenue per ad dollar, typically reported over fixed windows: **D1, D7, and D30**. Different game genres mature at different rates — some break even at D7, others not until D30 or later.
- **Lifetime Value (LTV):** Projected total revenue from a player cohort, accounting for ongoing monetization (DLC, in-game purchases, season passes). LTV-driven budgeting is what separates teams that scale spend profitably from those that don't.
- [**Retention curves**](../glossary.md#d)**:** D1 / D7 / D30 retention rates, segmented by acquisition source. A channel with high CPI but high D30 retention often beats a "cheap" channel with poor retention.
- [**Cohort analysis**](../glossary.md#c)**:** Slicing players by acquisition campaign to compare quality across creative, audience, and channel.

For LTV math and how lifecycle data should feed back into acquisition decisions, see the Academy's [Calculating lifetime value](https://secondstage.io/academy/player-lifecycle/calculating-lifetime-value){:target="_blank"} and [Lifecycle-informed marketing](https://secondstage.io/academy/player-lifecycle/lifecycle-informed-marketing){:target="_blank"} modules — or the full [Player Lifecycle path](https://secondstage.io/academy/player-lifecycle){:target="_blank"} for end-to-end coverage.

## What you can slice and compare

Reporting can be sliced across channel, geography (GEO), campaign beat, ad group, creative, audience, and player cohort — combined with any of the metrics above. Dashboards aggregate media, web, and attribution data in one place so cross-channel comparisons are possible without separate exports. Term definitions for every KPI live in the [Glossary](../glossary.md).

TRACKS installs, platform-reported conversions, and ad-platform audience sizes each count something different, so they will not match. [Conversions, Postbacks & Audiences](../attribution/postbacks/conversions-audiences.md) explains why the numbers differ and which one to use for reporting, optimisation, and audience building.

## Next

- For the **acquisition-funnel deep dive** (measured + probabilistic attribution, postbacks), see [Attribution Tracking](attribution.md).
- For **awareness, brand health, and LTV** background, follow the [Game marketing fundamentals](https://secondstage.io/academy/fundamentals){:target="_blank"} and [Player Lifecycle](https://secondstage.io/academy/player-lifecycle){:target="_blank"} paths in the Academy.
- For data handling, GDPR specifics, and the hybrid-hosted deployment that keeps granular data on your infrastructure, see [Architecture](architecture.md) and [Data Handling & Security](datasecurity.md).
