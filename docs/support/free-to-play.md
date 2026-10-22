# TRACKS for Free-to-Play Games

<p class="docs-audience">For: Marketing, analytics and engineering teams at free-to-play studios</p>

TRACKS tells a free-to-play studio which ad, campaign and channel produced each new player, and what those players are worth after they start playing. It joins three things that normally live apart: ad-platform spend, website behaviour, and first-party game or account events.

For a free-to-play title, TRACKS reports on:

- **Web visits and site conversions** — landing-page traffic and key clicks such as Play Free, Download, or Begin Checkout.
- **Account creations** — a player signs up on the web or in the launcher.
- **Installs (first gameplay)** — the first time an account enters the game. This is the core acquisition outcome.
- **Retention** — whether those players come back on later days.
- **Purchases and revenue** — first purchases, repeat purchases and membership renewals, tied back to the acquiring channel.
- **Cost and efficiency** — spend, cost per install, cost per account and return on ad spend, by channel and campaign.

The first sections explain what you see and how it is computed. The [Integration checklist](#integration-checklist) lists what we need from you, and the [Developer notes](#developer-notes) hold short guidance for the engineers who send us data.

## How data flows

Six sources feed one pipeline in your Google Cloud project, which produces the dashboard table and the ad-platform postbacks.

![Free-to-play data flow: website, signup, game servers and commerce backend send events to TRACKS; GA4 and the ad platforms are read directly; the TRACKS pipeline in your Google Cloud project produces an aggregated reporting table and consented conversion postbacks](../assets/diagrams/f2p_flow-light.svg#only-light)
![Free-to-play data flow: website, signup, game servers and commerce backend send events to TRACKS; GA4 and the ad platforms are read directly; the TRACKS pipeline in your Google Cloud project produces an aggregated reporting table and consented conversion postbacks](../assets/diagrams/f2p_flow-dark.svg#only-dark)

Your website, signup, game servers and commerce backend send events to two first-party endpoints: Collect for browser events and Measure for server events. Google Analytics 4 and the ad platforms are read directly. The pipeline joins them, attributes each player, and writes one daily reporting table.

## Attribution model

Each account, install and purchase is credited to at most one ad click, chosen by the strongest evidence available. A match on the same browser always beats a match on IP address, and a click must happen within 30 days before the event.

Free-to-play installs usually arrive through a launcher, Steam or a console store, which carry no click ID. So TRACKS links the ad click to the player through the website visit and the account, not through the store.

### The account is the hinge

Account creation is the one moment where a web visitor, already seen arriving from an ad, becomes a known account. When the account event carries the visitor's web analytics client ID (for example the GA4 client ID) and IP, everything the player does later (install, play, purchase) can be tied back to that first click.

### Account creation

An account is credited to an ad click from the same browser first, then to a click matched on IP address within 30 days. If neither exists but the account event carries its own campaign parameters or an off-site referrer, those are used.

### Purchases

A purchase is credited to an ad click made **after** the install, within 30 days, from any signal that telemetry has sent. The click that earned the install never earns its later purchases a second time. If no new click exists, a purchase within 30 days of install inherits the install's channel; otherwise it is Direct.

### Channel rules

A click ID (Google, Meta, TikTok, X, Reddit) or campaign parameters mark a visit as **Paid**. A referrer from another site, with no campaign parameters, marks it as **Referral**. Everything else is **Organic** or **Direct**. Your own domains never count as referrers.

## Metric definitions

Every metric comes in two flavours: **Paid** counts only events attributed to an ad click, and **Total** counts every event, paid and organic. An "e" in front of a cost metric (eCPI, eCPA) means spend divided by the Total count, which shows the blended cost including organic lift.

| Metric | Definition |
| --- | --- |
| Cost | Media spend pulled from each ad platform, on the ad account's local calendar day |
| Impressions, Clicks, Video Views | As reported by each ad platform |
| CPM / CPC / CTR % | Standard media ratios |
| CPV / View Rate % | Cost per video view; share of impressions that became a view |
| Web Visits | Website sessions from your web analytics (GA4) |
| Paid Web Visits | Web Visits that arrived with a click ID or campaign parameters |
| Web Conversions | The site actions you choose to count, such as Play Free, Download or Begin Checkout |
| CPA / eCPA (Web Conversions) | Cost per site conversion |
| Account Creations | New accounts reported by your backend or signup page |
| Cost per Account Creation / effective | Cost per new account |
| Game Installs | Accounts playing for the first time (first gameplay). Accounts on the one-off list of existing accounts (checklist item 6) never count |
| CPI / eCPI (Game Installs) | Cost per install |
| Install CR % | Share of ad clicks that became an install |
| Purchases | Completed orders reported by your commerce backend, one per transaction |
| Revenue | Value of those orders, converted to your reporting currency from the local price charged |
| ROAS % | (Paid revenue − cost) ÷ cost, from actual purchase revenue. Negative means paid revenue has not yet covered cost. Premium games use a different, [estimated ROAS](../reporting/roas.md) |
| Avg. Daily Active Users | Distinct accounts with a play session per day |
| Retention (D1, D7, D30) | Share of an install cohort that plays again on day N after install (see [Player Lifecycle](../reporting/player-lifecycle.md)) |
| CPQ | Cost per quality, an awareness metric (see the [Glossary](../glossary.md#c)) |

**Dates.** Installs, accounts and purchases are dated on the day the player did them, not the day the data arrived. Charts labelled "Cohorted by Campaign Date" place each install on the date of the ad click that earned it, so spend and its result sit on the same day.

## Dashboard walkthrough

**Filters (top bar).** Date range, Beat (campaign wave, such as AlwaysOn or a launch), GEO, Channel, Strategy and Campaign Objective. Every tile and table on the page follows them.

### 1. Headline tiles

- **Overall Campaign Trajectory (Last 14 Days)** — daily cost as a line against total and paid installs and web conversions as bars. A sudden drop on the last day or two is usually data still arriving, not a real decline.
- **Total Installs per GEO** — where new players came from over the last 14 days.
- **Cost-per-Install (Game)** — CPI and eCPI, paid and total installs, revenue, purchases and ROAS %.
- **Account Creations** — cost per account, paid and total.
- **Performance Metrics** — CPM, CPC, CPV, CTR % and CPQ with the change versus the previous period, plus impressions, clicks and video views.
- **Landing Page Metrics** — web visits, paid web visits and web conversions, with CPA and eCPA.
- **Influencer Marketing, Media Houses (Direct Buy), Game Analytics** — creator activity, direct media buys and average daily active users.

### 2. Campaign breakdown by channel and GEO

Two tables (Performance per GEO, Performance per Channel) carry the full funnel per row: cost, impressions, clicks, web visits, web conversions, CPA, paid installs and CPI. The four pies compare where the money went with where installs came from. For free-to-play titles Direct is often the largest install source, because many players arrive through launchers, stores and word of mouth rather than a tracked click.

### 3. Daily trends

- **Overall Daily Performance** — one row per day with every media metric, for spotting pacing changes.
- **UA Trends** — paid installs and CPI by campaign (click) date.
- **Media Performance** and **Creative Performance / Ad Fatigue** — volume against cost, and CTR and CPC against impressions; a falling CTR at steady impressions signals creative fatigue.
- **Landing Page Analytics** — weekly cost, CPA and web conversion rate.
- **Brand Health** — social and web mentions by source.

### 4. All campaign beats

One row per beat and channel, from cost to total installs. Use it to pick a beat, then apply it as a filter to see that wave across the whole page.

Each section links to a detail tab (Game Installs & UA, Website Analytics, Performance Media / Creative Evaluation, Influencer & Direct Buy), and every table can be exported as CSV.

## Conversion postbacks to ad platforms

TRACKS sends each attributed install and purchase back to the ad platform that earned it ([Postbacks](../attribution/postbacks/index.md)), so the platform's bidding can optimise toward real players instead of landing-page clicks. Postbacks run several times a day and only for players who granted marketing consent.

| Platform | Connection | Events sent |
| --- | --- | --- |
| Google Ads | Data Manager API, import-from-clicks conversion actions | Install, Purchase (with value) |
| Meta | Conversions API (pixel + access token) | Install, Purchase |
| TikTok | Events API | Install, Purchase |
| Reddit, Snapchat, X | Conversions APIs | Install, Purchase |

How it behaves:

- **Consent gates sending, not counting.** A player whose latest consent state has marketing granted is eligible. Everyone else is still counted in reporting but never sent to any platform. Consent given on the website carries over to that player's later installs and purchases.
- **Only clicks the platform can recognise.** An install is sent to a platform only when it was attributed to that platform's click, through the browser or IP evidence described under Attribution model.
- **Purchases carry their value**, in your reporting currency when available, otherwise in the local price and currency.
- **Freshness matters.** Most platforms reject conversions older than about 7 days, so late-arriving events (for example, a batch export that slips by a day) can lose their postback.

What we need from you per platform: the pixel or dataset ID and an access token (Meta, TikTok, Reddit, Snapchat, X), or two conversion actions created in Google Ads (for example `2S_Install` and `2S_Purchase`).

## Privacy, consent and data retention

Player-level data stays in your own Google Cloud project: the ingestion endpoints, the datasets and the scheduled pipeline all run there, under your project's own service account. Only aggregated reporting tables (no user IDs, no IPs) are copied out for the dashboard.

| Topic | How TRACKS handles it |
| --- | --- |
| Where processing runs | In your project, billed to your project, visible in your job logs. Second Stage deploys and maintains the pipeline code |
| User IDs | Your internal account ID, never an email, username or display name |
| IP addresses | Salt-hashed on receipt and never stored in plain text |
| Consent | Sent as data on every event. All events are counted; only consented players' conversions are forwarded to ad platforms |
| Deletion requests | The [GDPR API](../attribution/gdprapi.md) accepts an account ID; a scheduled sweep removes that player's rows from every TRACKS table |
| Minors | For players under 13 we recommend sending `marketing: false` unconditionally, enforced at source (COPPA, GDPR-K) |

**Why every event is sent, consented or not.** Dropping events at the source would corrupt install counts, retention denominators and revenue, and cannot be repaired later. Consent is enforced at the one point where it matters: forwarding a conversion to an advertiser. Your privacy team should confirm the lawful basis for the non-consented population (typically legitimate interest for first-party product analytics). We do not provide legal advice; see [Data Handling & Security](../support/datasecurity.md).

**Website tag.** The TRACKS web tag follows the same firing rules as your Google Analytics tag and sets no cookies of its own, so its coverage matches your GA4 coverage under your consent banner.

## Integration checklist

A free-to-play title goes live on TRACKS once these nine items are in place. Items 1–6 block go-live; 7–9 can follow shortly after.

| # | What we need | Usually owned by | Unlocks |
| --- | --- | --- | --- |
| 1 | Web Analytics access or export | Web / data | Web visits, site conversions |
| 2 | [Publish access](../platform/landingpages.md#inviting-second-stage-to-your-gtm-account) to your Google Tag Manager container (or Edit access if your team prefers to publish), so the TRACKS tag runs on all landing and signup pages | Web | Attribution |
| 3 | DNS records (TXT + CNAME) for your first-party tracking subdomains, see [Custom Domains](../platform/domains.md) | IT / web | Endpoints that ad blockers and site security rules allow |
| 4 | An account-creation event carrying the account ID | Web backend or signup page | Deterministic attribution of accounts and installs |
| 5 | Game events: a first-gameplay event once per account, and a session event on every login | Game / login servers | Installs, retention, daily active users |
| 6 | A one-off list of all existing account IDs, delivered before the first game events | Data | Returning players are not counted as new installs |
| 7 | `purchase_complete` from your commerce backend, every payment method, unique transaction ID | Commerce / platform | Revenue, ROAS, purchase postbacks |
| 8 | Read access to each ad account (Google Ads, Meta, TikTok, Reddit, DV360 and others), plus postback credentials | Marketing | Cost data, conversion postbacks |
| 9 | Confirmed lawful basis for non-consented events and the default marketing state for existing accounts | Privacy / legal | Compliant postbacks |

### Ad link conventions

Cost can only be joined to installs when the ad link carries the platform's IDs. Use the platform's dynamic macros on every ad:

- `utm_id` = campaign ID, `utm_content` = ad group or ad set ID, `utm_term` = ad ID.
- `utm_source` and `utm_medium` set per platform; keep auto-tagging (gclid, fbclid, ttclid) switched on.
- Check that macros are filled in live traffic. A link that reaches the site with a literal `{{campaign.id}}` or `${INSERTION_ORDER_ID}` falls back to Direct.
- Keep campaign parameters through every redirect between the ad and the signup page.
- Follow one campaign naming convention (beat, objective, strategy, GEO in fixed positions), so the dashboard filters can be derived from names.

## Developer notes

The Measure API takes one JSON event per request, server-to-server, and returns `200` once the event is safely queued. Most integration problems come from the six pitfalls listed below the example.

```bash
curl -X POST "https://tracks-m.yourgame.com/measure" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TRACKS_API_TOKEN" \
  -d '{
    "user_id": "acct_7f31ab77e0019c",
    "event_name": "session_start",
    "ip": "203.0.113.24",
    "timestamp": "2026-10-09T12:22:56.123Z",
    "platform": "PC",
    "is_first_game_open": true,
    "storefront": "Steam",
    "version": "1.0.1",
    "consent": { "analytics": true, "marketing": false, "consent_ts": "2026-10-09T12:22:50Z" }
  }'
```

| Response | Meaning |
| --- | --- |
| `200` | Accepted and queued |
| `400` | Missing `ip`, `event_name` or `user_id`, or the body was not parsed as JSON |
| `401` / `403` | Missing or wrong bearer token |
| `500` | Server error; retry with backoff |

### Pitfalls

1. **`ip` is the player's IP, not your server's.** Take it from the client connection or the forwarded-for header. If every event carries your backend's address, all players collapse onto one IP and attribution returns nothing. Prefer IPv4.
2. **Always send `Content-Type: application/json`.** Without it the body is not parsed and the API answers `400` as if `ip` were missing. Game engines set it automatically; hand-written curl calls often do not.
3. **The substring `test` anywhere in the payload drops the event silently.** This is how QA traffic is excluded. Watch for product names such as "Latest", "Greatest" or "Contest". For integration tests, send `"version": "0.0.1-test"` deliberately.
4. **Timestamps are ISO-8601 UTC.** In a server-to-server integration, take them from your server clock rather than a value reported by the player's device. A malformed timestamp is accepted but leaves the event without a date, so it never appears in reporting.
5. **Use the agreed platform strings.** For example `PC`, `Mac`, `PS4` / `PS5` with storefront `PSN`, `XboxOne` / `XboxSeries` with `Xbox`, `Switch` with `Nintendo`, and `Steam` as a storefront. Avoid ambiguous values such as `PlayStation`, `GDK` or a bare `Chromebook`; we agree the exact list with you.
6. **One stable account ID everywhere.** The same `user_id` on the account event, game events, purchases, the list of existing accounts and GA4. If you pseudonymise it, use a keyed hash (HMAC-SHA256 with a secret salt) applied identically on every surface. A plain SHA-256 of a guessable ID can be reversed by trying every value, and a different salt on each surface breaks the join.

## Related

- [Measurement API](../attribution/measurementapi.md): endpoint, payload fields and status codes.
- [Website Tracking & Consent](../platform/website-tracking.md): GTM, consent mode and ad pixels on your site.
- [Postbacks](../attribution/postbacks/index.md): platform setup for install and purchase conversions.
- [Player Lifecycle](../reporting/player-lifecycle.md): retention, churn and reactivations.
- [Data Handling & Security](../support/datasecurity.md): legal basis, retention and the GDPR API.
