# Console Launch Playbook

<p class="docs-audience">For: Studio engineering, production and release management</p>

This playbook covers game-client integration with the TRACKS [Measurement API](measurementapi.md) on **PlayStation 5, Xbox Series X|S / Xbox One (GDK) and Nintendo Switch / Switch 2**, with Steam / PC as the reference platform.

## Why this playbook exists

Console launches give you very little room to fix things after release. Every fix goes through platform submission, patches take days or weeks, and **telemetry identity mistakes cannot be repaired afterwards**. If a player's ID changes every launch, nothing can later rebuild their retention curve or cohort.

We've supported several multi-platform launches (Steam + PS5 + Xbox + Switch). The same few problems keep coming up, and almost all of them could have been caught with a test build weeks before certification. This playbook covers:

1. What the game client must do (three identity requirements)
2. How each console platform stores data, and what certification will test
3. Which work to **start in parallel with certification** so it doesn't block your launch date
4. A self-test checklist and a joint validation step before you submit

!!! tip "The single most useful check"

    Launch the game twice on the same device. If the second launch sends a different `user_id` than the first, stop and fix that before anything else. This one check catches most of the problems described below.

## 1. The Measurement API in one minute

The game sends a small JSON event to the Measurement API endpoint every time it starts. TRACKS uses these events to count installs, measure retention and cohorts, and attribute installs to the ad campaigns that drove them.

```http
POST https://<your-measure-endpoint>/measure
Authorization: Bearer <your-token>
Content-Type: application/json
```

```json
{
  "event_name": "game_open",
  "user_id": "3f2b8c1e-9a4d-4e7b-b1c2-6d5e8f9a0b1c",
  "is_first_game_open": true,
  "first_session_timestamp": "2026-10-02T20:31:47Z",
  "timestamp": "2026-10-02T20:31:47Z",
  "platform": "PS5",
  "storefront": "PSN",
  "version": "1.0.3",
  "ip": "203.0.113.24"
}
```

You'll receive the endpoint URL and token during onboarding.

| Field | What it means |
|---|---|
| `event_name` | `game_open` on **every** launch. More gameplay events can use the same format later; get identity right first. |
| `user_id` | A stable ID for the player or install. Generate a UUID **once** (see R1). |
| `is_first_game_open` | `true` exactly once, on the real first run (see R2). This drives your install counts. |
| `first_session_timestamp` | The original install time, saved and sent unchanged on every launch (see R3). |
| `timestamp` | When this event happened, as UTC ISO 8601 (see §4). |
| `platform` | The hardware platform, e.g. `PC`, `PS5`, `XboxSeries`, `XboxOne`, `Switch`, `Switch2`. **We agree the exact values with you before the first console build. Don't change them after launch.** |
| `storefront` | Where the game was bought or installed, e.g. `Steam`, `Epic`, `PSN`, `Xbox`, `Nintendo`. We agree the exact values with you, as for `platform`. |
| `version` | The build version string. We use it to split data by build when debugging. |
| `ip` | The device's public IP address, used to match installs to ad clicks. If the game client sends events directly (for example through the [TRACKS plugin](telemetry.md#option-2-the-tracks-plugin)), we can read the IP from the connection instead; agree this with us. |

### Two things to build in from day one

- **The endpoint URL must be configurable** (server-driven config, or at least a patchable setting), never a hardcoded string. Console patches are slow, so changing the URL must not need a resubmission. This also lets you move to a branded endpoint on your own domain later.
- **Treat the token as a secret.** Ship it in build config, not anywhere a player can read, and don't publish it outside this integration.

## 2. The three identity requirements (all platforms)

### R1 — Keep `user_id` the same across launches

Generate a UUID **once**, on the real first run, and store it in the platform's persistent save storage. Every later launch must read and reuse that same value: after crashes, patches, console restarts, and going offline and back online.

- Only generate a new ID when the stored value is **actually missing** (fresh install, or deliberate recovery from corrupt data).
- Never generate a new ID because an event **failed to send**.

### R2 — Send `is_first_game_open: true` exactly once

Send `true` only on the run that created the `user_id`, and `false` on every launch after that.

### R3 — Save `first_session_timestamp` as the original install time

Capture it once, at the moment the `user_id` is created, store it with the ID, and send that stored value every time. It never changes.

### The implementation that gets all three right

!!! success "One saved record"

    Create **one small saved record**, `{ user_id, first_session_timestamp }`, in a single step on first run.
    `is_first_game_open` is then just: *"did this record already exist when the game started?"*

These three values succeed or fail together. If they're built as separate pieces of logic, one usually ends up broken.

## 3. Platform-by-platform: storage and what cert will test

The requirements above are the same on every platform. What differs is **how each platform stores data**, and that is also what certification looks at.

### PlayStation 5

