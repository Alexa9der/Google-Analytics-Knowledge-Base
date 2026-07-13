---
id: "VIEW-01KXE8NX8MD193YNN78TP5AFWQ"
title: "Google Analytics 4 Flow"
question: "How does GA4 connect collection, identity, reporting, attribution, consent, Measurement Protocol, product links, APIs, and BigQuery export?"
audience: "Analytics architects, data engineers, application developers, analysts, and knowledge agents"
owner: "knowledge-architecture"
status: "published"
entity_ids:
  - "SERVICE-01KXB0H9ZMDHP3XY94QKJ681CN"
  - "SERVICE-01KXB0H9ZMCS60TJAYENWG55H2"
  - "FACT-01KXDD3E3KVGT85EHQ12QXBNXM"
  - "FACT-01KXDD3E3KE3CJTH0QPXGMM5NV"
  - "FACT-01KXDD3E3KZ2DWZNWCXAX30HF4"
  - "FACT-01KXDD3E3KP9RT1RJNWB4FVEJK"
  - "FACT-01KXDD3E3KG3FFQN23R5SB1B0A"
  - "FACT-01KXDE16WS4362G15PJ2DP6EVJ"
  - "FACT-01KXDE16WT7ACAAH53QGXC8QFY"
  - "FACT-01KXDE16WT9ETDFZEDZ4QR6ZE4"
  - "FACT-01KXDE86G09FYYQ7HD451XFNSC"
  - "FACT-01KXDE86G0GX815DGX2F8TJ725"
  - "FACT-01KXDE86G0X8DCEPQ91996FDFP"
  - "FACT-01KXDE86G00CZDYH2231GGR1B6"
  - "FACT-01KXDE86G1P4VCD0MNZ08QGPEK"
  - "FACT-01KXDKQ91S3Z7FG2J44RV07RDB"
  - "FACT-01KXDKQ91SA5R1MWX67HHFRTBX"
  - "FACT-01KXDKQ91SHDBHBTGAW45JNAAV"
  - "FACT-01KXDKQ91S9XBZWSKW3PE1X5N5"
  - "FACT-01KXE3CWP89P5XASVFHVMTWEC5"
  - "FACT-01KXE3CWPA00EZP5DCA9Z2CS4M"
  - "FACT-01KXE3CWPBMXWJEF0W1XPT88HP"
  - "FACT-01KXE3CWPCV1YHWGZYDPJW8XD7"
  - "FACT-01KXE6T4Z4BFKJ0WQEMBAP052B"
  - "FACT-01KXE6T4Z4PWQ9GQMQ1KFR6S8Y"
  - "FACT-01KXE6T4Z4BRDHFDCAG9717W75"
  - "FACT-01KXE6T4Z46A8FV009P7ATS6JW"
  - "FACT-01KXE6T4Z4WQ2NJ0SCX6ESJ4D8"
  - "FACT-01KXE6T4Z4JP0NSJCDPVD38RT3"
reading_order:
  - "SERVICE-01KXB0H9ZMDHP3XY94QKJ681CN"
  - "FACT-01KXDD3E3KVGT85EHQ12QXBNXM"
  - "FACT-01KXDD3E3KZ2DWZNWCXAX30HF4"
  - "FACT-01KXDE16WT7ACAAH53QGXC8QFY"
  - "FACT-01KXDE86G09FYYQ7HD451XFNSC"
  - "FACT-01KXDKQ91S3Z7FG2J44RV07RDB"
  - "FACT-01KXE3CWPA00EZP5DCA9Z2CS4M"
  - "FACT-01KXE6T4Z4BFKJ0WQEMBAP052B"
  - "FACT-01KXE6T4Z4PWQ9GQMQ1KFR6S8Y"
filters:
  service: "Google Analytics 4"
  channels: ["Web and app collection", "Reports", "Explorations", "Data API", "Admin API", "Measurement Protocol", "BigQuery export"]
  snapshot: "2026-07-13"
inclusion_criteria: "Includes confirmed Phase 5 GA4 entities covering property architecture, reporting identity, attribution, consent, retention, Measurement Protocol, product links, reporting-surface differences, and BigQuery export boundaries."
updated_at: "2026-07-13"
---

# End-to-end GA4 route

```text
Website or application
→ web/app Data Stream
→ event-based collection
→ GA4 property processing
→ identity, attribution, consent and modeling rules
→ Reports / Explorations / Data API
→ BigQuery event-level export
```

GA4 is one event-based measurement system for web and app data. Firebase supplies the app-side SDK
and project integration surface; it is not a separate competing analytics model.

# Property and stream architecture

A GA4 property can receive both website and application data. Collection is configured through web,
iOS, and Android Data Streams. Realtime is the first reporting surface used to verify newly arriving
data, while later reports depend on additional processing.

# Identity layer

```text
User-ID
+ device identifiers
+ optional modeling
→ Reporting identity
→ unified and de-duplicated users in report surfaces
```

Blended, Observed, and Device-based reporting identities affect report interpretation. Changing the
selected identity does not rewrite collection or permanently modify the underlying data.

# Reporting layer

Standard Reports monitor recurring questions. Explorations support deeper ad hoc analysis, segments,
filters, and custom techniques. The Data API programmatically accesses report data and follows the
property's reporting identity. The Admin API manages configuration rather than report results.

# Attribution and key events

Attribution assigns key-event credit to eligible touchpoints. GA4 attribution settings control the
reporting model, eligible channels, and lookback window. Report-layer attribution and key-event
modeling are not equivalent to raw event rows in BigQuery.

# Consent, thresholding, and retention

Consent mode changes tag behavior based on consent state and can produce cookieless pings for eligible
modeling. Privacy thresholds can withhold low-volume report output. Retention affects user- and
event-level analysis such as Explorations but does not remove standard aggregated reports on the same
schedule.

# Measurement Protocol boundary

```text
trusted server or offline system
→ HTTPS POST + API secret
→ client_id or app_instance_id
→ optional session and engagement context
→ GA4 collection endpoint
```

Measurement Protocol supplements client-side tagging and Firebase SDK collection. It is not a full
replacement. Session and engagement parameters are required when server-side events must contribute
correctly to session, engagement, and Realtime metrics.

# Product-link boundaries

- Firebase links app streams and audiences to one GA4 property.
- Google Ads exchanges campaign data, audiences, and key events with GA4.
- Search Console adds organic-search reports for one linked web stream.
- BigQuery receives selected stream and event data through daily or streaming export.

Each link has independent permissions, delays, cardinality, retention, and unlinking behavior.

# Why surfaces disagree

```text
Reports / Explorations / Data API
→ reporting identity
→ aggregation
→ attribution and modeling
→ thresholding
→ possible sampling
→ possible (other) row

BigQuery
→ granular event and user rows
→ no report-layer modeling
→ no report-layer data-driven attribution result
→ no sampling
→ no (other) row
```

Recent-period results can also change during intraday and daily processing. BigQuery daily tables can
receive late events for up to three days after the event date.

# Canonical interpretation rule

Use Reports for standard monitoring, Explorations for analyst-driven investigation, the Data API for
programmatic report retrieval, and BigQuery for event-grain reconstruction. None should be treated as
universally interchangeable without matching identity, attribution, date, filtering, freshness, and
modeling assumptions.
