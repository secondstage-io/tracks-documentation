# Reporting API

<p class="docs-audience">For: Analysts and data engineers</p>

The TRACKS Reporting API gives your team read-only access to the same marketing, attribution and player-lifecycle numbers behind your TRACKS dashboards. Every request is an authenticated `GET` that returns JSON, or CSV with `&format=csv`.

The service runs in **your own Cloud project**, reads only your TRACKS dataset, and is never shared with another client. It is built for analysts and engineers who want TRACKS data in their own BI tools, warehouses or scripts without exporting it from the dashboards.

!!! info "Enabled on request"

    The Reporting API is set up per client. Ask your Second Stage account team to enable it for your project; you then receive your base URL and token.

| Endpoint | One row per | Use it for |
| --- | --- | --- |
| `GET /v1/performance` | your chosen `group_by` combination | Spend, delivery, installs, wishlists, efficiency (CPI, CTR, CPM) |
| `GET /v1/lifecycle/cohorts` | install cohort × `group_by` | Day 1 / 3 / 7 / 14 / 30 retention |
| `GET /v1/lifecycle/churn` | install cohort × `group_by` | 30-day churn and return rates |
| `GET /v1/lifecycle/activity` | time period × `group_by` | DAU / WAU / MAU; new, returning and reactivated players |
| `GET /v1/attribution/users` | attributed install (one per player) | Player-level attribution. Enabled on request only |
| `GET /v1/schema/dimensions`, `/v1/schema/metrics` | field | Discovering every available field and formula |

!!! note "Developer note"

    The lifecycle endpoints return counts and rates only. Player identifiers are never included, whatever you request.

## Getting access

Second Stage issues two things: a **base URL** and a **bearer token**. Send the token on every data request as `Authorization: Bearer <token>`.

| Item | Example | Notes |
| --- | --- | --- |
| Base URL | `https://tracks-reporting-service-<id>.<region>.run.app` | One per client, hosted in your GCP project |
| Interactive docs | `<base>/docs` | Public page; reading the contract needs no token |
| Token | 40-character string | Read-only. Keep it server-side, never in a game build or browser app |

### Try it in the browser

1. Open `<base>/docs`.
2. Click **Authorize**, paste your token, then **Authorize** → **Close**. The page remembers it across reloads.
3. Expand an endpoint, fill in the fields and click **Execute**.
4. Copy the `curl` command the page shows. It is a working request you can paste into a terminal or script.

The docs page is generated from the running service, so it always matches what the API accepts.

!!! note "Developer note"

    Store the token and base URL as environment variables (`TRACKS_TOKEN`, `TRACKS_API`); the examples below assume them. To rotate a token or add a second consumer, contact Second Stage.

## Endpoints and parameters

Every data endpoint takes a date range, a list of metrics and an optional `group_by`. Change the shape of the answer by changing `group_by`; narrow it with filters.

### Common parameters

| Parameter | Required | Example | Meaning |
| --- | --- | --- | --- |
| `date_from`, `date_to` | Yes | `2026-09-01` | Reporting day, inclusive, ISO format |
| `metrics` | Yes | `cost,clicks,cpi` | Comma-separated metric names |
| `group_by` | No | `channel,geo` | Dimensions to split by. Omit for one total row |
| `order_by` | No | `cost` | Sort column, largest first |
| `<dimension>=` | No | `geo=US,DE` | Filter on a dimension with its own parameter. Commas = OR |
| `filter=` | No | `filter=beat:Launch` | Generic filter for any dimension; repeat it to AND filters |
| `limit`, `offset` | No | `limit=50000` | Paging. Default 1,000 rows, maximum 50,000 |
| `format` | No | `csv` | CSV instead of JSON |

### Performance: spend through to installs

`/v1/performance` is the main endpoint. It covers media spend and delivery from every connected ad platform, website visits and conversions, modeled wishlists and attributed installs.

```bash
curl -H "Authorization: Bearer $TRACKS_TOKEN" \
  "$TRACKS_API/v1/performance?date_from=2026-09-01&date_to=2026-09-30&metrics=cost,impressions,clicks,attribution_installs,paid_installs,cpi&group_by=channel&order_by=cost"
```

| Question | `group_by` |
| --- | --- |
| Total for the period | omit it |
| Daily trend | `date` |
| By campaign | `campaign_name` |
| By campaign and country | `campaign_name,geo` |
| By creative | `ad_name` |
| Paid vs organic | `channel_grouping` |
| By store or platform | `attribution_storefront`, `attribution_platform` |

