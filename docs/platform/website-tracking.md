# Website Tracking Setup: GTM, Consent & Ad Pixels

<p class="docs-audience">For: Web / marketing admin, privacy owner</p>

## Why this matters

Your website is where paid traffic lands, so it decides how much of your ad spend TRACKS can attribute. Three things have to be right: one clean Google Tag Manager (GTM) container, a consent setup that tells Google and the ad platforms what each visitor allowed, and a small set of tags that record visits and store clicks.

When these are in place you get:

- Website visits and store clicks per campaign in your TRACKS dashboards
- Conversions sent back to Meta, Google, Reddit, TikTok and DV360, so their bidding optimises toward real players
- A setup that respects visitor consent in the EU/UK and stays measurable everywhere else

We set this up together, through Google Tag Manager. Everything lives in GTM, so the website code itself does not change: the only requirement on your side is the GTM snippet on your website (see [Landing Page Integration](landingpages.md#google-tag-manager-integration-access)). Your agency or marketing team does not need to do any extra ad-operations work.

## A good game marketing website

A strong game site does one job: turn a visitor from an ad into a wishlist, pre-order or install. Keep it simple, fast and focused on the store buttons.

| Element | Why it matters |
| --- | --- |
| Store buttons above the fold | Visitors see where to go without scrolling. One clear button per store (Steam, PlayStation, Xbox, Epic). A high contrast CTA without a drawer is suggested. |
| Trailer near the top | The fastest way to show what the game is. Visitors who watch are far more likely to click through. YouTube embed is suggested. |
| Newsletter sign-up | Builds an audience you own, for launch day and future updates. |
| Discord and social buttons | Lets visitors who aren't ready to buy still follow the game. Discord grows a community of day-one players, and social links (X, YouTube, TikTok, Instagram, Reddit) carry every update to your followers. |
| News and updates | Gives returning visitors a reason to come back, and keeps the page fresh for search engines. |
| Fast and mobile-friendly | Most ad traffic is on phones. A slow page loses visitors before it loads. |

**Search (SEO) advantage.** A real website ranks for your game's name and genre. Without one, search results go to stores, wikis and resellers you don't control. Clear page titles, descriptions, language versions and news posts all help.

!!! tip "No website or no web team?"

    [ReadySet.gg](https://readyset.gg){:target="_blank"} is our sister tool: a ready-made marketing website for studios, with all of the above built in.

## Why the website matters for your ads

Stores like Steam don't let you install ad pixels, so your website is the only place where ad platforms can see what happens after a click.

- **Pixels need a page.** By default we set up two signals for every platform: a PageView on arrival and a Lead when the visitor clicks a store button.
- **Postbacks build on it.** TRACKS later sends installs and purchases back to the platforms. The website visit is what connects that player to the ad, and the cookie banner on it is where marketing consent is captured, so no in-game consent prompt is needed. See [Data Handling & Security](../support/datasecurity.md).
- **Better signals, better bidding.** Platforms optimise toward the people who reach your site and click through, not just the cheapest clicks.
- **The page sets your conversion rate.** The same ad sent to a clear page with a trailer and visible store buttons gets more store clicks per visit than a cluttered one. A few points of web conversion rate can mean a much lower cost per wishlist.

## Google Tag Manager best practice

Keep every marketing and analytics tag in one GTM container, and keep the website code down to the GTM snippet and the cookie banner. Most issues we find in audits come from tags living in two places at once.

1. **One container, installed once.** Use Google's standard GTM snippet high in the page `<head>`, on every page and every language version.
2. **No hard-coded duplicates.** If GA4, Google Ads or a pixel is also pasted into the site code or added by a CMS plugin, it fires twice and doubles your numbers. Move it into GTM and remove the copy.
3. **Give TRACKS Publish access.** We need to add, test and publish tags ([how to invite us](landingpages.md#inviting-second-stage-to-your-gtm-account)). Your team keeps admin rights and sees every change in the version history.
4. **Track store clicks by link, not button text.** Triggers match the store link (Steam, PlayStation, Xbox, Epic). Button text changes with language and design, links do not.
5. **One owner per pixel.** Each ad platform has one pixel or account ID, agreed with whoever runs the media. Two agencies with two pixels split your data.
6. **Single-page sites need page-change tracking.** On sites built with frameworks like React, Next.js or Vue, we add a history-change trigger so page views are not missed.

## Consent setup (Google Consent Mode v2)

We set consent by the visitor's location: EU, UK and Swiss visitors start fully denied (GCS 100), everyone else starts with analytics allowed and advertising denied (GCS 101). The visitor's own choice in the cookie banner always overrides the starting point.

Google Consent Mode v2 is how your site tells Google (and, through GTM, the other ad platforms) what a visitor has agreed to. Google records this as a short "GCS" code on every hit:

| Code | Analytics (GA4 cookies) | Advertising (ad cookies, pixels) |
| --- | --- | --- |
| G100 | Not allowed | Not allowed |
| G101 | Allowed | Not allowed |
| G111 | Allowed | Allowed |

### How each visitor is treated

| Visitor | Before choosing | After Accept | After Reject |
| --- | --- | --- | --- |
| EU / EEA, UK, Switzerland | G100 | G111 | G100 |
| Rest of the world | G101 | G111 | G100 |

- **Before choosing in the EU:** nothing is stored on the device. Google still receives anonymous, cookieless signals, which it uses to model conversions.
- **Before choosing elsewhere:** GA4 counts the visit normally, but no ad pixels fire until the visitor accepts.
- **After a choice:** the choice is remembered on return visits, and ad pixels fire only for visitors who accepted advertising.

### How we build it

- **Your cookie banner stays.** We work with the banner you already use (Cookiebot, Usercentrics, Axeptio, CookieYes, tarteaucitron and others). It needs an "Analytics" and a separate "Marketing/Advertising" category.
- **A small consent tag in GTM** reads the banner's choice and the visitor's country, then sends the right code before any other tag runs.
- **Every tag in GTM has a consent check,** so ad pixels wait for advertising consent and GA4 waits for analytics consent.
- **Some setups need one line in the page code.** If Google tags are also loaded outside GTM, a short consent default must sit above the GTM snippet. We provide it ready to paste.

!!! warning "A privacy decision"

    The country rules are a privacy decision. Please confirm them with your legal or privacy owner before we publish. We do not provide legal advice; see [Data Handling & Security](../support/datasecurity.md).

## Privacy policy and cookie banner

Every site that uses analytics or ad pixels needs a privacy policy and, for EU/UK visitors, a cookie banner. Your legal team owns both; these are the points we usually see missed.

**Privacy policy, EULA and GDPR opt-out**

- Linked in the footer of every page and from the cookie banner
- Lists the tools in use (Google Analytics, Google Ads, Meta, TikTok, Reddit, TRACKS and others) and what each collects
- Kept up to date when a new pixel or platform is added
- Links to the game's EULA, which also covers the in-game data your servers use to count installs and players
- Explains how players can opt out or ask for their data to be deleted under GDPR. TRACKS supports deletion requests, so one contact address or form is enough.

**Cookie banner**

- Offers Accept and Reject with equal weight, plus a settings option
- Has separate Analytics and Marketing choices
- Lets visitors change their mind later (a link in the footer)
- Doesn't cover the trailer or store buttons on mobile

**The trade-off.** A large banner that blocks the page gets more decisions, and so more measured visitors, but adds friction before the store buttons. A small banner that is easy to ignore keeps the page clean, but most EU visitors never choose, so they stay unmeasured (G100). We recommend a compact bottom bar that is clearly visible and asks once, without hiding the main call to action.

## Tags we typically add

A standard game website gets two kinds of tag: one that records each page visit, and one that records each click on a store button. We add these for every ad platform you buy media on.

| Tag | What it records | Needs consent for |
| --- | --- | --- |
| Consent tag | Sends the visitor's consent choice before anything else runs | Nothing, it runs first |
| TRACKS collect | Visits and campaign source, so TRACKS can link a visit to a later install | Set per your privacy policy ([details](../support/datasecurity.md)) |
| Google Analytics 4 | Page views and a `store_click` event with the store name (Steam, PlayStation, Xbox, Epic) | Analytics |
| Google Ads | Page view and store-click conversions, plus the conversion linker | Advertising |
| DV360 / Floodlight | Page view and store-click activities for programmatic campaigns | Advertising |
| Meta pixel | PageView, plus Lead on store click | Advertising |
| TikTok pixel | PageView, plus a Lead or ClickButton event on store click | Advertising |
| Reddit pixel | PageView, plus Lead on store click | Advertising |
| X (Twitter) pixel | PageView, plus a conversion on store click | Advertising |
| Link decorator | Copies the ad's campaign tags (UTMs) onto store links | Nothing, no data is sent |

The exact list depends on the platforms in your media plan. A store click is often named per store (for example `Lead_Steam`), so each platform can optimise toward the store that matters most to you.

Where a platform has an account sign-up, pre-order or purchase on your own site, we can add those events too.

## Ad links and store buttons

Tags only work if the ad link arrives intact. These are the link problems we see most often in audits, and each one turns paid traffic into "Direct" in your reports.

- **Send ads to your website, or to a [TRACKS link](../support/trackinglinks.md).** An ad that goes straight to a store page skips your site, so no tag can see the click.
- **Every ad link carries campaign tags.** We provide the UTM template per platform. Use the platform's own macros (for example `{{campaign.id}}` on Meta) so IDs fill in automatically.
- **Check macros fill in.** A link that shows `${INSERTION_ORDER_ID}` or `%7Bcampaignid%7D` in your browser means the macro was typed in a field that does not support it.
- **HTML5 and rich-media creatives must use the platform's click tag**, not a fixed link written into the creative.
- **Redirects must keep the link's parameters.** A redirect from `/` to `/en`, or from a short domain to the main site, often drops the UTMs. Your web team can check this in a minute.
- **Store buttons should be real links** to the store page. Buttons that open a pop-up or run script first need an extra listener, which we can build.
- **Store links open in a new tab** where possible, so the page is still there to record the click.

## What we report

Installs and cost per install (CPI) show the end result, but they come late and miss everything before launch. Web metrics show, campaign by campaign, whether ads reach interested people.

| Metric | What it tells you |
| --- | --- |
| Web visits | How many people each campaign brings to your site |
| Engaged web visits | Visits where people stayed, watched or browsed, not just bounced |
| Web conversions | Store clicks, wishlists or sign-ups from the site |
| Installs and CPI | Players who actually started the game, and what each cost |

### CPA next to CPI

Cost per web conversion (CPA) is the earlier signal: a store click happens within seconds of the ad click. An install on a paid game can come 3–4 days later, after the player has checked the price and the reviews. Read side by side, the two tell you where the funnel breaks.

| What you see | What it usually means |
| --- | --- |
| High CPI, low CPA | Paid media is working: people are interested and click through to the store. Price, the store page or the review score is holding them back. |
| Low CPI, high CPA | Visitors skip the site and go to the store directly, often because the game is already well known. Or the website itself is hard to use. |

- **Rule of thumb:** CPA should sit slightly below CPI.
- **Compare channels:** some channels bring awareness (many visits, fewer clicks), others bring conversions. CPA shows which is which.
- **Optimise on CPA day to day.** It responds in real time and isn't affected by pricing or review scores, so media decisions stay fast and fair. CPI remains the final check.

**CPQ: cost per quality.** Our awareness KPI: what you pay for attention that meets a quality bar, such as engaged web visits, ad engagements and video watches, rather than for raw impressions. Low CPQ means the budget reaches people who pay attention, which predicts installs well before launch. See the [Glossary](../glossary.md#c).

**Linking store clicks to Steam.** We copy each ad's campaign tags onto your store links. The same campaign name then shows up in your GA4 store clicks and in Steam's own UTM report, so we can follow each campaign from ad, to site, to Steam visit, to wishlist. See [Wishlist Insights](../reporting/wishlist-insights.md).

## What we need from you

With these items we can finish the setup and test it, usually within a few working days.

- [ ] Publish access to your GTM container for `analytics@secondstage.io` (or tell us which container to use)
- [ ] The name of your cookie banner tool, and confirmation it has separate Analytics and Marketing categories
- [ ] Sign-off from your legal or privacy owner on the country rules (EU/UK/CH vs rest of world)
- [ ] Your GA4 property, with Editor access for `analytics@secondstage.io`
- [ ] Pixel and account IDs for each ad platform in your media plan, plus who owns each one
- [ ] A contact on your web team for any snippet that has to go in the page code
- [ ] Your store links (Steam, PlayStation, Xbox, Epic and others) and any pre-order or wishlist pages
- [ ] A heads-up before a site redesign, migration or new cookie banner, so we can re-test

After publishing we test every visitor case (EU and non-EU, accept and reject, returning visitor) and share the results with you.

## Related

- [Landing Page Integration](landingpages.md): the TRACKS snippet and step-by-step GTM and GA4 access.
- [Data Handling & Security](../support/datasecurity.md): consent, legal basis and retention.
- [Postbacks](../attribution/postbacks/index.md): sending installs and purchases back to ad platforms.
- [Ad Ops Guide](../support/adopshelper.md): UTM templates and naming conventions per platform.
