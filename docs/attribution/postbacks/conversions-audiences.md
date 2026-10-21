# Conversions, Postbacks & Audiences: A Practical Guide

<p class="docs-audience">For: Agencies and game teams running paid media with TRACKS</p>

Purchase postbacks are used in three different ways: **reporting**, **optimisation** and **audiences**. Each use counts something different, so the three numbers will never match. This guide explains what each term means, why the numbers differ, and which tool to use for which goal.

---

## TL;DR

- **TRACKS installs, platform conversions and audience sizes measure different things.** Gaps between them are normal and expected.
- **Postbacks (server-side events, also called CAPI) are built for reporting and optimisation.** They tell the platform "this ad click led to a purchase (Install)".
- **Postbacks can be weak at building audiences in early campaigns.** In-game purchases carry no browser cookies and no email, so a platform can only identify a person through the original ad click. Its own privacy and eligibility rules then remove many of those people. "Below 1,000" on a Purchasers audience is common in the first weeks of your campaign.
- **For retargeting, start with browser-based audiences** (website visitors / PageView events, store-button clicks / Web Conversions / Leads). For prospecting, use **Purchasers as a lookalike seed**. Lookalikes work even when the seed is under 1,000.
- **Purchase can be the optimisation event** for ad sets that get **~50+ Purchases a week**. Test it alongside your current setup rather than switching everything at once.

---

## 1. The vocabulary

| Term | What it is | Example |
|---|---|---|
| **Pixel / browser tag** | Code on the website that sends events from the visitor's browser, with the platform's cookies. | Meta Pixel, Reddit Pixel, Google tag |
| **Web conversion** | An action on the website, recorded by the pixel. | Page View, **Lead** (= store-button click or Add_to_Cart) or Add to Wishlist |
| **Click ID** | A unique ID the platform appends to the landing URL when someone clicks an ad. | `fbclid` (Meta), `rdt_cid` (Reddit), `gclid` / `gbraid` / `wbraid` (Google), `ttclid` (TikTok) |
| **Postback / CAPI** | A server-to-server event that TRACKS sends to the platform after something happens **outside the website**, e.g. in the game. It carries the click ID. | Purchase, Demo Install, Reactivation |
| **Conversion (reported)** | An event the platform has **credited to one of its ads**, within its attribution window. | "1,940 Purchases" in Ads Manager |
| **TRACKS Reported Installs, Web Conversions** | Metrics shown on TRACKS suite are not cookie consent bound, and utilizes aggregated session stitching for non-consented visitors, however conversions reported on ad platforms are cookie consent bound and visitor needs to accept the cookies | "1,000 Installs" in TRACKS Suite, "400 Purchases" in Meta Ads Manager, "100 Purchasers" in Meta Custom Audiences |
| **Optimisation event** | The event the campaign's algorithm is told to find more of. It drives bidding and delivery. | Sales campaign optimising for Purchase or for Lead or Add to Cart |
| **Custom audience** | A list of **people** (not events) the platform can show ads to, or exclude. | "Purchasers, last 180 days" |
| **Lookalike audience** | New people who resemble a seed audience. | "3% lookalike of Purchasers" |
| **Attribution window** | How long after a click or view a conversion can still be credited to the ad. | Meta default: 7-day click, 1-day view, TRACKS Default 30-day click |
| **Learning phase** | The period in which the algorithm gathers enough optimisation events to stabilise delivery. | Meta: ~50 events per ad set per week |

---

## 2. How the data flows

```
 Ad click ──► Website (pixel fires: Page View, Lead or Add to Cart; click ID captured)
                │
                ▼
             Store (Steam / PlayStation / Xbox / Nintendo)  ← no pixel here
                │
                ▼
             Game install / purchase  ← reported by the game to TRACKS ──► Reported on TRACKS Dashboards as Installs, Web Conversions
                │
                ▼
      TRACKS links the install to the original ad click
                │
                ▼
      Postback (server event with the click ID) ──► Checks if the ad clicker person accepted marketing consent ──► Ad platform
                                                                                                                  ├─ Reporting   (conversions)
                                                                                                                  ├─ Optimisation (bidding)
                                                                                                                  └─ Audiences   (people lists)
```

The key point is that **the purchase happens in a store and a game, not in a browser.** There is no cookie, no login and no email at that moment. The only thread back to the ad platform is the click ID that TRACKS captured on the website.

---

## 3. One event, three uses

| | **Reporting** | **Optimisation** | **Audiences** |
|---|---|---|---|
| **Counts** | Events credited to an ad | Events the algorithm learns from | Unique, **eligible** people |
| **The platform needs** | The click ID within the attribution window | Enough volume (≈50/ad set/week) that arrives quickly | To identify the person **and** be allowed to target them |
| **Postbacks are** | ✅ Strong | ✅ Good, if volume and freshness are there | ⚠️ Weak: many events can't become audience members |
| **Shows up as** | "Purchases" column | Learning status, cost per result | "Estimated audience size" |

---

## 4. Why the numbers won't match

Think of it as a funnel where each step filters further:

