# Attribution Tracking

## Overview

With TRACKS Attribution, our proprietary full-funnel attribution tracking solution that is part of the TRACKS platform, we can provide valuable insight into your lower-funnel media campaigns. This solution consists of three components, all managed and supported by the Second Stage team.

1. **Integration of the TRACKS Measurement API**: The first step is to integrate the TRACKS Measurement API with your telemetric/logging server. This instance will be deployed to your cloud account. If you don't already have a cloud server, we'll help you create one, with full ownership at your end.  
2. **Ad Operations Support**: Once attribution tracking is verified, the Second Stage team will assist with media platform integrations. This process requires adherence to specific naming conventions for campaigns, ad groups, and ads to ensure accurate reporting. Additionally, UTM-tagged links must be used. The Second Stage team will provide a naming convention generator sheet tailored to your chosen ad platforms or activations. If you already have a naming convention in place, TRACKS can be adapted to your mapping.   
3. **Postback Setup**: With access to your media platforms, TRACKS will create events/pixels for game\_opens and activate the platform’s Conversion API to feed back attributed in-game data.

!!! info "Managed Service Approach:"

    All aspects of using TRACKS Attribution are configurable and will be tailored during your onboarding call with the Second Stage team. This documentation outlines a standard best-practice approach to building an attribution and BI suite, based on years of expertise in user acquisition, media, BI, tracking, and attribution from the Second Stage team. 

---

## Functionality

A proper attribution setup can shine a light into the "black box" of where valuable game purchases, activations or installs are coming from. Once an attribution solution is integrated, whether it's TRACKS or a third-party solution, the dashboard will display key lower-funnel metrics.

If you're using TRACKS Attribution, the default dashboard will show install metrics, including Measured, Paid, Organic and Modeled installs. It's important to note that "installs" refer to the first activation of the game (when the player starts the game for the first time), not purchases.

These install metrics can be further broken down by storefront or platform, such as CPI (Xbox), CPI (Steam), CPI (PS), CPI (Epic), and CPI (Nintendo), assuming the measurement API is provided with the appropriate parameters. Other install metrics we are providing in addition to CPI are eCPI and CR%.

Based on your average unit price, TRACKS can estimate revenue per install and report ROAS (Return on Ad Spend) percentages. This allows you to compare and analyze performance across multiple dimensions, including

<div class="mdx-columns" markdown>
:material-check: Date 
    
:material-check: Channel 

:material-check: Campaign 

:material-check: AdGroup (Ad Set)

:material-check: Creative (Ad)

:material-check: GEO

:material-check: Strategy

:material-check: Target

:material-check: Target Audience 

:material-check: Targeting 

:material-check: Ad Type

:material-check: Ad Format

:material-check: Placement 
</div>
 
In addition to tracking in-game events, web conversions are critical to understanding the user journey. TRACKS can report on web conversions such as Steam, PS, Xbox, Nintendo and Epic storefront button clicks, completing the event funnel for your user acquisition media campaigns.

To enable web conversion tracking, a TRACKS JavaScript snippet wraps your landing page's storefront button click URLs to ensure that Steam and other storefront UTM analytics capture as many UTM-tagged visits as possible. We recommend avoiding redirect tracking links and instead using a plain landing page URL with UTM tags for seamless integration with media platforms.

Post-view or impression-based tracking in video game marketing across paid media channels adds complexity and can negatively impact the accuracy of data-driven attribution. For top-of-funnel campaigns with awareness objectives, using awareness reports to evaluate performance is preferable. For consideration and conversion-focused campaigns, attribution is based on clicks, as a landing page session triggers the attribution touchpoint.

By combining all components of the user flow with TRACKS Attribution, the standard dashboard allows reporting across the entire funnel, e.g.:

Impression → Click → Web Visit → Web Conversion (button click) → Steam Visit → Steam Activation → Install

Metrics available in TRACKS include

- [x] Media Metrics  
- [x] Web Analytics Metrics  
- [x] Steamworks metrics  
- [x] Attribution Metrics  
- [x] Awareness Metrics

In addition, based on your onboarding call and the status of your game release, optional metrics may include

