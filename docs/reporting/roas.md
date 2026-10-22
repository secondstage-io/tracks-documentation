# ROAS %

<p class="docs-audience">For: UA and marketing leads, finance</p>

**ROAS % (Estimated)** tells you how much net game revenue your paid media brought back for every unit of currency you spent on it. A ROAS of 250% means that every $1 of ad spend returned an estimated $2.50 of net revenue.

## The formula

```text
ROAS % = SUM(Paid Installs × Unit Price) × 0.7
         ÷ SUM(Cost) × 100
```

| Part | What it means |
|---|---|
| **Paid Installs** | Installs that TRACKS attributed to a paid click |
| **Unit Price** | The Steam store price of the game for that install's country on its install date |
| **0.7** | The share the studio keeps after the store's 30% platform fee |
| **Cost** | Media spend pulled from the ad platforms (Media Analytics) |

`Paid Installs × Unit Price` is the estimated **gross revenue**. Multiplying it by 0.7 turns it into estimated **net revenue**, and dividing that by cost gives the return.

## The ingredients

### Paid Installs

Every install that TRACKS measures is matched back to the click that drove it, through the attribution chain. An install counts as **paid** when the source or medium of that click is a paid one, such as `cpc`, `cpm`, `paid`, `social`, `programmatic` or `creator`, or a paid platform such as Meta or TikTok. Organic, Direct and unattributed installs are left out of ROAS. They are still counted in Total Installs.

### Unit Price

The game's price comes from the Steam store, for each country and each day:

- **Local and on sale.** We use the price a player in that country actually saw that day. If the game was discounted in a sale, the discounted price is used.
- **One reporting currency.** The local price is converted into your reporting currency (USD for most clients) using that day's exchange rate.
- **Forward-filled.** Steam's price feed arrives a day late, so the last known price is carried forward. That way today's installs are priced too.
- **Install rows only.** Unit Price is filled only on full-game installs. Demo installs are not priced.

### The 0.7 factor

Steam keeps 30% of each sale, so the studio receives about 70% of the store price. Applying 0.7 makes ROAS compare spend against what the studio actually earns, not against the store price.

### Cost

Cost is the daily media spend from each connected ad platform (Meta, TikTok, Reddit, Google Ads, DV360 and others), plus any imported cost CSVs. It must be in the same currency as your reporting currency.

### Worked example

*Illustrative numbers.*

| | Value |
|---|---|
| Spend on the campaign | $10,000 |
| Paid installs, US at $39.99 | 400 |
| Paid installs, BR at $19.50 | 300 |
| Gross revenue | 400 × 39.99 + 300 × 19.50 = **$21,846** |
| Net revenue (× 0.7) | **$15,292** |
| **ROAS %** | 15,292 / 10,000 × 100 = **152.9%** |

Above 100% means the campaign earned back more than it spent, at least on the first purchase. Below 100% means it has not, yet.

## How to read it: it is an estimate

ROAS % is an **estimated** metric, not a revenue report. Keep these points in mind:

- **No actual sales data.** We assume every paid install is one full-price purchase at the local store price. Refunds, bundles, keys and gifted copies are not reflected.
- **DLC and in-game purchases are not included.** Only the base game counts.
- **Subscription services and other stores.** Game Pass and console installs get the Steam price unless your setup limits pricing to specific storefronts. For multi-platform games, check the storefront setting with the Second Stage team before quoting ROAS.
- **Installs without a country are unpriced.** If we cannot place an install in a country, it adds nothing to revenue. That makes ROAS slightly lower than it should be.
- **Timing.** Cost is booked on the day it was spent and installs on the day they happened. On short date ranges, a campaign's spend and its installs can fall into different days, so read ROAS over a week or longer.
- **Free-to-play and demo builds.** These have no unit price, so this estimated ROAS is empty for them.

!!! note "Free-to-play games"

    Free-to-play titles that send purchase events to TRACKS get a different ROAS: it is calculated from the actual purchase revenue those events report, not from a store price, and is shown as (paid revenue − cost) ÷ cost. A negative value there means paid revenue has not yet covered spend. See [TRACKS for Free-to-Play Games](../support/free-to-play.md#metric-definitions).

## Related

- [Wishlist Insights](wishlist-insights.md): cost per wishlist before launch.
- [Marketing Analytics](../support/marketinganalytics.md#post-launch-lifetime-value): ROAS, LTV and retention in the wider KPI picture.
- [Glossary: ROAS](../glossary.md#r)