```
TRACKS paid installs            (every install linked to a paid click)
   ▼  only events that can be sent to that platform
Postbacks sent                  (Purchase events delivered to the platform)
   ▼  platform credits only clicks inside its window, booked on the CLICK date
Platform-reported conversions
   ▼  events → unique people → only people the platform can identify and may target
Audience size
```

**Reasons for the drop at each step:**

1. **Attribution windows.** A purchase made 10 days after the click is received, but Meta's default 7-day click window doesn't credit it to a campaign.
2. **Reporting date.** Platforms such as Reddit and Google Ads book a conversion on the **date of the ad click**, not the date of the purchase. People who clicked a pre-launch or demo ad and bought at launch show up **in the earlier campaign, on the earlier dates**. A report filtered to "launch onwards" hides them. Always compare over the **full date range, including earlier campaigns**.
3. **Events ≠ people.** Several events like PageView + Leads + Purchase can belong to one person. An audience counts each person once.
4. **Identification.** Server events from a game have **no cookies, no email, no phone**. The platform can only use the click ID to find the person who clicked the ad.
5. **Eligibility rules.** The platform then silently excludes people it may not target. These rules are not disclosed and can't be measured from outside. They include iOS users who opted out of tracking (a large share of mobile traffic), people who disconnected their off-platform activity, minors, users without personalised-ads consent in some regions, and inactive accounts.
6. **Display floors.** Meta shows anything under 1,000 as **"Below 1,000"**. Reddit treats audiences under **1,000** as invalid for targeting.

---

## 5. Platform cheat sheet

| Platform | What TRACKS sends | Reporting date | Audience from postbacks? | Notes |
|---|---|---|---|---|
| **Meta** | Click ID (`fbc`), IP, TRACKS user ID, value + currency | Ad impression / click date (default) | Possible, but small: "Below 1,000" is common | Lookalikes work from small seeds. Website audiences (Pixel) are far larger. |
| **Reddit** | Click ID, IP, TRACKS user ID, value + currency | Click date | Possible, but small. **Min. 1,000** to be valid | Check conversions on **all campaigns**, including pre-launch ones. |
| **Google Ads** | `gclid` / `gbraid` / `wbraid`, value + currency | Click date ("by conv. time" columns exist) | **No.** Uploaded conversions never create audience segments. | Audiences come from the Google tag / GA4, YouTube, app users or Customer Match. `gbraid`/`wbraid` are privacy-aggregated IDs with no individual user behind them. |
| **TikTok** | Click ID, IP, value + currency | Platform default | Possible, but small | Same principles as Meta. |
| **GA4** | Website client ID, value + currency | Event date | Via GA4 audiences (if linked to Google Ads) | No click-based attribution. Used for analytics and GA4 audiences. |

---

## 6. Strategy playbook: what to use, when and why

### Optimisation: which event should the campaign bid on?

| Situation | Optimise for | Why |
|---|---|---|
| Pre-launch / wishlist phase | **Lead / Add to Wishlist / Add to Cart** (browser pixel) | No purchases exist yet. Browser events are real-time and high volume. |
| Launch, ad set gets **< 50 Purchases / week** | **Add to Cart or Lead** | Purchase is too sparse, so the ad set would stay "Learning limited". |
| Launch, ad set gets **≥ 50 Purchases / week** | **Test Purchase** | Purchase is the true business outcome and carries value. |
| Many small ad sets | Consolidate, then test Purchase | More events per ad set lets it exit the learning phase. |

**How to test Purchase optimisation safely:**

1. **Duplicate** your largest ad sets and set the copies to optimise for Purchase. Don't edit the live ones: changing the optimisation event restarts learning.
2. Run both for **2–3 weeks** and compare on **cost per Purchase**, not on day-one results.
3. Keep in mind that postbacks arrive **hours, not seconds,** after the purchase. TRACKS sends them in batches several times a day. Meta's performance drops when events are more than ~2 hours old, so Purchase optimisation may learn more slowly than Add to Cart or Lead.

### Audiences: which list should you build?

| Goal | Use | Avoid |
|---|---|---|
| **Retargeting** (bring back interested people) | **Website Visitors**, **Add to Cart or Lead or SubmitForm / store-button clickers** (browser pixel) | Relying on the Purchasers audience for reach |
| **Exclude existing buyers** | **Website Visitors minus Purchasers**, or exclude the Purchasers audience | Expecting the exclusion to catch every buyer, since it only removes identifiable ones |
| **Prospecting** (find new buyers) | **Lookalike seeded from Purchasers** (works under 1,000) | Waiting for the seed to reach a large size first |
| **Google / YouTube** | Google tag / GA4 audiences, YouTube engagers | Expecting uploaded Purchase conversions to become an audience |

Audiences built from postbacks **grow over time** as more purchases come in. Give them weeks, not days.

### Reporting: how to read platform numbers

- Compare **TRACKS vs platform over the full flight**, including pre-launch, demo and pre-order campaigns, because conversions are booked on the click date.
- Expect platform conversions **below** TRACKS installs because of attribution windows. The platform only credits its own window.
- Never compare **conversion counts** with **audience sizes**. They measure different things.

---

## 7. FAQ

