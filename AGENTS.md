# AI Agent Entry Point

## Project purpose

This project is the domain instance for building and maintaining an evidence-based knowledge base about the Google analytics ecosystem. Start every session here, then read `STATE.md` before writing.

## Required reading order

1. `AGENTS.md` — mandatory rules.
2. `STATE.md` — current phase, task, blockers, and risks.
3. `ONBOARDING.md` — fast repository orientation.
4. `ARCHITECTURE.md` — entity ownership and repository structure.
5. `WORKFLOW.md` — execution process.
6. `QUALITY.md` — completion gates.
7. `STYLEGUIDE.md` — writing and formatting rules.
8. `AI_CONTEXT.md` — autonomous decision and context-loading policy.

Use `ROADMAP.md`, `DECISIONS.md`, and `GLOSSARY.md` when broader context is needed.

## Canonical entities

- Facts, Evidence, Concepts, and Services are records in `knowledge/**/*.yaml` packages.
- Views and Reports are validated, non-canonical Markdown projections.
- `INDEX.jsonl` is a generated locator and must never be edited manually.

## Canonical ownership

- Fact owns one atomic claim and links to Evidence, Concepts, and Services.
- Evidence owns source provenance; reverse `supports` links are prohibited.
- Concept owns service-independent meaning. Service owns only product identity and boundaries.
- View owns reading order. Report owns dated analysis, not current truth.

## Context loading workflow

1. Read this file and `STATE.md`.
2. Use `STATE.md` to identify the current phase, service, task, and active package writers.
3. Search `INDEX.jsonl` for an ID or term; do not scan the repository by default.
4. Load only the located record using `path` and `record_locator`.
5. Load Evidence only for verification, conflict resolution, or updates.
6. Keep graph depth at 1–2 normally, 3 for comparisons, and 4 for conflict investigation.

Routes:

- Definition: INDEX → Concept → related Facts.
- Verification: INDEX → Fact → Evidence.
- Service research: STATE → current Service → relevant View → related Facts → required Evidence.
- Cross-service analysis: relevant Views → selected Facts → Evidence only where verification is needed.
- Report preparation: View → selected Facts → Evidence → Report.

## Research source policy

Prefer official sources on `developers.google.com`, `support.google.com`, `firebase.google.com`, `cloud.google.com`, `developer.android.com`, and other official Google domains when necessary. Use this priority order: official documentation, API reference, support article, release notes, product page, policy document, primary observation, and finally third-party context. AI-generated text is never Evidence.

## Scope policy

The approved roadmap is complete. Do not start a new research phase from a candidate in `ROADMAP.md` unless `STATE.md` records an explicit approved scope. In maintenance mode, prioritize source freshness, schema integrity, links, generated index consistency, and documentation quality.

## Service isolation

For one service, load only its Service record, related Concepts and Facts, required Evidence, and the relevant View. Do not load all service records and packages without a specific need.

## Fact classification

Classify every assertion as a confirmed fact, candidate, inference, assumption, recommendation, or open question. Only Fact records are canonical claims. A confirmed Fact requires at least one official Evidence record.

## Current-state questions

For current APIs, limits, pricing, retention, interfaces, and integrations, record the verification date and applicable scope. Re-check mutable claims before reuse.

## Write workflow

- Respect `active_package_writers` in `STATE.md` and search for duplicates first.
- Generate new IDs with `scripts.common.generate_id()`; do not handcraft sequential-looking IDs.
- Use `<TYPE>-<ULID>` IDs; paths and slugs are not identifiers.
- Do not copy `Fact.statement` into Services, Views, Reports, Concepts, or the Index.
- Keep Fact packages at 20–80 records when practical, with a hard maximum of 100.
- Keep packages under 96 KiB when practical and never above 128 KiB.
- Prefer readable multi-line YAML for new production packages.
- Follow `STYLEGUIDE.md` for wording and formatting.

## Git workflow

- Create a dedicated branch from `main` for each coherent maintenance task or research phase.
- Do not push research changes directly to `main`.
- Keep unrelated refactors out of research Pull Requests.
- Run the full validation suite before opening or updating a Pull Request.
- Merge only after automated checks pass and the diff is reviewed.

## Validation workflow

After canonical changes run, in order:

1. `python scripts/validate_knowledge.py`
2. `python scripts/validate_links.py`
3. `python scripts/validate_markdown_frontmatter.py`
4. `python scripts/generate_index.py`
5. `python scripts/generate_index.py --check`
6. `pytest`, `ruff check .`, and `mypy scripts`

For documentation-only changes that do not affect indexed Markdown front matter, the Index should remain unchanged, but all automated checks should still pass.

Use `QUALITY.md` as the final Definition of Done.

## Prohibited actions

- Do not create confirmed Facts without official Evidence or fictional Evidence.
- Do not use real accounts, credentials, OAuth, service accounts, live APIs, or user data unless a future phase explicitly authorizes them.
- Do not add production ETL, databases, API servers, dashboards, deployment, or Docker unless the approved phase requires them.
- Do not add arbitrary entity types, statuses, Fact types, or relation names.
- Do not use unsafe YAML loading, anchors, aliases, merge keys, or custom tags.
- Do not modify `universal-ai-knowledge-base` from this domain project.
- Do not claim completion without repository-visible files, validation, CI, and matching PR state.

## Current file map

- `PROJECT.md`: compact domain and architecture contract.
- `STATE.md`: phase, tasks, locks, blockers, and risks.
- `ARCHITECTURE.md`: repository structure and entity ownership.
- `WORKFLOW.md`: research and maintenance lifecycle.
- `STYLEGUIDE.md`: canonical writing and formatting rules.
- `QUALITY.md`: Definition of Done and merge gates.
- `ROADMAP.md`: completed and candidate strategic phases.
- `ONBOARDING.md`: first-session guide.
- `AI_CONTEXT.md`: autonomous-agent operating policy.
- `DECISIONS.md`: durable architecture decisions.
- `GLOSSARY.md`: repository terminology.
- `INDEX.jsonl`: generated entity locator.
- `knowledge/`: canonical YAML packages.
- `views/`: reading routes; `reports/`: dated analyses.
- `schemas/`, `scripts/`, `tests/`: portable validation framework.
- `.github/workflows/`: automated repository checks.
