---
id: "VIEW-01KXESQ2S1BYWE3C60E0F2J1RZ"
title: "BigQuery Analytics Foundation"
question: "How does BigQuery receive GA4 event exports, preserve their schema and lifecycle, reconstruct analytical entities, control cost and access, and publish governed downstream datasets?"
audience: "Analytics engineers, data architects, researchers, and AI agents"
owner: "knowledge-architecture"
status: "published"
entity_ids:
  - "CONCEPT-01KXB0H9ZMY0Z31MBFPCDF5Y3Q"
  - "CONCEPT-01KXB0H9ZMX4S975N077EGM94N"
  - "CONCEPT-01KXB0H9ZMXAWK23YMRYR5Q133"
  - "CONCEPT-01KXB0H9ZMXPT1ZMXS689KRCTK"
  - "CONCEPT-01KXB0H9ZMBYM231E33WXJADZ4"
  - "CONCEPT-01KXB0H9ZMQ30G90BCGR86CB87"
  - "FACT-01KXEFF7S3EZ2TCPGHE81A9C5E"
  - "FACT-01KXEFF7S362V31VDK3QPY1V3R"
  - "FACT-01KXEFF7S3K6QQHA5D0AKD7473"
  - "FACT-01KXEFF7S37H0N17XFQTN1XN6K"
  - "FACT-01KXEFF7S34QHVEG6ATEHZ9ZX3"
  - "FACT-01KXEFF7S3DR7E2BXME64D4P25"
  - "FACT-01KXEFF7S3XTD4QRFCTE8KWWKR"
  - "FACT-01KXEGYNBQ25QF7H687WZDXF2W"
  - "FACT-01KXEGYNBQ787Y11W6X18H4X4P"
  - "FACT-01KXEGYNBQCQEWSZQQYVYK40RN"
  - "FACT-01KXEGYNBQE08ASRMF7ED43A2M"
  - "FACT-01KXEGYNBQX444M2RB0EF476YZ"
  - "FACT-01KXEGYNBRVJF5F9HTW2RW0PNH"
  - "FACT-01KXEGYNBRRP57Q7FQPSR4C0QB"
  - "FACT-01KXEGYNBRHWNV0VP68ZVQT4A8"
  - "FACT-01KXEGYNBRNHVB6VF65C35VGKJ"
  - "FACT-01KXEGYNBRWYHSZJ6ZRB1H4041"
  - "FACT-01KXEJ170CSXY2WMRFXGB10M7F"
  - "FACT-01KXEJ170CR284GRHDYZR7VR4V"
  - "FACT-01KXEJ170CS126HM462EYHF8AB"
  - "FACT-01KXEJ170CSSWCC6J7THKNBPA7"
  - "FACT-01KXEJ170CD9FSDKYJNWTP50Y0"
  - "FACT-01KXEJ170CP12BJRY2P8DZQTGB"
  - "FACT-01KXEK8HMTD5TCYB99RWZ4J3V8"
  - "FACT-01KXEK8HMTG7ANV8X29TFCF95M"
  - "FACT-01KXEK8HMTEKVC2MCWDPBW80AA"
  - "FACT-01KXEK8HMTWQJ8ASVYAZPFRBD4"
  - "FACT-01KXEK8HMTD0NRMR6P1MNR6D2D"
  - "FACT-01KXEK8HMTKR5DS7JHK31WRX8P"
  - "FACT-01KXEK8HMTMM6NCNA2F21WMJZG"
  - "FACT-01KXEK8HMTB26495TQXF0NS0ED"
  - "FACT-01KXEK8HMTW35NKVY2EMQC6DQD"
  - "FACT-01KXEK8HMT8DZ5YJXBH61WFC6Z"
  - "FACT-01KXEK8HMTG06PQ3G1VDPGDGVK"
  - "FACT-01KXEK8HMT3NY5FGY6MTG7VSHN"
  - "FACT-01KXEK8HMT7K49B6Q16W6Y4YN7"