Useful dimensions include `channel`, `campaign_name`, `ad_group_name`, `ad_name`, `geo`, `beat`, `audience`, `ad_format` and `creative_label`. The full list of dimensions and metrics is at `/v1/schema/dimensions` and `/v1/schema/metrics`.

### Player lifecycle

| Endpoint | `date_from`/`date_to` select | Key metrics |
| --- | --- | --- |
| `/v1/lifecycle/cohorts` | Install dates (which cohorts) | `installs`, `retention_d1_pct` … `retention_d30_pct` |
| `/v1/lifecycle/churn` | Install dates | `matured_installs_30d`, `churn_rate_30d_pct`, `return_rate_30d_pct` |
| `/v1/lifecycle/activity` | Active days | `active_users`, `new_players`, `returning_players`, `reactivated_players` |

Lifecycle dimensions: `channel_grouping`, `channel`, `source`, `medium`, `campaign`, `platform`, `storefront`, `version`, `geo`. Activity adds `grain=day|week|month` for DAU, WAU or MAU, and `installed_only=true` to count only players with an install record.

```bash
curl -H "Authorization: Bearer $TRACKS_TOKEN" \
  "$TRACKS_API/v1/lifecycle/cohorts?date_from=2026-09-01&date_to=2026-09-30&metrics=installs,retention_d1_pct,retention_d7_pct&group_by=channel"
```

### Player-level attribution (on request)

`/v1/attribution/users` returns one row per attributed install: player ID, install date, channel, campaign, ad group, ad, country, platform, storefront and in-window activity. Because it carries player identifiers, it is switched off by default and enabled per client after written confirmation. Ask your account team if you need it.

## Responses and data definitions

Every JSON response has two keys: `meta` (row count, fields, the paging window you asked for) and `rows` (one object per result row).

```json
{
  "meta": { "row_count": 2, "limit": 1000, "offset": 0,
            "fields": ["channel", "cost", "paid_installs", "cpi"] },
  "rows": [
    { "channel": "Meta",    "cost": 13098.49, "paid_installs": 4120, "cpi": 3.18 },
    { "channel": "YouTube", "cost": 2625.25,  "paid_installs": 0,    "cpi": null }
  ]
}
```

### How metrics are calculated

| Kind | How it is computed | Examples |
| --- | --- | --- |
| Additive | Sum of the underlying values | `cost`, `impressions`, `clicks`, `attribution_installs` |
| Ratio | Total numerator ÷ total denominator, after grouping | `cpi`, `ctr_pct`, `cpm`, `retention_d7_pct` |
| Unique count | Distinct players in the period | `active_users`, `new_players` |

A ratio is never an average of daily ratios: a channel's `cpi` is its total cost over its total paid installs. A zero denominator returns `null`, not `0` (as for the YouTube row above). Percent metrics (`*_pct`) are fractions: `0.0279` means 2.79%.

### Key metric definitions

| Metric | Definition |
| --- | --- |
| `attribution_installs` | All installs TRACKS attributed |
| `paid_installs` / `organic_installs` | An exact split of `attribution_installs` by channel grouping |
| `cpi` | Cost per **paid** install |
| `ecpi` | Cost over **all** installs |
| `modeled_wishlists` | Wishlists attributed by the TRACKS wishlist model |
| `*_cr_pct` | Rate per click |
| `*_cvr_pct` | Rate per tracked website visit |
| `retention_dN_pct` | Share of a cohort active on **exactly** day N after install |
| `churn_rate_30d_pct` | Share of 30-day-old cohorts that never returned on days 1–30 |
| `reactivated_players` | Players who came back after 30+ days away |

`/v1/schema/metrics` returns every metric with its kind and, for ratios, the exact numerator and denominator.

### Dates, currency and freshness

- **Reporting day** (`date_from`/`date_to`) is the day spend was recorded or the day an install happened. Media rows use each ad account's local calendar day, matching the ad platform's own reporting.
- **Click day** (`campaign_date_from`/`campaign_date_to`, supplied together) answers "what did that week's clicks eventually convert to". It scans more data, so keep it narrow.
- **Currency** is your account currency; group by `currency` if you run accounts in more than one.
- **Freshness** follows your TRACKS pipeline schedule (several refreshes a day). The last few days can still move as ad platforms finalise spend and late installs are matched.

