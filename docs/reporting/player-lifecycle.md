# Player Lifecycle: Retention, Churn & Reactivation

<p class="docs-audience">For: UA and marketing leads, producers</p>

The Player Lifecycle report shows which media channels bring players who keep playing, not only players who install. Every metric is built from in-game Game Open events sent to TRACKS, joined to the TRACKS attribution of each player's install.

It answers four questions:

- **Who is playing today?** Daily active players, split into new installs and returning players.
- **Who stays?** D1 to D30 retention by country, channel, platform, storefront and game version.
- **Who leaves?** 30-day churn of installs that are old enough to judge.
- **Who comes back?** Players who return after 30 or more days away (reactivations).

The report is for UA and marketing leads judging channel quality, and for producers watching the health of the live player base.

## Lifecycle states and definitions

A player is "active" on a day when the game sends at least one Game Open event for them that day. Days are UTC calendar days. Every other state is derived from those active days and the player's install day.

| State | Rule | Counted on |
| --- | --- | --- |
| **Install (Day 0)** | The player's first detected Game Open. Install day = that event's UTC date. | Install date |
| **Daily active player (DAU)** | At least one Game Open on that day. One player counts once per day. | Activity date |
| **Returning player** | Active on a day after their install day. Players with no install record are also counted here. | Activity date |
| **Retained on Day N** | Active on exactly day N after install (N = 1, 3, 7, 14, 30). Not cumulative. | Install date |
| **Matured install (30d)** | Installed 30 or more days ago, so a full 30-day window has been observed. | Install date |
| **Returned (30d)** | A matured install that was active at least once on days 1 to 30 after install. | Install date |
| **Churned (30d)** | A matured install with no Game Open on days 1 to 30 after install. | Install date |
| **Reactivated player** | Active today, not on their install day, and their previous active day was more than 30 days earlier (31+ days apart). | Activity date |

Retained on Day N is a spot check. A player who skips day 7 but plays on day 14 counts for D14, not D7. For "still playing by day N", use the cohort matrix instead.

Churn and reactivation use the same 30-day threshold but measure different things. Churn judges each install's first 30 days. Reactivation can happen at any point in a player's life, including a player who already counted as returned.

## How TRACKS computes it

The game sends a Game Open event to the TRACKS Measurement API on every launch. TRACKS turns each player's first Game Open into an install, attributes it to the ad or link click that brought them in, and then follows their active days.

