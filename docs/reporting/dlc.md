# DLC Tracking & Reporting

<p class="docs-audience">For: Game / backend engineer, UA and marketing leads</p>

TRACKS reports, per day, how many players activated each DLC, and which marketing channel, campaign and country those players came from. Your game sends DLC ownership through the same [Measurement API](../attribution/measurementapi.md) it already uses for game opens; there is no separate SDK and no store integration.

With DLC tracking live you can answer:

- How many DLC activations came from paid media, and what each one cost (cost per DLC, effective cost per DLC).
- Which channel, campaign, country, platform and storefront drives DLC buyers.
- Which DLC, edition or bundle sells, side by side with base-game installs and spend.
- Whether DLC buyers are new players (bought with the game) or existing players coming back.

!!! note "What it does not measure"

    Store revenue and refunds. TRACKS sees the moment the game first detects the entitlement, not the store checkout. Revenue stays in your Steam, PlayStation, Xbox and Nintendo store reports.

## How it works

![DLC data flow: the game reports DLC through the Measurement API; TRACKS keeps one activation per player and DLC, credits it to a recent DLC ad click, the install source or Direct, and reports it on the DLC dashboard, optionally sending it to ad platforms as a conversion](../assets/diagrams/dlc_flow-light.svg#only-light)
![DLC data flow: the game reports DLC through the Measurement API; TRACKS keeps one activation per player and DLC, credits it to a recent DLC ad click, the install source or Direct, and reports it on the DLC dashboard, optionally sending it to ad platforms as a conversion](../assets/diagrams/dlc_flow-dark.svg#only-dark)

The game reports DLC through the Measurement API. TRACKS keeps one activation per player and DLC, credits it to a recent ad click, the player's install source or Direct, then reports it and optionally sends it to ad platforms as a conversion.

## Developer integration

DLC rides on the Measurement API you already call for game opens: one HTTPS POST per event, JSON body, your project API key as a Bearer token. Event names and key names are flexible because we map them in the backend; what matters is that they stay the same across builds and platforms.

### The request

```http
POST https://<your-measure-endpoint>/measure
Content-Type: application/json
Authorization: Bearer <API_KEY>
```

| Response | Meaning |
| --- | --- |
| `200` + `message_id` | Accepted and queued for processing |
| `400` "IP address missing" | No `ip` in the body (or the body is not valid JSON) |
| `400` "Missing required fields" | `event_name` or `user_id` is missing |
| `401` | Missing or wrong `Authorization: Bearer` header |

### The base event: game open

Fire one event on every game launch. Mark the player's first ever launch with a boolean flag, or send the first-launch timestamp; we detect the install from either.

```json
{
  "event_name": "game_open",
  "user_id": "12346",
  "ip": "203.0.113.24",
  "timestamp": "2026-10-09T12:22:56.123Z",
  "platform": "PC",
  "storefront": "Steam",
  "version": "0.12.013",
  "is_first_game_open": true,
  "first_session_timestamp": "2026-10-09T12:22:56.123Z"
}
```

You can also split this into two events, for example `first_open` (always `is_first_game_open: true`) and `game_open` (always `false`). Either way works; tell us which you chose.

### Sending DLC: pick one of two designs

#### Design A: DLC list in every game open (recommended)

Add a `dlc_activations` array listing every DLC the player owns, and re-send the full list on every game open. Each item keeps the same `dlc_activation_ts` on every re-send. We count each player and DLC pair once, at its earliest timestamp, so re-sending never double counts. No setup is needed on our side.

```json
{
  "event_name": "game_open",
  "user_id": "1dc642cc12345",
  "ip": "203.0.113.24",
  "timestamp": "2026-10-09T12:22:56.123Z",
  "platform": "PS5",
  "storefront": "PSN",
  "version": "1.0.1",
  "is_first_game_open": true,
  "sku_id": "basegame_complete_edition",
  "sku_name": "Base Game Complete Edition",
  "sku_type": "Bundle",
  "dlc_activations": [
    {"dlc_id": "expansion_01", "dlc_name": "Story Expansion 1", "dlc_activation_ts": "2026-10-09T12:22:56.123Z"},
    {"dlc_id": "expansion_02", "dlc_name": "Story Expansion 2", "dlc_activation_ts": "2026-10-09T12:22:56.123Z"},
    {"dlc_id": "cosmetic_pack_01", "dlc_name": "Cosmetic Pack 01", "dlc_activation_ts": "2026-10-10T08:15:22.456Z"}
  ]
}
```

#### Design B: one event per DLC

Fire a dedicated event when the game first sees a DLC (and, if convenient, again on later launches). Tell us the event name and key names before go-live; it is a one-line configuration on our side.

```json
{
  "event_name": "dlc_activation",
  "user_id": "e9665148-7f8a-4968-9abc-1762bddb949c",
  "ip": "198.51.100.42",
  "timestamp": "2026-10-10T08:15:22.456Z",
  "platform": "PC",
  "storefront": "Steam",
  "dlc_id": "cosmetic_pack_01",
  "dlc_name": "Cosmetic Pack 01",
  "dlc_activation_ts": "2026-10-10T08:15:22.456Z"
}
```

**Which to choose.** Design A suits games that already read the full entitlement list at boot. Design B suits a telemetry backend that already emits one event per item. Both produce the same reports. Do not send both for the same DLC.

## Field reference

Only `event_name`, `user_id` and `ip` are enforced by the API; the rest decide how much the reports can break down. Timestamps are ISO 8601 in UTC (`Z`) or with an offset (`+02:00`); fractional seconds are fine.

| Field | Need | Type | Example | Notes |
| --- | --- | --- | --- | --- |
| `event_name` | Required | string | `game_open` | Any name; we map it |
| `user_id` | Required | string | `1dc642cc12345` | Pseudonymised and persistent per player; the same ID on every event, including DLC |
| `ip` | Required | string | `203.0.113.24` | The player's public IP, not hashed, not a LAN address (192.168.x, 10.x). Drives country and ad-click matching. We hash it on arrival |
| `timestamp` | Recommended | ISO 8601 | `2026-10-09T12:22:56.123Z` | When the event happened on the device |
| `platform` | Recommended | string | `PC`, `PS5`, `XboxSeries`, `Switch` | Device family; a dashboard dimension |
| `storefront` | Recommended | string | `Steam`, `PSN`, `Xbox`, `Epic`, `Nintendo` | Where the game was bought; a dashboard dimension |
| `version` | Recommended | string | `1.0.1` | Build version; lets us split demo and full game. Use one key name everywhere (not `version` in one event and `game_version` in another) |
| `is_first_game_open` | Required for installs | boolean | `true` | `true` only on the player's first ever launch. Or send `first_session_timestamp` instead |
| `first_session_timestamp` | Optional | ISO 8601 | `2026-10-09T12:22:56.123Z` | Timestamp of the first launch, if you store it |
| `dlc_activations[]` | Design A | array | see above | Full list of owned DLC, re-sent every game open |
| `dlc_id` | Required for DLC | string | `expansion_01` | Stable, unique ID per DLC; never changes between builds or platforms |
| `dlc_name` | Recommended | string | `Story Expansion 1` | Display name in the dashboard. If missing, we derive it from the ID (`DLC_01` → "Dlc 01") |
| `dlc_activation_ts` | Recommended | ISO 8601 | `2026-10-10T08:15:22.456Z` | When the player first got the DLC. Keep it identical on every re-send. Missing or future-dated values fall back to our server receive time |
| `is_owned` | Optional, Design B | boolean | `true` | `false` skips the event; it does not remove a DLC already counted |
| `sku_id`, `sku_name`, `sku_type` | Optional | string | `basegame_complete_edition`, `Bundle` | The store product actually bought. Stored with the event, not yet a dashboard field; it lets us separate a bundle from separate purchases when you need that |

## Payload rules and common mistakes

Every rule below comes from a real launch where the data went wrong. Following them avoids silent data loss and miscounted DLC.

1. **Never use the word "test" in a real payload.** We treat any event containing "test" (any case, anywhere in the body) as QA traffic and drop the whole event, including the game open it rides on. That catches IDs like `latest_pack`, `contest_pack`, `greatest_hits` or `protest`. Use it on purpose for QA: add `"environment": "test"` to QA builds and their events stay out of reports.
2. **Keep `dlc_id` stable and meaningful.** One fixed ID per DLC, identical across platforms and builds. Never a timestamp, a counter or an empty string; a build that sends the activation timestamp as the ID creates junk DLC rows.
3. **Keep `dlc_name` consistent.** One display name per ID. Two testers sending different names for the same ID split the dashboard rows.
4. **Keep `dlc_activation_ts` stable.** Send the moment the player first got the DLC, the same value on every re-send. If you cannot know it, leave it out and we use the time we first receive it.
5. **DLC bought before the first launch is fine.** Send the real purchase time; we keep it. Players who pre-purchase DLC and launch days later are counted correctly.
6. **Free grants and giveaways are not purchases.** If a DLC is given away (a free update pack, a launch gift, a demo item), tell us its ID and the dates. We exclude it from DLC counts; otherwise a free grant to every player looks like thousands of sales overnight.
7. **Bundles and editions.** The game sees entitlements, not store products. A Deluxe Edition bought with all packs surfaces as several DLC at the same moment. We count those once as a purchase (see [Units vs Unique](#units-vs-unique)). Sending the `sku_id` of the bought product removes the guesswork.
8. **Refunds are not removed.** Once a DLC is counted it stays counted; a later `is_owned: false` does not subtract it. Use store reports for refund rates.
9. **Same `user_id` on every event.** If the DLC event carries a different ID than the game open, we cannot connect the DLC to the player's install source.
10. **Send the player's public IP.** A missing or LAN IP means no country and no ad-click match. If the game cannot fetch its public IP (blocked lookup, some regions), tell us and we read it server-side instead.
11. **Do not mark the first launch twice.** Send `is_first_game_open: true` once per player. A platform that re-sends it on every update does not create duplicate installs (we keep the earliest), but it hides real data issues.
12. **Tell us before you change shape.** New event names, renamed keys or a switch between Design A and B need a configuration change on our side; until then those events are not counted.

## How a DLC gets its channel

Each DLC activation is credited by the first rule that applies, in this order:

| Order | Rule | Credited to | When it applies |
| --- | --- | --- | --- |
| 1 | DLC click match (optional) | The ad clicked shortly before the activation | The player clicked a tracked ad link, then activated the DLC; matched on IP and time, as for installs |
| 2 | Install source | The campaign that brought the player in | The DLC was activated within 30 days of the player's install |
| 3 | Direct / organic | No paid channel | Everything else, including veteran players who installed before tracking began |

The 30-day window is the default and can be changed per game. Rule 1 is switched on per game: turn it on when you run DLC-specific campaigns, so a player who installed via Reddit and bought the DLC from a Meta ad credits Meta. Without it, the DLC credits the install source (Reddit).

What this means when reading the numbers:

- **"Meta DLC activations" with rule 1 off** means players Meta acquired who then got a DLC, not purchases a Meta ad drove.
- **Lapsed players.** A player inactive for 30+ days who comes back counts as a reactivation, with its own source. If they come back by buying a DLC, they show in both reports; the two are not merged. See [Player Lifecycle](player-lifecycle.md).

### Sending DLC conversions back to ad platforms

TRACKS can send each paid DLC activation as a conversion to Meta, Google Ads, TikTok, Snapchat, Reddit and X, so campaigns can optimise for DLC buyers. It needs a conversion name per platform and a fixed value and currency per DLC activation (for example 9.99 EUR). Each player and DLC is sent once per platform. See [Postbacks](../attribution/postbacks/index.md).

## Reporting: the DLC dashboard

DLC lives on its own page of your TRACKS dashboard, next to installs, cost and web traffic.

### Units vs Unique

Every DLC metric comes in two counts, because one checkout can unlock several DLC at once.

| Count | What it counts |
| --- | --- |
| **Units** | Every DLC a player activated, once per player and DLC |
| **Unique** | Purchases: an edition plus the packs activated with it within 5 minutes counts once; packs bought on their own count once each |

Use Unique for cost per DLC and conversion rates, Units for which DLC players own. Free grants are excluded from both.

### Metrics

| Metric | Definition |
| --- | --- |
| **Total DLC Activations** (Unique / Units) | All activations, paid and organic |
| **Paid DLC Activations** (Unique / Units) | Activations credited to a paid channel |
| **DLC Activations CR %** (Unique) | Paid DLC activations ÷ ad clicks |
| **Cost per DLC** (Unique) | Cost ÷ paid DLC activations |
| **Effective Cost per DLC** (Unique) | Cost ÷ all DLC activations, paid and organic |

### Dimensions and filters

Filter the whole page by date range, Beat (campaign phase), GEO, Channel, Strategy and Campaign Objective. Tables break down by DLC name, storefront (Steam, PSN, Nintendo, Xbox), platform, country, channel and campaign.

### Page sections

| Section | What it shows |
| --- | --- |
| **KPI header** | Total and paid DLC (Unique and Units), DLC CR %, effective cost per DLC |
| **DLC Activations by Channel** | DLC name × storefront rows, total and paid units per channel |
| **DLC Activations by GEO** | DLC name × storefront rows, total and paid units per country |
| **Paid DLC Activations × Paid Installs** (by campaign date) | Daily cost, paid DLC, cost per DLC, paid installs, CPI, ROAS, with a cost vs DLC vs installs chart |
| **Paid + Organic DLC Activations** (by install date) | Daily paid and total DLC, Unique and Units, against cost |
| **Daily trends per GEO and per channel** | Paid DLC by campaign date, top countries and channels |
| **Detailed breakdowns by GEO and channel** | Cost, CPI, ROAS, web visits, conversions, CPA and paid DLC per row, with share pies; CSV export |

### Campaign date vs install date

- **By campaign date (cohorted).** DLC and installs are tied to the day of the ad spend that drove them. Recent days keep growing for up to the attribution window, so CPI and cost per DLC settle after about a week.
- **By install date.** Activations land on the day they happened, paid and organic together. Spend on one day can drive DLC on later days, so read daily cost per DLC here as a trend, not a cost.

!!! tip "Reading tips"

    - The DLC date is when the game first saw the DLC, not the store checkout date; for new players it is within minutes of their first launch.
    - Revenue, refunds and true purchase dates stay in the store reports; DLC ROAS uses a static DLC unit price as an estimate.

## Go-live checklist

**Studio**

- [ ] Choose Design A (array in game open) or Design B (separate event) and share one sample payload per platform
- [ ] Share the list of DLC IDs and display names, plus which are editions, bundles or free grants (with dates)
- [ ] Confirm no real ID, name or value contains "test"; mark QA builds with `"environment": "test"`
- [ ] Same `user_id` on game open and DLC events, public `ip` on every event
- [ ] Send a QA build to the endpoint and check for `200` responses on every platform

**Marketing**

- [ ] Use TRACKS UTM or redirection [tracking links](../support/trackinglinks.md) on DLC ads
- [ ] For ad-platform optimisation: a DLC conversion name per platform, plus the value and currency per activation to send as postbacks

**TRACKS**

- [ ] Configure the event shape (Design B only) and any free-grant exclusions
- [ ] Confirm QA events reach the pipeline, then remove them before launch reporting
- [ ] Check DLC rows, channels and costs on the dashboard on launch day and day 3

## FAQ

**Do I need a new SDK or store integration?**
No. DLC uses the same Measurement API endpoint and API key as game opens.

**Will re-sending the full DLC list on every launch inflate numbers?**
No. Each player and DLC counts once, at its earliest timestamp.

**Does a DLC event count as a game session?**
Yes. Any Measurement API event counts as player activity for that day, DLC events included. A DLC event never creates an install on its own.

**Can we see revenue per DLC?**
Not from telemetry. Combine paid DLC Units with your store prices, or share the price per DLC and we can add an estimate.

**How fast does data appear?**
Within the next dashboard refresh, several times a day. Recent campaign dates keep filling in for about a week.

**A player bought the DLC on Steam but plays on Steam Deck, or moved from Switch to Switch 2.**
The DLC is counted on the device that reports it. A new device with a new `user_id` looks like a new player.

## Related

- [Measurement API](../attribution/measurementapi.md) and [Telemetry Setup](../attribution/telemetry.md): the endpoint DLC events are sent to.
- [Console Launch Playbook](../attribution/console-launch.md): keeping `user_id` stable on PlayStation, Xbox and Nintendo.
- [Player Lifecycle](player-lifecycle.md): reactivations and retention for the same players.