!!! note "Developer note"

    `/v1/attribution/users` responses also carry `meta.attribution_precision`. `exact` means each player's channel is their own referrer; `reduced` means players who arrived without campaign parameters get the most common channel for their signature. Install counts are exact either way.

## Limits, errors and best practices

Every request needs a date range of at most 400 days, and returns at most 50,000 rows per page. Each query also has a data-scan budget; a request over it returns `413` instead of running up a cost.

| Status | Meaning | What to do |
| --- | --- | --- |
| `401` | No bearer token sent | Add the `Authorization` header |
| `403` | Token not valid for this service | Check you are using this client's token |
| `404` | Path not found | Check the endpoint name (and that player-level attribution is enabled for you) |
| `413` | Query would scan more than the budget | Narrow the date range or add filters |
| `422` | Invalid request | Read `detail`: it names the bad field and points at the schema endpoint |
| `503` | Service not configured | [Contact Second Stage](../support/contact.md) |

```json
{ "detail": "unknown metric 'cost_of_goods'; see GET /v1/schema/metrics" }
```

### Best practices

- **Don't sum unique counts across periods.** A player active in two weeks counts once in each; request `grain=month` for a monthly figure.
- **Align windows to week or month boundaries.** A range that starts mid-week makes the first `grain=week` bucket a partial week.
- **Judge churn and D30 on mature cohorts only.** Keep `date_to` at least 30 days in the past; younger cohorts show `0` for day 30 because it has not happened yet.
- **Re-pull the most recent days on each sync.** We recommend the trailing 3–7 days: late spend corrections and late install matches land there.
- **Prefer the reporting day axis.** It is indexed and fast; use click-day filters only for narrow windows.
- **Read field names from the schema endpoints** rather than hard-coding them from this page.

## Developer notes

### Paging and bulk export

Ordering is stable, so `limit`/`offset` pages never overlap. There is deliberately no total row count (it would double the cost of every query): page until a page comes back shorter than `limit`.

```bash
curl -H "Authorization: Bearer $TRACKS_TOKEN" \
  "$TRACKS_API/v1/performance?date_from=2026-09-01&date_to=2026-09-30&metrics=cost,clicks,attribution_installs&group_by=date,campaign_name,ad_name&format=csv&limit=50000" \
  -o september.csv
```

### Minimal Python client

```python
import os, requests

BASE = os.environ["TRACKS_API"]
S = requests.Session()
S.headers["Authorization"] = f"Bearer {os.environ['TRACKS_TOKEN']}"

def fetch(path, **params):
    rows, offset, limit = [], 0, 50_000
    while True:
        r = S.get(f"{BASE}{path}", params={**params, "limit": limit, "offset": offset}, timeout=300)
        r.raise_for_status()
        page = r.json()["rows"]
        rows += page
        if len(page) < limit:
            return rows
        offset += limit

for row in fetch("/v1/performance", date_from="2026-09-01", date_to="2026-09-30",
                 metrics="cost,attribution_installs,cpi", group_by="channel", order_by="cost"):
    print(row)
```

### Gotchas

- `metrics` and `group_by` take one comma-separated string; repeating the parameter (`metrics=a&metrics=b`) also works.
- Field names are lower-case. Matching is case-insensitive, but the schema endpoints give the canonical form.
- Filter values are typed: dates as `YYYY-MM-DD`, integers and booleans as plain values. A malformed value returns `422`.
- A filter cannot match a value that itself contains a comma, because commas separate values.
- Rows whose dimension is empty group together as one `null` row, and can't be targeted by a filter.
- `*_cvr_pct` metrics divide by tracked website visits. Most installs come from players who never visit the website, so install and wishlist CVRs can exceed 100%.
- Small differences against your dashboards are possible for the newest days, while a pipeline refresh is in progress.

### Versioning

All endpoints sit under `/v1`. New metrics and dimensions can be added at any time, so ignore unknown fields in responses. Breaking changes, such as renaming or removing a field or changing a definition, will be announced in advance.

## Related

- [Data Collection](../support/datacollection.md#what-reporting-exposes): what the dashboards and the API each expose.
- [Player Lifecycle](player-lifecycle.md): definitions behind the lifecycle endpoints.
- [Wishlist Insights](wishlist-insights.md): how `modeled_wishlists` is calculated.

Questions about your data, your token or a metric definition: [contact Second Stage](../support/contact.md).
