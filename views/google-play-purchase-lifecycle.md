---
id: "VIEW-01KXBBGJPAWTR7P0PQXJ4ANCH3"
title: "Google Play purchase lifecycle route"
question: "How should purchase and subscription lifecycle knowledge be traversed without mixing operational, entitlement, or financial state?"
audience: "Billing analysts, researchers, and AI agents"
owner: "knowledge-architecture"
status: "published"
entity_ids:
  - "CONCEPT-01KXB0H9ZM8Q0EGP8QRMF2CAD7"
  - "CONCEPT-01KXB0H9ZM40HGECRYWM7VSPCM"
  - "CONCEPT-01KXB0H9ZMPHJCZMXVQTC5AMX0"
  - "FACT-01KXBBGJPAWH99D3MFXFEV1R11"
  - "FACT-01KXBBGJPAH29Z4BSQXPAHMR8Y"
  - "FACT-01KXBBGJPAENY40QDGQNYKV1X5"
  - "FACT-01KXBBGJPA1NA5GSVCHW6F2Y8N"
  - "FACT-01KXBBGJPAZCCHW8NPA1FW2A0S"
  - "FACT-01KXBBGJPAHHX285NTW7WS0FQ1"
  - "FACT-01KXBBGJPAC6FWS3MGSJZBG5QR"
  - "FACT-01KXBBGJPAPWS38GPGJ75YQFW5"
  - "FACT-01KXBBGJPAXK2MJY4NGK5914CJ"
  - "FACT-01KXBBGJPAQNK0NGYS5BPA1J9G"
reading_order:
  - "CONCEPT-01KXB0H9ZM8Q0EGP8QRMF2CAD7"
  - "FACT-01KXBBGJPAWH99D3MFXFEV1R11"
  - "FACT-01KXBBGJPAH29Z4BSQXPAHMR8Y"
  - "FACT-01KXBBGJPAENY40QDGQNYKV1X5"
  - "FACT-01KXBBGJPA1NA5GSVCHW6F2Y8N"
  - "FACT-01KXBBGJPAZCCHW8NPA1FW2A0S"
  - "FACT-01KXBBGJPAHHX285NTW7WS0FQ1"
  - "CONCEPT-01KXB0H9ZM40HGECRYWM7VSPCM"
  - "FACT-01KXBBGJPAC6FWS3MGSJZBG5QR"
  - "FACT-01KXBBGJPAPWS38GPGJ75YQFW5"
  - "FACT-01KXBBGJPAXK2MJY4NGK5914CJ"
  - "FACT-01KXBBGJPAQNK0NGYS5BPA1J9G"
  - "CONCEPT-01KXB0H9ZMPHJCZMXVQTC5AMX0"
filters: {service_id: "SERVICE-01KXB0H9ZM3Z8V674FKJP8T657", statuses: ["confirmed"]}
inclusion_criteria: "Include only reviewed Google Play purchase lifecycle entities; Firebase and GA4 purchase events remain future transitions."
updated_at: "2026-07-12"
---

# Routes

Product → Purchase → Purchase state → Acknowledgment / Consumption → Refund / Revoke / Voided
purchase → Entitlement → Revenue boundary.

Subscription → Active → Renewal / Cancellation → Grace period / Account hold / Pause → Expiry /
Revoke → Entitlement → Revenue boundary.

This View contains IDs and navigation only. Financial accounting remains Phase 1.4 scope.
