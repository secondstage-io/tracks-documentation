---
description: "Handle player data access and deletion requests through the TRACKS GDPR API, provisioned per integration once your setup is live."
---

# GDPR API

<p class="docs-audience">For: Backend engineer / Privacy team</p>

!!! note "Reference only — not yet actionable"

    The GDPR API is provisioned per-integration. Endpoint URLs and credentials are delivered **via a setup email once your overall TRACKS integration is complete and live in production**. Until then, this page is reference information only. See [Data Handling & Security → Right to Forget](../support/datasecurity.md) for the underlying privacy rationale.

For teams with existing data management systems, **TRACKS’ GDPR APIs** can be integrated to centralize and automate your GDPR compliance processes.

Under the GDPR framework, **personal data** includes (but is not limited to):

- Online identifiers
- IP addresses
- User location data
- Behavioral and demographic profiling data

TRACKS handles **user opt-outs** through a dedicated **GDPR Forget API**, which will be provided **via a setup email once your overall TRACKS integration is complete and live in production**.

## Capabilities

The GDPR API offers the following features:

- **Data Removal by `user_id`**
- **Data Request by `user_id`**
- **User opt-out (Forget API)**

The `user_id` parameter is used to identify users across the GDPR API. When passed to the Forget API, it will:

- Permanently delete all associated records
- Block that `user_id` from being recorded in the future

> **Note:** IP addresses will **not** be returned in plain text. They are stored as a **SHA256 hash** and cannot be accessed directly from the API response.
