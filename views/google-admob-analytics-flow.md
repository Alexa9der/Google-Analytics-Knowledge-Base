---
id: "VIEW-01KXBVE319E7Z5PN1HBKNDMFDZ"
title: "Google AdMob Analytics Flow"
question: "How does AdMob reporting move from ad requests through impressions and clicks to estimated earnings, and where do Firebase analytics and payment boundaries begin?"
audience: "Analytics architects, application developers, and knowledge agents"
owner: "knowledge-architecture"
status: "published"
entity_ids:
  - "SERVICE-01KXB0H9ZMWZPRWF59R76WVCJN"
  - "SERVICE-01KXB0H9ZMDHP3XY94QKJ681CN"
  - "FACT-01KXBTRX58RYJJ878ADHRPMQ55"
  - "FACT-01KXBTRX58R1QRSEC9Q447AKS6"
  - "FACT-01KXBTRX58FNXF8BXFA963MW2G"
  - "FACT-01KXBTRX58N24R1RDGH5SEMF37"
  - "FACT-01KXBTRX58FM09B964PV2HTNNK"
  - "FACT-01KXBTRX58ZAJ8CHMW3KPVM8KF"
  - "FACT-01KXBTRX593NQD36RS3GAWHB4W"
  - "FACT-01KXBTRX5996C3ATVK1DFCB6D2"
  - "FACT-01KXBTRX597D2V9THGMSSZFV0X"
  - "FACT-01KXBVE318EKJ7RMCMAMM653K2"
  - "FACT-01KXBVE319Y123F05C3EVEV3X8"
  - "FACT-01KXBVE319D0BP3NE3NQRG4X8W"
  - "FACT-01KXBVE319XKR911APSDS8BGJB"
  - "FACT-01KXBVE319HVDK3EM6ZVQJW2EE"
reading_order:
  - "SERVICE-01KXB0H9ZMWZPRWF59R76WVCJN"
  - "FACT-01KXBTRX58RYJJ878ADHRPMQ55"
  - "FACT-01KXBTRX58R1QRSEC9Q447AKS6"
  - "FACT-01KXBTRX58N24R1RDGH5SEMF37"
  - "FACT-01KXBTRX58FM09B964PV2HTNNK"
  - "FACT-01KXBTRX593NQD36RS3GAWHB4W"
  - "FACT-01KXBVE319HVDK3EM6ZVQJW2EE"
filters:
  service: "Google AdMob"
  channels: ["UI", "API", "SDK", "CSV"]
  snapshot: "2026-07-12"
inclusion_criteria: "Includes confirmed AdMob reporting, API, SDK revenue, Firebase integration, retention, and payment-boundary entities from Phase 3."
updated_at: "2026-07-12"
---

# Core delivery and monetization route

```text
Ad unit in application
→ ad request
→ matched request
→ impression
→ optional ad click
→ estimated earnings
→ later adjustment and finalized-payment boundary
```

The canonical records distinguish each count and formula. A matched request does not guarantee an
impression, and an impression does not require a click. Estimated earnings remain a reporting value
that can be adjusted before payment.

# Reporting routes

## Network report

The network report covers AdMob performance. Without dimensions, its grain is the whole account.
Dimensions can refine the report by time, app, ad unit, format, country, or platform. Oversized API
reports are truncated at the documented row limit.

## Mediation report

The mediation report adds third-party ad-source performance. Its scope must not be treated as
identical to the network report.

# Revenue routes

```text
Aggregated reporting:
impressions → estimated earnings → eCPM / impression RPM

SDK route:
individual impression → paid-event callback → revenue value + precision
```

The SDK route has impression grain and can forward impression-level revenue to the linked Firebase
analytics layer. It is not the same dataset or financial state as a finalized payment.

# Firebase boundary

Linking the AdMob app to Firebase and integrating Google Analytics for Firebase enables user metrics
such as sessions and active users. Those analytics-derived metrics are separate from AdMob delivery
counts such as requests and impressions.

# Export and retention

AdMob supports CSV export and API-generated reports within applicable retention windows. User
Activity has a shorter retention period than Ads Activity.

# Open transitions

The following transitions remain for later service phases:

```text
Firebase user/session metrics → GA4 event and attribution model
AdMob estimated earnings → finalized earnings → payment
AdMob/Firebase revenue data → BigQuery and unified LTV model
```
