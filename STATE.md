---
current_phase: "Phase 5"
project_status: "research_in_progress"
completed:
  - "Google Play Console Store Performance research"
  - "Google Play Console Statistics research"
  - "Google Play purchases and subscriptions research"
  - "Google Play Console Financial Reports research"
  - "Google Play Console Ratings & Reviews research"
  - "Google Play Console Android Vitals research"
  - "Google Play Console Final Consolidation"
  - "Google Search Console Analytics Research"
  - "Google AdMob Analytics Research"
  - "Firebase Analytics, Events, Integrations and Export Research"
current_task: "Google Analytics 4 Property, Data Streams, Identity, Reporting, API, Attribution and Consent Research"
next_tasks:
  - "Complete Phase 5 Google Analytics 4 Research"
  - "Prepare Phase 6 BigQuery Research"
blockers: []
active_package_writers:
  - "knowledge/evidence/ga4-foundation.yaml"
  - "knowledge/evidence/ga4-reporting-apis.yaml"
  - "knowledge/evidence/ga4-attribution-consent.yaml"
  - "knowledge/facts/ga4-foundation.yaml"
  - "knowledge/facts/ga4-reporting-apis.yaml"
  - "knowledge/facts/ga4-attribution-consent.yaml"
  - "views/ga4-analytics-flow.md"
  - "reports/ga4-analytics-phase-5.md"
known_risks:
  - "Google Analytics UI, reporting identity, attribution settings, quotas, retention, and privacy controls can change"
  - "Firebase Analytics and GA4 share the same measurement model and must not be duplicated as separate event systems"
  - "web-to-app attribution through Google Play may not preserve a deterministic user-level identifier"
  - "Measurement Protocol events may have attribution and identity limitations"
  - "thresholding, consent mode, Google signals, and modeled data can change report completeness"
  - "BigQuery export schema and streaming-versus-daily behavior require separate confirmation"
  - "cross-service joins can be aggregate-only where no shared stable identifier exists"
last_updated: "2026-07-13"
---