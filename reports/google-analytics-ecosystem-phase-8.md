---
id: "REPORT-01KXFVY52FFTSF0VDBQGEJY5D6"
title: "Google Analytics Ecosystem Phase 8"
research_question: "How should the seven researched Google analytics services be connected into an end-to-end measurement architecture while preserving identity, attribution, freshness, retention, privacy and reconciliation boundaries?"
created_at: "2026-07-14"
as_of: "2026-07-14"
author: "google-analytics-knowledge-project"
status: "issued"
fact_ids: []
evidence_ids: []
concept_ids:
  - "CONCEPT-01KXB0H9ZM80395EP8SM7W6T0Z"
  - "CONCEPT-01KXB0H9ZMBPTYGA7SHR0K94VE"
  - "CONCEPT-01KXB0H9ZMYRQ1M9SS0TJR22Z6"
  - "CONCEPT-01KXB0H9ZMY0Z31MBFPCDF5Y3Q"
  - "CONCEPT-01KXB0H9ZMXAWK23YMRYR5Q133"
  - "CONCEPT-01KXB0H9ZMX4S975N077EGM94N"
  - "CONCEPT-01KXB0H9ZM8Q0EGP8QRMF2CAD7"
  - "CONCEPT-01KXB0H9ZMPHJCZMXVQTC5AMX0"
  - "CONCEPT-01KXB0H9ZMH409C8HS5KKTPH98"
  - "CONCEPT-01KXB0H9ZMQ30G90BCGR86CB87"
  - "CONCEPT-01KXB0H9ZMXPT1ZMXS689KRCTK"
  - "CONCEPT-01KXB0H9ZMBYM231E33WXJADZ4"
  - "CONCEPT-01KXB0H9ZMG7GCKKQ7WE2SHH6Z"
service_ids: []
method: "Cross-service synthesis of the validated Google Play Console, Search Console, AdMob, Firebase, GA4, BigQuery and Looker Studio Views and their confirmed official-source Facts, with explicit separation of identity, attribution, time, privacy, financial and reporting boundaries."
limitations: "No live Google account, user data, production redirect, advertising campaign, API, warehouse or dashboard was used. Cross-service joins remain architecture contracts rather than proof of deterministic person-level continuity."
---

# Summary

Phase 8 combines the seven completed service phases into one measurement architecture without treating the ecosystem as a single ledger. The valid operating model is a sequence of related systems whose metrics differ in grain, eligible population, identity, attribution, processing, retention, privacy treatment and financial meaning.

# End-to-end architecture

```text
search or campaign exposure
→ source click
→ website or governed redirect
→ Google Play store listing
→ store acquisition
→ application launch and first_open
→ app engagement
→ purchase, subscription or advertising-revenue event
→ GA4 reporting and attribution
→ BigQuery export and governed SQL models
→ Looker Studio reporting and delivery
```

Each arrow is a measurement boundary. It may represent a supported product integration, a URL transition, an event collection boundary, an export, or an aggregate reconciliation step. It must not be interpreted automatically as a deterministic user-level join.

# Identity gaps

There is no universal identifier shared by Search Console rows, website sessions, Play Console acquisition metrics, Firebase or GA4 app events, Play financial records, AdMob earnings, BigQuery models and Looker Studio reports. Identity must therefore be limited to identifiers documented for a specific surface and purpose.

Permitted joins include campaign parameters, click identifiers where officially supported, landing URLs, transaction or order identifiers, subscription identifiers, and aggregate bridge dimensions. Pseudonymous analytics identifiers may be used only within their consent, retention and product-policy boundaries. Synthetic cross-service person IDs are prohibited.

# Attribution gaps

Search attribution, website acquisition, store-listing attribution, GA4 attribution and advertising-revenue attribution are separate models. They can differ by eligible event, lookback window, channel rules, processing time and privacy modeling. A common label such as source, campaign, conversion or revenue does not make two metrics equivalent.

Every published funnel or ROI metric must name its attribution model, lookback window, source system and eligible population. Where adjacent systems cannot be joined deterministically, the output must be described as aggregate reconciliation or directional analysis rather than user-level attribution.

# Freshness and retention

Reporting interfaces, APIs, exports and financial reports can update on different schedules and can restate history differently. Warehouse models must preserve event time, ingestion time and processing date separately. Late-arriving events, refunds, subscription state changes and revised earnings require explicit restatement rules.

Retention must be documented independently for source interfaces, APIs, GA4 event data, BigQuery tables and reporting extracts. A dashboard cannot be treated as the historical system of record unless the underlying governed dataset provides that history.

# Revenue reconciliation

Purchase events, subscription events, Play financial proceeds and AdMob estimated earnings represent different revenue scopes. Reconciliation must define currency conversion, taxes, platform fees, refunds, chargebacks, settlement periods and accounting status.

Recommended marts keep at least three separate measures:

1. behavioral purchase or subscription events;
2. platform financial proceeds and adjustments;
3. advertising earnings.

A total-business-revenue metric may combine them only after scope, currency and period contracts are aligned.

# `/fb` short-link architecture

A short link such as `/fb` should be implemented as a governed first-party redirect rather than an undocumented alias.

```text
visitor requests /fb
→ server or edge endpoint records a minimal redirect event
→ endpoint validates the fixed destination and campaign contract
→ HTTP 302 or 307 redirect to the destination
→ downstream website or store measurement continues independently
```

The redirect record should contain only the minimum operational fields: timestamp, redirect key, approved campaign parameters, destination version, response status and a privacy-safe request classification. Raw personal identifiers should not be introduced merely to bridge systems.

The endpoint must use an allowlisted destination, prevent open redirects, preserve approved campaign parameters, document caching behavior and provide a fallback destination. Client-side analytics alone is insufficient because navigation may occur before the measurement request completes. Server- or edge-side logging is therefore the preferred reliability boundary.

# Metric contract

Every cross-service metric must define:

1. source service and reporting surface;
2. grain and eligible population;
3. identifier and join method;
4. attribution model and lookback window;
5. event, ingestion and processing time;
6. freshness and retention;
7. privacy, consent, thresholding and modeling behavior;
8. currency, tax, fee, refund and revenue scope;
9. deduplication and late-arrival policy;
10. reconciliation target and accepted tolerance.

# Governance conclusion

The canonical source of a metric is its governed definition and source dataset, not its dashboard label. BigQuery should contain explicit transformation and reconciliation contracts; Looker Studio should expose those governed outputs without redefining business logic in isolated charts or blends.

Phase 8 therefore closes the service-research roadmap with an integration map, a marketing-attribution funnel and a cross-service operating contract. The resulting architecture supports analysis across the ecosystem while preserving the differences required for technically and financially defensible conclusions.
