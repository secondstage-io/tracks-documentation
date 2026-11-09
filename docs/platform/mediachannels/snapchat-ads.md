# Snapchat Ads Integration

<p class="docs-audience">For: Ad ops / platform admin</p>

Grant Second Stage access to Snapchat Business Manager and the Snap Pixel so TRACKS can read campaign performance and pixel-level events.

!!! tip "Next"

    Once access is in place, enable install + in-game event postbacks via the [Snapchat Conversions API](../../attribution/postbacks/snapchat.md).

<ol class="setup-steps" markdown="1">

<li markdown="block">

### Invite the Second Stage user

In Snapchat Business Manager, go to **Business Settings → Members** and invite `analytics@secondstage.io` with **Ad Account Analyst** access. This grants the permissions TRACKS needs to view campaign, ad squad, and ad performance, export reports, access attribution data in reporting, and use the API reporting endpoints.

<figure markdown="span">
  ![Snapchat Business Manager — Members → Invite](../../assets/marketinganalytics_snapchat.jpg)
  <figcaption>Business Settings → Members → Ad Account Analyst</figcaption>
</figure>

</li>

<li markdown="block">

### Grant Snap Pixel access

For the Snap Pixel asset, grant **Data Admin** or **Pixel Editor** permission to `analytics@secondstage.io` so TRACKS can read and configure pixel events.

</li>

<li markdown="block">

### Use UTM-tagged destination URLs

Use the UTM-tagged destination URLs provided by the Second Stage team in the Ad Ops Helper.

</li>

<li markdown="block">

### Apply the naming conventions

Follow the campaign, ad squad, and ad naming conventions shared by the Second Stage team.

</li>

</ol>