reading_order:
  - "FACT-01KXEFF7S3EZ2TCPGHE81A9C5E"
  - "FACT-01KXEFF7S362V31VDK3QPY1V3R"
  - "FACT-01KXEFF7S3K6QQHA5D0AKD7473"
  - "FACT-01KXEFF7S37H0N17XFQTN1XN6K"
  - "FACT-01KXEFF7S34QHVEG6ATEHZ9ZX3"
  - "FACT-01KXEFF7S3DR7E2BXME64D4P25"
  - "FACT-01KXEFF7S3XTD4QRFCTE8KWWKR"
  - "FACT-01KXEGYNBQ25QF7H687WZDXF2W"
  - "FACT-01KXEGYNBQ787Y11W6X18H4X4P"
  - "FACT-01KXEGYNBQCQEWSZQQYVYK40RN"
  - "FACT-01KXEGYNBQE08ASRMF7ED43A2M"
  - "FACT-01KXEGYNBQX444M2RB0EF476YZ"
  - "FACT-01KXEGYNBRVJF5F9HTW2RW0PNH"
  - "FACT-01KXEGYNBRRP57Q7FQPSR4C0QB"
  - "FACT-01KXEGYNBRHWNV0VP68ZVQT4A8"
  - "FACT-01KXEGYNBRNHVB6VF65C35VGKJ"
  - "FACT-01KXEGYNBRWYHSZJ6ZRB1H4041"
  - "FACT-01KXEJ170CSXY2WMRFXGB10M7F"
  - "FACT-01KXEJ170CR284GRHDYZR7VR4V"
  - "FACT-01KXEJ170CS126HM462EYHF8AB"
  - "FACT-01KXEJ170CSSWCC6J7THKNBPA7"
  - "FACT-01KXEJ170CD9FSDKYJNWTP50Y0"
  - "FACT-01KXEJ170CP12BJRY2P8DZQTGB"
  - "FACT-01KXEK8HMTD5TCYB99RWZ4J3V8"
  - "FACT-01KXEK8HMTG7ANV8X29TFCF95M"
  - "FACT-01KXEK8HMTEKVC2MCWDPBW80AA"
  - "FACT-01KXEK8HMTWQJ8ASVYAZPFRBD4"
  - "FACT-01KXEK8HMTD0NRMR6P1MNR6D2D"
  - "FACT-01KXEK8HMTKR5DS7JHK31WRX8P"
  - "FACT-01KXEK8HMTMM6NCNA2F21WMJZG"
  - "FACT-01KXEK8HMTB26495TQXF0NS0ED"
  - "FACT-01KXEK8HMTW35NKVY2EMQC6DQD"
  - "FACT-01KXEK8HMT8DZ5YJXBH61WFC6Z"
  - "FACT-01KXEK8HMTG06PQ3G1VDPGDGVK"
  - "FACT-01KXEK8HMT3NY5FGY6MTG7VSHN"
  - "FACT-01KXEK8HMT7K49B6Q16W6Y4YN7"
filters: {service_id: "SERVICE-01KXB0H9ZMCS60TJAYENWG55H2", statuses: ["confirmed"]}
inclusion_criteria: "Include confirmed BigQuery architecture, GA4 export lifecycle and schema, canonical SQL reconstruction, retention, optimization, transformation and governance boundaries."
updated_at: "2026-07-14"
---

# Primary flow

GA4 property → `analytics_<property_id>` dataset → daily and optional intraday event tables →
query-time extraction and reconstruction → governed transformation layer → downstream marts and reports.

# Platform and resource boundary

BigQuery is a managed serverless analytical platform with independent storage and compute. Datasets
belong to Google Cloud projects; tables and views belong to datasets. Dataset location is selected at
creation, and one query can reference only datasets in a compatible location.

# GA4 export lifecycle

Daily export writes `events_YYYYMMDD`. Streaming export writes temporary
`events_intraday_YYYYMMDD`, which is replaced after the complete daily table is available. Daily
tables can change for up to three days because of late-arriving events, so recent-period pipelines
must support restatement rather than treating yesterday as immutable.

# Schema and grain

One exported row represents an event. Repeated records such as `event_params`, `user_properties` and
`items` require explicit `UNNEST` logic. Ecommerce therefore has at least event, transaction and item
grains. Event-collected traffic-source values are distinct from attributed session traffic-source
records, and consent-state fields describe the event rather than proving complete user identity.

# Analytical reconstruction

Date-sharded tables are limited with `_TABLE_SUFFIX`. Event totals count event rows. User totals depend
on the selected identifier. Sessions commonly combine `user_pseudo_id` and `ga_session_id`.
Transactions should use distinct `ecommerce.transaction_id` where duplicate purchase events are
possible. These definitions are explicit SQL contracts, not guaranteed replicas of GA4 report-layer
identity, attribution, thresholding or modeled data.

# Cost and performance controls

Dry runs estimate processed bytes. Maximum-bytes-billed settings can reject unexpectedly expensive
on-demand queries. Partition pruning and clustering block pruning reduce scanned data when filters
match table design. Partitioning and clustering can be combined for stable high-volume workloads.

# Retention and recovery

Time travel defaults to seven days and can be configured from two to seven days. Deleted data then
enters a separate seven-day fail-safe period that is not directly queryable. Table snapshots provide a
read-only point-in-time preservation path beyond time travel. Table expiration overrides partition
expiration, while expired data remains subject to recovery retention.

# Transformation and governance

Scheduled queries run GoogleSQL and can materialize repeatable transformations. Logical views rerun
their defining query; supported materialized views persist and incrementally maintain derived results.
Row access policies filter rows, policy tags protect columns, and Cloud Audit Logs record supported
administrative and data-access activity.

# Measurement boundary

BigQuery contains exported source events and downstream logic chosen by the analyst. It does not
implicitly reproduce GA4 reporting identity, attribution, modeled data, privacy thresholding or
interface-specific aggregates. Every production metric therefore requires an explicit grain,
identifier, deduplication rule, currency policy, late-arrival policy and verification window.
