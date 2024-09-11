# Marketing Analytics

## Overview

TRACKS integrates ad, website and attribution data into an holistic view to enable easy comparison between channels, GEOs, beats and more at a glance. Created using the combined experience and perspective of performance media and gaming experts over the years, our marketing analytics reports are designed to show each dimension combination to provide clear picture to campaign performance.

???+ question "What type of data is tracked?"

    TRACKS combines Media Performance, Website and Attribution Data.

## Setup

To set up a game for marketing analytics with TRACKS, log into your TRACKS account and select the "Add New Game" option. For more details, refer to the relevant section.

Next, follow the steps below to allow us to connect your campaign data to our marketing analytics dashboard. If you're interested in using attribution tracking, please refer to the [corresponding section](/attribution-tracking/) in our documentation and complete the required steps. For further assistance, please feel free to contact our team at any time.

### Media Platforms & Ad Networks Integration

This section outlines the integration of major media channels for media analytics reporting, ad operations, and postbacks. It is recommended that you complete the integration of each channel one at a time, in collaboration with the Second Stage team, to ensure proper attribution setup.

!!! note ""

    Once a channel is integrated, there's no need to return to this step for future campaigns. This one-time platform configuration will enable comprehensive marketing analytics reporting for TRACKS. With the ad operations guide, you can easily launch new campaigns without further assistance.

#### Google Ads Integration

In your Google Ads account, click the Admin icon.

1. Navigate to Access and Security, then click the `plus` icon to add a new user.
2. Invite analytics@secondstage.io with `Standard` access permissions.
3. Follow the Campaign, Ad Set, and Ad naming conventions provided in the builder sheet shared by the Second Stage team.
4. Ensure your ad creatives use a UTM-tagged link template.

