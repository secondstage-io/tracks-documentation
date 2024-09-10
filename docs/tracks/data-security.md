# Data Handling & Security

!!! tip "Important:"

    We do not provide legal advice. This page is designed to help game developers gain a better understanding of managing their players' rights when working with Second Stage. You should consult your legal counsel before making decisions about how your company complies with the evolving landscape of consumer privacy. 
    
Second Stage is committed to providing our partners and clients with the highest level of transparency and governance, ensuring they comply with the GDPR and CCPA at all times. As a result, privacy is a fundamental principle of TRACKS.

Tracks enhances privacy by minimizing data exposure through a smart and secure hybrid cloud setup. On top, TRACKS offers API-level access to GDPR compliance tools, enabling you to efficiently manage rights such as access requests, the right to be forgotten, and opt-outs. As a managed service provider, our team is always available to support you in maintaining GDPR compliance.

Under the GDPR, the roles of data controller and data processor are defined as follows:

**Data Controller:** The data controller is the entity that determines the purposes and means of processing personal data. Essentially, the controller decides why and how personal data will be processed. They are responsible for ensuring GDPR compliance, handling data subjects' rights, and managing relationships with data processors.

**Data Processor:** The data processor acts on behalf of the data controller and processes personal data according to the controller's instructions. The processor doesn't own or control the data but is responsible for implementing appropriate technical and organizational measures to protect it. They must comply with the controller’s instructions and maintain records of processing activities.

Both controllers and processors have specific responsibilities and obligations under GDPR, particularly regarding data protection, breach notifications, and agreements defining the scope of data processing.

## Data Handling under GDPR regulations

Second Stage TRACKS is fully compliant with GDPR regulations. There are two integration options available:

1. Data Sent to the TRACKS Server: Here, the data is sent to TRACKS servers, which can be located in either the US or the EU. If the data is sent to the US, the client must update its privacy policy to reflect this and obtain user consent when the game is launched for the first time.

2. Data Sent to the customers’ server: In this method, all data is sent directly to the customer’s server at their location. TRACKS does not collect any data on its side. This means it is the customer’s responsibility to ensure that proper opt-in and opt-out mechanisms are in place. 

Our suggested deployed method is to use Publisher / Developer studio’s configured Google Cloud project.  Other Google Cloud microservices used include Cloud Storage, Cloud Run, Pub/Sub, Cloud Functions, Artifact Registry, and App Engine.  The system user: analytics@secondstage.io will be added as an Owner to your Google Cloud Project for operational and management purposes. If you are unable to use GCP for deployment, Second Stage can host TRACKS in an isolated environment. This would require change in your EULA as Second Stage will need to host attribution data in the account.   

**Data Transfer Compliance:** Transferring data from an EU client to the US requires a strict EULA agreement and user consent. TRACKS’ default cloud servers are located in the EU (Google Cloud Frankfurt). Per request, Second Stage can offer both EU-based and US-based cloud servers. A self-hosted (hybrid) version is also available for customers.

**PII Compliance:** TRACKS handles PII in a standard manner, similar to other telemetric data collection vendors. While data is collected at the user level, it is processed in a pseudonymized and aggregated form. The primary PII concern is the client IP, which is collected as a parameter through the API. This information is not stored openly but is instead hashed using a non-reversible method, with a 30-day data retention period. The reporting suite only provides aggregated data, not user-level data, ensuring that no PII is stored or accessible.

For marketing campaigns involving a website, TRACKS distinguishes between marketing, analytics and necessary cookies and configures the required tags according to the cookie consent mechanism.

## Data Retention

Event data retention is by default 18 months and resets with new activity. This period can be adjusted upon request. Event data tables will contain one-way SHA256 hashed user IPs, user_ids, event and other supplied parameters like os_platform, storefront, acquisition source etc.  

However, granular log history of the attribution inserts, such as in-game events and web visits, have a 30-day data retention period and can not be increased for only logging, error handling and record keeping purposes and doesn’t get stored in any database.   

## EULA information

Your End User License Agreement (EULA) must clearly state what data will be tracked and why. Please consult your legal councel for further information.

If you need assistance, we can provide examples of EULAs or privacy agreements.

## TRACKS GDPR API

For those with existing data management systems, TRACKS‘ GDPR APIs can be integrated to centralize your GDPR compliance. 

Under GDPR, personal data includes the following: 

- Online identifiers
- IP addresses
- User location data
- Behavioral and demographic profiling data 

User opt-outs are managed through the GDPR Forget API, which will be provided once TRACKS is integrated into production.  

Data Removal by User_id and Data Request by User_id is available via GDPR API. 

The parameter for identifying a user is the user_id, using this key in your GDPR forget API call, deletes all records of the user_id permanently, and blocks the same user_id from new entries.  

IP parameters will not be returned openly from the GDPR API call as they are stored with SHA256 hash.  

## Right to Access / Erasure

When your users consent to being tracked, it is your responsibility as the data owner to safeguard this information. You must provide proper opt-in, opt-out options, and the right to be forgotten. Second Stage is providing assistance for you to meet these obligations.

A key principle under both GDPR and CCPA is the player's right to request the deletion of their personal information from data controllers at any time. We support this right by a user privacy API that integrates right-to-access and opt-out requests into customers' internal processes.

Our service is designed to comply with our customers' DPAs, which we execute as part of our service agreements.

## IP Truncation

We do not offer IP truncation, as it can result in inaccurate or poor data for Measured Attribution Tracking. In this case, we recommend using a Modeled Attribution Tracking solution instead.



