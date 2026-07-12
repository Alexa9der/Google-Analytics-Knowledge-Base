---
id: "VIEW-01KXCN00000000000000000001"
title: "Google Search Console Analytics Flow"
question: "How does Google Search performance move from an impression through a click to the website boundary, and through which reporting channels can it be analyzed?"
audience: "Analytics researchers, data architects, and AI agents"
owner: "knowledge-architecture"
status: "published"
entity_ids:
  - "CONCEPT-01KXCN00000000000000000001"
  - "CONCEPT-01KXCN00000000000000000002"
  - "CONCEPT-01KXCN00000000000000000003"
  - "CONCEPT-01KXCN00000000000000000005"
  - "CONCEPT-01KXCN00000000000000000006"
  - "CONCEPT-01KXCN00000000000000000007"
  - "CONCEPT-01KXCN00000000000000000009"
  - "FACT-01KXCN00000000000000000001"
  - "FACT-01KXCN00000000000000000002"
  - "FACT-01KXCN00000000000000000003"
  - "FACT-01KXCN00000000000000000004"
  - "FACT-01KXCN00000000000000000007"
  - "FACT-01KXCN00000000000000000010"
  - "FACT-01KXCN00000000000000000011"
  - "FACT-01KXCN00000000000000000012"
  - "FACT-01KXCN00000000000000000013"
  - "FACT-01KXCN00000000000000000021"
  - "FACT-01KXCN00000000000000000024"
  - "FACT-01KXCN00000000000000000037"
  - "FACT-01KXCN00000000000000000040"
  - "FACT-01KXCN00000000000000000046"
  - "FACT-01KXCN00000000000000000047"
  - "FACT-01KXCN00000000000000000053"
  - "FACT-01KXCN00000000000000000055"
  - "FACT-01KXCN00000000000000000056"
reading_order:
  - "CONCEPT-01KXCN00000000000000000003"
  - "CONCEPT-01KXCN00000000000000000007"
  - "CONCEPT-01KXCN00000000000000000006"
  - "CONCEPT-01KXCN00000000000000000001"
  - "FACT-01KXCN00000000000000000001"
  - "CONCEPT-01KXCN00000000000000000002"
  - "FACT-01KXCN00000000000000000002"
  - "CONCEPT-01KXCN00000000000000000005"
  - "FACT-01KXCN00000000000000000003"
  - "FACT-01KXCN00000000000000000004"
  - "FACT-01KXCN00000000000000000007"
  - "FACT-01KXCN00000000000000000010"
  - "FACT-01KXCN00000000000000000011"
  - "FACT-01KXCN00000000000000000012"
  - "FACT-01KXCN00000000000000000013"
  - "CONCEPT-01KXCN00000000000000000009"
  - "FACT-01KXCN00000000000000000021"
  - "FACT-01KXCN00000000000000000024"
  - "FACT-01KXCN00000000000000000037"
  - "FACT-01KXCN00000000000000000040"
  - "FACT-01KXCN00000000000000000055"
  - "FACT-01KXCN00000000000000000056"
  - "FACT-01KXCN00000000000000000046"
  - "FACT-01KXCN00000000000000000047"
  - "FACT-01KXCN00000000000000000053"
filters: {service_id: "SERVICE-01KXB0H9ZMVPFDX90GE5ZQZWQQ", statuses: ["confirmed"]}
inclusion_criteria: "Include reviewed Search Performance metrics, dimensions, privacy rules, API, direct export, BigQuery bulk export, Looker Studio, and website-boundary entities only."
updated_at: "2026-07-12"
---

# Primary flow

Google Search → query/search type/search appearance → search impression → search click → landing page
→ website boundary → future GA4 web analytics.

# Reporting channels

- UI: four primary metrics, dimensions, filters, comparisons, preliminary data, and 16-month history.
- API: grouped aggregate rows, filters, freshness states, offset pagination, top-row and quota limits.
- Export: the filtered UI report to Sheets, Excel, or CSV, with a 1,000-row table limit.
- Bulk Export: daily property- and URL-grain tables in BigQuery, excluding anonymized queries.
- Looker Studio: official Site Impression or URL Impression connector data sources.

# Measurement boundary

An impression is not a visit. A click is not a session, user, or conversion. Country is search
origin rather than exact user location, and device is a category rather than a physical-device ID.
GA4 begins after the website boundary and can associate landing-page behavior through its official
link, but Search Console remains aggregated search-performance measurement.
