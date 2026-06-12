# Cloud Environment

<p class="docs-audience">For: Cloud / DevOps engineer</p>

TRACKS is designed to be deployed using a "hybrid-hosted" model, where all granular data processing and storage occur directly on the publisher’s or developer studio’s cloud environment. This setup functions like an enterprise-grade on-premise solution tailored for the video game industry. TRACKS supports the Google Cloud Platform for this purpose.

## Google Cloud Platform (GCP) Setup

<ol class="setup-steps" markdown="1">

<li markdown="block">

### Create the project

Go to [Google Cloud Console](https://console.cloud.google.com/), sign in with your email address. Create a new Project named "TRACKS - yourgame" (replace "yourgame" with the title or a unique identifier of your game, e.g. "TRACKS - Urban Brawl").

If your organization does not use Google Workspace (Gsuite email account), you can link your email following [these steps](https://support.google.com/accounts/answer/27441).

<figure markdown="span">
  ![Google Cloud Console — create new project](../assets/attribution_GCP.png)
  <figcaption>Google Cloud Console → New Project → "TRACKS - yourgame"</figcaption>
</figure>

</li>

<li markdown="block">

### Enable billing

[Enable billing for your account and link to your Project](https://cloud.google.com/billing/docs/how-to/modify-project#how-to-change-ba).

- Microservices enabled in your Google Cloud will autoscale depending on data ingestion volume.
- Estimated costs for 2 million installs in a single month should be around ~$40.

</li>

<li markdown="block">

### Grant access to Second Stage

Go to IAM and admin, click on Grant Access, select permission: Basic → Owner for `analytics@secondstage.io`.

</li>

<li markdown="block">

### Deployment

The Second Stage team will be notified after access is granted and TRACKS Attribution Measurement microservices are deployed for your instance.

</li>

<li markdown="block">

### Configure environment variables

[Your API key and secret will be entered as environment variables to Google Cloud Run functions](https://cloud.google.com/functions/docs/configuring/env-var).

</li>

</ol>

!!! info "What we configure on your Google Cloud"

    After access is granted, the Second Stage team deploys and configures the following services in your project:

    - **Cloud Run** — hosts the APIs: receives in-game session events from your telemetry backend and handles web-side event ingestion from your landing page.
    - **Pub/Sub** — handles event messaging between services.
    - **Firestore** — powers the shorten link feature.
    - **BigQuery** — stores and processes data through Dataform.
    - **Cloud Scheduler** — triggers periodic jobs, e.g. for postback processing.
    - **Cloud Storage, Artifact Registry & Cloud Build** — Docker image containers and deployment.

    For more detail on the architecture hosted on Google Cloud, see the [Measurement API](../attribution/measurementapi.md).

## Next

With the cloud environment set up, continue with the rest of [Platform Integration](overview.md) (media channels, landing page, storefronts). The [Attribution](../attribution/overview.md) section then covers [Telemetry](../attribution/telemetry.md) and the [Measurement API](../attribution/measurementapi.md) that run on this cloud project.
