---
title: "Firebase Phase 4 follow-up"
phase: 4
status: "follow-up"
updated_at: "2026-07-13"
---

# Firebase Phase 4 follow-up

PR #3 completed the Phase 4 Firebase research and was merged on 2026-07-12. A post-merge review identified two repository-integrity corrections:

1. BigQuery export facts reference the Looker Studio service ID and must use the canonical BigQuery service ID `SERVICE-01KXB0H9ZMCS60TJAYENWG55H2`.
2. The key-events and attribution fact/evidence packages contain patterned identifiers that must be regenerated with `scripts.common.generate_id()` and all references updated atomically.

The researched scope itself is complete for:

- Firebase Analytics event model;
- automatically collected, recommended, and custom events;
- event parameters and custom definitions;
- key events and prospective reporting behavior;
- attribution and user/session/event traffic-source scopes;
- Firebase-to-GA4 measurement boundary;
- Google Play purchase event handling;
- AdMob linking, user metrics, and impression-level ad revenue;
- BigQuery event-grain export and synchronization behavior.

## Remaining implementation work

The identifier regeneration must be executed from a repository checkout so the canonical generator and validation suite can run together. After regeneration, run the full repository validation suite and update the generated index before merging the corrective PR.
