---
id: "REPORT-01KXBVE31A3VE15VZ3P4SWJ4D2"
title: "Google AdMob Analytics Phase 3"
research_question: "Which AdMob delivery, monetization, reporting, API, integration, retention, and revenue-boundary capabilities are officially documented?"
created_at: "2026-07-12"
as_of: "2026-07-12"
author: "google-analytics-knowledge-project"
status: "issued"
fact_ids:
  - "FACT-01KXBTRX585VAD6212TWGBDEAV"
  - "FACT-01KXBTRX584XSBE8M5A2KQ6YTJ"
  - "FACT-01KXBTRX58J5V1B6Q0BBZCC0HQ"
  - "FACT-01KXBTRX58N86840WF10ZFPP4G"
  - "FACT-01KXBTRX581KSHPJZFPXKMK4AN"
  - "FACT-01KXBTRX58RYJJ878ADHRPMQ55"
  - "FACT-01KXBTRX58R1QRSEC9Q447AKS6"
  - "FACT-01KXBTRX58FNXF8BXFA963MW2G"
  - "FACT-01KXBTRX58N24R1RDGH5SEMF37"
  - "FACT-01KXBTRX58FM09B964PV2HTNNK"
  - "FACT-01KXBTRX58ZAJ8CHMW3KPVM8KF"
  - "FACT-01KXBTRX593NQD36RS3GAWHB4W"
  - "FACT-01KXBTRX5996C3ATVK1DFCB6D2"
  - "FACT-01KXBTRX597D2V9THGMSSZFV0X"
  - "FACT-01KXBV137J5Q8XSWW9XNTQ4FS7"
  - "FACT-01KXBVE318EKJ7RMCMAMM653K2"
  - "FACT-01KXBVE318WSX8S3PQZMJCS13A"
  - "FACT-01KXBVE3191DC3JP1FYKZ51FBN"
  - "FACT-01KXBVE319Y123F05C3EVEV3X8"
  - "FACT-01KXBVE31915MHVEW3ME7X84PD"
  - "FACT-01KXBVE319D0BP3NE3NQRG4X8W"
  - "FACT-01KXBVE319XKR911APSDS8BGJB"
  - "FACT-01KXBVE319HVDK3EM6ZVQJW2EE"
  - "FACT-01KXBVE319MZFN5YJKYF7YAC8Z"
  - "FACT-01KXBVE319CBH3ZZY1ZBC3G8FH"
  - "FACT-01KXBVE319YXP6V231KXVGKS2J"
  - "FACT-01KXBVE319QBH7DKG7JYEP9MRM"
  - "FACT-01KXBVE319MMG4GRCHS739QB3B"
  - "FACT-01KXBVE3199027110RBQ4AACHR"
evidence_ids:
  - "EVID-01KXBTRX58TCTDT9CSNVGQ8SVB"
  - "EVID-01KXBTRX585YZ1RWP31DR7MZ5J"
  - "EVID-01KXBTRX58GVR7MM4KPGKGAT1B"
  - "EVID-01KXBTRX58HQEWM0JGQQYD4JB3"
  - "EVID-01KXBTRX586XH4G3FRTG5YRSR1"
  - "EVID-01KXBTRX58MY1F0FR1VWWTYRM5"
  - "EVID-01KXBTRX58Q6816KR0JFC0DCS2"
  - "EVID-01KXBTRX58AYXF33YXGTWSNQZ4"
  - "EVID-01KXBVE317PJ52HGV4C6TG90V1"
  - "EVID-01KXBVE317Q439T05ZESFGF7JR"
  - "EVID-01KXBVE317XQ6W0Z9SWF2FRB5N"
  - "EVID-01KXBVE317BH9F6ZA4FMSJH21D"
  - "EVID-01KXBVE31863MJYJXKNR7NEYT1"
  - "EVID-01KXBVE318F0N3NNZP73YXVQ72"
  - "EVID-01KXBVE318TJ1VXBZ6133MJ12F"
  - "EVID-01KXBVE318J8YWAJ34RCWNVBJ6"
