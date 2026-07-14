# Repository Style Guide

## General language

- Canonical entity content is written in clear English unless a future scope explicitly requires another language.
- Use direct, testable statements.
- Avoid marketing language, vague qualifiers, and unsupported certainty.
- Prefer full product names on first use and stable abbreviations afterward.

## File naming

Use lowercase kebab-case for production package and projection file names.

Examples:

```text
knowledge/evidence/ga4-reporting-surfaces.yaml
knowledge/facts/bigquery-ga4-export-schema.yaml
views/google-analytics-4-flow.md
reports/bigquery-analytics-phase-6.md
```

Root engineering documents use uppercase conventional names such as `ARCHITECTURE.md`.

## IDs

IDs use the format:

```text
<TYPE>-<ULID>
```

Examples:

```text
FACT-01K...
EVID-01K...
CONCEPT-01K...
SERVICE-01K...
VIEW-01K...
REPORT-01K...
```

Generate IDs with `scripts.common.generate_id()`. Never create patterned or sequential IDs manually.

## Dates

Use ISO 8601 calendar dates:

```text
2026-07-14
```

Use explicit dates rather than relative phrases in canonical records.

## YAML style

- Use UTF-8.
- Use two-space indentation.
- Prefer readable multi-line records.
- Quote strings when ambiguity is possible.
- Do not use anchors, aliases, merge keys, or custom tags.
- Keep package-level metadata at the top.
- Keep records under `records`.
- Keep fields in a consistent order matching nearby production files and schemas.

Recommended Fact field order:

```yaml
- id:
  title:
  statement:
  type:
  subject:
  predicate:
  object:
  scope:
  status:
  confidence:
  evidence_ids:
  concept_ids:
  service_ids:
  owner:
  created_at:
  last_verified_at:
```

Omit optional fields only when allowed by schema and genuinely not applicable.

## Fact style

### Atomicity

A Fact must contain one claim that can be independently verified and updated.

Good:

> BigQuery time travel defaults to seven days.

Bad:

> BigQuery has seven-day time travel, a fail-safe period, snapshots, and low-cost storage.

The bad example combines multiple independently changing claims.

### Statement wording

- Begin with the subject or clearly identify it.
- Use present tense for current product behavior.
- Include plan, platform, geography, or channel scope when relevant.
- Avoid “always” and “never” unless directly supported and properly scoped.
- Do not include citations or URLs in the statement.
- Do not include recommendations in confirmed Facts.

### Subject, predicate, object

Use stable, machine-readable phrasing.

Good:

```yaml
subject: "BigQuery time travel"
predicate: "default_window"
object: "7 days"
```

Avoid predicates that merely repeat prose or contain full sentences.

### Scope

Scope should carry conditions needed to interpret the claim, such as:

- product surface;
- plan or edition;
- platform;
- geography;
- verified date;
- channel.

Do not use scope as a dumping ground for unrelated notes.

## Evidence style

Evidence summaries describe what the official source directly supports.

Good:

> Official documentation defines the dataset naming pattern and daily table lifecycle.

Bad:

> This proves BigQuery is the best source for all analytics reporting.

Evidence must not contain analysis, recommendation, or conclusions beyond the source.

Use `primary_authoritative` for official first-party documentation when appropriate. Use directness values consistently with existing schema.

## Concept style

Concept definitions should be:

- stable;
- reusable;
- service-independent where practical;
- free of operational limits that belong in Facts.

Do not create a Concept merely to mirror every topic or file name.

## Service style

Service records describe identity and boundaries. They should not repeat detailed Fact statements.

Use Services to answer:

- what product is this;
- who publishes it;
- what broad analytical role it has;
- what it is not.

## View style

A View must include valid front matter and a focused question.

Body guidance:

- start with a concise route or flow;
- organize selected knowledge in reading order;
- explain boundaries and distinctions;
- avoid unsupported numeric claims;
- avoid turning the View into a second Report.

## Report style

A Report is dated analysis.

Required characteristics:

- clear research question;
- method and limitations;
- selected entity references in front matter;
- summary of findings;
- distinctions and open questions;
- next phase or maintenance implication.

Use Reports for synthesis, not as the only location of a claim.

## Markdown style

- Use one H1 per document.
- Use sentence-case headings.
- Keep paragraphs short and explicit.
- Use fenced code blocks for commands, schemas, and flows.
- Prefer lists only when they improve scanning.
- Use tables sparingly because they are harder to edit and diff.
- Use repository-relative file references in prose when useful.
- Avoid raw external links in canonical analysis when an Evidence record should own the source.

## Commands

Commands should be copyable and run from repository root unless stated otherwise.

```bash
python scripts/validate_knowledge.py
```

Do not use pseudo-commands that cannot run.

## Naming consistency

Use these preferred terms:

- `Evidence`, not “evidences”;
- `Fact`, not “fact item”;
- `View`, not “dashboard” unless describing a product dashboard;
- `Report`, not “research note” for validated Report entities;
- `key event` for current GA4 terminology, while preserving source-specific historical terms where necessary;
- `Google Analytics 4` or `GA4` consistently;
- `BigQuery`, not “Big Query”.

## Cross-reference style

Reference stable IDs in structured fields. In prose, prefer file names or entity names when the ID would reduce readability.

Do not create dangling IDs. All references must pass validation.

## Package size

- Prefer 20–80 records per package when practical.
- Hard maximum: 100 records.
- Prefer package size below 96 KiB.
- Never exceed 128 KiB.

Split by coherent topic, not arbitrary record count alone.

## Prohibited patterns

- manually edited `INDEX.jsonl`;
- handcrafted sequential IDs;
- confirmed Facts without official Evidence;
- duplicate claims with cosmetic wording changes;
- recommendations stored as confirmed Facts;
- unsupported prose in Views or Reports;
- reverse Evidence ownership lists;
- YAML anchors or unsafe tags;
- temporary diagnostics committed in final PR state;
- tests weakened to hide invalid production data.
