# Attribution Tracking

## Overview

With TRACKS Attribution, our proprietary full-funnel attribution tracking solution that is part of the TRACKS platform, we can provide valuable insight into your lower-funnel media campaigns. This solution consists of three components, all managed and supported by the Second Stage team.

1. **Integration of the TRACKS Measurement API**: The first step is to integrate the TRACKS Measurement API with your telemetric/logging server. This instance will be deployed to your cloud account. If you don't already have a cloud server, we'll help you create one, with full ownership at your end.  
2. **Ad Operations Support**: Once attribution tracking is verified, the Second Stage team will assist with media platform integrations. This process requires adherence to specific naming conventions for campaigns, ad groups, and ads to ensure accurate reporting. Additionally, UTM-tagged links must be used. The Second Stage team will provide a naming convention generator sheet tailored to your chosen ad platforms or activations. If you already have a naming convention in place, TRACKS can be adapted to your mapping.   
3. **Postback Setup**: With access to your media platforms, TRACKS will create events/pixels for game\_opens and activate the platform’s Conversion API to feed back attributed in-game data.

All aspects of using TRACKS Attribution are configurable and will be tailored during your onboarding call with the Second Stage team. This documentation outlines a standard best-practice approach to building an attribution and BI suite, based on years of expertise in user acquisition, media, BI, tracking, and attribution from the Second Stage team.

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

By combining all components of the user flow with TRACKS Attribution, the standard dashboard allows reporting across the entire funnel, from:

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

#### Modelled Attribution Tracking

This method calculates conversions using our data modeling solution. Due to the specific data requirements, this approach is available only for games released through Steam.

1. Data Sync: TRACKS first syncs data from Steamworks UTM Analytics and Steam Traffic Breakdown reports, capturing trusted visits, tracked visits, wishlists, purchases and activations.
2. Web Conversions: Where available, GA4 Web Conversions are included via multi-funnel channel data, detailing the user journey for each web session. TRACKS uses a Markov chain attribution model, a data-driven methodology, to accurately assign conversion weights.
3. Media Uplift Analysis: Using a marketing mix modeling approach, TRACKS integrates data from Steam's traffic breakdown, media and web analytics (spend, impressions, clicks and web conversions) to determine the uplift generated by paid media across all traffic sources. A linear regression model is then applied using estimated total Steam activations by date and market (based on reviews, followers, and CCU) to extrapolate the impact of media campaigns (Steam Activations / Attributed Steam Modeled Installs).
   
The following metrics will be available:

- Measured Installs (from Steamworks UTM Analytics)
- Modeled Installs
- Estimated CPI
- eCPI
- Web Conversions
- CR% (Conversion Rate)
- ROAS (Return on Ad Spend)

#### Measured Attribution Tracking

Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.

#### Measured Attribution Tracking + Modeling (TRACKS Suggested Solution)

Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.

## Integration 

Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.

### Managed Service Approach

Integration Plan & Checklist

### Enterprise-Level Deployment (Hybrid SaaS)

Some text

### TRACKS Attribution Measurement API

Some text

### Postbacks 

Some text

### Test Environment (?)

Some text
