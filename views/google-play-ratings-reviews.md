---
id: "VIEW-01KXCH0000S5VBRB13DC6ZJ298"
title: "Google Play ratings and reviews route"
question: "How should Google Play rating metrics, written reviews, replies, exports, API access, and tester feedback be traversed without conflating them?"
audience: "Product analysts, review operations researchers, and AI agents"
owner: "knowledge-architecture"
status: "published"
entity_ids:
  - "CONCEPT-01KXCH0000PN2PFDFBRFASGKGP"
  - "CONCEPT-01KXCH0000AKE3D1RV9RXAAKXW"
  - "CONCEPT-01KXCH00002HTN7PET65GS7FZM"
  - "CONCEPT-01KXCH0000YDZ4DAN41FZ1NFCM"
  - "CONCEPT-01KXCH0000PY0R0VTX3T5Z5SK7"
  - "FACT-01KXCH0000MQCHQ4310V1P7FFF"
  - "FACT-01KXCH0000CRY92P6BNCK1F7MR"
  - "FACT-01KXCH0000F6YDYDY2BNJ1KFXM"
  - "FACT-01KXCH0000QNYV3RKW0Q48R7GD"
  - "FACT-01KXCH0000SC3ZY64BXDKGHKGA"
  - "FACT-01KXCH0000H66NMDC81XJEDDN6"
  - "FACT-01KXCH0000F8Y79MG6Y8ZXG0A7"
  - "FACT-01KXCH000055DF9W9893YPFQES"
  - "FACT-01KXCH00007HS41ZGN9MJP49A8"
  - "FACT-01KXCH000071HNA6XBZ9YTJEZM"
  - "FACT-01KXCH0000DJQPHVQJKE5D7YP6"
  - "FACT-01KXCH0000MYJ8DPDG622HXT98"
reading_order:
  - "CONCEPT-01KXCH0000PN2PFDFBRFASGKGP"
  - "FACT-01KXCH0000MQCHQ4310V1P7FFF"
  - "FACT-01KXCH0000CRY92P6BNCK1F7MR"
  - "CONCEPT-01KXCH0000AKE3D1RV9RXAAKXW"
  - "FACT-01KXCH0000F6YDYDY2BNJ1KFXM"
  - "FACT-01KXCH0000QNYV3RKW0Q48R7GD"
  - "CONCEPT-01KXCH00002HTN7PET65GS7FZM"
  - "FACT-01KXCH0000SC3ZY64BXDKGHKGA"
  - "FACT-01KXCH0000H66NMDC81XJEDDN6"
  - "CONCEPT-01KXCH0000YDZ4DAN41FZ1NFCM"
  - "FACT-01KXCH0000F8Y79MG6Y8ZXG0A7"
  - "FACT-01KXCH000055DF9W9893YPFQES"
  - "FACT-01KXCH00007HS41ZGN9MJP49A8"
  - "FACT-01KXCH000071HNA6XBZ9YTJEZM"
  - "CONCEPT-01KXCH0000PY0R0VTX3T5Z5SK7"
  - "FACT-01KXCH0000DJQPHVQJKE5D7YP6"
  - "FACT-01KXCH0000MYJ8DPDG622HXT98"
filters: {service_id: "SERVICE-01KXB0H9ZM3Z8V674FKJP8T657", statuses: ["confirmed"]}
inclusion_criteria: "Include reviewed Google Play rating, written-review, reply, export, Reviews API, and tester-feedback entities; exclude review analysis and engagement definitions from other services."
updated_at: "2026-07-12"
---

# Reading route

Rating → aggregate rating metrics → rating distribution → breakdown dimensions → written review →
review metadata → developer response → UI / Reviews API / CSV boundary → private testing feedback.

# Scope and limitations

Use rating entities for scale values and aggregate metrics. Move to Review only when written comment
content exists. Treat display name as API metadata, not verified identity. API access is recent,
production-only, and comment-only; CSV supplies a separate historical export route. Tester feedback
is private and does not enter the public rating.

Firebase and GA4 engagement remain an open transition for later service phases; no engagement
meaning is imported here.
