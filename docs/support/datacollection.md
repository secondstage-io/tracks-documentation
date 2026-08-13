# Data Collection and Processing

This page describes how TRACKS collects and processes data through its two API endpoints — `/collect` and `/measure` — covering what is gathered, how it is stored, and how long it is retained.

!!! tip "Related"

    - **Integrating** the endpoints: see [Measurement API](../attribution/measurementapi.md).
    - **Privacy and security** posture: see [Data Handling & Security](datasecurity.md).

## Data Flow Overview

### /collect Endpoint
**Trigger:** Activated on every page visit via first-party JavaScript on the product landing page or through a redirect link.  

**Data Collected:**

- Page URL, UTM parameters, `document.referrer`
- IP address (salt-hashed)
- User-Agent (used to detect device type, e.g., mobile vs. desktop)
- Marketing-consent flag from your landing page's consent banner (controls whether [postbacks](../attribution/postbacks/index.md) to ad channels may fire — see [Postback consent](datasecurity.md#lawful-basis-for-processing))

**Storage:** Data is stored in pseudonymized logs (`collect_logs`).  
**Retention:** Logs are stored for 30 days and then automatically deleted.  
**Notes:** No cookies, LocalStorage, or other client-side storage is used by this endpoint.

### /measure Endpoint
**Trigger:** Activated on `game_open` event  

**Data Collected:**

- Hashed `user_id` (pseudonymized)
- IP address (salt-hashed)
- Storefront (e.g., Steam)
- Event (e.g., first_game_open)
- Event timestamp

**Storage:** Data is stored in `measure_logs`.  
**Retention:** Logs are stored for 30 days and then automatically deleted.

## Cross-Endpoint Linking
Records from `/measure` can be matched to `/collect` logs using the salt-hashed IP address.  
This enables user-level telemetry by linking game activity to prior visits.

## Data Storage and Security

- Data storage is handled on a server deployed on the client side.  
- Data in transit is encrypted (TLS).  
- Data at rest is encrypted, with salt-rotation applied to hashes.  
- Access is controlled through strict permissions.

## Data Deletion and Retention

Retention is tiered. The raw request logs and the event data derived from them are kept for different periods:

| Data | Retention |
| :--- | :--- |
| **Raw logs** (`collect_logs`, `measure_logs`) — the granular request-level records described above | **30 days**, then automatically deleted. |
| **Event data** — pseudonymized event rows holding salt-hashed IPs, pseudonymized `user_id`s, and event parameters (storefront, platform, acquisition source) | **18 months by default**, resetting on new activity from the same `user_id`. Configurable to your own retention policy on request. |

Both tiers live in your own BigQuery dataset. A "forget API" is available to delete all records associated with a given `user_id` on request, across both tiers — see [GDPR API](../attribution/gdprapi.md).

!!! warning "Reflect your configured period in your privacy policy"

    The 18-month figure is the default. If you have asked us to change it, state your actual configured period in your privacy policy and records of processing — not the default.

## Technical Notes

- Core attribution uses no browser cookies and no local storage. Cookies are only involved where the optional [postback](../attribution/postbacks/index.md) function is enabled, which depends on the marketing consent captured by your landing page's consent banner — never on an in-game prompt.  
- Only minimal data fields are collected (no persistent device identifiers).  
- IP addresses are never stored in raw form but are salted and hashed before storage.
