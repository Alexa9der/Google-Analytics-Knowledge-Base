# Onboarding

## Purpose

This guide helps a new human contributor or AI agent understand the repository quickly and begin work without scanning every file.

## First 10 minutes

Read in this order:

1. `README.md` — project overview.
2. `PROJECT.md` — compact project contract.
3. `AGENTS.md` — mandatory agent rules.
4. `STATE.md` — current operational state.
5. `ARCHITECTURE.md` — repository structure and entity ownership.
6. `WORKFLOW.md` — execution process.
7. `QUALITY.md` — completion criteria.
8. `STYLEGUIDE.md` — writing and formatting rules.
9. `AI_CONTEXT.md` — autonomous-agent decision rules.

Read `ROADMAP.md`, `DECISIONS.md`, and `GLOSSARY.md` when broader context is needed.

## Quick repository model

```text
Official sources
→ Evidence
→ Facts
→ Concepts and Services
→ Views
→ Reports
→ generated INDEX.jsonl
```

Canonical truth lives in structured records under `knowledge/`. Views and Reports are projections.

## Determine current work

Open `STATE.md` and identify:

- `current_phase`;
- `project_status`;
- `current_task`;
- `next_tasks`;
- `blockers`;
- `active_package_writers`;
- `known_risks`.

If `project_status` is `maintenance`, do not invent a new phase. Work only on an approved maintenance task or explicit new scope.

## Load minimal context

Do not recursively read the whole repository.

Use this route:

```text
STATE.md
→ INDEX.jsonl search
→ relevant record or View
→ directly linked Facts or Concepts
→ Evidence only for verification
```

Use repository search when the index does not cover root engineering documents or when checking duplicates by wording.

## Before writing

Check:

- Is there already an equivalent Fact?
- Is the official source already represented as Evidence?
- Is there an existing Concept?
- Is a Service record actually needed?
- Is the task inside the approved scope?
- Is another package listed in `active_package_writers`?

## First local checks

From repository root:

```bash
python scripts/validate_knowledge.py
python scripts/validate_links.py
python scripts/validate_markdown_frontmatter.py
python scripts/generate_index.py --check
pytest
ruff check .
mypy scripts
```

Run these before changing anything to distinguish pre-existing issues from your work.

## Starting a task

1. Create a dedicated branch from `main`.
2. Update `STATE.md` if the task changes active project state.
3. Search for duplicate entities.
4. Make the smallest coherent change.
5. Validate locally.
6. Open or update a draft PR.
7. Continue until the approved scope is complete.

## Research task checklist

- [ ] Scope is explicit.
- [ ] Official sources identified.
- [ ] Evidence records added.
- [ ] Atomic Facts extracted.
- [ ] Existing Concepts reused.
- [ ] View created when phase-level navigation is needed.
- [ ] Report created when phase-level synthesis is required.
- [ ] `STATE.md` updated.
- [ ] `INDEX.jsonl` regenerated.
- [ ] Full validation passes.

## Maintenance task checklist

- [ ] Root cause is identified.
- [ ] Existing semantics are preserved unless correction is intended.
- [ ] References and IDs remain valid.
- [ ] No temporary diagnostics remain.
- [ ] Tests are not weakened to hide errors.
- [ ] PR explains the cause and resolution.

## Common mistakes

### Reading too much

Do not load every Evidence and Fact package. Use the index and Views.

### Creating duplicate Facts

Semantic duplication is still duplication even when titles differ.

### Handcrafting IDs

Always use `scripts.common.generate_id()`.

### Editing the index

`INDEX.jsonl` is generated. Change canonical sources and regenerate it.

### Treating Reports as truth

Reports are dated synthesis. Confirm important claims through Facts and Evidence.

### Starting unapproved research

Roadmap candidates are not active tasks. Require explicit scope.

### Declaring completion too early

Files created does not mean task complete. Use `QUALITY.md`.

## Where to look for answers

- Architecture question → `ARCHITECTURE.md`
- Current task → `STATE.md`
- Research process → `WORKFLOW.md`
- Formatting and wording → `STYLEGUIDE.md`
- Done criteria → `QUALITY.md`
- Strategic direction → `ROADMAP.md`
- Agent decision logic → `AI_CONTEXT.md`
- Why a rule exists → `DECISIONS.md`
- Term meaning → `GLOSSARY.md`

## Handoff format

At the end of a work session, leave the repository understandable without chat history:

- update `STATE.md`;
- update the PR body;
- commit coherent changes;
- record blockers precisely;
- state the next executable task;
- avoid relying on private notes or conversation memory.

## Success condition

Onboarding is complete when you can answer:

1. What is canonical truth?
2. What is the current task?
3. Which files may be changed?
4. How are IDs generated?
5. What validations are required?
6. What conditions must pass before merge?
