# Data Handling & Security

!!! tip "Important:"

    We do not provide legal advice. This page is designed to help game developers gain a better understanding of managing their players' rights when working with Second Stage. You should consult your legal counsel before making decisions about how your company complies with the evolving landscape of consumer privacy. 
    
Second Stage is committed to providing our partners with the highest level of transparency and governance. **TRACKS** is designed to be a "privacy-first" marketing intelligence platform, enabling you to optimize your strategies while adhering to strict data protection standards like the GDPR.

TRACKS, in its standard configuration, operates on principles that support a consent-free model for basic attribution, relying instead on legitimate business interests and strict data minimization.

---

## Roles under GDPR

The architecture of TRACKS is unique in that it places the customer in full control of the data processing environment.

* **You are the Sole Controller:** Because the software operates entirely on your own infrastructure and you determine the means of processing, you are the sole "Controller" under the GDPR.
* **We are the Software Provider:** Second Stage GmbH does not process end-user data on its own servers and is therefore **not** classified as a "Processor" or "Controller" of your user data. We simply provide the code that runs in your environment.

## Lawful Basis for Processing

TRACKS is built to enable data processing under **Article 6(1)(f) GDPR (Legitimate Interest)**.

* **Legitimate Interest:** TRACKS is designed to help you measure campaign success, analyze product performance, and optimize marketing spend. Independent legal analysis supports treating this as a legitimate business interest. That analysis is not a binding assessment of your specific deployment — as controller, you remain responsible for carrying out and documenting your own balancing of interests. Because the data is pseudonymized, subject to defined retention limits, and places no persistent identifiers on the player's device, this interest typically outweighs the impact on user privacy.
* **No Consent Required (Standard):** Consequently, you generally do not need to obtain explicit end-user consent (e.g., via a cookie banner) for standard attribution functions, provided you inform users in your privacy policy.

!!! info "Exception: Postback Functionality"
    If you choose to activate the **Postback function** to send conversion signals back to third-party advertising channels, that function requires **explicit consent (Art. 6(1)(a) GDPR)**. Core attribution is unaffected — the consent requirement applies to postbacks only.

    **Where consent is obtained:** as *marketing consent* on your product landing page, through the consent banner already running there (typically wired up via GA4 consent mode in GTM). TRACKS records the resulting flag through the `/collect` endpoint and uses it to decide whether a postback may fire.

    **No in-game consent prompt is required.** The consent captured on the landing page covers the postback for the install that follows. You do not need to ask again inside the game, and TRACKS does not display any consent UI to players.

## Data Minimization & Retention

TRACKS adheres to the principle of data minimization by collecting only what is technically necessary and deleting it as soon as possible.

| Feature | Description |
| :--- | :--- |
| **No Cookies for Attribution** | Core attribution sets no cookies, uses no LocalStorage, and places no persistent identifiers on the player's device. The only exception is the optional [Postback](../attribution/postbacks/index.md) function, which reads the marketing-consent flag captured by your landing page's consent banner — see the postback note above. |
| **Hashed IP Addresses** | IP addresses are never stored in plain text. They are cryptographically salted and hashed immediately upon receipt. |
| **Salt Rotation** | The "salt" used for hashing is rotated regularly, preventing long-term re-identification or cross-referencing of users. |
| **30-Day Raw Log Retention** | The raw logs used for attribution (`collect_logs` and `measure_logs`) are automatically deleted after 30 days. |
| **9-Month Event Data Retention** | The pseudonymized event data derived from those logs — salt-hashed IPs, pseudonymized `user_id`s, and event parameters — is retained for 9 months by default, resetting on new activity from the same `user_id`. Configurable to your own retention policy on request. |
| **Encryption** | All data is encrypted during transmission (TLS) and at rest on your servers. |

