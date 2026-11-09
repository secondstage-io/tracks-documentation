# Google Ads Conversion API

<p class="docs-audience">For: Ad ops / backend engineer</p>

[→ Google Ads: About offline conversion imports](https://support.google.com/google-ads/answer/2998031)

!!! note

    Complete the [Google Ads access integration](../../platform/mediachannels/google-ads.md) first.

TRACKS sends installs and in-game events to Google Ads through Google's **Data Manager API**. **No developer token, API application or manager account is needed.**

## Set up Google Ads postbacks

<ol class="setup-steps" markdown="1">

<li markdown="block">

### Give access

`analytics@secondstage.io` needs **Standard** access to the ad account, or to the manager account above it. If you completed the [Google Ads access integration](../../platform/mediachannels/google-ads.md), this is already done.

</li>

<li markdown="block">

### Agree the conversion actions

We create one **Import from clicks** conversion action per event (for example Purchase, or one per storefront), or you tell us which existing conversion actions to use.

</li>

<li markdown="block">

### Keep auto-tagging on

Leave **auto-tagging** switched on in your Google Ads account, so the `gclid` reaches your landing page. It is the click ID each conversion is matched on.

</li>

</ol>

## Conversion event mapping

Install postbacks are sent as **Purchase**. Tell your Second Stage contact if you would like them sent to a different conversion action.
