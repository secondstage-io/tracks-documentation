# Meta Conversion API

<p class="docs-audience">For: Ad ops / backend engineer</p>

[→ Conversions API Setup Guide for Meta](https://www.facebook.com/business/help/232481544843294?id=818859032317965)

!!! note

    Complete the [Meta Ads access integration](../../platform/mediachannels/meta-ads.md) first. The CAPI setup assumes the Second Stage analytics user already has the permissions granted there.

Editor access for the Data Source Asset to `analytics@secondstage.io` is required.

To set up a Meta Postback Token, follow these steps using a Business Manager Admin login:

<ol class="setup-steps" markdown="1">

<li markdown="block">

### Open or create a Data Source

In Meta Business Manager, navigate to **Data Sources**. If you haven't already, create a new data source.

</li>

<li markdown="block">

### Note the Data Set ID

Go to the **Settings** tab of your data source and note down the **Data Set ID**.

</li>

<li markdown="block">

### Go to the Conversion API section

Scroll down to the **Conversion API** section within the data source settings.

</li>

<li markdown="block">

### Generate and share the access token

Click **Generate Access Token**. Copy the token and send it to the Second Stage team to enable Meta install postbacks.

</li>

</ol>

Once complete, ensure the data source asset is shared with the active Ad Account so your campaigns can access and utilize the data, and with `analytics@secondstage.io` so Second Stage can configure and manage the postbacks.

## Conversion event mapping

Install postbacks are sent under the standard Meta event **Purchase**. Tell your Second Stage contact if you would like them mapped to a different conversion event.

<figure markdown="span">
  ![Meta Events Manager — Conversions API configuration](../../assets/Meta_capi_doc1.png)
  <figcaption>Meta Events Manager → Conversions API setup</figcaption>
</figure>

<figure markdown="span">
  ![Meta Conversions API — system user assignment](../../assets/Meta_capi_doc2.png)
  <figcaption>Assign a system user to your ad account for CAPI access</figcaption>
</figure>

<figure markdown="span">
  ![Meta Conversions API — access token generation](../../assets/Meta_capi_doc3.png)
  <figcaption>Generate the CAPI access token for the Second Stage analytics user</figcaption>
</figure>