**"We have thousands of Purchase conversions but the Purchasers audience shows 'Below 1,000'. Is something broken?"**

No. The events arrive and are counted correctly as conversions. An audience needs people the platform can identify **and** is allowed to target. Without cookies or email, only the ad click identifies the person, and the platform's eligibility rules (e.g. iOS tracking opt-outs) remove many of them. The platform doesn't disclose these rules.

**"The platform shows far fewer conversions than TRACKS installs. Who is right?"**

Both are, for what they measure. TRACKS counts every install linked to an ad. The platform counts only those inside its attribution window, marketing consent is granted and books them on the click date. Check the full date range, including earlier campaigns, before comparing.

**"Can we build a Google Ads audience from the Purchase conversions?"**

No. Google Ads doesn't turn uploaded conversions into audience segments. Use Google tag / GA4 audiences or YouTube engagers instead.

**"Should we switch our Sales campaigns to optimise for Purchase?"**

For ad sets with ~50+ Purchases a week, it's worth testing. Duplicate those ad sets rather than editing live ones. Keep smaller ad sets on Lead or Add to Cart, or consolidate them first.

**"Will the Purchasers audience get bigger?"**

Yes, slowly, as more purchases come in. Meanwhile it's already usable as a lookalike seed and as an exclusion list.

---

## 8. Example (anonymised PC/console launch, first ~2 weeks)

| Metric | Value |
|---|---|
| Purchase postbacks received by Meta | ~2,500 |
| Purchases Meta credited to campaigns | ~1,800 |
| Meta "Purchasers" custom audience | Below 1,000 (status: ready for use) |
| Meta "Website Visitors – 180 days" audience | ~60,000–70,000 |
| Purchases per week in the 5 largest ad sets | 56–383 (eligible for a Purchase-optimisation test) |
| Purchases per week in the 5 smallest ad sets | 8–29 (stay on Add to Cart) |
| Typical postback delay | a few hours (batched several times a day) |

Takeaways from this launch:

- The events were delivered and counted correctly.
- The Purchasers audience was small, as expected.
- The browser-based audience was large.
- The biggest ad sets had enough Purchase volume to test Purchase optimisation.

---

## 9. Checklist for agencies

- [ ] Pixel live on the website with **Page View** and **Add to Cart or Lead or SubmitForm** (store-button clicks).
- [ ] Ad links keep the platform click ID intact, so no redirect strips `fbclid` / `rdt_cid` / `gclid`.
- [ ] Platform conversion events created and named to match what TRACKS sends (e.g. `Purchase`).
- [ ] Reports compared over the **full date range**, including pre-launch campaigns.
- [ ] Retargeting built on **browser audiences**; Purchasers used as **lookalike seed** and **exclusion**.
- [ ] Purchase optimisation tested only on ad sets with **~50+ Purchases / week**, via duplicates.

## 10. TRACKS Conversion Events & Postbacks Framework

Here's an overview of the conversion events our TRACKS postbacks will send to the ad platforms once your Game launches.

### Postback events

| Event | When it fires | Value |
|---|---|---|
| `Purchase` | A full-game install on any storefront: the player's first launch of the full game | Price |
| `Purchase_PC` / `_PS` / `_Xbox` / `_Nintendo` | The same full-game install, broken down by storefront. Fires together with "Purchase" | Price |
| `Demo_Installs` | First launch of the demo (not the full game). "Purchase" does not fire for these | 1 |
| `Reactivation` | A lapsed full-game player returns. Not sent for demo players | 1 |
| `Lead` | Website behavioural intent event, Button Clicks to Storefront. | 1 |
| `Lead_Steam` / `_PS` / `_Xbox` / `_Nintendo` | The same website storefront button click event, broken down by storefront. | 1 |
| `PageView` | Standard Page View event of the marketing landing page. | 1 |

**Notes:**

- "Purchase" is the total of full-game installs. The storefront events are a split of the same installs, so don't add them to "Purchase" in reporting. Custom rules can be applied based on your choice.
- Event name is Purchase in order to utilize Standard Events of Ad Platforms but note that this is actually an "Install".
- A demo player who later buys the full game counts once as a full-game install, on the full-game launch.
- The Unit Price is a dynamic value per install, based on Steampowered Regional and today's pricing.

**Good to know:**

- To keep the pixels active, a small number of organic installs (at most 5 per platform per send) are also sent as "Purchase", if there is no attributed Install to a click for 7 days, postbacks system will go keep-alive mode.
- System default attribution window is 30 days, you can choose to adjust your attribution settings in ad platforms however you'd like.

---

*Sources:*

- [Meta Conversions API – server event parameters](https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/server-event)
- [Meta custom audiences guide](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/custom-audiences)
- [Reddit custom audience minimum size (Adobe Experience League)](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/advertising/reddit-custom-audience)
- [Google Ads – About your data segments](https://support.google.com/google-ads/answer/2453998?hl=en)
- [Learning phase (~50 events/week)](https://readme.anytrack.io/glossary/learning-phase.md)
- [CAPI data freshness](https://easyinsights.ai/blog/strategies-to-optimize-meta-conversion-api-capi/)
