---
id: "VIEW-01KXCK0000NEFR6APHQR4M9XTX"
title: "Google Play Console end-to-end funnel"
question: "Which Google Play Console entities form the researched acquisition-to-payout route, and where are the measurement and service boundaries?"
audience: "Analytics architects, researchers, and AI agents"
owner: "knowledge-architecture"
status: "published"
entity_ids:
  - "CONCEPT-01KXB0H9ZMR0V5MR51TCWN4AAP"
  - "CONCEPT-01KXB0H9ZM80395EP8SM7W6T0Z"
  - "CONCEPT-01KXB0H9ZMBPTYGA7SHR0K94VE"
  - "CONCEPT-01KXB0H9ZMX4S975N077EGM94N"
  - "CONCEPT-01KXB0H9ZM410EY10Q7A190K5X"
  - "CONCEPT-01KXB0H9ZMYRQ1M9SS0TJR22Z6"
  - "CONCEPT-01KXB0H9ZM8Q0EGP8QRMF2CAD7"
  - "CONCEPT-01KXB0H9ZM40HGECRYWM7VSPCM"
  - "CONCEPT-01KXB0H9ZMPHJCZMXVQTC5AMX0"
  - "CONCEPT-01KXCH0000PN2PFDFBRFASGKGP"
  - "CONCEPT-01KXCH00002HTN7PET65GS7FZM"
  - "CONCEPT-01KXCJ00008ZXK47F56XZ1CEDH"
  - "CONCEPT-01KXCJ0000JM9GY1DBQTT3MP39"
  - "FACT-01KXB1T830W2V9604Y3BQXC8VQ"
  - "FACT-01KXB1T830G58R2GC21G593MVP"
  - "FACT-01KXB8RT71S8JB2WCRR7NACD9Q"
  - "FACT-01KXB8RT71PQEA7HYS6D3MTEEQ"
  - "FACT-01KXBBGJPAWH99D3MFXFEV1R11"
  - "FACT-01KXBBGJPA1CA6SRESDQA7W40F"
  - "FACT-01KXCG0000M1H6ZFD089YQNT8C"
  - "FACT-01KXCG00005DFFDS3DH3V4C8WW"
  - "FACT-01KXCG0000T4EWMV5GZM113RWP"
  - "FACT-01KXBBGJPAZCCHW8NPA1FW2A0S"
  - "FACT-01KXBBGJPAHHX285NTW7WS0FQ1"
  - "FACT-01KXCH0000SC3ZY64BXDKGHKGA"
  - "FACT-01KXCJ0000CSVYSYKPB5AZVKZY"
  - "FACT-01KXCJ00001MH36MQTXGBCDA7J"
reading_order:
  - "CONCEPT-01KXB0H9ZMR0V5MR51TCWN4AAP"
  - "FACT-01KXB1T830W2V9604Y3BQXC8VQ"
  - "CONCEPT-01KXB0H9ZM80395EP8SM7W6T0Z"
  - "FACT-01KXB1T830G58R2GC21G593MVP"
  - "CONCEPT-01KXB0H9ZMBPTYGA7SHR0K94VE"
  - "FACT-01KXB8RT71S8JB2WCRR7NACD9Q"
  - "CONCEPT-01KXB0H9ZMX4S975N077EGM94N"
  - "CONCEPT-01KXB0H9ZM410EY10Q7A190K5X"
  - "CONCEPT-01KXB0H9ZMYRQ1M9SS0TJR22Z6"
  - "FACT-01KXB8RT71PQEA7HYS6D3MTEEQ"
  - "CONCEPT-01KXB0H9ZM8Q0EGP8QRMF2CAD7"
  - "FACT-01KXBBGJPAWH99D3MFXFEV1R11"
  - "CONCEPT-01KXB0H9ZM40HGECRYWM7VSPCM"
  - "FACT-01KXBBGJPA1CA6SRESDQA7W40F"
  - "FACT-01KXCG0000M1H6ZFD089YQNT8C"
  - "CONCEPT-01KXB0H9ZMPHJCZMXVQTC5AMX0"
  - "FACT-01KXCG00005DFFDS3DH3V4C8WW"
  - "FACT-01KXCG0000T4EWMV5GZM113RWP"
  - "FACT-01KXBBGJPAZCCHW8NPA1FW2A0S"
  - "FACT-01KXBBGJPAHHX285NTW7WS0FQ1"
  - "CONCEPT-01KXCH0000PN2PFDFBRFASGKGP"
  - "CONCEPT-01KXCH00002HTN7PET65GS7FZM"
  - "FACT-01KXCH0000SC3ZY64BXDKGHKGA"
  - "CONCEPT-01KXCJ00008ZXK47F56XZ1CEDH"
  - "FACT-01KXCJ0000CSVYSYKPB5AZVKZY"
  - "CONCEPT-01KXCJ0000JM9GY1DBQTT3MP39"
  - "FACT-01KXCJ00001MH36MQTXGBCDA7J"
filters: {service_id: "SERVICE-01KXB0H9ZM3Z8V674FKJP8T657", statuses: ["confirmed"]}
inclusion_criteria: "Include representative canonical entities for the researched Google Play Console funnel, downstream reputation and quality branches, and documented operational/financial boundaries."
updated_at: "2026-07-12"
---

# Main route

External-source boundary → store-listing visitor → acquisition → install-related observation →
user/device grains → first-open boundary → purchase/subscription → order linkage → Estimated Sales →
Earnings → payout schedule.

# Measurement and channel boundaries

- External click and web-session measurement precede the first supported Play Console visitor stage.
- Acquisition and install remain distinct; user and device routes branch before downstream events.
- First open is a transition to later app-analytics research, not a confirmed Play Console event route.
- Operational billing state joins orders through documented identifiers; it does not become settlement.
- Estimated Sales, Earnings, and payout are separate financial stages.

# Downstream branches

- Refund, revoke, and voided-purchase records branch from operational purchase/order handling.
- Rating and written review form a reputation branch, not an attribution continuation.
- Crash and ANR metrics form a technical-quality branch, not an attribution continuation.
- No entity in this route establishes individual-acquisition-to-payout attribution.
