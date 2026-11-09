# GA4 Measurement Protocol

<p class="docs-audience">For: Web / marketing admin</p>

[→ Google Analytics: Measurement Protocol](https://developers.google.com/analytics/devguides/collection/protocol/ga4)

TRACKS can send installs and in-game events to your GA4 property as events, tied to the GA4 visitor who came through your website. Use it to see installs in GA4 next to your web data, or to build GA4 audiences.

GA4 is not an ad platform. Linking GA4 to Google Ads is optional and separate; for Google Ads bidding, use [Google Ads postbacks](google.md).

## Requirements

- The GA4 tag on your website (see [Landing Page Integration](../../platform/landingpages.md)).
- Only players who visited your website first can be sent, because each event is tied to that GA4 visitor.

## Create an API secret

<ol class="setup-steps" markdown="1">

<li markdown="block">

### Open your web stream

In Google Analytics, go to **Admin → Data streams** and select your web stream.

</li>

<li markdown="block">

### Create the secret

Open **Measurement Protocol API secrets** and click **Create**. Any nickname is fine.

</li>

<li markdown="block">

### Send the details

Send the secret and the stream's **Measurement ID** (`G-XXXXXXX`) to the Second Stage team.

</li>

</ol>
