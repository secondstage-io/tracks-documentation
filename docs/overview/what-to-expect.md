# What to Expect

Setting up TRACKS is less work than it looks — Second Stage drives most of the integration, and your team's hands-on time stays light.

!!! tip "Not every area applies to every game"

    Depending on your stage and stack, you may not need every area yet — landing-page setup is only relevant if you have one, Steamworks only if you ship there, and attribution waits until your telemetry is ready. During kickoff, Second Stage scopes the integration to what you actually need.

!!! note "What we provide"

    Each project comes with a **custom integration plan** — a live roadmap with task owners, milestones, and deadlines — plus an **Ad Ops Helper sheet** that handles naming conventions and UTM-tagged campaign URLs for you.

## Who you'll need

Identify a point of contact for each area ahead of kickoff. Most teams already have everyone listed — you're just confirming who'll drive each piece. If a role isn't filled on your side, the Second Stage team will advise during kickoff.

<div class="roles-grid" markdown>

-   :material-server:{ .lg .middle } &nbsp; **Backend developer**

    ---

    Spins up the GCP project, later wires telemetry into the Measurement API, and integrates the GDPR Forget API.

    *Tracks: Cloud foundation · Attribution & GDPR*

-   :material-dns:{ .lg .middle } &nbsp; **Webmaster / IT**

    ---

    Adds the TXT and CNAME records that map your branded subdomains to the TRACKS endpoints and tracking links.

    *Tracks: Cloud foundation · Landing page & Steam*

-   :material-bullhorn-outline:{ .lg .middle } &nbsp; **Media specialist / ad-ops lead**

    ---

    Holds admin access to your ad accounts, completes the Ad Ops Helper, and applies UTM-tagged links across campaigns.

    *Tracks: Ad & media platforms*

-   :material-account-tie:{ .lg .middle } &nbsp; **Marketing or data lead**

    ---

    Owns GA4 / Google Tag Manager and Steamworks access, and signs off on validation before go-live.

    *Tracks: Landing page & Steam · Attribution & GDPR*

</div>

## What gets set up

The first three areas can run in parallel; attribution is the final piece, completed right before your game goes live.

<div class="grid cards grid--two-cols" markdown>

-   :material-cloud-outline:{ .lg .middle } &nbsp; __Cloud foundation & custom domains__

    ---

    **Who:** backend developer or IT lead, plus someone who can edit DNS records.

    **You provide:** access to a Google Cloud project, plus TXT and CNAME records for your branded subdomains (e.g. `tracks-m.mygame.com`).

    **We handle:** GCP project setup, microservice deployment, and branded-domain mapping for the Measurement API and tracking links.

    [:octicons-arrow-right-24: Cloud Setup](../platform/cloud.md) &nbsp; · &nbsp; [:octicons-arrow-right-24: Custom Domains](../platform/domains.md)

-   :material-bullhorn-outline:{ .lg .middle } &nbsp; __Ad & media platforms__

    ---

    **Who:** media specialist or ad-ops lead with admin access to your ad accounts.

    **You provide:** ad-account access plus your share of the [Ad Ops Helper sheet](../support/adopshelper.md) (campaign info, naming conventions) — we fill in the rest.

    **We handle:** UTM tagging, tracking-link generation, postback configuration, plus a 2-day review.

    [:octicons-arrow-right-24: Media Platform Access](../platform/mediachannels/index.md)

-   :material-web:{ .lg .middle } &nbsp; __Landing page & Steam__

    ---

    *Optional — only if your game has a landing page or ships on Steam.*

    **Who:** webmaster or marketing-ops lead (Google Tag Manager) plus your Steamworks admin.

    **You provide:** Publish access to Google Tag Manager — plus GA4 and Steamworks if you have them. We can set GA4 up from scratch if you don't.

    **We handle:** tracking snippet deployment, GA4 configuration, conversion pixels, and Steam UTM setup.

    [:octicons-arrow-right-24: Landing Page Integration](../platform/landingpages.md)

-   :material-api:{ .lg .middle } &nbsp; __Attribution & GDPR__

    ---

    *Activates right before launch, once your game is emitting events.*

    **Who:** backend developer or data engineer.

    **You provide:** a telemetry backend that forwards `game_open` or `session_start` events (we can help set this up if you don't have one), plus integration of the GDPR Forget API into your right-to-erasure flow.

    **We handle:** Measurement API guidance, payload review, end-to-end testing, and the GDPR Forget API endpoint.

    [:octicons-arrow-right-24: Telemetry Setup](../attribution/telemetry.md) &nbsp; · &nbsp; [:octicons-arrow-right-24: Measurement API](../attribution/measurementapi.md) &nbsp; · &nbsp; [:octicons-arrow-right-24: GDPR API](../attribution/gdprapi.md)

</div>

## Timeline & sequencing

<figure class="setup-flow" aria-label="Setup flow from kickoff to live attribution">

  <div class="setup-flow__stage setup-flow__stage--single">
    <div class="setup-flow__node setup-flow__node--start">
      <span class="setup-flow__eyebrow">Step 1 · Foundation</span>
      <strong>Cloud & custom domains</strong>
      <span class="setup-flow__when">~1 hour total · everything else plugs in here</span>
    </div>
  </div>

  <div class="setup-flow__connector" aria-hidden="true"></div>

  <div class="setup-flow__stage setup-flow__stage--parallel">
    <div class="setup-flow__node">
      <span class="setup-flow__eyebrow">Step 2 · In parallel</span>
      <strong>Ad & media platforms</strong>
      <span class="setup-flow__when">~2–4 hours · pre-launch</span>
    </div>
    <div class="setup-flow__node">
      <span class="setup-flow__eyebrow">Step 2 · In parallel</span>
      <strong>Landing page & Steam</strong>
      <span class="setup-flow__when">~1 hour · only if applicable</span>
    </div>
  </div>

  <div class="setup-flow__connector setup-flow__connector--dashed" aria-hidden="true"></div>

  <div class="setup-flow__stage setup-flow__stage--single">
    <div class="setup-flow__node setup-flow__node--final">
      <span class="setup-flow__eyebrow">Step 3 · Right before launch</span>
      <strong>Attribution & GDPR</strong>
      <span class="setup-flow__when">~1–2 hours integration + ~1 day sign-off</span>
    </div>
  </div>

  <figcaption class="setup-flow__caption">~10–14 days end-to-end. The dashed line is the only sequential dependency — attribution finalizes right before launch, once your telemetry is ready.</figcaption>

</figure>

## Have a question or ready to start?

Use the **Add a New Game** option on the [TRACKS homepage](https://tracks.secondstage.io){:target="_blank"} to kick things off, or email us at [hello@secondstage.io](mailto:hello@secondstage.io). The Second Stage team will scope the integration to your stage and your stack — you don't need to map this out yourself.
