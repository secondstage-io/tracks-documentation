# Audience Segments

<p class="docs-audience">For: Ad ops / performance marketing</p>

Audience segments are two optional postback events that exist to **build audiences** on the ad platforms, not to measure conversions. They let you reach players you could not otherwise identify: the purchase and the play happen in a store and a game, and the click ID TRACKS captured on your website is the only thread back to the ad platform.

!!! note

    This page assumes postbacks are already running. For what a postback is and how to enable it, see the [Postbacks overview](index.md). For why audience sizes differ from conversion counts, see [Conversions & Audiences](conversions-audiences.md).

## The two segments

| Segment | Event | A player qualifies when | Sent |
|---|---|---|---|
| **Returned in week 2** | `TRACKS_Week2_Active` | They played on any day 7–13 after their install | Once per player |
| **Lapsed players** | `TRACKS_Lapsed_30d` | They have not played for 30 full days | Once each time they lapse |

- **Returned in week 2** is an engaged-owner signal: the player bought the game and came back after the first week.
- **Lapsed players** are owners who stopped playing. A player who returns and later lapses again is sent again, so the audience reflects the current lapse.
- Both events carry a value of 0. They are not purchases and should never be used as an optimization or conversion goal.
- Event names can be changed on request. GA4 receives them in lowercase (`tracks_week2_active`, `tracks_lapsed_30d`), and Snapchat uses a custom event slot (`CUSTOM_EVENT_3` / `CUSTOM_EVENT_4` by default).

## Who can be reached

A player can only be sent to a platform if their install was matched to a click on **that platform's** ad, with its click ID. GA4 is the exception: it uses the GA4 visitor who came through your website. So each platform's audience covers the players it brought in, not your whole player base, and a platform with little spend will have a small audience.

Google Ads, DV360 and X do not receive these events. See [Google Ads and YouTube](#google-ads-and-youtube).

## How to use them

| Goal | Use |
|---|---|
| **Stop paying to reach owners** | Exclude *Returned in week 2* from prospecting campaigns |
| **Find more players like your engaged ones** | Seed a lookalike audience from *Returned in week 2* |
| **Bring players back for an update, season or DLC** | Retarget *Lapsed players* |

Players who come back stay in the *Lapsed players* audience until its retention expires: the platforms are not told when someone returns. Keep its retention short (30–60 days) so the list stays current.

## Turning them on

<ol class="setup-steps" markdown="1">

<li markdown="block">

### Ask TRACKS to enable the segments

Tell your TRACKS contact which segments and which platforms you want. Postbacks for those platforms must already be set up.

</li>

<li markdown="block">

### Create the GA4 audiences first (if you use GA4)

GA4 audiences only collect members from the day they are created, so create them **before** the one-time backfill below. See [GA4](#ga4) for the steps. Meta, TikTok, Reddit and Snapchat audiences can be created at any time: they look back over events already received.

</li>

<li markdown="block">

### One-time backfill

TRACKS sends both events to every player who already qualifies, going back up to 180 days (the longest audience retention the platforms offer). A large backfill can take a few hours. It runs alongside the regular postbacks, and no player is sent twice.

</li>

<li markdown="block">

### Daily sends

From then on, new qualifiers are sent with the regular postback runs, several times a day.

</li>

</ol>

## Building the audiences

The events appear in each platform's events manager once the first ones arrive. Then create a custom audience on them:

| Platform | Where | Notes |
|---|---|---|
| **Meta** | Audiences → Create audience → Custom audience → **Website** → your dataset → the event | The events are sent server-side. If they are not offered under Website, contact us. For a hard exclusion in Advantage+ campaigns, add it under **Audience controls** |
| **TikTok** | Assets → Audiences → Create → Custom audience → **Website traffic** → your pixel → the event | Needs roughly 1,000 matched users to deliver |
| **Reddit** | Audiences → Custom audience → **Website retargeting** → your pixel → event type **Custom** → the event name | Minimum roughly 1,000 |
| **Snapchat** | Audiences → Pixel custom audience → the custom event slot | Minimum roughly 1,000 |

### GA4

1. In Google Analytics, go to **Admin → Data display → Audiences → New audience → Create a custom audience**.
2. Under **Include users when**, add the event `tracks_week2_active` (or `tracks_lapsed_30d`). Keep the default scope, *Across all sessions*.
3. Set the **membership duration**: up to 180 days for *Returned in week 2*, 30–60 days for *Lapsed players*.
4. Save. Repeat for the second segment.

If the event is not offered yet (GA4 lists events it has already received), contact us before the backfill.

### Google Ads and YouTube

GA4 is the only route for these segments into Google Ads:

- Uploaded conversions never become remarketing lists.
- Customer Match needs emails or phone numbers, which TRACKS does not have.
- Google tag audiences are filled only by the browser tag.

With GA4 linked to Google Ads (**Admin → Product links → Google Ads links**, with **personalized advertising** enabled), GA4 audiences appear in **Google Ads → Tools → Shared library → Audience manager** within 24–48 hours. Display serves from about 100 active users; YouTube and Demand Gen need about 1,000.

## Limits

- **Reach.** Only players matched to a platform's click (or GA4 visitor) can be sent. Platforms then silently remove people they cannot or may not target, as described in [Conversions & Audiences](conversions-audiences.md#audience-size-limits).
- **Consent.** In regions where personalized advertising needs consent, the platforms may leave some players out of the targetable part of an audience. Compare the audience size in the ad platform with the number of events sent.
- **No attribution credit.** Lapsed players' clicks are usually older than any attribution window, so platforms will rarely credit a return to the retargeting campaign. Judge a lapsed campaign by comparing return rates against a holdout group (ask us).
- **Event age.** Daily events are sent within about 60 hours of qualifying, inside GA4's 72-hour limit and the 7-day limit of Meta and Snapchat.
