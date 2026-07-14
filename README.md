# Google Analytics Knowledge Base

An evidence-based, file-based knowledge base for the Google analytics ecosystem. It is an independent domain instance of the `universal-ai-knowledge-base` framework; the universal project remains a separate reusable template.

## Current status

The approved research roadmap is complete and the repository is in maintenance mode.

Completed areas:

- Google Play Console;
- Google Search Console;
- Google AdMob;
- Firebase Analytics;
- Google Analytics 4;
- BigQuery;
- Looker Studio;
- cross-service ecosystem synthesis;
- repository intelligence and AI-agent documentation.

The current operational task is always defined in `STATE.md`.

## Start here

For a new human contributor or AI agent:

1. Read `AGENTS.md`.
2. Read `STATE.md`.
3. Follow `ONBOARDING.md`.
4. Use `ARCHITECTURE.md` to understand entity ownership.
5. Use `WORKFLOW.md` and `QUALITY.md` before changing the repository.

Supporting engineering documents:

- `STYLEGUIDE.md` — writing and formatting rules;
- `ROADMAP.md` — completed and candidate phases;
- `AI_CONTEXT.md` — autonomous-agent decision policy;
- `DECISIONS.md` — durable architecture decisions;
- `GLOSSARY.md` — shared terminology.

## Knowledge architecture

```text
Official sources
→ Evidence
→ Facts
→ Concepts and Services
→ Views
→ Reports
→ generated INDEX.jsonl
```

- `knowledge/services/`: product identity and boundaries.
- `knowledge/concepts/`: service-independent terminology.
- `knowledge/facts/`: atomic canonical claims.
- `knowledge/evidence/`: official-source provenance and exact source locations.
- `views/`: non-canonical reading routes.
- `reports/`: dated analyses and phase summaries.
- `schemas/`, `scripts/`, and `tests/`: the validation framework.
- `INDEX.jsonl`: generated locator for canonical and validated Markdown entities.

For a point lookup, search `INDEX.jsonl` by ID or term, then open the row's `path` and `record_locator`. Do not scan all packages by default.

## Add or update knowledge

1. Read `AGENTS.md` and `STATE.md`.
2. Confirm the task is inside the approved scope.
3. Search `INDEX.jsonl` and repository files for duplicates.
4. Generate IDs with `scripts.common.generate_id()`.
5. Store one atomic claim per Fact.
6. Link every confirmed Fact to at least one official Evidence record.
7. Give Evidence an exact source location and retrieval date.
8. Update Views and Reports only after canonical records stabilize.
9. Regenerate the Index and run all checks.

Never edit `INDEX.jsonl` manually and never add reverse `supports` links to Evidence.

## Install and verify

```shell
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python scripts/validate_knowledge.py
python scripts/validate_links.py
python scripts/validate_markdown_frontmatter.py
python scripts/generate_index.py --check
pytest
ruff check .
mypy scripts
```

On Windows, activate the environment with `.venv\Scripts\activate`. On Linux or macOS, use `source .venv/bin/activate`.

## Git workflow

1. Create a branch from `main`.
2. Make one coherent maintenance task or research phase per branch.
3. Run the full validation suite.
4. Open a Pull Request.
5. Merge only after automated checks pass and the diff is reviewed.

Do not push research changes directly to `main`.

## Restrictions

Do not use live accounts, credentials, OAuth, service accounts, live APIs, or real user data unless an explicit approved phase authorizes them. Do not create fictional Evidence or unverified confirmed Facts. Production ETL, databases, dashboards, deployments, and changes to the universal template require a separate approved scope.