![Player Lifecycle data flow: the game sends a Game Open event on every launch; the first one marks the install, which is credited to an ad or link click; active days then feed DAU, retention, churn and reactivations](../assets/diagrams/lifecycle_flow-light.svg#only-light)
![Player Lifecycle data flow: the game sends a Game Open event on every launch; the first one marks the install, which is credited to an ad or link click; active days then feed DAU, retention, churn and reactivations](../assets/diagrams/lifecycle_flow-dark.svg#only-dark)

## Metrics and formulas

Every rate is a sum of counts divided by a sum of counts, so it stays correct under any filter or breakdown. Never average percentages across rows.

| Metric | Formula |
| --- | --- |
| **Total Installs** | Players whose install day falls in the date range |
| **Total Unique Players** | Distinct players with at least one Game Open in the range |
| **DAU** | Distinct active players per day |
| **WAU (last 7 days)** | Distinct active players over the last 7 days |
| **MAU (last 30 days)** | Distinct active players over the last 30 days |
| **Returning Players** | Active players on a day that is not their install day |
| **Share of Returning Players %** | Returning Players ÷ Active Players |
| **D1 / D3 / D7 / D14 / D30 Retention %** | Retained on Day N ÷ Installs |
| **Cohort Matrix cell** | Distinct players from an install cohort active on day N after install (N = 0 to 30) |
| **Matured Installs 30d** | Installs made 30 or more days ago |
| **Return Rate % (30-day lookback)** | Returned within 30 days ÷ Matured Installs |
| **Churn Rate % (30-day lookback)** | Churned (30d) ÷ Matured Installs |
| **Reactivated Players (30d inactivity)** | Active days that follow a gap of more than 30 days |
| **Share of Reactivated Players %** | Reactivated Players ÷ Active Players |

Return Rate and Churn Rate always add up to 100% of matured installs.

!!! note "Unique counts don't add up"

    DAU, WAU and MAU are distinct counts. A week's DAU values cannot be summed into WAU, and weekly values cannot be summed into a month.

## Dashboard walkthrough

**Filters.** Date range, Version, GEO, Channel, Platform and Storefront. Channel, GEO, Platform, Storefront and Version describe the player's install, not the day they played.

### 1. Headline KPIs

- **D1, D3, D7, D14, D30 Retention %** for installs in the selected range.
- **Total Unique Players, Total Installs, WAU (last 7 days), MAU (last 30 days)**, each with its change against the previous period.

### 2. Daily Trends

**DAU vs Installs & Returning Players.** The line is DAU; the bars split it into new installs and returning players. A tall installs bar means today's activity is driven by acquisition. A tall returning bar means it rests on the existing player base. Launches, sales and content updates show as spikes in one or the other.

### 3. Retention by GEO and Channel

- **Retention by GEO.** One row per country: installs, then D1 to D30 retention with in-cell bars. Sort by installs to focus on markets with enough volume.
- **Retention by Channel.** Bars show D1 to D30 retention per channel; the line shows installs on the right axis. Read a channel's curve against its volume: a high curve on a few hundred installs is weak evidence.

### 4. Churn & Reactivations

- **Tiles:** Churn Rate % (30-day lookback), Share of Reactivated Players %, Share of Returning Players %.
- **Daily Trend Reactivations.** Installs and returning players as bars, reactivated players as a line. Reactivation peaks usually follow updates, sales or re-engagement campaigns.
- **Churn by GEO and Churn by Channel.** Installs, matured installs, Return Rate % and Churn Rate % per row. Only matured installs (30+ days old) enter the rates, so recent installs never inflate churn.
- **Reactivated Players by Channel and by GEO.** Active players, reactivated players and the reactivated share per row. The channel here is the player's original install channel.

### 5. Cohort Matrix

Rows are install cohorts (for example, grouped by install month) and columns are days since install. Each cell is the number of players from that cohort active on that day. Read across a row to see how fast a cohort decays; read down a column to compare cohorts at the same age. Empty rows are periods before tracking started.

## Requirements per game

The report needs one Game Open event per game launch, sent to the game's TRACKS Measurement API endpoint. No extra events are needed for retention, churn or reactivation.

| Field | Example | Why it matters |
| --- | --- | --- |
| `event_name` | `game_open` | Marks an active day. The name is configurable per game. |
| `user_id` | a stable player or account ID | Must stay the same across sessions and reinstalls, or one player becomes several installs. |
| `timestamp` | `2026-08-20T12:00:00Z` | Sets the activity day (UTC). Send ISO 8601 with a time zone. |
| `is_first_game_open` | `true` on the very first launch | Marks the install. |
| `first_session_timestamp` | `2026-08-20T12:00:00Z` | Install time; an alternative install signal when no first-open flag exists. |
| `ip` | `203.0.113.7` | Country and click matching. |
| `platform`, `storefront`, `version` | `PC`, `Steam`, `1.0.3` | Report filters and breakdowns. |

Attribution by channel also needs [TRACKS tracking links](../support/trackinglinks.md) or the [TRACKS website tag](../platform/landingpages.md) on the paths players take to the store. Without them, every install lands in Direct.

## Caveats and FAQ

**Why is D30 retention so low for the last few weeks?**
Retention divides by all installs in the date range, including players who have not reached day 30 yet. For a fair D30 figure, end the install range at least 30 days ago (14 days ago for D14).

**Why is Direct so large in active players?**
Players with no install record count as returning and have no channel, so they land in Direct. This covers players who installed before TRACKS tracking started and installs no click could be matched to.

**Can reactivations be sent to ad platforms?**
Yes, as an additional Reactivation postback per game. It needs its own event name, value and currency. Only confident and consented matches are sent, 1 to 7 days after the return, for clicks within 30 days before it. See [Conversions & Audiences](../attribution/postbacks/conversions-audiences.md).

**Can a player reactivate more than once?**
Yes. Each return after a gap of more than 30 days is a separate reactivation.

**Why are churn and reactivations empty for a new game?**
Churn needs installs at least 30 days old, and a reactivation needs a 31-day gap. Both stay empty for the first month after launch.

**Why did recent numbers change after I looked?**
Late events are folded in on every pipeline run, so the most recent days can still move. Treat the last 2 to 3 days as provisional.

**Which clock defines a day?**
The timestamp the game sends, converted to UTC. A wrong device clock can move a session to another day.

**What if a player uses two platforms?**
They count as one player only if the game sends the same `user_id` on both. Otherwise each platform is a separate install.

**Demo and full game?**
For games with a demo, use the Version filter to separate demo and full-game players. See [Demo → Full Game Conversion](demo-conversion.md).

## Related

- [Telemetry Setup](../attribution/telemetry.md) and [Measurement API](../attribution/measurementapi.md): how the game sends Game Open events.
- [Marketing Analytics](../support/marketinganalytics.md#post-launch-lifetime-value): retention and LTV in the wider KPI picture.
- [Glossary](../glossary.md#d): DAU, retention, churn and reactivation in one line each.
