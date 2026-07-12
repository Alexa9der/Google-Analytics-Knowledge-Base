---
id: "VIEW-01KXC0F4V2U7H3A8D0F2G4J6S7"
title: "Firebase Analytics Flow"
question: "How does Firebase Analytics move from SDK-collected app activity to aggregated reporting, audiences, and BigQuery export?"
audience: "Analytics architects, application developers, and knowledge agents"
owner: "knowledge-architecture"
status: "draft"
entity_ids:
  - "SERVICE-01KXB0H9ZMDHP3XY94QKJ681CN"
  - "SERVICE-01KXB0H9ZMFN9JW1GNN614Q1BJ"
  - "FACT-01KXC0F4V1C2S8K3N5Q7R9T1A2"
  - "FACT-01KXC0F4V1E4U0M5Q7S9T1V3C4"
  - "FACT-01KXC0F4V1G6W2P7S9U1V3X5E6"
  - "FACT-01KXC0F4V1H7X3Q8T0V2W4Y6F7"
  - "FACT-01KXC0F4V1M0A6T1W3Y5Z7B9J0"
  - "FACT-01KXC0F4V1N1B7U2X4Z6A8C0K1"
  - "FACT-01KXC0F4V1P2C8V3Y5A7B9D1M2"
  - "FACT-01KXC0F4V1Q3D9W4Z6B8C0E2N3"
  - "FACT-01KXC0F4V1R4E0X5A7C9D1F3P4"
reading_order:
  - "SERVICE-01KXB0H9ZMDHP3XY94QKJ681CN"
  - "FACT-01KXC0F4V1H7X3Q8T0V2W4Y6F7"
  - "FACT-01KXC0F4V1E4U0M5Q7S9T1V3C4"
  - "FACT-01KXC0F4V1G6W2P7S9U1V3X5E6"
  - "FACT-01KXC0F4V1R4E0X5A7C9D1F3P4"
  - "FACT-01KXC0F4V1Q3D9W4Z6B8C0E2N3"
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
