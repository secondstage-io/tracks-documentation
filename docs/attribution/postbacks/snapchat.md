# Snapchat Conversions API

<p class="docs-audience">For: Ad ops / backend engineer</p>

[→ Snapchat Conversions API: Get started](https://developers.snap.com/api/marketing-api/Conversions-API/GetStarted)

!!! note

    Complete the [Snapchat Ads access integration](../../platform/mediachannels/snapchat-ads.md) first. The Snap Pixel access granted there is needed here too.

TRACKS sends installs and in-game events to Snapchat through the Snapchat Conversions API, matched to the Snap click ID captured on your landing page.

## Generate the token

<ol class="setup-steps" markdown="1">

<li markdown="block">

### Open Business Details

Log in to Snapchat **Ads Manager**, open the menu in the top corner and select **Business Details**. The **Conversions API Tokens** section is below *OAuth Apps*. Only an **Organization Admin** can see it.

</li>

<li markdown="block">

### Generate the token

Click **Generate Token**. The token doesn't expire; you can delete it at any time to revoke it.

</li>

<li markdown="block">

### Send the token and Pixel ID

Send the token, together with your **Snap Pixel ID**, to the Second Stage team to enable Snapchat postbacks.

</li>

</ol>

## Conversion event mapping

Snapchat accepts a fixed list of event names. Install postbacks are sent as **PURCHASE**. Reactivations and DLC activations use custom events (`CUSTOM_EVENT_1` and `CUSTOM_EVENT_2`), which you can rename in Snapchat Events Manager. Tell your Second Stage contact if you would like a different mapping.
