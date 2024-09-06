# Attribution Tracking

## Overview

With TRACKS Attribution, our proprietary full-funnel attribution tracking solution that is part of the TRACKS platform, we can provide valuable insight into your lower-funnel media campaigns. This solution consists of three components, all managed and supported by the Second Stage team.

1. **Integration of the TRACKS Measurement API**: The first step is to integrate the TRACKS Measurement API with your telemetric/logging server. This instance will be deployed to your cloud account. If you don't already have a cloud server, we'll help you create one, with full ownership at your end.  
2. **Ad Operations Support**: Once attribution tracking is verified, the Second Stage team will assist with media platform integrations. This process requires adherence to specific naming conventions for campaigns, ad groups, and ads to ensure accurate reporting. Additionally, UTM-tagged links must be used. The Second Stage team will provide a naming convention generator sheet tailored to your chosen ad platforms or activations. If you already have a naming convention in place, TRACKS can be adapted to your mapping.   
3. **Postback Setup**: With access to your media platforms, TRACKS will create events/pixels for game\_opens and activate the platform’s Conversion API to feed back attributed in-game data.

> **All aspects of using TRACKS Attribution are configurable and will be tailored during your onboarding call with the Second Stage team. This documentation outlines a standard best-practice approach to building an attribution and BI suite, based on years of expertise in user acquisition, media, BI, tracking, and attribution from the Second Stage team.**

### Functionality

A proper attribution setup can shine a light into the "black box" of where valuable game purchases, activations or installs are coming from. Once an attribution solution is integrated, whether it's TRACKS or a third-party solution, the dashboard will display key lower-funnel metrics.

If you're using TRACKS Attribution, the default dashboard will show install metrics, including Measured, Paid, Organic and Modeled installs. It's important to note that "installs" refer to the first activation of the game (when the player starts the game for the first time), not purchases.

These install metrics can be further broken down by storefront or platform, such as CPI (Xbox), CPI (Steam), CPI (PS), CPI (Epic), and CPI (Nintendo), assuming the measurement API is provided with the appropriate parameters. Other install metrics we are providing in addition to CPI are eCPI and CR%.

Based on your average unit price, TRACKS can estimate revenue per install and report ROAS (Return on Ad Spend) percentages. This allows you to compare and analyze performance across multiple dimensions, including

- Date 
- Channel  
- Campaign 
- AdGroup (Ad Set)  
- Creative (Ad)  
- GEO  
- Strategy  
- Target  
- Target Audience  
- Targeting  
- Ad Type  
- Ad Format  
- Placement

In addition to tracking in-game events, web conversions are critical to understanding the user journey. TRACKS can report on web conversions such as Steam, PS, Xbox, Nintendo and Epic storefront button clicks, completing the event funnel for your user acquisition media campaigns.

To enable web conversion tracking, a TRACKS JavaScript snippet wraps your landing page's storefront button click URLs to ensure that Steam and other storefront UTM analytics capture as many UTM-tagged visits as possible. We recommend avoiding redirect tracking links and instead using a plain landing page URL with UTM tags for seamless integration with media platforms.

Post-view or impression-based tracking in video game marketing across paid media channels adds complexity and can negatively impact the accuracy of data-driven attribution. For top-of-funnel campaigns with awareness objectives, using awareness reports to evaluate performance is preferable. For consideration and conversion-focused campaigns, attribution is based on clicks, as a landing page session triggers the attribution touchpoint.

By combining all components of the user flow with TRACKS Attribution, the standard dashboard allows reporting across the entire funnel, e.g.:

Impression \-\> Click \-\> Web Visit \-\> Web Conversion (button click) \-\> Steam Visit \-\> Steam Activation \-\> Install

Metrics available in TRACKS include

- Media Metrics  
- Web Analytics Metrics  
- Steamworks metrics  
- Attribution Metrics  
- Awareness Metrics

In addition, based on your onboarding call and the status of your game release, optional metrics may include

- Steam wishlist and pre-order metrics  
- DLC installs and in-game purchases metrics (requires an additional measurement API call)  
- Influencer / Streamer Analytics metrics  
- Brand Health metrics


### Attribution Tracking Options 

TRACKS offers three different approaches to attribution tracking that can be implemented based on different requirements, which are detailed here. Our recommended solution for best results is the **Measured Attribution Tracking & Modeling** approach.

| Methodology     | Description | Benefits     |
| ----------- | ----------- | ----------- |
| Modelled Attribution Tracking    | This methodology uses a data-driven approach to assign conversion weights using data from Steam UTM Analytics and Google Analytics (GA4). It calculates conversions using a Markov chain attribution model and integrates data from Steam and media campaigns to determine the uplift generated by paid media.  | This method provides a comprehensive view by combining web and Steam data, accurately assigns conversion weights, and offers insights into media campaign effectiveness through Marketing Mix Modeling.      |
| Measured Attribution Tracking   | This method uses server-side integration to track game installs directly through the TRACKS attribution solution. It requires no SDK implementation and collects telemetry data to accurately attribute installs.  | It enables real-time, accurate install tracking without client-side risks, requires no changes to game code, and is optimized for PC/console games following industry best practices.   |
| Measured Attribution Tracking + Modeling (Best Practice)   | This methodology combines measured attribution (server-side) with a Markov chain modeling solution for untracked installs. This unified approach compensates for untraceable sources by redistributing untracked installs to their potential origins.  | This approach ensures up to 98% attribution accuracy within a 24-hour window, combines measured and modeled data for a complete attribution view, and increases install tracking accuracy by redistributing untracked game opens.   |


#### Modelled Attribution Tracking

This method calculates conversions using our data modeling solution. Due to the specific data requirements, this approach is available only for games released through Steam.

1. **Data Sync:** TRACKS first syncs data from Steamworks UTM Analytics and Steam Traffic Breakdown reports, capturing trusted visits, tracked visits, wishlists, purchases and activations.
2. **Web Conversions:** Where available, GA4 Web Conversions are included via multi-funnel channel data, detailing the user journey for each web session. TRACKS uses a Markov chain attribution model, a data-driven methodology, to accurately assign conversion weights.
3. **Media Uplift Analysis:** Using a marketing mix modeling approach, TRACKS integrates data from Steam's traffic breakdown, media and web analytics (spend, impressions, clicks and web conversions) to determine the uplift generated by paid media across all traffic sources. A linear regression model is then applied using estimated total Steam activations by date and market (based on reviews, followers, and CCU) to extrapolate the impact of media campaigns (Steam Activations / Attributed Steam Modeled Installs).
   
The following metrics will be available:

- Measured Installs (from Steamworks UTM Analytics)
- Modeled Installs
- Estimated CPI
- eCPI
- Web Conversions
- CR% (Conversion Rate)
- ROAS (Return on Ad Spend)

TRACKS uses a Marketing Mix Modeling (MMM) approach enhanced with Steam UTM Analytics, Traffic Breakdown data and Google Analytics (GA4) data. If you don't have a website or don't use it as a landing page, the efficiency of the model is reduced by 30% because it relies solely on Steam UTM Analytics, Visits and Traffic data.

> If you're interested in this method but don't have a landing page or are unsure of your current setup, Second Stage can help you create a landing page or game website for marketing purposes. [Contact us](https://secondstage.io/contact/) for a quote!


#### Measured Attribution Tracking

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

```
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


#### Measured Attribution Tracking + Modeling

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

## Integration 

Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.

### Managed Service Approach

Integration Plan & Checklist

### Enterprise-Level Deployment (Hybrid SaaS)

Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.

### TRACKS Attribution Measurement API

Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.

### Postbacks 

Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.

### Test Environment 

Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
