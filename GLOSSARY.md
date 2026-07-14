# Glossary

## Purpose

This glossary defines repository terms consistently. Product-specific definitions remain in canonical Concept and Fact records.

## Agent

A human or AI contributor that reads repository state, performs scoped work, validates changes, and leaves a repository-visible handoff.

## Assumption

A statement accepted temporarily for planning but not confirmed by Evidence. Assumptions must not be stored as confirmed Facts.

## Atomic Fact

A Fact containing one independently verifiable claim that can be updated without changing unrelated claims.

## Blocker

A condition that prevents the current approved task from continuing. A blocker should state the exact missing permission, decision, credential, or user action.

## Candidate

A possible claim that has not yet met confirmation requirements.

## Canonical entity

A validated structured record under `knowledge/` that owns repository truth: Evidence, Fact, Concept, or Service.

## Canonical source

The repository location that owns a piece of structured knowledge. For product claims this is normally a Fact linked to Evidence.

## Concept

A canonical entity defining reusable meaning, preferably independent of a single product implementation.

## Confidence

The repository’s declared certainty level for a claim, separate from status and Evidence authority.

## Cross-service analysis

Analysis that compares or connects multiple services while preserving differences in identity, grain, attribution, freshness, retention, and processing.

## Evidence

A canonical record describing official source provenance, source location, retrieval date, and the information directly supported by the source.

## Fact

A canonical record containing one atomic claim with subject, predicate, object, scope, status, confidence, and supporting references.

## Generated artifact

A file produced deterministically from canonical repository content. `INDEX.jsonl` is a generated artifact and must not be edited manually.

## Graph depth

The number of relationship hops loaded while following entities. Normal work uses depth 1–2; comparison may use 3; conflict investigation may use 4.

## Inference

A conclusion logically derived from Facts or Evidence but not directly stated by a source. Inferences must be labeled and normally belong in Reports.

## INDEX.jsonl

The generated line-delimited JSON locator for repository entities. It supports low-token search by ID, title, type, path, and record location.

## Key event

A GA4 event marked as especially important to the business. Historical sources may use the term conversion; preserve source context where required.

## Knowledge package

A YAML file containing multiple records of one canonical entity type and coherent topic.

## Maintenance mode

Repository state after the approved roadmap is complete, where work focuses on freshness, integrity, corrections, documentation, and explicitly approved new phases.

## Open question

A documented issue that remains unresolved because Evidence is incomplete, behavior is property-specific, or the scope excludes verification.

## Phase

A coherent approved research or engineering scope with defined outputs, validation, and one primary Pull Request.

## Projection

A non-canonical representation over canonical entities. Views and Reports are projections.

## Recommendation

Suggested action based on Facts, analysis, or design judgment. Recommendations are not confirmed product Facts.

## Report

A validated Markdown projection containing dated analysis, method, limitations, selected entity references, findings, and open questions.

## Research scope

The explicit boundary describing what a phase will investigate, what outputs it will create, and what is excluded.

## Service

A canonical entity representing a product or platform identity and its broad boundary in the ecosystem.

## Scope

Conditions necessary to interpret a Fact, such as product surface, edition, platform, geography, channel, or verification date.

## Source freshness

How recently a mutable claim and its Evidence were rechecked against current official documentation.

## Statement status

Classification such as confirmed, candidate, inference, assumption, recommendation, or open question. Only schema-supported canonical statuses may be stored in structured records.

## View

A validated Markdown projection defining a focused question, selected entities, filters, and reading order.

## Validation suite

The complete set of schema, reference, Markdown, index, test, lint, and type checks required before merge.

## Active package writer

A package path listed in `STATE.md` to signal current ownership and reduce conflicting parallel edits.

## Data grain

The unit represented by one row or record, such as event, item, session, user, query, page, or daily aggregate.

## Attribution

The rules used to assign credit to touchpoints associated with a key event or outcome. Different services and surfaces can use different attribution rules.

## Reporting identity

The identity spaces and rules GA4 uses to unify and de-duplicate users in report-layer outputs.

## Retention

The period for which a product or repository surface keeps data available. Retention is distinct from freshness, recovery, and report aggregation.

## Freshness

The delay and processing state between data collection and availability in a reporting, API, export, or analytical surface.

## Reconciliation

The process of explaining and, where possible, aligning metrics from different systems while respecting grain, scope, identity, attribution, timing, currency, and processing differences.

## Definition of done

The complete set of conditions in `QUALITY.md` that must pass before a task, phase, or PR is considered complete.
