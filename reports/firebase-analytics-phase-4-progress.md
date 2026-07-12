---
id: "REPORT-01KXC0F4V2T6G2Z7C9E1F3H5R6"
title: "Firebase Analytics Phase 4 Research Progress"
research_question: "How does Firebase Analytics collect, model, report, segment, and export application analytics data?"
created_at: "2026-07-12"
as_of: "2026-07-12"
author: "google-analytics-knowledge-project"
status: "draft"
fact_ids:
  - "FACT-01KXC0F4V1C2S8K3N5Q7R9T1A2"
  - "FACT-01KXC0F4V1D3T9L4P6R8S0U2B3"
  - "FACT-01KXC0F4V1E4U0M5Q7S9T1V3C4"
  - "FACT-01KXC0F4V1F5V1N6R8T0U2W4D5"
  - "FACT-01KXC0F4V1G6W2P7S9U1V3X5E6"
  - "FACT-01KXC0F4V1H7X3Q8T0V2W4Y6F7"
  - "FACT-01KXC0F4V1J8Y4R9U1W3X5Z7G8"
  - "FACT-01KXC0F4V1K9Z5S0V2X4Y6A8H9"
  - "FACT-01KXC0F4V1M0A6T1W3Y5Z7B9J0"
  - "FACT-01KXC0F4V1N1B7U2X4Z6A8C0K1"
  - "FACT-01KXC0F4V1P2C8V3Y5A7B9D1M2"
  - "FACT-01KXC0F4V1Q3D9W4Z6B8C0E2N3"
  - "FACT-01KXC0F4V1R4E0X5A7C9D1F3P4"
  - "FACT-01KXC0F4V1S5F1Y6B8D0E2G4Q5"
evidence_ids:
  - "EVID-01KXC0F4V0C2S8K3N5Q7R9T1A2"
  - "EVID-01KXC0F4V0D3T9L4P6R8S0U2B3"
  - "EVID-01KXC0F4V0E4U0M5Q7S9T1V3C4"
  - "EVID-01KXC0F4V0F5V1N6R8T0U2W4D5"
  - "EVID-01KXC0F4V0G6W2P7S9U1V3X5E6"
  - "EVID-01KXC0F4V0H7X3Q8T0V2W4Y6F7"
  - "EVID-01KXC0F4V0J8Y4R9U1W3X5Z7G8"
  - "EVID-01KXC0F4V0K9Z5S0V2X4Y6A8H9"
  - "EVID-01KXC0F4V0M0A6T1W3Y5Z7B9J0"
concept_ids: []
service_ids:
  - "SERVICE-01KXB0H9ZMDHP3XY94QKJ681CN"
  - "SERVICE-01KXB0H9ZMFN9JW1GNN614Q1BJ"
method: "Official Firebase documentation review, granular Evidence capture, atomic Fact extraction, and boundary separation between SDK collection, console reporting, audiences, and BigQuery export."
limitations: "This is an in-progress report. first_open, session_start, user ID, user properties, attribution, key events, retention, consent, DebugView, Crashlytics, Performance Monitoring, Remote Config, A/B Testing, AdMob, Google Play, and complete BigQuery schema research remain incomplete."
---

# Current progress

Phase 4 has started. The first research block establishes the Firebase Analytics measurement role,
event model, automatically collected and custom data, audience inputs, console reporting cadence,
and the initial BigQuery integration boundary.

# Confirmed distinctions

- Firebase Analytics event ≠ user.
- Automatically collected event ≠ custom event.
- Event type count ≠ total event volume.
- Logged custom parameter ≠ report-visible custom dimension or metric.
- Console event reporting ≠ raw BigQuery export.
- Analytics audience ≠ authenticated user list.

# Current coverage

Covered in the first block:

- Analytics measurement role;
- 500 distinct event-type limit;
- automatic event and user-property collection;
- custom events;
- event naming case sensitivity;
- audience source attributes;
- custom-parameter registration boundary;
- custom parameters in BigQuery export;
- aggregated Events dashboard and periodic refresh.

# Next research blocks

1. Automatically collected events, especially `first_open` and `session_start`.
2. User properties, user ID, app-instance identifiers, and identity boundaries.
3. Sessions, screens, engagement, conversions/key events, and attribution.
4. Data collection controls, consent, retention, thresholding, and privacy.
5. BigQuery daily and streaming export schemas, timing, limits, and billing prerequisites.
6. Crashlytics, Performance Monitoring, Remote Config, A/B Testing, FCM, AdMob, and Google Play integrations.
7. Final Firebase analytics flow View, consolidation Report, STATE, INDEX, tests, and CI.
