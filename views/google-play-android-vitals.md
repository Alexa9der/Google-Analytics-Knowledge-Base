---
id: "VIEW-01KXCJ00000V3GHP10K0YXKN28"
title: "Google Play Android Vitals route"
question: "How should Android Vitals quality signals, metrics, thresholds, dimensions, API access, and export boundaries be traversed?"
audience: "Android quality analysts, researchers, and AI agents"
owner: "knowledge-architecture"
status: "published"
entity_ids:
  - "CONCEPT-01KXCJ0000B5CS7C0SQTSBNN67"
  - "CONCEPT-01KXCJ00008ZXK47F56XZ1CEDH"
  - "CONCEPT-01KXCJ0000JM9GY1DBQTT3MP39"
  - "CONCEPT-01KXCJ0000KEH4JX1R4FZYM258"
  - "CONCEPT-01KXCJ0000KSD4RT927QDMGA11"
  - "CONCEPT-01KXCJ0000JBFBH400BJGFBTSY"
  - "FACT-01KXCJ00008GBC4J6MA8JTCTGM"
  - "FACT-01KXCJ0000CSVYSYKPB5AZVKZY"
  - "FACT-01KXCJ00001MH36MQTXGBCDA7J"
  - "FACT-01KXCJ00001ZXTT11G9FQ7XRZ7"
  - "FACT-01KXCJ0000V5DR3HN8SSA55RPP"
  - "FACT-01KXCJ0000EB2AFGRSMWGCQME0"
  - "FACT-01KXCJ0000RRE0AW1QR09DXDS0"
  - "FACT-01KXCJ0000A8AVJMAXZTHB034P"
  - "FACT-01KXCJ000000QPF9FRABGMXT97"
reading_order:
  - "CONCEPT-01KXCJ0000B5CS7C0SQTSBNN67"
  - "FACT-01KXCJ00008GBC4J6MA8JTCTGM"
  - "CONCEPT-01KXCJ00008ZXK47F56XZ1CEDH"
  - "FACT-01KXCJ0000CSVYSYKPB5AZVKZY"
  - "CONCEPT-01KXCJ0000JM9GY1DBQTT3MP39"
  - "FACT-01KXCJ00001MH36MQTXGBCDA7J"
  - "CONCEPT-01KXCJ0000KEH4JX1R4FZYM258"
  - "FACT-01KXCJ00001ZXTT11G9FQ7XRZ7"
  - "CONCEPT-01KXCJ0000KSD4RT927QDMGA11"
  - "FACT-01KXCJ0000V5DR3HN8SSA55RPP"
  - "CONCEPT-01KXCJ0000JBFBH400BJGFBTSY"
  - "FACT-01KXCJ0000EB2AFGRSMWGCQME0"
  - "FACT-01KXCJ0000RRE0AW1QR09DXDS0"
  - "FACT-01KXCJ0000A8AVJMAXZTHB034P"
  - "FACT-01KXCJ000000QPF9FRABGMXT97"
filters: {service_id: "SERVICE-01KXB0H9ZM3Z8V674FKJP8T657", statuses: ["confirmed"]}
inclusion_criteria: "Include reviewed Android Vitals UI, core and supporting metrics, thresholds, dimensions, Reporting API, history, privacy, and export-boundary entities only."
updated_at: "2026-07-12"
---

# Reading route

Android Vitals → quality signals → crash → ANR → rendering → startup → battery → dimensions →
Reporting API → history and freshness → thresholds → export boundary.

# Limits

Keep crash separate from ANR and user-perceived rates separate from overall rates. Rendering and
startup use different events and denominators. UI retains 90 days; API exposes three years and its
own dimensions, timezone, pagination, and freshness metadata. Dedicated detailed crash/ANR bulk
downloads are retired. The conflicting official hot-start threshold remains open.
