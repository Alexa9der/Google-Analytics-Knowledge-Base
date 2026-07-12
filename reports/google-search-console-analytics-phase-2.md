---
id: "REPORT-01KXCN00000000000000000001"
title: "Google Search Console Analytics Phase 2"
research_question: "Which Search Performance metrics, dimensions, filters, API capabilities, exports, privacy boundaries, and cross-service paths are officially documented?"
created_at: "2026-07-12"
as_of: "2026-07-12"
author: "google-analytics-knowledge-project"
status: "issued"
fact_ids:
  - "FACT-01KXCN00000000000000000001"
  - "FACT-01KXCN00000000000000000002"
  - "FACT-01KXCN00000000000000000003"
  - "FACT-01KXCN00000000000000000004"
  - "FACT-01KXCN00000000000000000007"
  - "FACT-01KXCN00000000000000000015"
  - "FACT-01KXCN00000000000000000021"
  - "FACT-01KXCN00000000000000000024"
  - "FACT-01KXCN00000000000000000031"
  - "FACT-01KXCN00000000000000000037"
  - "FACT-01KXCN00000000000000000040"
  - "FACT-01KXCN00000000000000000046"
  - "FACT-01KXCN00000000000000000047"
  - "FACT-01KXCN00000000000000000053"
  - "FACT-01KXCN00000000000000000055"
  - "FACT-01KXCN00000000000000000056"
evidence_ids:
  - "EVID-01KXCN00000000000000000001"
  - "EVID-01KXCN00000000000000000002"
  - "EVID-01KXCN00000000000000000003"
  - "EVID-01KXCN00000000000000000004"
  - "EVID-01KXCN00000000000000000005"
  - "EVID-01KXCN00000000000000000006"
  - "EVID-01KXCN00000000000000000007"
  - "EVID-01KXCN00000000000000000008"
  - "EVID-01KXCN00000000000000000009"
  - "EVID-01KXCN00000000000000000010"
  - "EVID-01KXCN00000000000000000011"
  - "EVID-01KXCN00000000000000000012"
  - "EVID-01KXCN00000000000000000013"
  - "EVID-01KXCN00000000000000000014"
  - "EVID-01KXCN00000000000000000015"
  - "EVID-01KXCN00000000000000000016"
concept_ids:
  - "CONCEPT-01KXCN00000000000000000001"
  - "CONCEPT-01KXCN00000000000000000002"
  - "CONCEPT-01KXCN00000000000000000003"
  - "CONCEPT-01KXCN00000000000000000004"
  - "CONCEPT-01KXCN00000000000000000005"
  - "CONCEPT-01KXCN00000000000000000006"
  - "CONCEPT-01KXCN00000000000000000007"
  - "CONCEPT-01KXCN00000000000000000008"
  - "CONCEPT-01KXCN00000000000000000009"
service_ids: ["SERVICE-01KXB0H9ZMVPFDX90GE5ZQZWQQ"]
method: "Official Google source discovery, Evidence-first capture, atomic Fact extraction, channel and grain separation, privacy-boundary review, cross-service confirmation, and repository validation."
limitations: "No live accounts, credentials, API calls, real sites, indexing tools, SEO diagnostics, or non-Google sources were used. Direct Firebase, Google Play, and AdMob integration is not asserted because no official Phase 2 evidence confirmed one."
---

# Summary

Search Console measures aggregated visibility and outbound interactions for property links on Google
Search surfaces. It ends at the search click and landing-page boundary; it does not natively measure
the resulting session, user, or conversion.

# Official Sources

Sixteen granular Evidence records cover Search Console Help, Search Analytics API reference and
limits, Google Analytics Help, Google Search Central, and Looker Studio documentation.

# Evidence

Evidence is separated into performance, dimensions and filters, API, exports, and integrations.
Every confirmed Fact points to at least one official Google source verified on 2026-07-12.

# Facts

Fifty-six atomic Facts distinguish definitions, formulas, channel availability, limits, privacy,
measurement boundaries, and officially supported integrations.

# Metrics

The primary metrics are clicks, impressions, average CTR, and average position. CTR is clicks divided
by impressions. Position averages the property's topmost result per impression. Counting details can
vary by result type.

# Dimensions

The core dimensions are query, page, country, device, search appearance, search type, and date.
Pages generally aggregate to Google's canonical URL; country is search origin; device is a category.

# Filters

Different dimension filters combine with AND. Date and search type remain mandatory. Query and page
regex uses RE2 partial matching by default, and only one comparison can be active at a time.

# API

The query method returns aggregate keys and the four metrics. It supports grouping, filtering,
freshness states, and offset pagination. Requests return at most 25,000 rows; the API exposes top
rows, is capped at 50,000 Performance rows per day/type/property, and has OAuth and quota controls.

# Export

Direct export supports Sheets, Excel, and CSV with at most 1,000 representative table rows. Bulk
export sends daily property- and URL-grain tables to BigQuery, excludes anonymized queries, does not
backfill, and has operational retry limits.

# Privacy

Anonymized query strings are removed from tables and bulk export but can remain in unfiltered chart
totals. Table truncation is separate from privacy omission. The researched schema is aggregate.

# Measurement Boundary

Search impression ≠ visit; search click ≠ session, user, or conversion; query ≠ page; search-origin
country ≠ exact user location; device category ≠ physical device. Search Console and GA4 measure
different sides of the website boundary.

# Cross-Service Readiness

GA4 has an official property/web-stream link and landing-page reporting path. BigQuery receives the
official bulk export and supports URL-grain joins. Looker Studio has an official connector. No direct
Firebase, Google Play, or AdMob path was confirmed, so those joins remain open rather than impossible.

# Coverage

Covered: metric definitions/formulas/grain, dimensions, filters, UI, API, exports, privacy, retention,
measurement boundary, and confirmed GA4, BigQuery, and Looker Studio paths.

# Open Questions

Mutable search-appearance inventories, internal truncation selection, historical correction rules,
exact anonymization thresholds, and official Firebase/Play/AdMob bridges remain open. Direct GCS and
Pub/Sub delivery were not confirmed.

# Quality Review

Claims are atomic and channel-scoped; recommendations were not promoted to Facts. Nine new Concepts
are service-independent, while Search Console-specific behavior remains in Facts.

# Files Changed

Added sixteen Evidence packages, one Fact package, one View, and this Report; extended Concepts; updated
STATE and production counts; regenerated INDEX.jsonl.

# Validation

Knowledge, links, Markdown frontmatter, generated-index consistency, pytest, ruff, and mypy are run
after generation and reported in the final handoff.

# Next Phase

Phase 2 is complete. The next service is Google AdMob; its research has not started.