[→ Google Ads Setup Guide](https://support.google.com/google-ads/answer/6372672)

![Google Ads Setup](/assets/marketinganalytics_googleads.png)

#### Meta Ads Integration

1. Invite analytics@secondstage.io to your Ad Account and Business Manager with `Reader` permissions (ads reporting).
2. Share your Ad Account ID and Business Manager ID with the Second Stage team.
3. Follow the Campaign, Ad Set, and Ad naming conventions provided in the builder sheet shared by the Second Stage team.
4. Ensure your ad creatives use a UTM-tagged link template.

![Meta Ads Setup](/assets/marketinganalytics_meta.png)

#### TikTok Ads Integration

1. Log in to your TikTok for Business account.
2. Navigate to the Members tab and click Invite Member.
3. Invite analytics@secondstage.io to your Ad Account and Business Manager with `Standard` permissions (assets and ad accounts).
4. Follow the Campaign, Ad Set, and Ad naming conventions provided in the builder sheet shared by the Second Stage team.
5. Ensure your ad creatives use a UTM-tagged link template.

![TikTok Ads Setup](/assets/marketinganalytics_tiktok.png)

#### X Ads Integration

1. In your ads account, select "Edit access to account" from the drop-down menu.
2. On the multi-user page, click "Add access" and grant access to @2s-analytics with `Account Administrator` permissions (or invite analytics@secondstage.io).
3. Share your handle and ad account details with the Second Stage team.
4. Follow the Campaign, Ad Set, and Ad naming conventions provided in the builder sheet shared by the Second Stage team.
5. Use UTM-tagged links in your ad creatives. (Note: X Ads does not support macros, so ensure each ad creative has the correct landing page URL.)

![X Ads Setup](/assets/marketinganalytics_xads.png)

#### Reddit Ads Integration

1. Contact the Reddit team to have your ad account whitelisted for using the Reddit Ads API.
2. In the upper right-hand corner, click your account name and select ‘Switch user’ from the drop-down menu.
3. Choose the account you want to manage.
4. Grant Business Member access to analytics@secondstage.io with the following permissions: Ad Account Editor, Conversions, Reporting, History, and Analytics.
5. Follow the Campaign, Ad Set, and Ad naming conventions provided in the builder sheet shared by the Second Stage team.
6. Ensure your ad creatives use UTM-tagged links.

[→ Reddit Ads Setup Guide](https://business.reddithelp.com/helpcenter/s/article/Add-users-to-a-Reddit-Ads-account)

![Reddit Ads Setup](/assets/marketinganalytics_reddit.png)

### Web Analytics Integration (Landing page)

#### Google Tag Manager Integration & Access

In Google Tag Manager, please grant Editor access to analytics@secondstage.io. TRACKS will implement events and conversion pixels on your website to optimize landing page interactions and improve media platform targeting algorithms, as detailed above.

For guidance on installing GTM, refer to the documentation [here](https://support.google.com/tagmanager/answer/14842164).
Below is an sample image of the Google Tag Manager integration code that needs to be implemented on your landing page. 

![Google Tag Manager Setup](/assets/marketing-analytics_gtm.png "Google Tag Manager Setup")

#### Google Analytics Integration & Access

In Google Analytics (GA4), please grant Editor access to analytics@secondstage.io. For guidance on creating a GA4 account, refer to the documentation [here](https://support.google.com/analytics/answer/9304153). Alternatively, the Second Stage team can create one for you if needed.

![Google Analytics Integration](/assets/marketinganalytics_g4access-1.png "Google Analytics Setup")

![Google Analytics Integration](/assets/marketinganalytics_g4access-2.png "Google Analytics Setup")

### Steamworks Integration

If your game is available on Steam, please grant us access by sending an invitation to analytics@secondstage.io with "View Marketing Traffic Data" permissions only.

You can find the "Invite New User" section in Steamworks by navigating to Steamworks → Users & Permissions → Invite New User.

![Steamworks Setup](/assets/marketinganalytics_steamaccess.png "Steamworks Setup")

### Campaign Naming Conventions

After integrating an ad account, the Second Stage team will guide you through the Ad Operations aspect of the integration. This includes applying a specific taxonomy for media data analytics, mapping, and consolidation. An example of the builder sheet is provided below:

![Naming Conventions](/assets/marketinganalytics_namingconventions.png "Naming Conventions")

### UTM-tagged Links

For each integrated media platform, UTM-tagged link templates will be provided through the Ad Ops guide. These templates will include copy-and-paste-ready UTM tracking landing pages for use in your ads and assets.

``
https://landingpage.mygame.com/?utm_source=2S_socialmedia&utm_medium=meta&utm_campaign={{campaign.name}}&utm_content={{adset.name}}&utm_term={{ad.name}}
``

### Other Media Platforms and Ad Networks

For guidance on integrating additional ad platforms not mentioned above, such as Twitch, DV360, Quantcast, Disney Ads, Amazon Ads, CPMstar, Spotify Ads, Microsoft Ads, Snapchat, and others, please contact the Second Stage team. The integration process is generally similar, with seamless integration possible if the platform provides a reporting API. If an API is not available, data import via spreadsheet is recommended.

### Direct Buy Campaigns / Media Houses

For media houses and branded/direct buy campaigns like IGN, Gamespot, Gamerant, Loots, Fandom, etc., the reporting process is manual. You will receive a UTM tracking link builder spreadsheet for each activation. Regardless of attribution tracking, please report these activations' performance in the Awareness Reporting Suite rather than lower funnel tracking.

Media cost reporting for direct buy activations can be done via data imports. Contact the Second Stage team to obtain the media cost sheet format.

### Influencer Campaigns

The integration process for influencer campaigns is manual. You will be provided with a UTM tracking link builder spreadsheet for each content creator, streamer, or influencer. Use this spreadsheet to generate UTM-tagged links for each creator, which will then be tracked in the reporting dashboard.

Media cost reporting for influencer campaigns is also available through data imports. Contact the Second Stage team to get the media cost sheet format.

If you wish to include Video Content / Stream Analytics in your campaign reports, TRACKS can retrieve metrics such as Unique Viewers, Views, Comments, Likes, Engagement Rates, CCV, and Sentiment. This data will be collected based on the platform information, creator channel handle, video hashtags, and video IDs you provide.

## Media Services

If you require additional support, our team of gaming media specialists can manage your digital marketing campaigns from planning to execution. Leveraging TRACKS and our data-driven insights, we continuously optimize campaigns to deliver the best results for our clients. Our experts specialize in all major performance marketing channels and offer direct media buying with key gaming partners.

Using TRACKS, we craft full-funnel media strategies, managing and optimizing campaigns from the upper funnel through to purchase. From planning and setup to execution and reporting, we provide support wherever needed, allowing you to focus on what matters most. Please [contact us](https://secondstage.io/contact/) for further information and assistance.