- [x] Steam wishlist and pre-order metrics  
- [x] DLC installs and in-game purchases metrics (requires an additional measurement API call)  
- [x] Influencer / Streamer Analytics metrics  
- [x] Brand Health metrics

---

## Attribution Tracking Options 

TRACKS offers three different approaches to attribution tracking that can be implemented based on different requirements, which are detailed here. Our recommended solution for best results is the **Measured Attribution Tracking & Modeling** approach.

| Methodology     | Description | Benefits     |
| ----------- | ----------- | ----------- |
| Modelled Attribution Tracking    | This methodology uses a data-driven approach to assign conversion weights using data from Steam UTM Analytics and Google Analytics (GA4). It calculates conversions using a Markov chain attribution model and integrates data from Steam and media campaigns to determine the uplift generated by paid media.  | This method provides a comprehensive view by combining web and Steam data, accurately assigns conversion weights, and offers insights into media campaign effectiveness through Marketing Mix Modeling.      |
| Measured Attribution Tracking   | This method uses server-side integration to track game installs directly through the TRACKS attribution solution. It requires no SDK implementation and collects telemetry data to accurately attribute installs.  | It enables real-time, accurate install tracking without client-side risks, requires no changes to game code, and is optimized for PC/console games following industry best practices.   |
| Measured Attribution Tracking + Modeling (Best Practice)   | This methodology combines measured attribution (server-side) with a Markov chain modeling solution for untracked installs. This unified approach compensates for untraceable sources by redistributing untracked installs to their potential origins.  | This approach ensures up to 98% attribution accuracy within a 24-hour window, combines measured and modeled data for a complete attribution view, and increases install tracking accuracy by redistributing untracked game opens.   |


### Modelled Attribution Tracking

This method calculates conversions using our data modeling solution. Due to the specific data requirements, this approach is available only for games released through Steam.

1. **Data Sync:** TRACKS first syncs data from Steamworks UTM Analytics and Steam Traffic Breakdown reports, capturing trusted visits, tracked visits, wishlists, purchases and activations.
2. **Web Conversions:** Where available, GA4 Web Conversions are included via multi-funnel channel data, detailing the user journey for each web session. TRACKS uses a Markov chain attribution model, a data-driven methodology, to accurately assign conversion weights.
3. **Media Uplift Analysis:** Using a marketing mix modeling approach, TRACKS integrates data from Steam's traffic breakdown, media and web analytics (spend, impressions, clicks and web conversions) to determine the uplift generated by paid media across all traffic sources. A linear regression model is then applied using estimated total Steam activations by date and market (based on reviews, followers, and CCU) to extrapolate the impact of media campaigns (Steam Activations / Attributed Steam Modeled Installs).
   
The following metrics will be available:

<div class="mdx-columns" markdown>
- [x] Measured Installs (from Steamworks UTM Analytics)
- [x] Modeled Installs
- [x] Estimated CPI
- [x] eCPI
- [x] Web Conversions
- [x] CR% (Conversion Rate)
- [x] ROAS (Return on Ad Spend)
</div>

TRACKS uses a Marketing Mix Modeling (MMM) approach enhanced with Steam UTM Analytics, Traffic Breakdown data and Google Analytics (GA4) data. If you don't have a website or don't use it as a landing page, the efficiency of the model is reduced by 30% because it relies solely on Steam UTM Analytics, Visits and Traffic data.

