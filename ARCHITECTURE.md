# Repository Architecture

## Purpose

This repository is an evidence-based knowledge system for the Google analytics ecosystem. It separates source provenance, atomic claims, shared terminology, navigation routes, and dated analysis so that both humans and AI agents can inspect, verify, and extend the knowledge base without treating prose as an unstructured source of truth.

## Architectural principles

1. Canonical knowledge is structured and validated.
2. Every confirmed claim is traceable to official Evidence.
3. Facts are atomic and reusable.
4. Concepts are service-independent definitions.
5. Services describe product identity and boundaries, not detailed claims.
6. Views organize reading order but do not create new knowledge.
7. Reports synthesize dated analysis and do not replace canonical Facts.
8. `INDEX.jsonl` is generated and never edited manually.
9. Validation is part of the architecture, not an optional final step.
10. Context loading should be narrow and intentional.

## Repository map

```text
.
├── AGENTS.md
├── AI_CONTEXT.md
├── ARCHITECTURE.md
├── DECISIONS.md
├── GLOSSARY.md
├── ONBOARDING.md
├── PROJECT.md
├── QUALITY.md
├── README.md
├── ROADMAP.md
├── STATE.md
├── STYLEGUIDE.md
├── WORKFLOW.md
├── INDEX.jsonl
├── knowledge/
│   ├── concepts/
│   ├── evidence/
│   ├── facts/
│   └── services/
├── views/
├── reports/
├── schemas/
├── scripts/
├── tests/
└── .github/workflows/
```

## Canonical and non-canonical layers

### Canonical entities

Canonical entities are validated records stored under `knowledge/`.

- **Evidence** records official source provenance and what the source supports.
- **Fact** records one atomic claim and references supporting Evidence.
- **Concept** records reusable, service-independent meaning.
- **Service** records product identity, ownership, and high-level boundaries.

Canonical entities may be referenced by stable IDs and are indexed in `INDEX.jsonl`.

### Projection entities

Projection entities are validated Markdown documents.

- **View** defines a question, selected entities, and reading order.
- **Report** provides dated analysis based on selected Facts and Evidence.

Views and Reports must not introduce unsupported canonical claims.

## Knowledge flow

```text
Official source
    ↓
Evidence
    ↓
Atomic Facts
    ↓
Shared Concepts and Service boundaries
    ↓
Views
    ↓
Reports
    ↓
Generated INDEX.jsonl
```

The arrows represent derivation and navigation, not ownership reversal. Evidence does not contain reverse links to every supported Fact. Facts own their outgoing references.

## Entity responsibilities

### Evidence

Evidence answers: “Where does this claim come from?”

It owns:

- source URL;
- publisher;
- retrieval date;
- source location;
- concise source summary;
- authority and verification state.

It does not own:

- reverse `supports` lists;
- analytical conclusions;
- recommendations;
- service-wide summaries.

### Fact

Fact answers: “What exactly is claimed?”

It owns:

- one atomic statement;
- subject, predicate, and object;
- scope and verification date;
- confidence and status;
- Evidence, Concept, and Service references.

A confirmed Fact must have official Evidence.

### Concept

Concept answers: “What does this term mean across services?”

Concepts should remain reusable and avoid product-specific implementation details unless the concept itself is product-specific.

### Service

Service answers: “What product or platform boundary is this?”

Services identify products and their high-level role. Detailed behavior belongs in Facts.

### View

View answers: “Which entities should be read, and in what order, to answer this question?”

A View selects existing entities and provides a route through them. It must not become a hidden source of new Facts.

### Report

Report answers: “What was concluded from the selected evidence and facts as of a given date?”

Reports are snapshots. Mutable product behavior must remain traceable to verified Facts.

## Reference direction

Preferred reference direction:

```text
Fact → Evidence
Fact → Concept
Fact → Service
View → selected entities
Report → Facts, Evidence, Concepts, Services
```

Avoid:

- Evidence → reverse lists of Facts;
- duplicated Fact statements inside Service records;
- hand-maintained Index entries;
- circular ownership between canonical entities.

## Generated index

`INDEX.jsonl` is a generated locator used for low-token navigation. Each row points to an entity and its record location.

The index is rebuilt with:

```bash
python scripts/generate_index.py
```

Freshness is checked with:

```bash
python scripts/generate_index.py --check
```

Manual editing is prohibited because it creates divergence from canonical files.

## Validation architecture

The repository validates four layers:

1. YAML and JSON schema conformance.
2. Cross-entity references and ID integrity.
3. Markdown front matter for Views and Reports.
4. Generated index freshness and repository acceptance tests.

The canonical validation order is defined in `WORKFLOW.md` and enforced by CI.

## Context-loading architecture for AI agents

Agents should not scan all files by default.

Preferred route:

```text
AGENTS.md
→ STATE.md
→ INDEX.jsonl search
→ located entity
→ directly related entities
→ Evidence only when verification is needed
```

Normal graph depth should remain 1–2. Cross-service comparisons may use depth 3. Conflict investigations may use depth 4.

## Phase architecture

A research phase is a coherent scope that normally produces:

- one or more Evidence packages;
- one or more Fact packages;
- Concepts only when genuinely reusable terminology is missing;
- one final View;
- one final Report;
- updated `STATE.md`;
- regenerated `INDEX.jsonl`;
- green CI;
- one merged Pull Request.

Maintenance work may be smaller but must preserve the same quality gates.

## Extension rules

When adding a new service or domain:

1. Define an explicit scope in `STATE.md` and `ROADMAP.md`.
2. Reuse existing Concepts before creating new ones.
3. Search for duplicate Facts and Evidence.
4. Create a Service only when the product boundary is genuinely new.
5. Keep packages coherent and below repository size limits.
6. Add Views and Reports only after the canonical layer is stable.
7. Update tests if production inventory counts are intentionally changed.

## Stable architectural constraints

Do not change these without an explicit architecture decision:

- Fact and Evidence separation;
- generated Index ownership;
- stable typed IDs;
- official-source requirement for confirmed Facts;
- Views and Reports as non-canonical projections;
- validation-before-merge policy;
- dedicated branch and PR per coherent phase or maintenance task.

See `DECISIONS.md` for rationale and `QUALITY.md` for completion criteria.
