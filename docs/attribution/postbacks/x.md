# X Ads Conversion API

<p class="docs-audience">For: Ad ops / backend engineer</p>

[→ Conversions API Setup Guide for X](https://developer.x.com/en/docs/x-ads-api/measurement/web-conversions/conversion-api)

!!! note

    Complete the [X Ads access integration](../../platform/mediachannels/x-ads.md) first.

TRACKS sends installs and in-game events to X through the X Ads Conversion API.

## Set up X postbacks

<ol class="setup-steps" markdown="1">

<li markdown="block">

### Create an app with Ads API access

In the [X Developer Portal](https://developer.x.com/en/portal/dashboard), create a project and app under your company account, and apply for **Ads API** access. The *Conversions* access level is enough.

</li>

<li markdown="block">

### Generate keys

In the app's **Keys and tokens** tab, generate the **API key and secret** and the **access token and secret**.

</li>

<li markdown="block">

### Create conversion events

In X Ads **Events Manager**, create one conversion event per postback (for example Purchase). Note the **pixel ID** and each **event ID**.

</li>

<li markdown="block">

### Send the details

Send the four keys, the pixel ID and the event IDs to the Second Stage team.

</li>

</ol>

## Conversion event mapping

Installs go to the event you name as Purchase. Per-storefront events need their own event IDs; otherwise only the main event is sent.
