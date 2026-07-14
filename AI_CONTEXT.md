# AI Context

## Purpose

This document defines how an AI agent should reason about the repository, choose work, minimize context, preserve integrity, and continue autonomously without relying on chat history.

## Core objective

Optimize for a repository that is:

- evidence-based;
- traceable;
- structurally valid;
- easy to navigate with limited context;
- maintainable by future humans and agents;
- explicit about uncertainty and scope.

Do not optimize for file count, prose volume, or apparent activity.

## Source-of-truth hierarchy

When instructions conflict, use this order:

1. Repository schemas and executable validation.
2. `AGENTS.md` mandatory operating rules.
3. `PROJECT.md` project contract.
4. `STATE.md` current approved scope and execution state.
5. `ARCHITECTURE.md` entity ownership and repository structure.
6. `QUALITY.md` completion gates.
7. `WORKFLOW.md` execution process.
8. `STYLEGUIDE.md` presentation conventions.
9. `ROADMAP.md` strategic candidates.
10. Conversation context and ad hoc notes.

A lower-priority source cannot silently override a higher-priority constraint.

## Decision policy

Before changing the repository, answer:

1. Is the task explicitly approved?
2. Is the work canonical research, projection, maintenance, or documentation?
3. Which entity owns the information?
4. Does equivalent knowledge already exist?
5. What is the smallest coherent change?
6. What validation proves completion?

If these questions cannot be answered, gather repository context before writing.

## Context minimization

Default context route:

```text
AGENTS.md + STATE.md
→ INDEX.jsonl search
→ one relevant View or package
→ linked entities only
```

Avoid:

- loading every package;
- reading all Reports for a local fix;
- opening Evidence unless verification is needed;
- repeating large file contents in working notes;
- relying on chat summaries instead of repository state.

Use graph depth:

- 1–2 for normal work;
- 3 for cross-service comparison;
- 4 only for conflict investigation.

## Autonomous task selection

When no confirmation is required, select work in this order:

1. Active blocker that can be resolved without user action.
2. Current task in `STATE.md`.
3. First executable item in `next_tasks`.
4. CI or validation failure on the active PR.
5. Repository hygiene required to complete the approved scope.

Do not start roadmap candidates merely because current work is finished.

## Bounded execution loop

For each cycle:

1. Inspect state and PR status.
2. Choose one bounded outcome.
3. Load minimal context.
4. Make coherent changes.
5. Run targeted checks.
6. Run the complete suite when the cycle closes a block.
7. Update `STATE.md` and PR body.
8. Continue to the next approved task when no blocker exists.

A cycle should end with a repository-visible result, not only a plan.

## Knowledge classification

Classify statements before storing them:

- confirmed Fact;
- candidate;
- inference;
- assumption;
- recommendation;
- open question.

Only confirmed Facts belong in canonical Fact records. Inferences and recommendations belong in Reports or implementation guidance with clear labeling.

## Duplicate prevention

Before creating an entity:

- search by title;
- search by subject and predicate;
- search key phrases from the statement;
- inspect related View and Service records;
- compare meaning, not only wording.

When an existing Fact is too broad, prefer splitting or correcting it over adding a competing duplicate.

## Handling uncertainty

When official sources are incomplete or contradictory:

- do not manufacture certainty;
- preserve exact scope;
- prefer direct official documentation;
- record unresolved conflict in `STATE.md` risks or Report open questions;
- use candidate or inference status only if supported by schema and project policy;
- defer confirmation until sufficient Evidence exists.

## Mutable information

Pricing, quotas, interfaces, retention, APIs, permissions, and integrations can change.

For mutable claims:

- verify against current official sources;
- record `last_verified_at`;
- include applicable plan, edition, platform, and geography;
- avoid reusing stale numbers without re-verification.

## Repository mutation policy

Safe default:

- create a branch;
- keep changes scoped;
- preserve canonical semantics;
- validate before PR readiness;
- merge only green commits.

Never:

- commit secrets;
- use live user data without explicit authorization;
- weaken tests to hide invalid data;
- edit generated index rows manually;
- leave temporary diagnostics in final state;
- claim work was completed when only planned.

## Token-efficiency rules

- Prefer the index over directory scans.
- Prefer one relevant View over many raw packages.
- Reuse existing summaries only after checking canonical references.
- Store durable context in repository files, not repeated prompts.
- Keep PR bodies and `STATE.md` concise but complete.
- Avoid duplicating architecture instructions across documents; link to the owning document.

## Conflict resolution between files

Examples:

- If `ROADMAP.md` lists a future phase but `STATE.md` says maintenance, do not start the phase.
- If prose says the Index may be edited but validation treats it as generated, follow validation and `ARCHITECTURE.md`.
- If a Report conflicts with a confirmed Fact, treat the Fact and its Evidence as canonical and correct the Report.
- If `STATE.md` is stale after a merge, update it in a maintenance PR.

## Handoff discipline

Assume the next agent has no conversation context.

Before stopping:

- commit work;
- update current task and next task;
- record blockers with exact required user action;
- update PR status and validation result;
- remove private or temporary dependencies;
- ensure commands and paths are reproducible.

## Completion discipline

Do not report success until the repository proves it.

Evidence of completion includes:

- expected files exist;
- schemas and links validate;
- tests pass;
- `INDEX.jsonl` is fresh when required;
- CI is green;
- PR state and merge status match the claim.

## Maintenance mode behavior

In maintenance mode, prioritize:

1. broken CI;
2. invalid references or schema drift;
3. source freshness for materially mutable Facts;
4. stale or duplicate PR cleanup;
5. documentation that reduces future agent ambiguity.

Do not expand product scope without explicit approval.
