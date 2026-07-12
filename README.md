# Google Analytics Knowledge Base

An evidence-based, file-based knowledge base for the Google analytics ecosystem. It is an
independent domain instance of the `universal-ai-knowledge-base` framework; the universal project
remains a separate reusable template.

## Research order

Google Play Console → Google Search Console → Google AdMob → Firebase → Google Analytics 4 →
BigQuery → Looker Studio. Detailed product research has not started in this foundation phase.

## Structure and navigation

- `knowledge/services/`: product identity and boundaries.
- `knowledge/concepts/`: neutral terminology.
- `knowledge/facts/` and `knowledge/evidence/`: added during research.
- `views/`: non-canonical reading routes; `reports/`: dated analyses.
- `schemas/`, `scripts/`, and `tests/`: the portable validation framework.
- `INDEX.jsonl`: generated locator for all canonical and Markdown entities.

Search `INDEX.jsonl` by ID or term, then open the row's `path` and `record_locator`. Do not scan all
packages for a point lookup.

## Add a Fact or Evidence

Read `AGENTS.md` and `STATE.md`, search the Index for duplicates, and use
`scripts.common.generate_id()` for the correct ID prefix. A Fact is one atomic claim; a confirmed
Fact must link to at least one official Evidence record. Evidence must identify an exact source
location, provenance, retrieval date, and verification date. Never add reverse `supports` links.

After changes, regenerate the Index and run every check below. Never edit `INDEX.jsonl` manually.

## Install and verify

```shell
python -m venv .venv
.venv/Scripts/python -m pip install -e ".[dev]"
pytest
ruff check .
mypy scripts
python scripts/validate_knowledge.py
python scripts/validate_links.py
python scripts/validate_markdown_frontmatter.py
python scripts/generate_index.py
python scripts/generate_index.py --check
```

## Restrictions

Do not use live accounts, credentials, OAuth, service accounts, live APIs, or real user data. Do
not create fictional Evidence or unverified confirmed Facts. This phase does not add ETL,
databases, dashboards, deployments, Docker, CI/CD, or changes to the universal template.
