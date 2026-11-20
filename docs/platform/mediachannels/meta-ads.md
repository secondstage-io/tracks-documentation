---
description: "Grant Second Stage access to your Meta Business Manager in six steps so TRACKS can read campaign, ad account and pixel data."
---

# Meta Ads Integration

<p class="docs-audience">For: Ad ops / platform admin</p>

Grant the Second Stage analytics team access to your Meta Business Manager so TRACKS can read campaign, ad account, and pixel data. Follow the six steps below.

!!! tip "Next"

    Once access is in place, enable install + in-game event postbacks via the [Meta Conversions API](../../attribution/postbacks/meta.md).

<ol class="setup-steps" markdown="1">

<li markdown="block">

### Add the user

Go to Meta Business Manager and navigate to the **Users** section. Add the email address `analytics@secondstage.io` and click **Next**.

<figure markdown="span">
  ![Meta Business Manager — Users → Add a new user](../../assets/marketinganalytics_meta_1.png)
  <figcaption>Business Manager → Users → Add → enter <code>analytics@secondstage.io</code></figcaption>
</figure>

</li>

<li markdown="block">

### Assign access level

Assign **Partial (Basic) Access** to the user and click **Next**.

<figure markdown="span">
  ![Assign Partial (Basic) Access](../../assets/marketinganalytics_meta_2.png)
  <figcaption>Partial (Basic) Access is the correct level for analytics</figcaption>
</figure>

</li>

<li markdown="block">

### Share business-page access

Select your business page and grant **Partial access** (business tools and Facebook), then click **Next**.

<figure markdown="span">
  ![Partial access to business tools and Facebook page](../../assets/marketinganalytics_meta_3-1.png)
  <figcaption>Business page → Partial access → business tools + Facebook</figcaption>
</figure>

</li>

<li markdown="block">

### Grant ad account access

Select your ad account and grant **Manage campaigns (ads)** access, then click **Next**.

<figure markdown="span">
  ![Ad account access level — Manage campaigns](../../assets/marketinganalytics_meta_3-2.png)
  <figcaption>Ad account → Manage campaigns access</figcaption>
</figure>

</li>

<li markdown="block">

### Grant pixel access (optional)

Select any pixels that exist on the account and assign access, then click **Next**. This step is only required if you already run Meta conversion events — skip it if no pixel has been created yet.

<figure markdown="span">
  ![Pixel access assignment](../../assets/marketinganalytics_meta_3-3.png)
  <figcaption>Pixel access — required only if you already run Meta conversion events</figcaption>
</figure>

</li>

<li markdown="block">

### Review and send

Review the invitation summary, then click **Send invitation**.

<figure markdown="span">
  ![Invitation summary review](../../assets/marketinganalytics_meta_4.png)
  <figcaption>Review all selected permissions before sending</figcaption>
</figure>

</li>

</ol>
