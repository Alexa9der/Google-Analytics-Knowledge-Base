# Repository Workflow

## Purpose

This document defines the standard operating procedure for research, maintenance, validation, Pull Requests, and merge. Follow it unless `STATE.md` explicitly records an approved exception.

## Session start

At the beginning of every work session:

1. Read `AGENTS.md`.
2. Read `STATE.md`.
3. Check open Pull Requests and latest CI status.
4. Identify the current phase, task, blockers, and active package writers.
5. Search `INDEX.jsonl` and repository files for duplicates before writing.
6. Load only the context needed for the selected task.

## Branch policy

Create one dedicated branch from `main` for each coherent phase or maintenance task.

Recommended names:

```text
agent/phase-<number>-<scope>
agent/maintenance-<scope>
agent/docs-<scope>
```

Never push research changes directly to `main`.

## Research phase workflow

### 1. Define scope

Update `STATE.md` with:

- current phase;
- project status;
- current task;
- next tasks;
- blockers;
- active package writers;
- known risks.

A phase must have a clear boundary and completion target.

### 2. Locate existing knowledge

Before adding records:

- search `INDEX.jsonl` for related IDs and terms;
- inspect existing Concepts and Services;
- search existing Facts for semantically equivalent claims;
- search existing Evidence for the same source page.

Do not create duplicates merely because wording differs.

### 3. Collect official Evidence

Use official Google sources whenever available.

For each source:

- capture the exact URL or source location;
- record retrieval date;
- summarize only what the source directly supports;
- classify authority and directness;
- avoid invented publication dates;
- do not treat AI-generated text as Evidence.

### 4. Extract atomic Facts

Each Fact should express one independently verifiable claim.

A good Fact:

- has one subject;
- uses one clear predicate;
- has a bounded object;
- includes applicable scope;
- links to at least one official Evidence record when confirmed;
- avoids recommendations or interpretation in the statement.

Split combined claims when they can change independently.

### 5. Create or reuse Concepts

Create a Concept only when:

- the term has reusable meaning across multiple services or packages;
- an existing Concept does not already cover it;
- the definition can remain stable and service-independent.

Do not create Concepts as labels for every Fact topic.

### 6. Maintain Service boundaries

Create or update a Service only for product identity and high-level boundaries. Keep operational details in Facts.

### 7. Build the final View

After canonical packages stabilize, create a View that:

- asks one clear question;
- selects only relevant entities;
- defines a useful reading order;
- contains no unsupported new claims;
- explains boundaries and navigation.

### 8. Build the final Report

Create a dated Report that:

- states the research question;
- cites selected Fact and Evidence IDs in front matter;
- summarizes findings without replacing canonical records;
- records method and limitations;
- lists open questions and next phase.

### 9. Update project state

When a block is complete:

- move it into `completed`;
- update `current_task`;
- update `next_tasks`;
- clear finished package writers;
- preserve real risks and blockers.

Do not mark a phase complete before final validation.

## ID generation

Generate IDs with the repository helper:

```python
from scripts.common import generate_id

print(generate_id("FACT"))
```

Use the required typed prefix and generated ULID. Never handcraft sequential-looking IDs.

## Validation sequence

After canonical changes, run in this order:

```bash
python scripts/validate_knowledge.py
python scripts/validate_links.py
python scripts/validate_markdown_frontmatter.py
python scripts/generate_index.py
python scripts/generate_index.py --check
pytest
ruff check .
mypy scripts
```

For documentation-only changes that do not alter indexed front matter, `INDEX.jsonl` should remain unchanged, but the complete automated suite should still pass.

## Handling failures

When validation fails:

1. Capture the complete error, not only the final line.
2. Identify the first root cause.
3. Fix canonical data or documentation rather than weakening validation.
4. Re-run the smallest relevant validator.
5. Re-run the complete suite before declaring success.
6. Remove temporary diagnostic workflows and files.

Never update tests to hide an unintended inventory change. Update acceptance counts only when the production inventory intentionally changes.

## Pull Request workflow

### Draft stage

Open a draft PR early when work spans multiple commits.

The PR body should contain:

- current status;
- completed blocks;
- current inventory additions;
- remaining scope;
- validation status.

Keep the body current as the phase progresses.

### Ready stage

A PR can move from Draft to Ready only when:

- scope is complete;
- View and Report exist when required;
- `STATE.md` is accurate;
- `INDEX.jsonl` is current;
- all temporary files are removed;
- the full validation suite passes;
- CI is green;
- the diff has been reviewed for unrelated changes.

### Merge stage

Prefer squash merge for a coherent phase unless repository policy changes.

After merge:

1. Confirm `main` contains the expected files.
2. Confirm post-merge CI is green when available.
3. Update or close stale duplicate PRs.
4. Start the next explicit phase on a new branch.

## Maintenance workflow

Maintenance may include:

- source freshness review;
- corrected Evidence URLs;
- changed API limits or pricing;
- schema migrations;
- ID integrity fixes;
- broken-link fixes;
- generated-index repair;
- documentation improvements.

Maintenance must preserve traceability. If a confirmed Fact changes materially, update its Evidence, verification date, and scope rather than silently rewriting history.

## Conflict workflow

When sources conflict:

1. Load the relevant Facts and Evidence.
2. Check source date, product edition, geography, platform, and scope.
3. Prefer the more direct official source for the exact claim.
4. Record the conflict as a risk or open question if unresolved.
5. Do not merge incompatible claims into one ambiguous Fact.

## Autonomous-agent loop

An autonomous agent should repeat:

```text
Read state
→ select next bounded task
→ load minimal context
→ execute one complete cycle
→ validate
→ update state and PR
→ continue without waiting when no blocker exists
```

The agent should stop only when the approved scope is complete or a genuine blocker requires user action.
