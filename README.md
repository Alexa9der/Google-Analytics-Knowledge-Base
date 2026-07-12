# Google Analytics Knowledge Base

An evidence-based, file-based knowledge base for the Google analytics ecosystem. It is an
independent domain instance of the `universal-ai-knowledge-base` framework; the universal project
remains a separate reusable template.

## Current status

Completed research blocks:

- Google Play Console — researched and consolidated.
- Google Search Console analytics — researched and consolidated.

Next service:

- Google AdMob.

The current phase and active task are always defined in `STATE.md`.

## Research order

Google Play Console → Google Search Console → Google AdMob → Firebase → Google Analytics 4 →
BigQuery → Looker Studio.

## Structure and navigation

- `knowledge/services/`: product identity and boundaries.
- `knowledge/concepts/`: service-independent terminology.
- `knowledge/facts/`: atomic canonical claims.
- `knowledge/evidence/`: official-source provenance and exact source locations.
- `views/`: non-canonical reading routes.
- `reports/`: dated analyses and phase summaries.
- `schemas/`, `scripts/`, and `tests/`: the validation framework.
- `INDEX.jsonl`: generated locator for all canonical and Markdown entities.

For a point lookup, search `INDEX.jsonl` by ID or term, then open the row's `path` and
`record_locator`. Do not scan all packages by default.

## Add a Fact or Evidence

1. Read `AGENTS.md` and `STATE.md`.
2. Search `INDEX.jsonl` for duplicates and related entities.
3. Generate IDs with `scripts.common.generate_id()`.
4. Store one atomic claim per Fact.
5. Link every confirmed Fact to at least one official Evidence record.
6. Give Evidence an exact source location, retrieval date, and verification date.
7. Regenerate the Index and run all checks.

Never edit `INDEX.jsonl` manually and never add reverse `supports` links to Evidence.

## Install and verify

```shell
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
pytest
ruff check .
mypy scripts
python scripts/validate_knowledge.py
python scripts/validate_links.py
python scripts/validate_markdown_frontmatter.py
python scripts/generate_index.py --check
```

On Windows, activate the environment with `.venv\\Scripts\\activate`. On Linux or macOS, use
`source .venv/bin/activate`.

## Git workflow

All project changes should be reviewable:

1. Create a branch from `main`.
2. Make one coherent change or research phase per branch.
3. Run the full validation suite.
4. Open a Pull Request.
5. Merge only after automated checks pass and the diff is reviewed.

Do not push research changes directly to `main`.

## Restrictions

Do not use live accounts, credentials, OAuth, service accounts, live APIs, or real user data unless a
future phase explicitly authorizes them. Do not create fictional Evidence or unverified confirmed
Facts. The current project scope excludes production ETL, databases, dashboards, deployments, and
changes to the universal template.