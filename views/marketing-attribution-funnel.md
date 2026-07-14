---
id: "VIEW-01KXFTAHAEY57YS5SHVB4Q6YZS"
title: "Cross-service Marketing Attribution Funnel"
question: "How should source clicks, website visits, Google Play acquisition, app activity, purchases, subscriptions, and advertising revenue be connected without treating different service metrics as one continuous user-level funnel?"
audience: "Marketing analysts, product analysts, analytics engineers, data architects, researchers, and AI agents"
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
inclusion_criteria: "Include the measurement stages, identifiers, attribution boundaries, reconciliation requirements and architecture controls needed to analyse acquisition through monetization without asserting unsupported person-level continuity."
updated_at: "2026-07-14"
---

# Funnel contract

```text
source impression or campaign exposure
  → source click
      → website landing or redirect
          → Google Play store listing
              → store acquisition or install-related reporting
                  → application launch and first_open
                      → later app engagement
                          → purchase or subscription event
                          → advertising-revenue event
                              → GA4 reporting and attribution
                                  → BigQuery export and reconciliation models
                                      → Looker Studio governed reporting
```

This is a sequence of adjacent measurement stages, not a guaranteed person-level path. Each arrow must
state whether it represents a supported product integration, an instrumented application event, a
warehouse join, an aggregate comparison, or only a business hypothesis.

# Stage definitions

## 1. Source exposure and click

Search Console can describe Google Search impressions and clicks at aggregated query, page, country,
device and search-appearance scopes. Campaign platforms and owned links may supply their own click and
campaign parameters. These records describe acquisition activity before the measured website or app
session begins.

## 2. Website landing or redirect

GA4 web measurement starts only after a page or redirect endpoint executes measurement successfully.
A short link such as `/fb` should preserve campaign parameters, record the redirect server-side when
possible, and avoid depending exclusively on client-side JavaScript that may not run before navigation.
The redirect event is an acquisition record, not proof of a later store visit or install.

## 3. Google Play store boundary

Google Play Console reports store-listing and acquisition metrics under Play-specific definitions.
Store visitors, acquisitions and install-related metrics must retain their Play Console scope and
processing rules. They are not interchangeable with website users, GA4 sessions, Firebase users or
`first_open` events.

## 4. App activation and engagement

Firebase and GA4 app measurement begins when the installed application initializes analytics and emits
events. `first_open` is an analytics event produced after application launch; it is not a direct copy of
a Play Console install metric. Later app events describe measured product behavior, subject to consent,
SDK implementation, identity settings, event definitions and processing rules.

## 5. Purchase and subscription activity

A GA4 purchase or subscription-related event represents the instrumented analytics event and its
parameters. Play purchase, subscription-state and financial surfaces have different grains and business
meanings. Analytics revenue must therefore be reconciled against order, refund, tax, fee, currency,
subscription-state and payout records before it is used as accounting revenue.

## 6. Advertising revenue

AdMob advertising-revenue data can enter Firebase and GA4 through supported linking and event
collection. Advertising revenue remains a separate monetization stream from purchases and
subscriptions. Estimated earnings, finalized revenue and warehouse event values must retain explicit
source and status fields.

## 7. Warehouse and reporting layers

GA4 BigQuery export provides event-level rows for governed SQL reconstruction and reconciliation. It is
not guaranteed to reproduce every GA4 interface number without an explicit contract for identity,
attribution, late events, privacy processing, currency and session logic. Looker Studio should consume
approved warehouse models or clearly scoped direct connectors rather than redefine canonical metrics in
individual charts.

# Join strategy

Use deterministic identifiers only where their documented scope permits:

- campaign and click identifiers for acquisition records;
- landing URL and campaign parameters for aggregate source-to-website analysis;
- transaction or order identifiers for purchase reconciliation;
- subscription identifiers for lifecycle reconciliation when lawfully available;
- event date, platform, country, campaign and product dimensions for aggregate bridge tables;
- pseudonymous analytics identifiers only inside their permitted consent and retention boundary.

Never fabricate a universal key across Search Console, website, Play Console, Firebase, GA4, AdMob and
financial reporting. Where no documented key exists, publish aggregate conversion rates with an explicit
matching window and uncertainty statement.

# Minimum metric contract

Every funnel metric should record:

1. source system and reporting surface;
2. grain and counting unit;
3. eligible population and exclusions;
4. identifier and join method;
5. attribution model, source precedence and lookback window;
6. event time, processing time, timezone and freshness;
7. retention and historical-restatement behavior;
8. consent, privacy, thresholding and modeling effects;
9. currency, tax, fee, refund and revenue status;
10. reconciliation target, tolerance and owner.

# Recommended reporting layers

```text
raw service exports and reports
  → source-normalized staging models
      → identity-safe aggregate bridges
          → canonical funnel and revenue marts
              → governed Looker Studio data sources
                  → published reports
```

The canonical funnel should expose both stage totals and reconciliation diagnostics. Conversion rates
must use compatible numerator and denominator scopes; otherwise they should be labeled as directional
comparisons rather than exact funnel conversion.