---
id: "VIEW-01KXCG0000MRMCEMD2SGNF5C3R"
title: "Google Play financial flow route"
question: "How should Google Play purchase, sales, earnings, adjustment, and payout knowledge be traversed without conflating operational and financial records?"
audience: "Financial data analysts, researchers, and AI agents"
owner: "knowledge-architecture"
status: "published"
entity_ids:
  - "CONCEPT-01KXB0H9ZM8Q0EGP8QRMF2CAD7"
  - "CONCEPT-01KXB0H9ZMPHJCZMXVQTC5AMX0"
  - "CONCEPT-01KXB0H9ZMXPT1ZMXS689KRCTK"
  - "FACT-01KXCG00009AV15CT6GFGATQ7R"
  - "FACT-01KXCG0000SJB0KKC02FC2GG6Y"
  - "FACT-01KXCG0000616C2NW6SP0BE2SM"
  - "FACT-01KXCG0000M1H6ZFD089YQNT8C"
  - "FACT-01KXCG0000GPJC0TMMF6C6AYZM"
  - "FACT-01KXCG0000GJT5J4K6P21FMHSN"
  - "FACT-01KXCG0000FQ9QTJHW079MCQWV"
  - "FACT-01KXCG00000SF6RWR5ASKM5RX3"
  - "FACT-01KXCG00005DFFDS3DH3V4C8WW"
  - "FACT-01KXCG0000T4EWMV5GZM113RWP"
reading_order:
  - "CONCEPT-01KXB0H9ZM8Q0EGP8QRMF2CAD7"
  - "FACT-01KXCG00009AV15CT6GFGATQ7R"
  - "FACT-01KXCG0000SJB0KKC02FC2GG6Y"
  - "FACT-01KXCG0000616C2NW6SP0BE2SM"
  - "FACT-01KXCG0000M1H6ZFD089YQNT8C"
  - "CONCEPT-01KXB0H9ZMPHJCZMXVQTC5AMX0"
  - "FACT-01KXCG0000GPJC0TMMF6C6AYZM"
  - "FACT-01KXCG0000GJT5J4K6P21FMHSN"
  - "FACT-01KXCG0000FQ9QTJHW079MCQWV"
  - "FACT-01KXCG00000SF6RWR5ASKM5RX3"
  - "FACT-01KXCG00005DFFDS3DH3V4C8WW"
  - "FACT-01KXCG0000T4EWMV5GZM113RWP"
  - "CONCEPT-01KXB0H9ZMXPT1ZMXS689KRCTK"
filters: {service_id: "SERVICE-01KXB0H9ZM3Z8V674FKJP8T657", statuses: ["confirmed"]}
inclusion_criteria: "Include reviewed Google Play financial-report entities and the Phase 1.3 operational boundary; exclude accounting conclusions and future GA4, Firebase, or AdMob mappings."
updated_at: "2026-07-12"
---

# Reading route

Purchase → Order → Estimated sale → buyer amount → documented tax and fee entries → Earnings
transaction → correction or adjustment → payout schedule.

# Scope and limits

Start with the operational purchase boundary, then use Estimated Sales for low-latency analysis and
Earnings for transaction-type financial reporting. Report rows, earnings amounts, and bank payouts
are separate stages. This route does not establish invoice equivalence, country-specific tax
treatment, a universal fee rate, or a direct financial-report API. GA4, Firebase, and AdMob remain
future service phases.