- Save data storage is declared in the title's project configuration and goes to QA with the master submitted through the Partner Portal. Include the identity record in your save-data plan from the start, not as a late addition.
- Certification tests the **failure cases**: **save data missing, storage full, save data corrupt.** The identity record must survive each of these or be recreated cleanly. Recovering from a corrupt save by generating a new `user_id` is acceptable. Crashing, or sending malformed events, is not.
- **Do not gate telemetry on PSN sign-in.** Offline play must work, and a UUID needs no account. The identity record must be readable and writable without a signed-in network session.

### Xbox (GDK)

- Data is stored in **connected storage**, which syncs to the cloud by default. That keeps the ID the same across consoles for free, but you **must handle sync conflicts and roaming** (the same player on a second console). Cert will check both.
- Set the conflict rule in advance and apply it the same way every time, e.g. *keep the record with the older `first_session_timestamp`*.
- Be careful with `storefront`: some setups report the same store (e.g. "Xbox") for both console and **PC Game Pass**. `platform` must always identify the hardware.

### Nintendo Switch / Switch 2

- Save data is declared in the application's metadata. Set the **user-account save data size** and a large enough **journal size**. If the journal is too small, commits fail and the save can disappear without any error.
- Prefer **user-account save data** over device save data. It makes the ID per profile, which is the right meaning for a user ID, and you don't have to justify device-wide storage.
- **You must explicitly commit save data** with the SDK's commit call. Writes that aren't committed are thrown away silently. This is the most common reason a Switch build generates a new ID every launch.
- Save data size can **grow but never shrink** in later versions. Leave headroom now.
- The Switch system clock can be set by the user. See §4; this matters more on Nintendo than anywhere else.
- **Switch and Switch 2 are separate submissions.** Test identity on both, and give them distinct `platform` values.

### Steam / PC (reference)

- Store the identity record in a stable per-user location, or in Steam Cloud if you want it to follow the player across machines (decide deliberately, see the next section).
- Make sure it isn't stored somewhere wiped by "Verify integrity of game files", unless that is the behaviour you want.
- Check that the write actually happens and survives a process restart. A build that never saves the record looks fine in a single session.

### One decision you need to make: what is an "install"?

| Storage choice | What an "install" means |
|---|---|
| Local only (device or profile save) | One install per machine or profile |
| Cloud-synced (Xbox connected storage, Steam Cloud, cloud saves) | One install per player across all their devices |

Both are valid. **Choose one per platform, tell us, and keep it stable.** Switching partway through the game's life breaks every long-term metric.

## 4. Timestamps and device clocks

Console and PC clocks are user-adjustable and often wrong. We've received live data dated **decades in the past and years in the future** from consoles with bad clock settings.

- Send all timestamps as **UTC ISO 8601** (`2026-10-02T20:31:47Z`). Never local time, and never a bare epoch number where the unit isn't clear.
- Taking `timestamp` from the device clock is fine. Our servers also record when each event arrives, so normal drift can be corrected.
- **`first_session_timestamp` is different.** It's captured once and kept forever, so a first run on a clock set to 2031 stays wrong for good. Use the platform's **network-synchronised time** at first run if it's available. On Nintendo, fall back to the steady (monotonic) clock rather than the user clock.
- Events queued offline keep their **original** timestamps. Don't replace them with the send time.

!!! warning "Fix both together"

    Fixing identity without fixing the clock gives you stable IDs with wrong install dates. Fix both in the same patch.

## 5. Start these in parallel with certification

Compliance and platform configuration take longer than the code change. Start these as soon as the telemetry design is agreed, not when the launch candidate is ready.

| Workstream | What to do | Why it can't wait |
|---|---|---|
| **Privacy policy** | Update it to cover the telemetry you collect, and have it **live before submission** | Reviewers follow the link during cert |
| **Platform data declarations** | Update the data-collection declarations in each platform's partner portal (Sony, Microsoft, Nintendo, Steam) | Each platform has its own form and review |
| **Child accounts** | Check your age rating and expected audience against each platform's rules for data from child accounts | This can limit what you're allowed to collect, whatever cert says about save data. Better to find out before submission than after a failed submission |
| **Save-data configuration** | Include the identity record in the PS5 project configuration, the Nintendo save-data sizes and the Xbox connected-storage setup | Part of the submission package; Nintendo sizes can't shrink later |
| **Platform values** | Agree the `platform` and `storefront` values with us | Changing them after launch splits reporting |
| **Endpoint configuration** | Make the URL configurable; optionally set up a branded endpoint on your own domain (a couple of DNS records from you) | Changing a hardcoded URL later needs a patch and resubmission |
| **Joint validation (§7)** | Send a test build's events to the endpoint | Must pass **before** the launch candidate goes to cert |

### Suggested sequence

1. **First playable builds:** integrate the identity record and `game_open`. Agree platform values. Make the endpoint configurable.
2. **First console dev and QA builds:** run the §6 self-test checklist on every platform. Send events to the endpoint so we can watch them.
3. **Before the launch-candidate submission:** pass the joint validation (§7). Privacy policy live, portal declarations updated, child-account assessment done.
4. **During cert:** don't touch identity code. A cert fix that changes save-data handling should be re-run against the §6 checklist.
5. **Launch week:** we watch install, retention and attribution data closely and flag anything unusual.
6. **First patch:** if identity needs fixing, fix it going forward. **Never reset existing players' IDs**, and treat an existing record as "not first open".

