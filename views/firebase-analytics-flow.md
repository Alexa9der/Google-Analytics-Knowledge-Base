---
id: "VIEW-01KXBYPZME2MXYTQE136YGYTA0"
title: "Firebase Analytics Flow"
question: "How does Firebase Analytics connect app launch, sessions, behavior, key events, purchases, AdMob revenue, attribution, and BigQuery export?"
audience: "Analytics architects, application developers, and knowledge agents"
owner: "knowledge-architecture"
status: "published"
entity_ids:
  - "SERVICE-01KXB0H9ZMDHP3XY94QKJ681CN"
  - "SERVICE-01KXB0H9ZM3Z8V674FKJP8T657"
  - "SERVICE-01KXB0H9ZMWZPRWF59R76WVCJN"
  - "SERVICE-01KXB0H9ZMFN9JW1GNN614Q1BJ"
  - "FACT-01KXBYPZMESACJQD3TSFMPZBM9"
  - "FACT-01KXBYPZMER68M1VYXZF4T7D0D"
  - "FACT-01KXBYPZMET0F2D5Z4Y8H0Q5HS"
  - "FACT-01KXBYPZMEX2VAS02DC7FCTD28"
  - "FACT-01KXBZYE665N5XWCRWHA9VY7FY"
  - "FACT-01KXBZYE66AWZAMQ7FBYHA3HMV"
  - "FACT-01KXBZYE66JVQWR43HQ6VX5H9C"
  - "FACT-01KXBZYE66VCX1W7JY6XR72HK8"
  - "FACT-01KXBZYE67Q8GBVX6Q3PC2CPFS"
  - "FACT-01KXBZYE67D5GB8GM5YSAN599C"
  - "FACT-01KXBZYE6779Z72AW1R8BZGE70"
  - "FACT-01KXBZYE67K0Z8XSXSAHV2E06R"
  - "FACT-01KXBZYE67AWR53FQYX68QQSMG"
  - "FACT-01KXBZYE686Q8D8K4667WKBX6X"
  - "FACT-01KXBZYE68R3Q9W348MBVRBK1K"
  - "FACT-01KXBZYE68M91M8A396JAJSZPY"
  - "FACT-01KXBZYE69B8P6TQ2W3X4Y5Z6A"
  - "FACT-01KXBZYE69D0R8W4Y5Z6A7B8C9"
  - "FACT-01KXC0J7P9B2Q5S9V3W6X1Y4Z7"
  - "FACT-01KXC0J7P9F6V9X3Z7A0B5C8D1"
  - "FACT-01KXC0J7P9K0Z3B7D1E4F9G2H5"
  - "FACT-01KXC0J7P9N2B5D9F3G6H1J4K7"
  - "FACT-01KXC0J7P9Q4D7F1H5J8K3M6N9"
  - "FACT-01KXBVE318EKJ7RMCMAMM653K2"
  - "FACT-01KXBVE319D0BP3NE3NQRG4X8W"
  - "FACT-01KXBVE319HVDK3EM6ZVQJW2EE"
  - "FACT-01KXC04A4V7BH3JBE7XMWDJNVD"
  - "FACT-01KXC04A4X1REKJW4TEE63JPT9"
reading_order:
  - "SERVICE-01KXB0H9ZMDHP3XY94QKJ681CN"
  - "FACT-01KXBZYE665N5XWCRWHA9VY7FY"
  - "FACT-01KXBZYE66JVQWR43HQ6VX5H9C"
  - "FACT-01KXBZYE67Q8GBVX6Q3PC2CPFS"
  - "FACT-01KXBZYE67D5GB8GM5YSAN599C"
  - "FACT-01KXC0J7P9B2Q5S9V3W6X1Y4Z7"
  - "FACT-01KXBZYE6779Z72AW1R8BZGE70"
  - "FACT-01KXBVE319D0BP3NE3NQRG4X8W"
  - "FACT-01KXC04A4X1REKJW4TEE63JPT9"
filters:
  service: "Firebase"
  channels: ["SDK", "Firebase console", "Google Analytics reporting", "BigQuery export"]
  snapshot: "2026-07-12"
inclusion_criteria: "Includes confirmed Phase 4 Firebase Analytics entities and previously confirmed Google Play and AdMob integration boundaries needed for the app measurement route."
updated_at: "2026-07-12"
---

# End-to-end app analytics route

```text
Google Play install observation
→ first app launch
→ first_open
→ session_start
→ user_engagement and screen_view
→ automatic, recommended, or custom events
→ key events
→ purchase and subscription events
→ user-, session-, and event-scoped attribution
→ BigQuery event-level export
```

An app download does not itself trigger `first_open`. This preserves the boundary between Google Play
install-related observations and analytics events generated after the application is launched.

# Collection model

The Analytics SDK collects some events and user properties automatically and permits custom events.
Events are occurrences in the application, not users or sessions. Event names are case-sensitive,
and logged custom parameters require custom-dimension or custom-metric registration before they are
visible in standard reports.

# Session and engagement model

`session_start` begins the Analytics session model and generates `ga_session_id` and
`ga_session_number`. `user_engagement` measures foreground or focused engagement of at least one
second. `screen_view` follows screen-transition rules. These events describe different grains and
must not be treated as interchangeable counts.

# Identity model

```text
optional user_id
≠ automatically generated user_pseudo_id
≠ authenticated personal identity
```

`user_id` applies prospectively. `user_pseudo_id` is the app-on-device identifier exported with
events to BigQuery. Directly identifying information is prohibited in `user_id`.

# Key events and attribution

Any collected event can be marked as a key event. `first_open` and `in_app_purchase` are default app
key events in applicable streams. Attribution assigns credit for key events across touchpoints, while
source, medium, and campaign have separate user, session, and event scopes.

# Purchase boundary

Android automatic in-app purchase data requires a Google Play link. Analytics purchase revenue can
differ from Google Play Console values, and overlapping automatic and manual purchase collection can
create duplicates.

# AdMob boundary

```text
AdMob delivery counts
→ AdMob impression
→ impression-level revenue callback
→ Google Analytics for Firebase
```

Firebase linkage and SDK integration enable AdMob user metrics and allow impression-level revenue to
flow into the Analytics event model. That revenue is not equivalent to finalized AdMob earnings or
payment.

# Consent and collection boundary

Analytics collection can be disabled and re-enabled at runtime, with the setting persisting across
app executions. Measurement collection and ad-personalization eligibility are separate controls.

# BigQuery boundary

The export stores event-grain data and can include custom parameters, `user_id`, and
`user_pseudo_id`. Initial propagation can take up to 48 hours, followed by daily synchronization.
Unlinking stops future population but does not delete data already exported.

# Firebase and GA4 boundary

Google Analytics is the measurement system surfaced inside Firebase. Phase 4 establishes app-side
collection and Firebase integration behavior. The next GA4 phase will research the broader property,
data-stream, reporting, API, cross-platform, retention, thresholding, and attribution configuration
model without treating Firebase Analytics as a separate competing event system.
