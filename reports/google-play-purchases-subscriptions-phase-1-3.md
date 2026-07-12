---
id: "REPORT-01KXBBGJPAFFZTW2ZYZB42KJ53"
title: "Google Play purchases and subscriptions Phase 1.3"
research_question: "Which Google Play purchase, subscription, order, notification, entitlement, and operational states are officially documented?"
created_at: "2026-07-12"
as_of: "2026-07-12"
author: "google-analytics-knowledge-project"
status: "issued"
fact_ids:
  - "FACT-01KXBBGJPAWH99D3MFXFEV1R11"
  - "FACT-01KXBBGJPAH29Z4BSQXPAHMR8Y"
  - "FACT-01KXBBGJPAENY40QDGQNYKV1X5"
  - "FACT-01KXBBGJPA1NA5GSVCHW6F2Y8N"
  - "FACT-01KXBBGJPA1CA6SRESDQA7W40F"
  - "FACT-01KXBBGJPA33298JXFDJYK2EH7"
  - "FACT-01KXBBGJPAC6FWS3MGSJZBG5QR"
  - "FACT-01KXBBGJPAPWS38GPGJ75YQFW5"
  - "FACT-01KXBBGJPAXK2MJY4NGK5914CJ"
  - "FACT-01KXBBGJPA9W4W4M1DMV82V507"
  - "FACT-01KXBBGJPAZCCHW8NPA1FW2A0S"
  - "FACT-01KXBBGJPAHHX285NTW7WS0FQ1"
  - "FACT-01KXBBGJPAYJDJPSDYFZ6NN6F5"
  - "FACT-01KXBBGJPACSS3S9EM65MD34MR"
  - "FACT-01KXBBGJPAQNK0NGYS5BPA1J9G"
  - "FACT-01KXBBXHHYPNEGBH3B1R3J3ZT3"
  - "FACT-01KXBBXHHY6VPDFQQG327WW7A1"
evidence_ids:
  - "EVID-01KXBBGJPAVWM4WKZT4HRJHA5F"
  - "EVID-01KXBBGJPA40FGZGJFK1QVH682"
  - "EVID-01KXBBGJPAJ8NTN4YN8WGV4MKD"
  - "EVID-01KXBBGJPABSRPY8YXKZJ338XC"
  - "EVID-01KXBBGJPA0YQ95C1KG9D62809"
  - "EVID-01KXBBGJPAKY4PN45BTF7KYMVF"
  - "EVID-01KXBBGJPAHGEXHR3YZ32FKH2T"
  - "EVID-01KXBBGJPAC427WX7FWN3HKEKE"
  - "EVID-01KXBBGJPATB1649R985N2Z78D"
  - "EVID-01KXBBGJPAJRERFV52RGJ2JEPC"
  - "EVID-01KXBBGJPAFVWF6V9FSYB5Z2PV"
  - "EVID-01KXBBGJPAXNEKPG52JMX6CYSN"
  - "EVID-01KXBBGJPA6SM3JMMPS74ZS7JT"
  - "EVID-01KXBBGJPA65Y1CN9BNRPX0V3Y"
  - "EVID-01KXBBXHHY7ARZNN52WKGRXACE"
concept_ids:
  - "CONCEPT-01KXB0H9ZM8Q0EGP8QRMF2CAD7"
  - "CONCEPT-01KXB0H9ZM40HGECRYWM7VSPCM"
  - "CONCEPT-01KXB0H9ZMPHJCZMXVQTC5AMX0"
  - "CONCEPT-01KXB0H9ZMX4S975N077EGM94N"
  - "CONCEPT-01KXB0H9ZMY0Z31MBFPCDF5Y3Q"
  - "CONCEPT-01KXB0H9ZMXPT1ZMXS689KRCTK"
  - "CONCEPT-01KXB0H9ZMBYM231E33WXJADZ4"
service_ids: ["SERVICE-01KXB0H9ZM3Z8V674FKJP8T657"]
method: "Official source discovery, section-level Evidence mapping, candidate extraction, API-version review, lifecycle and entitlement review, then validation."
limitations: "Financial accounting, payout, tax, invoices, production Pub/Sub, and external payment systems were not researched."
---

# Scope and sources

This dated report covers operational Google Play Billing purchases, subscriptions, orders, voided
purchases, Android Publisher API v3 resources, and RTDN. Source details live in Evidence.

# Established lifecycle routes

- One-time processing: `FACT-01KXBBGJPAWH99D3MFXFEV1R11`, `FACT-01KXBBGJPAENY40QDGQNYKV1X5`, `FACT-01KXBBGJPA1NA5GSVCHW6F2Y8N`
- Subscription recovery: `FACT-01KXBBGJPAC6FWS3MGSJZBG5QR`, `FACT-01KXBBGJPAPWS38GPGJ75YQFW5`
- Refund/revoke: `FACT-01KXBBGJPA9W4W4M1DMV82V507`, `FACT-01KXBBGJPAZCCHW8NPA1FW2A0S`
- RTDN/API: `FACT-01KXBBGJPAYJDJPSDYFZ6NN6F5`, `FACT-01KXBBGJPACSS3S9EM65MD34MR`

# Operational, analytical, and financial boundary

Operational purchase resources expose current lifecycle metadata. They are not a replacement for
analytical time-series or financial accounting. Earnings and payout definitions remain open for
Phase 1.4.

# Uncertainties and next phase

Detailed prepaid-plan transitions, all replacement modes, RTDN ordering guarantees, accounting
revenue, earnings, payout, taxes, and invoice semantics remain outside confirmed coverage. The
recommended next phase is Phase 1.4 — Google Play Console Financial Reports Research.