> If you're interested in this method but don't have a landing page or are unsure of your current setup, Second Stage can help you create a landing page or game website for marketing purposes. [Contact us](https://secondstage.io/contact/) for a quote!


### Measured Attribution Tracking

Using this method, installs are tracked using the TRACKS Attribution solution, which is based on a data streaming pipeline.

If your game does not have a backend server for telemetry and event logging, we do not recommend integrating the TRACKS measured attribution solution or any other vendor's solution. In such cases, we recommend using our modeled attribution method instead.

**Server-side integration:** First, the TRACKS Measurement API needs to be deployed in a cloud environment (preferably Google Cloud). This API works as an HTTP webhook that connects to your backend or existing telemetry logging pipeline. When a game_open event signal is received from your server-side telemetry, the TRACKS API endpoint receives an HTTP POST request.

**No SDK required:** TRACKS integration through the Measurement API is the only supported method and does not require any SDK implementation in your game code or server. This ensures there is no added latency or risk of client-side errors, while giving you full control over the data and parameters sent to TRACKS.

**Best practice for PC/Console games:** This integration flow has been tested specifically for the PC/Console gaming ecosystem, following best practices for both gamers and studios.

The Measurement API endpoint uses the following parameters:

- IP Address
- User ID
- Event timestamp
- Platform
- Storefront

If any of these parameters are not currently collected by your telemetry server, you will need to ensure that they are collected before providing them to the TRACKS Measurement API after deployment.

Below is a pseudocode snippet that demonstrates how to build the API request. The API should be triggered every time a game_open (session start) event is logged in your telemetry system. If you choose to host TRACKS Attribution on your cloud servers, the API endpoint domain will be updated accordingly.

```json
# Example Python Code for server-side
   import requests


   url = "https://api.secondstage.io/tracks"  # (or https://api.your-game.com/tracks)
   payload = {
     'user_id': '1a23fd44c21f8l5r',
     'event_name': 'game_open',
     'ip': '175.124.248.15',
     'time_stamp': '1724094783',
     'platform': 'pc',
     'storefront': 'steam'
   }
   headers = {
     'Authorization': 'Bearer API_KEY_TOKEN'
   }
   response = requests.request("POST", url, headers=headers, data=payload)
   print(response.text)   
```

Implementation on your end can be managed by a DevOps or backend developer, or by your business intelligence / data science teams - game developers do not need to be directly involved. On average, the process should take about 2 hours for a mid-level backend developer or data engineer.

> For each game added, the Second Stage Analytics team will fully support the integration, deployment and testing, starting with your onboarding call.


### Measured Attribution Tracking + Modeling

Measured Attribution Tracking combined with Modeling is the best practice approach to Attribution Tracking in PC & Console Gaming and our **recommended methodology**. 

Due to the opacity of storefronts in the player acquisition journey, a fully deterministic measurement solution is not feasible for PC/Console marketing attribution. Like all attribution tracking vendors, TRACKS relies on IP addresses to identify the acquisition source of the game_open event. This approach, known as fingerprint tracking or probabilistic measurement, involves matching the ad click IP to the game_open IP, which can lead to decreased accuracy as the time between click and conversion increases.

Effective attribution depends on a number of factors, including game setup, campaign strategy, ad placement, targeting, geographic region, and platform. The challenge often lies not in the attribution method itself, but in its complex implementation. TRACKS is designed to seamlessly integrate marketing analytics with attribution tracking. As a managed service, we provide comprehensive support throughout the process to ensure that all client needs are thoroughly addressed.

Research shows a 98% accuracy rate within a 24-hour window, meaning the ad click and game launch occur on the same device. However, this accuracy drops significantly after 24 hours. With a typical attribution window of seven days from click to purchase for PC and console games, accuracy drops to approximately 85%. In addition, cross-device measurement typically achieves about 80% accuracy. These factors are taken into account based on our experience with PC/console game attribution.

For example, if there are 100 ad clicks resulting in 100 game opens (installs), TRACKS Attribution targets at least 65% accuracy in measured attribution and before modeling. This means that 65 game opens will be correctly attributed to the source, while 35 will be reported as organic. The accuracy rate may be higher if your game has a lower barrier to entry and is available on more storefronts.

By enabling the modeling solution alongside the measured attribution solution, untracked game opens are redistributed to attribution sources using a Markov chain model, similar to Google's conversion modeling in Google Analytics 4. This approach allows marketers to view both measured and modeled installs for a complete understanding of their data.
While the 65% attribution accuracy of measured data is typically sufficient for data-driven insights, the TRACKS modeling solution is valuable for capturing the remaining 35% and providing a complete picture.

The approach of combining measured and modeled data is common and not unique to Second Stage. This method, known as Unified Marketing Measurement (UMM), is a recent advancement in modern marketing technology. Given the challenges of untrackable storefront silos and player privacy concerns, UMM is an ideal solution for PC/console video game marketing.

TRACKS uses the UMM methodology to integrate three different data sources:

- **TRACKS Measurement API:** For measured, attributed installs
- **Web Analytics (GA4):** Leverages Markov Chain for multi-touch attribution
- **Steam UTM Analytics & Traffic Breakdown:** For Marketing Mix Modeling (MMM)

> For more information on Markov Chain Attribution, Marketing Mix Modeling, or Unified Marketing Measurement, please visit our [Further Reading](https://documentation.secondstage.io/resources/) section.

---

## Integration 

TRACKS using Attribution Tracking consists of four primary data source components:

- Media Analytics – Integrations with media channels
- Web Integration – Incorporating the TRACKS JS code and Google Analytics 4
- Steamworks UTM Analytics and Traffic Breakdown
- Attribution Measurement API
  
Media platforms, Google Analytics (via Google Tag Manager), and Steamworks integrate by providing access to our service account: analytics@secondstage.io.

However, the TRACKS Attribution Measurement API must be deployed into your Google Cloud Platform (GCP) account (a new account will be created if one doesn't exist).

The TRACKS Attribution data source collects granular data for each web visit and game open event. This data is funneled into the partitioned tracks_attribution dataset. More information regarding data retention, GDPR compliance, and the Data Processing Agreement is available in the [Data Handling & Security](/tracks/data-security/) section.

Once the ELT (Extract-Load-Transform) pipeline is deployed, all data sources will be consolidated into a Google Cloud BigQuery database.

![Integration](/assets/attribution_integration-1.png)


### Integration Plan & Checklist

**Marketing Analytics Integration**

The TRACKS data automation backend integrates seamlessly with various media platforms, starting with access to our service account at analytics@secondstage.io. 

1. Users begin by completing the media channel information sheet provided by Second Stage.
2. Based on the information supplied, TRACKS generates UTM-tagged URLs, allowing media specialists to deploy these URLs across ad platforms and configure campaign names, ad groups, and creative assets.
3. The user then inputs this information into the media platforms. Once the campaign is live, TRACKS will notify you, and the data will be available in the reporting suite the following day.
4. By integrating with Google Tag Manager, GA4, and Steamworks, TRACKS also implements a JavaScript snippet on the landing page to enable attribution session tracking and capture Steam page click-throughs. This step also includes setting up event and conversion pixels for the media platforms.
5. To configure postbacks—such as sending signals for game_open, install, and other in-game events back to media platforms—a system user is assigned to your account. Editor-level access to the Events Manager or Events Builder on the media platforms is required for this.

If you already have a Campaign Naming Convention in place, you can provide your taxonomy to TRACKS for automatic mapping.

**Attribution Tracking Integration**

The Second Stage team will assist in setting up a Google Cloud Platform (GCP) project for deployment on your side. If you already have an existing GCP account, start by creating a new project and grant Project Owner access to analytics@secondstage.io.

Once deployment is complete, the TRACKS Measurement API will be available for connection to your telemetry backend server.

Next, install Google Tag Manager on your website. Using the editor access provided to analytics@secondstage.io, a JavaScript snippet will be deployed to track web visits through the Attribution Measurement API, capturing the first touchpoint with acquisition source data.

The TRACKS attribution solution will then be ready to collect both web and in-game events, reporting attribution metrics in the reporting suite. Ensure that campaign naming conventions and UTM taxonomies are properly implemented as outlined in your ad operations guide.


### Deployment

!!! tip "Important:"

    Required for Measured Attribution Tracking and Measured Attribution Tracking + Modeling. If you only plan to use Modeled Attribution Tracking, please refer to Web (Landing Page) Setup in the Marketing Analytics section.


#### Hybrid Cloud Approach

The recommended deployment approach for TRACKS is a "hybrid-hosted" solution, similar to an on-premise setup, where all granular data is processed and stored on the publisher or developer studio’s Google Cloud servers. This method can be considered as an enterprise level solution, and we are of the opinion that it is the optimal choice for the video game industry.
This approach has been streamlined by the Second Stage team to maximize the effectiveness of performance media campaigns in gaming, without introducing latency or errors to game servers. It also ensures maximum data privacy, safeguards player data, and fully complies with GDPR regulations.

![Deplyoment](/assets/attribution_deployment-1.png)


*Branded Domain*

Once the TRACKS backend is deployed in your Google Cloud Platform instance, you'll have the option to whitelabel the Measurement API endpoint domain. This feature is not only for branding purposes but also provides greater control over privacy and compliance with client-side CORS (Cross-Origin Resource Sharing) policies.
To enable your branded domain, the Second Stage team will provide a CNAME record for you to add through your DNS provider. The default suggested domain is a subdomain: tracks./[mygame/].com.

#### Managed Service Approach
 
We do not recommend integrating the attribution measuement solution if your game lacks a backend server for telemetry and event logging, whether planned or currently in use. In such cases, instead of implementing TRACKS Attribution Measurement API or any other vendor's solution, we suggest leveraging our attribution modeling.

However, if you do have a telemetry backend server but are unable to use Google Cloud Platform for deployment, the Second Stage team can assist by hosting the attribution solution in a dedicated cloud environment for you.


### TRACKS Attribution Measurement API

!!! tip "Important:"

    Required for Measured Attribution Tracking and Measured Attribution Tracking + Modeling. If you only plan to use Modeled Attribution Tracking, please refer to Web (Landing Page) Setup in the Marketing Analytics section.

The Measurement API tracks the customer acquisition source, enabling you to identify which channels, campaigns, ads drive install and other in-game events. By integrating with TRACKS Attribution, you can accurately attribute conversions to the correct media sources, helping you optimize your marketing efforts.

#### Prerequisites

Before you begin, please ensure the following:

- A Google Cloud Platform account with billing enabled (Google Cloud Platform microservices will auto-scale as needed for your game).
- Access to Measurement API credentials (API key and secret).
- A TRACKS account with the attribution package enabled and ready for integration.
- Basic knowledge of server-side programming, cloud services, and API integrations.
- A telemetry server capable of reading and collecting client IPs via HTTP headers or X-Forwarded-For (XFF).
- A webhook, postback, or proxy mechanism that can trigger real-time Measurement API requests or perform batch uploads via cron jobs.

To integrate with TRACKS Attribution, you'll need to create and implement a lightweight server-side HTTP request as a webhook on your backend. The Measurement API is the only supported method for this integration. You can view a pseudo-code example for constructing the API request below.

The webhook should trigger every time a game open (session start) event is logged in your telemetry system.

The Measurement API Endpoint requires the following parameters:

- IP address
- User ID
- Event timestamp
- Platform
- Storefront

??? question "API Request Pseudo-code example"

    ```json
    # Example Python Code for server-side telemetry
    import requests
    
    
    url = "https://tracks.your-game.com/measure"  
    
    
    payload = {
     'user_id': '1a23fd44c21f8l5r',
     'event_name': 'game_open',
     'ip': '175.124.248.15',
     'time_stamp': '1724094783',
     'platform': 'pc',
     'storefront': 'steam'
    }
    headers = {
     'Authorization': 'Bearer API_KEY_TOKEN'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)   
    ```

For each game added, the Second Stage Analytics team provides comprehensive support for integration, deployment, and testing, starting with an onboarding call.

#### Integration Overview

The integration process involves the following steps:

1. Obtain API Credentials: Retrieve your API key and secret from the TRACKS dashboard.
2. Set Up Server Environment: Ensure your Google Cloud Platform (GCP) infrastructure is configured to handle HTTP requests.
3. API Endpoints: Utilize the Measurement API endpoints to send data. Use /measure for game events (e.g., game opens) from your telemetry server, and /collect for web visits containing traffic acquisition sources from your website.
4. Test the Integration: Verify that acquisition data is being tracked accurately.

##### Step 1: Obtain API Credentials

1. Log in to your TRACKS account.
2. Navigate to Settings > API Credentials.
3. Copy the API key and secret for use in your server configuration.

##### Step 2: Set Up Google Cloud Platform (GCP) Environment

1. Go to [Google Cloud Console](https://console.cloud.google.com/), sign in with your email address. Create a new Project.
If your organization does not use Google Workspace (Gsuite email account), you can link your email following these steps: https://support.google.com/accounts/answer/176347)

![Google Cloud Access](/assets/attribution_GCP.png)

2. [Enable billing for your account and link to your Project](https://cloud.google.com/billing/docs/how-to/modify-project#how-to-change-ba)
    - Microservices enabled in your Google Cloud will autoscale depending on data ingestion volume.
    - Estimated costs for 2 million installs in a single month should be around ~$40.
3. Go to IAM and admin, click on Grant Access, select permission: Basic -> Owner for analytics@secondstage.io
4. The Second Stage team will be notified after access is granted and TRACKS Attribution Measurement microservices are deployed for your instance.
5. [Your API key and secret will be entered as environment variables to Google Cloud Run functions](https://cloud.google.com/functions/docs/configuring/env-var) 

##### Step 3: API Endpoints

To track media channel acquisition sources, you need to implement the API endpoint that records acquisition events.
    
=== "API endpoint `collect`"

    *API Endpoint:* `/collect`

    *Description:* This endpoint records web events, capturing details about the acquisition source.

    *Method:* POST

    *Endpoint URL:* `https://tracks.yourgame.com/v1/collect`

    *Headers:*
    `Authorization:` Bearer `<API_KEY>`
    `Content-Type: application/json`

    Here is an example of source code for your reference:

    ```json
    # Example Python Code for web client-side
    import config
    import requests


    def track_acquisition(data):
       headers = {
           'Authorization': f'Bearer {config.API_KEY}',
           'Content-Type': 'application/json'
       }
       try:
           response = requests.post(f"{https://tracks.yourgame.com/v1/collect", json=data, headers=headers)
           response.raise_for_status()
           print('Acquisition event recorded:', response.json())
       except requests.exceptions.HTTPError as err:
           print('Error recording acquisition event:', err.response.json())


    acquisition_data = {
       "event_name": "web_visit",
       "timestamp": "2024-08-29T12:00:00Z",
       "channel": "paid_search",
       "campaign": "summer_sale",
       "source": "google",
       "medium": "cpc",
       "term": "steamsale",
       "content": "ad_1",
       "clientId": "12345",
       "sessionId": "abcdef123456",
       "ip": "175.124.248.15",
       "device": "mobile",
       "browser": "chrome"
    }


    track_acquisition(acquisition_data)
    ```

=== "API Endpoint `measure`"

    *API Endpoint:* `/measure`

    Description: This endpoint records web events, capturing details about the acquisition source.

    *Method:* `POST`

    *Endpoint URL:* `https://tracks.yourgame.com/v1/collect`

    *Headers:*
    `Authorization:` Bearer `<API_KEY>`
    `Content-Type: application/json`

    Here is an example of source code for your reference:

    ```json
    # Example Python Code for server-side 
    import requests

    url = "https://tracks.yourgame.com/v1/measure" 

    payload = {
     'user_id': '1a23fd44c21f8l5r',
     'event_name': 'game_open',
     'ip': '175.124.248.15',
     'timestamp': '2024-08-29T12:00:00Z',
     'platform': 'pc',
     'storefront': 'steam'
    }
    headers = {
      'Authorization': f'Bearer {config.API_KEY}',
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    ```

#### Architecture 

![Architecture](/assets/attribution_architecture.png)

### Web (Landing Page) Integration

!!! tip "Important:"

    Required for Modeled Attribution Tracking, Measured Attribution Tracking, Measured Attribution Tracking + Modeling.
    By linking TRACKS with Steamworks, Google Analytics 4 and Google Tag Manager access, you will be able to use the Modeled Installs reporting feature. Please note that postbacks only work if you are using the Measured Attribution Tracking or Measured Attribution Tracking + Modeling solution. 

By embedding the TRACKS JavaScript code into your landing page, device fingerprints are collected from visitors during each website session. These fingerprints are then matched with those gathered in-game, allowing for precise user attribution.

To ensure accurate attribution when using your website as the attribution source, it’s important to correctly implement UTM tagging in your paid media or content creator campaigns. We recommend using the TRACKS UTM builder sheet to properly generate tracking links for your landing page (please refer to Marketing Analytics > Setup for more information).

![Landingpage](/assets/attribution_landingpage.png)

An additional benefit of using your landing page with the TRACKS JavaScript snippet is the ability to track not only paid media, but also web referrals and organic traffic. This means that even without running paid media ads, you can still monitor and report on installs generated from organic referral sources. We also recommend applying UTM tagging to your owned media, such as CRM emails and social media, to further expand your attributed install data.

In addition, the TRACKS JavaScript code automatically applies UTM parameters to your outbound storefront links. When a visitor with a defined acquisition source, medium, or referral clicks on the storefront buttons and navigates to platforms like Steam, the UTM information is captured and transferred to the storefront page. This allows for seamless integration between Google Analytics and Steamworks Analytics, providing a comprehensive view of your traffic sources.

Implementation of the TRACKS JavaScript code is managed by the Second Stage team and requires access to Google Tag Manager as described below. If you do not already have Google Tag Manager installed on your landing page, we can help you integrate it.

By providing access to Google Tag Manager, we will be able to configure the following:

- **Google Analytics 4 (GA4) for website conversion measurement and identifying session/visit sources:**
    TRACKS integrates with GA4 to capture a session's acquisition source and access multi-channel funnel data. As mentioned in the features section, TRACKS also uses web conversions as a key source of behavioral data that is included in the reporting suite as web conversion metrics.
If GA4 is not already set up on your site, provide us with access to Google Tag Manager at analytics@secondstage.io and we will create and configure it for you. If GA4 is already installed, granting access will enable us to audit and optimize your analytics setup for your marketing campaigns.

- **Media platform web pixel tagging**: 
    By granting Google Tag Manager and media platform access to analytics@secondstage.io, TRACKS can set up a web conversion event or pixel if one is not already in place. You can use this event to optimize your media platform campaigns in addition to Install Postbacks. Since web conversion events provide valuable insights into user behavior, it’s recommended to include them in your conversion objective campaigns. When used alongside the Installs (game_opens) event, this creates an optimized conversion funnel, helping you achieve the best possible campaign performance.

Here is an example of source code for your reference:

```json
<script>
// TRACKS by Second STAGE Web Snippet
(function (A, S, D, F, W, E) {
 (A.tracks =
   A.tracks ||
   function () {
     (A.tracks.q = A.tracks.q || []).push(arguments);
   }),
   (A.tracks.q = []),
   (A.tracks.r = 1 * new Date());
 (W = S.createElement(D)), (E = S.getElementsByTagName(D)[0]);
 W.async = 1;
 W.src = F;
 E.parentNode.insertBefore(W, E);
})(window, document, "script", "https://cdn.secondstage.io/tracks.js");
tracks("page_view", "2S-XXXXXX");
</script>
```

Each game will be assigned a unique token to replace "2S-XXXXX." After granting Google Tag Manager access, you'll be able to see the TRACKS JavaScript snippet deployed in your GTM container.

*Example*

![GTM Web Snippet](/assets/attribution_gtmwebsnippet.png)

![GTM Web Snippet](/assets/attribution_datasources.png)

*Integration:*

If you have already set up these accounts with Second Stage as part of the [Marketing Analytics](/marketing-analytics) setup for TRACKS, there is no additional step to take.
For more information,

- please refer to our section [Marketing Analytics > Setup > Google Tag Manager](marketing-analytics/#google-tag-manager-integration-access) on how to set up Google Tag Manager for TRACKS
  
- please refer to our section [Marketing Analytics > Setup > Google Analytics (GA4)](/marketing-analytics/#google-analytics-integration-access)  on how to set up Google Analytics  for TRACKS.
  
- please refer to our section [Marketing Analytics > Setup > Steamworks](/marketing-analytics/#steamworks-integration) on how to set up Steamworks for TRACKS.

### Postbacks 

Postbacks are HTTP requests, typically GET or POST, sent to external servers. TRACKS can transmit installation and in-game event data back to advertising channels using a click ID as the key identifier. This enables platforms like Meta, Google, X, TikTok, and Reddit to identify users with similar behaviors. Instead of focusing solely on clicks, it's more effective to send postbacks for installs and in-game events to optimize campaign performance.

The click ID, collected on the landing page via the TRACKS JavaScript snippet after an ad click, is the only identifier passed along with event data to these advertising channels.

Most media platforms offer an Event/Conversion API module designed for developers. TRACKS' backend can integrate with these platforms' Conversion APIs to post back in-game events, such as installs, that match the click ID collected during attribution. Enabling postbacks closes the loop on tracking and targeting, enhancing media platforms' algorithms to optimize for valuable in-game conversions rather than just ad clicks, engagements, or web conversions. This is particularly beneficial for performance marketing campaigns focused on conversion objectives.

However, for campaigns with objectives such as driving traffic, optimizing for web conversions may be more advantageous, as these occur earlier in the user journey.

Below is an example postback guide template for mapping the Conversion API for various platforms. By utilizing the access provided for media platforms, TRACKS can automatically deploy each platform’s Conversion API from its backend. The TRACKS postback solution can be activated simply by granting editor access for the Events/Dataset management of the media platform.

This one-time setup for each media platform allows TRACKS to implement the Conversion API for your ad accounts without consuming developer resources or relying on third-party solutions like Customer Data Platforms (CDPs).

![Postbacks](/assets/attribution_postbacks.png)

**Meta Conversion API Guide:**

[→ Conversions API Setup Guide for Meta](https://www.facebook.com/business/help/232481544843294?id=818859032317965)

Editor access for the Data Source Asset to analytics@secondstage.io is required.

**Google Conversion API Guide:**

[→ Conversions API Setup Guide for Google](https://developers.google.com/google-ads/api/docs/get-started/dev-token)

A manager account (MCC) is needed to enable Conversion API for Google ads. Follow the guide above to activate your API (Apply for access to the Google Ads API). 
Share the developer token from the “API Center” after you complete your API access process.

**TikTok Conversion API Guide:**

[→ Conversions API Setup Guide for TikTok](https://business-api.tiktok.com/portal/docs?id=1738855176671234)

TikTok business developers account is needed for the Conversion API. Follow registration steps by choosing “Direct Advertiser”. After your developer profile is approved, inform your Second Stage contact to handle creating the [Business App](https://business-api.tiktok.com/portal/docs?id=1738855242728450) and configuring the [Web Events API](https://business-api.tiktok.com/portal/docs?id=1739584855420929). 

**Reddit Conversion API Guide:**

[→ Conversions API Setup Guide for TikTok](https://business.reddithelp.com/helpcenter/s/article/Conversions-API)

Reddit access given prior would be sufficient for TRACKS to activate Conversion API for Reddit. Developer access token can be created through Reddit Events Manager.

For your reference Reddit’s documentation that are required for CAPI listed here: 

[→ Reddit Conversion Access Token](https://business.reddithelp.com/helpcenter/s/article/conversion-access-token)

[→ Conversions API Setup Guide for Reddit](https://business.reddithelp.com/helpcenter/s/article/using-the-API-for-conversions)

**X Ads Conversion API Guide:**

Use your company Twitter handle to create a developer account and apply to have Ads API access. 

Sign up for Developer Access [here](https://developer.twitter.com/en/portal/petition/essential/basic-info) (select free). Then send a request for Conversions Only Access. Once approved, inform your Second Stage contact to deploy X Ads CAPI for TRACKS.  

[→ Conversions API Setup Guide for X](https://developer.x.com/en/docs/x-ads-api/measurement/web-conversions/conversion-api)

### Test Environment 

**Test the Integration:**

- Click on the UTM-tagged test link and open the game for the first time.
- Ensure your server is running and correctly configured to handle HTTP requests.
- Trigger acquisition events manually or through your application to test the integration.
- Check Cloud Run logging to confirm that the endpoint logs show no errors.
- Verify on the attribution tool dashboard that acquisition events are tracked accurately.
- Ensure that the data (channels, campaigns, sources) aligns with your expectations.
  
**Troubleshooting:**

- Invalid Credentials: Confirm that your API key and secret are correct and have the necessary permissions.
- Network Errors: Review your server’s network configuration and API base URL.
- Data Mismatches: Ensure the event payload matches the required schema and that timestamp formats are correct.