concept_ids: []
service_ids:
  - "SERVICE-01KXB0H9ZMWZPRWF59R76WVCJN"
  - "SERVICE-01KXB0H9ZMDHP3XY94QKJ681CN"
method: "Official Google documentation discovery, granular Evidence capture, atomic Fact extraction, channel and grain separation, integration-boundary review, and automated repository validation."
limitations: "No live AdMob account, credentials, API calls, mediation configuration, payment profile, real ad traffic, or user data were used. Exact payment schedules, finalized-earnings schemas, invalid-traffic calculations, and complete metric compatibility were not established."
---

# Summary

Phase 3 models AdMob as an advertising-delivery and monetization reporting source. Its core route is
ad request → matched request → impression → optional click → estimated earnings. Network and
mediation reports have distinct scopes, while Firebase linkage adds analytics-derived user metrics.

# Official evidence coverage

Sixteen granular Evidence records cover the official Reporting API, metrics and dimensions,
network and mediation reports, OAuth, quotas, ad units and formats, Firebase linkage,
impression-level revenue, report freshness, exports, and retention.

# Delivery metrics

Ad requests, matched requests, impressions, and clicks are distinct counts. Match rate uses matched
requests over ad requests. Show rate uses impressions over matched requests. Impression CTR uses
clicks over impressions.

# Monetization metrics

Estimated earnings are a mutable reporting value. Impression RPM is estimated earnings per thousand
impressions and corresponds to eCPM terminology in the UI. Estimated earnings can be adjusted before
payment and therefore must not be treated as a finalized payout amount.

# Reporting channels

The API supports network and mediation reports, dimensions, filters, OAuth-based access, a documented
request quota, and a fixed row limit with truncation. CSV is a separate UI export route. Reports
without dimensions have account grain.

# Inventory and formats

An ad unit is the in-app container responsible for requesting and displaying ads. Supported formats
include banner, interstitial, rewarded, rewarded interstitial, native, and app open.

# Firebase integration

Linking an AdMob app to Firebase and integrating Google Analytics for Firebase enables sessions,
active users, and other user metrics. This does not convert AdMob request or impression counts into
user metrics; the grains remain distinct.

# Impression-level revenue

The Mobile Ads SDK can emit a paid-event callback at impression grain. The callback includes a USD
revenue value and an explicit precision classification. With the documented Firebase integration,
this revenue can flow into the application analytics layer.

# Freshness and retention

AdMob reporting is delayed and recent values may be revised. User Activity retention is materially
shorter than Ads Activity retention, so historical architecture must account for the report family.

# Measurement boundary

AdMob directly describes ad delivery and estimated monetization. It does not, by itself, establish
marketing-source attribution, first-open attribution, a unified cross-service user identity, or a
finalized payment record.

# Key distinctions

- ad request ≠ matched request;
- matched request ≠ impression;
- impression ≠ click;
- impression CTR ≠ match rate ≠ show rate;
- network report ≠ mediation report;
- delivery metric ≠ analytics-derived user metric;
- aggregated estimated earnings ≠ impression-level callback value;
- estimated earnings ≠ finalized payment.

# Coverage

Covered: core delivery metrics and formulas, network and mediation report scope, API grain and
limits, OAuth scope, quota, ad units and formats, Firebase user metrics, impression-level revenue,
CSV availability, freshness, and major retention windows.

Partially covered: dimension/metric compatibility, third-party mediation freshness, user-level
monetization metrics, and payment reconciliation.

# Open questions

- exact finalized-earnings and payment-report schema;
- exact invalid-traffic adjustment methodology;
- complete compatibility matrix for every dimension and metric;
- direct BigQuery export boundary for AdMob account reporting;
- relationship between SDK impression revenue and later finalized financial records;
- consent-state effects on report completeness and user metrics.

# Next phase

The next service is Firebase. Its research should close the app-analytics side of first open,
sessions, events, audiences, user properties, AdMob-linked revenue, and BigQuery export boundaries.
