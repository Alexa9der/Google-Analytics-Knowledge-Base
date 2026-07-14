# Repository Roadmap

## Purpose

This document records the strategic development path of the knowledge base. `STATE.md` remains the operational source for current work, while this file describes completed phases, maintenance expectations, and possible future expansions.

## Completed roadmap

### Phase 0 — Repository foundation

- canonical entity model;
- schemas and validators;
- generated entity index;
- CI and branch workflow.

### Phase 1 — Google Play Console

- store performance;
- statistics;
- purchases and subscriptions;
- financial reports;
- ratings and reviews;
- Android Vitals;
- final service consolidation.

### Phase 2 — Google Search Console

- search impressions and clicks;
- query, page, device and country analysis;
- API and export boundaries;
- connection to landing-page analytics.

### Phase 3 — Google AdMob

- requests, matches, impressions and clicks;
- estimated earnings and RPM;
- mediation and reporting API boundaries;
- Firebase user metrics and impression-level revenue;
- payment versus estimated-earnings boundary.

### Phase 4 — Firebase Analytics

- app-side event collection;
- automatic and custom events;
- users, properties and audiences;
- key events and attribution;
- AdMob and BigQuery integrations;
- Firebase-to-GA4 measurement boundary.

### Phase 5 — Google Analytics 4

- property and data-stream architecture;
- Reports, Explorations and APIs;
- reporting identity;
- attribution, consent and retention;
- Measurement Protocol;
- product integrations;
- reporting-surface reconciliation.

### Phase 6 — BigQuery

- architecture, datasets, locations and IAM;
- billing and cost controls;
- GA4 export schema;
- SQL reconstruction;
- retention, time travel and fail-safe;
- partitioning, clustering and governance;
- transformation layers.

### Phase 7 — Looker Studio

- report and data-source architecture;
- connectors and credentials;
- calculated fields and blending;
- filters and controls;
- sharing, embedding, publishing and governance.

### Phase 8 — Cross-service synthesis

- end-to-end integration map;
- marketing attribution funnel;
- identity-safe join strategy;
- metric contract;
- freshness, retention and reconciliation gaps;
- governed first-party `/fb` redirect architecture.

### Phase 9 — Repository intelligence

- architecture documentation;
- workflow and style standards;
- quality gates;
- onboarding and AI operating context;
- decision log and glossary;
- maintenance-ready repository documentation.

## Current lifecycle state

After Phase 9, the repository enters maintenance mode. New work should be either:

- source freshness maintenance;
- schema and validation maintenance;
- correction of confirmed knowledge;
- explicitly approved new research phase;
- engineering documentation improvement.

## Maintenance roadmap

Recurring maintenance should include:

1. Review official Google documentation for material changes.
2. Re-verify mutable claims such as pricing, quotas, retention and interfaces.
3. Repair changed or removed source URLs.
4. Keep schemas, tests and production inventory aligned.
5. Regenerate `INDEX.jsonl` after canonical changes.
6. Preserve green CI.
7. Record important architecture changes in `DECISIONS.md`.

## Candidate future phases

The following are not current commitments. Each requires an explicit scope before work begins.

### Google Tag Manager

Potential scope:

- containers, workspaces and versions;
- tags, triggers and variables;
- server-side tagging;
- consent integration;
- GA4 and advertising tag boundaries;
- preview, debugging and governance.

### Google Ads analytics

Potential scope:

- account and manager hierarchy;
- campaign reporting;
- conversion imports;
- attribution and enhanced conversions;
- Google Ads API;
- BigQuery transfer and reconciliation.

### Campaign Manager 360 and Display & Video 360

Potential scope:

- floodlight and conversion boundaries;
- campaign and placement reporting;
- cross-channel attribution;
- export and API surfaces.

### Dataform

Potential scope:

- SQL workflow compilation;
- dependency graph;
- incremental tables;
- assertions;
- release and workflow configurations;
- BigQuery data-mart governance.

### BigLake and data governance expansion

Potential scope:

- external and federated data;
- object tables;
- cross-cloud access;
- policy tags and governance patterns;
- data residency boundaries.

### Vertex AI and analytics ML

Potential scope:

- governed feature creation;
- BigQuery ML versus Vertex AI;
- model training and evaluation;
- prediction pipelines;
- privacy and data-governance boundaries.

### Google Cloud Storage and event pipelines

Potential scope:

- export staging;
- lifecycle management;
- Pub/Sub and Cloud Run or Functions;
- batch and streaming ingestion;
- operational monitoring.

## New-phase admission criteria

A candidate becomes an active phase only when:

- the user explicitly approves the scope;
- the service has a clear relation to the project purpose;
- expected canonical entities and outputs are defined;
- source availability is sufficient;
- risks and exclusions are recorded in `STATE.md`;
- a dedicated branch and draft PR are created.

## Roadmap governance

- `ROADMAP.md` describes strategy.
- `STATE.md` describes current execution.
- `PROJECT.md` describes the project contract.
- `DECISIONS.md` records durable architecture choices.

Do not use roadmap candidates as authorization to start research automatically.
