---
id: "VIEW-01KXBYPZME2MXYTQE136YGYTA0"
title: "Firebase Analytics Flow"
question: "How does Firebase Analytics move from SDK-collected app activity to aggregated reporting, audiences, and BigQuery export?"
audience: "Analytics architects, application developers, and knowledge agents"
owner: "knowledge-architecture"
status: "draft"
entity_ids:
  - "SERVICE-01KXB0H9ZMDHP3XY94QKJ681CN"
  - "SERVICE-01KXB0H9ZMFN9JW1GNN614Q1BJ"
  - "FACT-01KXBYPZMEVR8ZNV789KPTASPP"
  - "FACT-01KXBYPZMEY844K6S8558Z7AAC"
  - "FACT-01KXBYPZMER68M1VYXZF4T7D0D"
  - "FACT-01KXBYPZMESACJQD3TSFMPZBM9"
  - "FACT-01KXBYPZMET0F2D5Z4Y8H0Q5HS"
  - "FACT-01KXBYPZME1JEPWV14B0NTYJHK"
  - "FACT-01KXBYPZMEX2VAS02DC7FCTD28"
  - "FACT-01KXBYPZME8GJ96CN78FVX932Q"
  - "FACT-01KXBYPZME3K5ZPW1T4RFVCW56"
reading_order:
  - "SERVICE-01KXB0H9ZMDHP3XY94QKJ681CN"
  - "FACT-01KXBYPZMESACJQD3TSFMPZBM9"
  - "FACT-01KXBYPZMEY844K6S8558Z7AAC"
  - "FACT-01KXBYPZMER68M1VYXZF4T7D0D"
  - "FACT-01KXBYPZME3K5ZPW1T4RFVCW56"
  - "FACT-01KXBYPZME8GJ96CN78FVX932Q"
filters:
  service: "Firebase"
  channels: ["SDK", "Firebase console", "BigQuery export"]
  snapshot: "2026-07-12"
inclusion_criteria: "Includes confirmed Firebase Analytics event, audience, reporting, and BigQuery boundary entities from the active Phase 4 research."
updated_at: "2026-07-12"
---

# Initial route

```text
Application activity
→ automatically collected or custom event
→ event parameters and user properties
→ aggregated Firebase Analytics reporting
→ audience definitions
→ BigQuery export boundary
```

# Collection boundary

The Analytics SDK automatically collects some events and user properties. Applications may also log
custom events. Event names are case-sensitive, so naming discipline affects the event taxonomy.

# Reporting boundary

The Firebase Events dashboard presents aggregated statistics and updates periodically. A logged
custom parameter does not automatically become report-visible; it must be registered as a custom
dimension or metric.

# Audience boundary

Audience definitions may use device data, custom events, and user properties. Audiences are derived
segments, not direct evidence of an authenticated person or a portable cross-service identity.

# Export boundary

When linked, Analytics data and custom event parameters can be exported to BigQuery for custom
analysis and joins with other sources. Detailed schema, timing, identity fields, retention, and
billing prerequisites remain under investigation.

# Open transitions

```text
Google Play install observation → first_open
first_open → session_start → engaged app activity
app event → key event / conversion
AdMob impression revenue → Firebase event model
Firebase Analytics export → GA4 and BigQuery identity model
```