Both retention tiers sit in your own BigQuery dataset, and the [Right to Forget](#right-to-forget) API clears a given `user_id` from both. For the field-level breakdown, see [Data Collection and Processing](datacollection.md#data-deletion-and-retention).

## Infrastructure & Control

For the highest level of security and transparency, TRACKS operates on a scalable, auto-managed cloud infrastructure built like an on-premise solution.

* **Your Cloud Environment:** Our deployment method uses your own configured Google Cloud project. Services include Cloud Storage, Cloud Run, Pub/Sub, and Cloud Functions.
* **Full Control:** You decide the server location (e.g., EU-only data centers), access rights, and security configurations.
* **No External Transfer of Personal Data:** Personal data is sent directly to your server endpoints. TRACKS does not collect or mirror it on Second Stage servers. Only **anonymized, aggregated** results — figures that cannot be traced back to an individual player — are passed to the Second Stage datalake that powers the TRACKS Reporting Suite. No per-user records, hashed identifiers, or raw logs leave your project.

## PII & Global Compliance (CCPA, CPRA)

The "privacy-by-design" architecture of TRACKS also supports compliance with US frameworks regarding Personally Identifiable Information (PII).

* **No Sensitive PII:** TRACKS does not collect sensitive PII such as names, emails, phone numbers, or physical addresses.
* **Pseudonymization:** IP addresses are salt-hashed and user IDs are pseudonymized before storage, so records cannot be attributed to an identifiable person without additional information. This reduces the risk associated with PII storage and supports the data minimization principles found in the CCPA and CPRA.
* **Pseudonymized is not anonymized:** The data held in your project is pseudonymized, and pseudonymized data remains **personal data** under the GDPR — it stays in scope for data subject rights and for your records of processing. Only the aggregated figures passed to the Second Stage datalake are anonymized. Keep the two apart in your documentation.

## Right to Forget

To support your obligations under the GDPR, TRACKS includes a specific **"Right to Forget" API**.

This feature allows you to permanently delete all records associated with a specific `user_id` or `hash` upon a user's request. This ensures that you can fully comply with **Data Subject Access Requests (DSARs)** without manual database intervention.

For integration instructions, please refer to the [GDPR API Documentation](../attribution/gdprapi.md).

---

## Privacy Policy Disclosures

To ensure transparency, you should disclose the use of TRACKS in your privacy policy to inform your users about the data processing.

!!! quote "Example Policy Text"
    *Please note that this text is provided as an example only and should be reviewed by your legal team.*

    **Note on the use of the TRACKS analysis software**

    **1. Scope of personal data processing**
    We use the TRACKS analysis software from Second Stage GmbH, Roedernstr. 5, 13053 Berlin, on our website and game to evaluate page views and the use of our website and game. The API endpoints used for this purpose process, among other things, the URL accessed, referrer information, UTM parameters, the user agent used, and event data from our product (e.g., “first_game_open”). In addition, the IP address is processed exclusively in pseudonymized form (salt hash); complete IP addresses are not stored. The software sets no cookies and places no local storage elements or other persistent identifiers on your device. Where we have enabled the postback function, conversion signals (for example, that the game was installed) are shared with the advertising channels we use — and only if you have given marketing consent on our landing page.

    **2. Legal basis for the processing of personal data**
    Processing is carried out on the basis of **Art. 6 (1) lit. f GDPR**. We have a legitimate interest in evaluating the use of our website and our product range, measuring the effectiveness of our campaigns, and optimizing our services from a technical perspective. Due to the exclusively pseudonymous processing, the defined storage periods set out below, and the fact that no cookies or other persistent identifiers are placed on your device, we believe that there are no overriding interests of the data subjects that are worthy of protection.

    **3. Recipients**
    Processing takes place entirely on servers controlled by us. No personal data is passed on to the software provider. Apart from any contract processors we engage ourselves, data is disclosed to third parties only where the postback function is active: in that case, and only if you have given marketing consent, conversion signals are transmitted to the advertising channels we use (for example Meta, Google, TikTok, or Reddit).

    **4. Purpose of data processing**
    The data is processed for the purpose of analyzing the use of our website and our products, optimizing our offering, and to evaluate the effectiveness of our marketing and sales channels. In addition, the pseudonymous linking of website visits and product usage events enables better technical control and error analysis of our offering.

    **5. Duration of storage**
    The raw access and event logs are stored pseudonymously and automatically deleted after 30 days. The pseudonymized event data derived from them — salt-hashed IP addresses, pseudonymized user IDs, and the associated event parameters — is stored for a maximum of 9 months from the last recorded activity and is then deleted. Data subjects can request erasure of the data relating to them at any time, using the contact details given in this privacy policy.

!!! warning "Check the retention figures before you publish"

    The 30-day and 9-month periods above are the TRACKS defaults. If your event data retention has been configured differently, state your actual period. Publishing a shorter period than you operate is an Art. 13 accuracy problem, so confirm the configured value with us before adopting this text.