## 6. Self-test checklist (run on every platform before cert)

For each case, confirm the events behave as specified: same `user_id`, correct `is_first_game_open`, and an unchanged `first_session_timestamp`.

- [ ] **Second launch, same device → same `user_id` as the first launch** *(do this first)*
- [ ] Fresh install, no save data → new ID, `is_first_game_open: true`, timestamp set once
- [ ] Third launch on a different day → same ID, flag `false`, same `first_session_timestamp`
- [ ] Save data from an earlier build or version → existing ID reused, flag `false`
- [ ] Storage full → handled cleanly, no malformed events
- [ ] Save data corrupt → clean recovery, with the behaviour documented
- [ ] Platform account not signed in, or offline → still works, and queued events keep their original timestamps
- [ ] Device clock deliberately set wrong (forward and back) → `first_session_timestamp` unaffected on later launches
- [ ] Multiple local profiles on one console → each profile follows your §3 "install" decision
- [ ] Cloud-save restore onto a second console → follows your §3 decision; no second "first install"
- [ ] **Each platform tested separately**, incl. Switch **and** Switch 2, and Xbox Series **and** Xbox One where shipped

## 7. Joint validation before you submit

Once a test build sends events to the endpoint, tell us. **Within one working day** we'll check:

1. **ID stability:** the same `user_id` across multiple days from the same test device.
2. **Install meaning:** exactly one `is_first_game_open: true` per test device, `false` after that.
3. **Timestamp stability:** `first_session_timestamp` is identical on every event from a device, and event timestamps are plausible UTC.
4. **Per-platform coverage:** at least one clean pass of the §6 checklist visible in the data for **every** platform you ship.

!!! tip

    Several QA launches spread over a few days on each console tell us much more than one event. One event can't prove the ID persists. Repeat launches can.

Once these four checks pass, install, retention, cohort and attribution reporting will be correct from day one.

## 8. What we've seen go wrong (and how to avoid it)

These are real patterns from multi-platform launches, anonymised.

| What happened | Why it happened | How to avoid it |
|---|---|---|
| **Every launch counted as an install.** All events said `is_first_game_open: true`, and the user ID and timestamp were new each session. | The identity record was never saved between launches | Build the single-record approach (§2); run "second launch, same device" |
| **ID persistence fixed, but the install flag was inverted on every platform at once** (always `false`). Installs dropped to zero after launch. | The flag logic was in shared code, so one bug affected all platforms | Test the flag explicitly on a fresh install on every platform, not just the ID |
| **Console IDs changed every launch on two platforms while a third worked.** | Each console's save path is different; one being right says nothing about the others | Test each platform separately. Never assume one console's result carries over |
| **`storefront` repeated the platform name** (e.g. "Xbox/Xbox" instead of "Xbox/Microsoft Store") on exactly the devices with broken IDs | Platform services were queried before the user or save-data context was ready | Initialise telemetry **after** the user/profile and save data are loaded |
| **Nintendo build sent zero installs.** The flag was always `false` on Switch. | The Nintendo build never took the first-run path | Include Switch and Switch 2 in the fresh-install test |
| **Events dated 2000–2053** from one console family | User-adjustable system clock, used for the install timestamp | Use network-synchronised time for `first_session_timestamp` (§4) |
| **Developer sessions in production data** (editor or dev-kit platform values, hand-written test events) | Dev and QA builds pointed at the production endpoint without being marked | Send dev and editor builds to a test endpoint, or tag them clearly; never send hand-written payloads to production |
| **Players coming from a demo or early access looked like new installs**, or were never counted | Demo and full game shared or reset IDs without anyone deciding which | Decide whether demo IDs carry over, and use a distinct `version` or app identifier for the demo |

## Quick reference

- One record `{ user_id, first_session_timestamp }`, created once, on every platform.
- `is_first_game_open` = "did the record already exist?"
- UTC ISO 8601 everywhere; network time for the install timestamp.
- PS5: handle missing, full and corrupt saves; no PSN gating.
- Xbox: handle sync conflicts and roaming; `platform` ≠ `storefront`.
- Nintendo: commit your writes, size the journal, leave headroom; Switch and Switch 2 tested separately.
- Configurable endpoint URL; token kept secret.
- Privacy policy, portal declarations and child-account review **start now, in parallel**.
- A test build to us **before** cert, with four checks passed per platform.

## Related

- [Measurement API](measurementapi.md): endpoint, payload fields and status codes.
- [Telemetry Setup](telemetry.md): backend or plugin routes for sending events.
- [Custom Domains](../platform/domains.md): a branded endpoint on your own domain.
- [DLC Tracking](../reporting/dlc.md): sending DLC ownership on the same events.

Questions about payload details, platform values or a branded endpoint: [contact us](../support/contact.md).
