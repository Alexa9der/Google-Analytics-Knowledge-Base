---
id: "REPORT-01KXCG0000M8PZWH73A407E666"
title: "Google Play financial reports Phase 1.4"
research_question: "Which Google Play financial reports, fields, delivery methods, timing rules, and operational-to-payout boundaries are officially documented?"
created_at: "2026-07-12"
as_of: "2026-07-12"
author: "google-analytics-knowledge-project"
status: "issued"
fact_ids:
  - "FACT-01KXCG000013N1T6EXAMBGTPZX"
  - "FACT-01KXCG0000KZ9390W10K4476SR"
  - "FACT-01KXCG0000FH55YWCE0M3SD48G"
  - "FACT-01KXCG00002KEM1K4MQAHE7G03"
  - "FACT-01KXCG0000B7X3JW5W79PAXYY0"
  - "FACT-01KXCG0000SJB0KKC02FC2GG6Y"
  - "FACT-01KXCG0000616C2NW6SP0BE2SM"
  - "FACT-01KXCG0000HGPBS40D6Z4EEZ5H"
  - "FACT-01KXCG0000K298VW7FX9KGFVD6"
  - "FACT-01KXCG0000M1H6ZFD089YQNT8C"
  - "FACT-01KXCG00009AV15CT6GFGATQ7R"
  - "FACT-01KXCG0000GPJC0TMMF6C6AYZM"
  - "FACT-01KXCG0000N3NVFJ3Z3SBKRXQD"
  - "FACT-01KXCG0000ZJQ7M6TN7XJ1E35Q"
  - "FACT-01KXCG00000SF6RWR5ASKM5RX3"
  - "FACT-01KXCG0000ZATKTCCQ08E46PMB"
  - "FACT-01KXCG0000GJT5J4K6P21FMHSN"
  - "FACT-01KXCG0000YN8JFPYF7HZ6EYH1"
  - "FACT-01KXCG000045JMPJFM9GZXZ0MX"
  - "FACT-01KXCG0000CV0KRD5G9E5M5BRW"
  - "FACT-01KXCG0000M067JK3FV7DT0FWK"
  - "FACT-01KXCG00006RV5V0T8ENCVC01Q"
  - "FACT-01KXCG0000FQ9QTJHW079MCQWV"
  - "FACT-01KXCG00005DFFDS3DH3V4C8WW"
  - "FACT-01KXCG0000T4EWMV5GZM113RWP"
evidence_ids:
  - "EVID-01KXCG0000AVKG3SC9H512BEVH"
  - "EVID-01KXCG0000CD2R2P5ZDBP3VH5A"
  - "EVID-01KXCG0000N1TD1W60DTR5MF1C"
  - "EVID-01KXCG0000CHJE5PKFN1QCY7XS"
  - "EVID-01KXCG0000WW5DFYWVF1CXSJBC"
  - "EVID-01KXCG0000GAG2F8FFVN0CK1BR"
  - "EVID-01KXCG0000CG27Q5DK2AEYFHW1"
  - "EVID-01KXCG0000HM6F22NB6DRMM78G"
  - "EVID-01KXCG0000702J94Q0V5461HEM"
  - "EVID-01KXCG0000SH0VH2A3J5243KZC"
  - "EVID-01KXCG00006EA2NKD4YNTKRKWF"
  - "EVID-01KXCG0000XPXET83JPAFYDRQB"
concept_ids:
  - "CONCEPT-01KXB0H9ZM8Q0EGP8QRMF2CAD7"
  - "CONCEPT-01KXB0H9ZM40HGECRYWM7VSPCM"
  - "CONCEPT-01KXB0H9ZMPHJCZMXVQTC5AMX0"
  - "CONCEPT-01KXB0H9ZMXPT1ZMXS689KRCTK"
  - "CONCEPT-01KXB0H9ZM2J36209PV7RXPCD3"
  - "CONCEPT-01KXB0H9ZMB53TZPK3Q8N6XDVB"
  - "CONCEPT-01KXB0H9ZMBYM231E33WXJADZ4"
service_ids: ["SERVICE-01KXB0H9ZM3Z8V674FKJP8T657"]
method: "Official Google support-source discovery, section-level Evidence mapping, candidate extraction, atomic Fact review, Phase 1.3 boundary reconciliation, and repository validation."
limitations: "No account data, live API, tax or accounting advice, invoice analysis, bank operations, or non-Google-Play services were included. Payout schema, identifiers, currency mapping, history retention, and a dedicated financial-report API remain unconfirmed."
---

# Scope

This dated report covers Google Play financial reports, exports, field meanings, currencies, timing,
corrections, and the payout boundary. Canonical truth remains in Facts and Evidence.

# Official reports and established facts

The documented detailed inventory contains Estimated Sales and Earnings. Thirty-two new confirmed
Facts cover report scope, CSV and Cloud Storage delivery, publication lag, purpose, row grain,
identifiers, amount and currency fields, tax and fee fields, corrections, exclusions, and payout
timing.

# Estimated Sales

This lower-latency analytical report covers apps, in-app products, and subscriptions. Buyer amounts
do not deduct taxes or Google fees and are not converted to payout currency. It updates daily, but
transactions may lag. UTC is explicit for charge fields. Google does not recommend it for accounting.

# Earnings

This monthly prior-period report has transaction-type grain and original plus converted amounts.
It includes charge, Google fee, tax, refund/rebill, and adjustment types. Full and partial refunds
are distinguished. Chargebacks are excluded, and corrected transactions may arrive in an adjustment
file.

# Taxes, fees, and adjustments

Only report semantics were captured: Tax Type, fee transaction entries, Service Fee percentage, and
Fee Description. No jurisdictional interpretation was made. A transaction-varying percentage does
not support a universal rate. Refund, chargeback, revoke, cancellation, and adjustment remain
distinct.

# Payouts and boundaries

Earnings publication precedes payout by several weeks. Monthly activity is generally paid around
the following month's fifteenth, subject to timing variation. Operational purchase records,
Estimated Sales, Earnings, and final amounts are separate stages. The Phase 1.3 boundary candidate
was superseded by narrower confirmed relationships.

# Currency, time, access, and exports

Estimated Sales uses buyer currency; Earnings exposes buyer and merchant amounts plus conversion
rate. CSV download and private Cloud Storage delivery are documented. Storage delivery is not proof
of a financial-report API or direct BigQuery export. Field-specific timezone context must be kept
with each date instead of generalized across reports.

# Uncertainties, coverage, and next phase

A standalone payout schema, payout ID/status, exact payout-currency mapping, history retention,
direct API/BigQuery delivery, and invoice equivalence remain unconfirmed. Any legal or accounting
conclusion requires legal or accounting review. The recommended next phase is Phase 1.5 — Google
Play Console Ratings & Reviews Research; it has not been started.
