# Conversions & Audiences

<p class="docs-audience">For: Ad ops / performance marketing</p>

A purchase postback is used in three different ways: reporting, optimization, and audience building. Each one counts something different, so the three numbers will never match. Gaps between TRACKS installs, platform-reported conversions, and ad-platform audience sizes are expected rather than a sign of a broken setup.

!!! note

    This page assumes postbacks are already running. For what a postback is and how to enable it, see the [Postbacks overview](index.md).

## The three numbers

| | Counts | The platform needs |
|---|---|---|
| **Reported conversions** | Events credited to one of its ads | The click ID, inside its attribution window |
| **Optimization events** | Events the bidding algorithm learns from | Enough volume that arrives quickly, roughly 50 per ad set per week |
| **Audience size** | Unique people it can identify **and** is allowed to target | Far more than a click ID alone |

Postbacks are strong for the first two. They are weak for the third, for the reasons below.

## Conversion gaps

**Attribution windows.** TRACKS defaults to a 30-day click window. Meta's default is 7-day click and 1-day view. A purchase 10 days after the click is received and recorded by TRACKS, but Meta will not credit it to a campaign.

**Conversions are booked on the click date.** Platforms such as Reddit and Google Ads record a conversion against the date of the ad click, not the date of the purchase. Someone who clicked a pre-launch or demo ad and bought at launch appears in that earlier campaign, on those earlier dates. A report filtered to launch onwards hides them. Always compare over the full flight, including pre-launch, demo, and pre-order campaigns.

**Consent.** Metrics in the TRACKS suite are not bound to cookie consent and use aggregated session stitching for non-consented visitors. Conversions reported in an ad platform are consent-bound. The two populations are not the same.

## Audience size limits

A conversion is an event. An audience is a list of people, and a person has to clear three more hurdles to join one.

**Events are not people.** A PageView, a Lead, and a Purchase can all belong to one person. An audience counts that person once.

**Identification.** The purchase happens in a store and a game, not in a browser. There is no cookie, no login, and no email at that moment. The only thread back to the ad platform is the click ID TRACKS captured on the website.

**Eligibility.** The platform then silently removes people it is not allowed to target: iOS users who opted out of tracking, people who disconnected their off-platform activity, minors, users without personalized-ads consent in some regions, and inactive accounts. These rules are not published and cannot be measured from outside.

**Display floors.** Meta shows any audience under 1,000 as "Below 1,000". Reddit treats audiences under 1,000 as too small to target.

A Purchasers audience showing "Below 1,000" while conversions run into the thousands is normal, especially in the first weeks of a campaign. It still works as a lookalike seed and as an exclusion list, and it grows over time.

## Platform differences

| Platform | Reporting date | Audience from postbacks |
|---|---|---|
| **Meta** | Ad impression or click date | Possible but small. Lookalikes work from small seeds; website (Pixel) audiences are far larger |
| **Reddit** | Click date | Possible but small, and needs 1,000 to be valid |
| **Google Ads** | Click date, with "by conv. time" columns available | **No.** Uploaded conversions never become audience segments. Use the Google tag, GA4, YouTube engagers, or Customer Match |
| **TikTok** | Platform default | Possible but small, same principles as Meta |
| **GA4** | Event date | Through GA4 audiences, if linked to Google Ads |

## Optimization events

| Situation | Optimize for |
|---|---|
| Pre-launch or wishlist phase | Lead, Add to Wishlist, or Add to Cart. No purchases exist yet, and browser events are real-time and high volume |
| Ad set gets fewer than 50 purchases a week | Add to Cart or Lead. Purchase is too sparse and the ad set stays "Learning limited" |
| Ad set gets 50 or more purchases a week | Test Purchase. It is the real business outcome and carries value |
| Many small ad sets | Consolidate first, then test Purchase |

To test Purchase optimization safely, duplicate your largest ad sets and set the copies to optimize for Purchase. Do not edit the live ones, because changing the optimization event restarts learning. Run both for two to three weeks and compare cost per Purchase rather than day-one results.

Postbacks arrive hours after the purchase, not seconds, because TRACKS sends them in batches several times a day. Meta's performance degrades on events older than roughly two hours, so Purchase optimization can learn more slowly than Add to Cart or Lead.

## Audience selection

| Goal | Use | Avoid |
|---|---|---|
| **Retargeting** | Website visitors and store-button clickers, from the browser pixel | Relying on the Purchasers audience for reach |
| **Excluding buyers** | Website visitors minus Purchasers | Expecting it to catch every buyer, since it only removes identifiable ones |
| **Prospecting** | A lookalike seeded from Purchasers, which works under 1,000 | Waiting for the seed to grow first |
| **Google and YouTube** | Google tag or GA4 audiences, YouTube engagers | Expecting uploaded Purchase conversions to become an audience |

## Postback events

| Event | When it fires | Value |
|---|---|---|
| `Purchase` | A full-game install on any storefront, at the player's first launch of the full game | Price |
| `Purchase_PC` / `_PS` / `_Xbox` / `_Nintendo` | The same install, split by storefront. Fires alongside `Purchase` | Price |
| `Demo_Installs` | First launch of the demo. `Purchase` does not fire for these | 1 |
| `Reactivation` | A lapsed full-game player returns. Not sent for demo players | 1 |
| `Lead` | A store-button click on the website | 1 |
| `Lead_Steam` / `_PS` / `_Xbox` / `_Nintendo` | The same store-button click, split by storefront | 1 |
| `PageView` | A page view on the marketing landing page | 1 |

The storefront events are a split of the same installs counted by `Purchase`, so do not add them together in reporting. A demo player who later buys the full game counts once, on the full-game launch. Purchase value is a dynamic per-install price based on Steam regional pricing at the time.

## Reporting guidance

- Compare TRACKS against the platform over the full flight, not just the launch window.
- Expect platform conversions below TRACKS installs. The platform only credits its own window.
- Never compare conversion counts against audience sizes. They measure different things.

*Sources: [Meta Conversions API server event parameters](https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/server-event), [Meta custom audiences](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/custom-audiences), [Google Ads data segments](https://support.google.com/google-ads/answer/2453998?hl=en).*
