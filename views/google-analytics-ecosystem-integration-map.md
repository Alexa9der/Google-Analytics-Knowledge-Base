---
id: "VIEW-01KXFRHTMZJH3GFYPJF4JQ21F0"
title: "Google Analytics Ecosystem Integration Map"
question: "How do Google Play Console, Search Console, AdMob, Firebase, GA4, BigQuery, and Looker Studio connect, and where do their measurement and identity boundaries remain separate?"
audience: "Analytics architects, data engineers, product analysts, researchers, and AI agents"
owner: "knowledge-architecture"
status: "published"
entity_ids:
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
reading_order:
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
filters: {statuses: ["confirmed", "reviewed", "proposal"]}
inclusion_criteria: "Include the validated service boundaries and integration paths needed to interpret acquisition, store, app, purchase, advertising-revenue, export, warehouse, and reporting stages without treating them as one universal identity or attribution system."
updated_at: "2026-07-14"
---

# Ecosystem map

```text
Google Search
  → Search Console: impression, click, query, page, country, device, search appearance
  → website boundary
      → GA4 web measurement when implemented

Campaign or owned link
  → website or redirect endpoint
  → Google Play store listing
      → Play Console acquisition and store-performance reporting
      → install boundary
          → Firebase / GA4 app measurement
              → first_open and later app events
              → purchase and subscription events when instrumented
              → AdMob advertising-revenue events when linked and available
                  → GA4 reporting and attribution surfaces
                  → BigQuery event export
                      → governed SQL models and reconciled marts
                          → Looker Studio data sources, reports, controls, and governed delivery
```

# Confirmed integration directions

## Search Console → website → GA4

Search Console measures aggregated Google Search performance up to the landing-page boundary. A search
click is not itself a GA4 session, user, or conversion. GA4 begins only after the website loads and
measurement is implemented. The official product link supports combined analysis, but it does not
convert Search Console query rows into person-level GA4 events or create a universal identifier.

## Google Play Console → Firebase / GA4

Play Console owns store-listing, acquisition, install-related, purchase, subscription, financial,
quality, rating, and review surfaces within its own reporting definitions. Firebase and GA4 own app
measurement after the application starts producing events. Store acquisition, install, and
`first_open` therefore represent different scopes and should not be substituted for one another.

## Firebase → GA4

Firebase provides the app SDK and product integration layer used to collect analytics events and link
other Firebase services. GA4 provides the property, reporting, attribution, audience, API, and export
surfaces for those events. Product linking enables data movement defined by the integration; it does
not imply historical backfill, identical retention, or identical report totals across every surface.

## AdMob → Firebase / GA4

When the products are linked and the required SDK and event collection are present, advertising
revenue can enter the analytics event model. AdMob reporting and GA4 event reporting remain different
processing surfaces with different aggregation, attribution, freshness, and reconciliation rules.
Advertising revenue must remain distinct from purchase revenue and total business revenue.

## GA4 → BigQuery

GA4 exports event rows to a BigQuery dataset. BigQuery receives exported source data, not a guaranteed
replica of every GA4 interface result. Identity, attribution, modeled data, privacy thresholding,
late-arriving events, currency handling, deduplication, and session reconstruction require explicit
warehouse contracts.

## BigQuery and Google connectors → Looker Studio

Looker Studio connects to BigQuery and other supported sources through data sources. Reports consume
data-source fields, calculations, blends, filters, and controls. Report sharing, data credentials, and
underlying dataset permissions are separate access boundaries. A dashboard is a presentation layer,
not the canonical source of a metric definition.

# Explicit non-integrations and boundary conditions

- No service supplies one universal person identifier across search, website, store, app, purchase,
  subscription, and advertising-revenue stages.
- Search Console impressions and clicks are aggregated search-performance records, not GA4 users or
  sessions.
- A Play Console install-related metric is not equivalent to Firebase or GA4 `first_open`.
- A GA4 purchase event is not automatically identical to Play financial proceeds, cash received,
  refunds, taxes, fees, or subscription state.
- AdMob estimated earnings are not interchangeable with purchase revenue or accounting revenue.
- A product link defines a supported data path; it does not prove bidirectional transfer, complete
  history, equal retention, equal freshness, or equal totals.
- BigQuery export preserves event-level analytical flexibility but requires explicit SQL definitions
  for users, sessions, transactions, attribution, and reconciliation.
- Looker Studio can combine and present sources, but blending does not create a shared identity key or
  guarantee SQL-equivalent joins.

# Identity and reconciliation contract

Every cross-service metric should document:

1. source service and reporting surface;
2. event or aggregate grain;
3. identifier used, if any;
4. attribution model and lookback rule;
5. processing-time and freshness expectation;
6. retention and historical-restatement policy;
7. privacy, consent, thresholding, and modeling behavior;
8. currency, tax, fee, refund, and revenue scope;
9. deduplication and late-arrival policy;
10. acceptable reconciliation tolerance against adjacent services.

# Measurement boundary

The ecosystem is a chain of related measurement systems, not one continuous ledger. Integration links
reduce manual movement of data, but they do not erase differences in scope, grain, identity,
attribution, privacy processing, freshness, retention, or accounting meaning. Cross-service analysis
must preserve those differences explicitly before any funnel, cohort, revenue, or ROI conclusion is
published.
