# Google Analytics Knowledge Base

## Project purpose

Create an evidence-based knowledge base about the Google analytics ecosystem using the independent
domain instance derived from `universal-ai-knowledge-base`.

## Scope

Includes official documentation, APIs, UI capabilities, exports, metrics, events, integrations,
identifiers, privacy, retention, marketing-funnel coverage, and architecture options. Excludes live
account changes, production integrations, OAuth, service accounts, API clients, ETL, dashboards,
real data loading, and deployment unless a later approved implementation phase changes that scope.

## Services

1. Google Play Console
2. Google Search Console
3. Google AdMob
4. Firebase
5. Google Analytics 4
6. BigQuery
7. Looker Studio

## Current research status

- Google Play Console: complete and consolidated.
- Google Search Console analytics: complete and consolidated.
- Google AdMob: next research service.

The authoritative task state is maintained in `STATE.md`.

## Research order

Research follows the Services list in order: primary product data sources first, then application
and monetization services, the central analytics layer, storage, and visualization. A service phase
must finish before the next begins unless `STATE.md` records an explicit decision to change the
order.

## Source policy

Use sources in this order: official documentation, official API reference, official support
article, official release notes, official product page, official policy document, primary
observation, and third-party context. AI-generated text is not Evidence.

## Knowledge principles

- **Single Source of Truth:** each entity and atomic claim has one canonical record.
- **Evidence First:** every confirmed Fact links to official Evidence.
- **Temporal Truth:** mutable claims include scope and verification dates.
- **Canonical Ownership:** Fact, Evidence, Concept, Service, View, and Report stay separate.
- **Small Context:** locate with the Index, then load only relevant records.
- **Separation:** Facts, Evidence, Concepts, and Services have distinct responsibilities.

## Delivery model

- Research and maintenance changes are developed on dedicated branches.
- Each coherent phase is reviewed through a Pull Request.
- Automated validation must pass before merge.
- `main` represents the latest accepted knowledge state.
- `INDEX.jsonl` is generated and tracked, but never edited manually.

## Expected result

After all research phases, the project should contain confirmed Facts, official Evidence,
service-independent Concepts, Service records, Views, final Reports, an integration map, marketing
funnel coverage, gap analysis, and architecture options.

The final applied outcome is a concrete marketing-attribution architecture for short links such as
`/fb`, covering the route from source click through website, Google Play, app activity, purchases,
advertising revenue, and reporting boundaries.

## Versioning

- framework_version: `1.0`
- domain_project_version: `0.2.0`
- schema_version: `1.0`
- research_snapshot_date: `2026-07-12`