---
id: "VIEW-01KXFECEYYS7A9D8PZW23C02SP"
title: "Looker Studio Reporting and Governance"
question: "How does Looker Studio connect datasets to reports, model and blend fields, provide viewer interaction, and separate asset sharing, data access, publishing and governance?"
audience: "Analytics engineers, BI developers, data architects, researchers, and AI agents"
owner: "knowledge-architecture"
status: "published"
entity_ids:
  - "SERVICE-01KXB0H9ZMFN9JW1GNN614Q1BJ"
  - "FACT-01KXF42THT7V7DE5VMS003MAQN"
  - "FACT-01KXF42THT2RGTV4EE3WAGB4BP"
  - "FACT-01KXF42THT3370VJG893ATCB0Z"
  - "FACT-01KXF42THT7C21G3B6D9JYZASB"
  - "FACT-01KXF42THTKJW3GVZH4MT9DZR3"
  - "FACT-01KXF42THTTEN8JJ8JKQ6H0ZZS"
  - "FACT-01KXF42THT4KGH1MNPTYD0YB1Z"
  - "FACT-01KXF42THTTS4HWPGWFX1ADSNT"
  - "FACT-01KXF42THT1J5QFQDW2YKZ8Q3Q"
  - "FACT-01KXF42THTDRB05QMJXFBFE9KS"
  - "FACT-01KXF42THT2ZW0AJVM9MA7KW23"
  - "FACT-01KXF7A3S6QG684GPCBTZKYA7Y"
  - "FACT-01KXF7A3S6RQPGBBF7MS1CWDBE"
  - "FACT-01KXF7A3S6CQF1FE0VXWV9GKDB"
  - "FACT-01KXF7A3S6GWXRWXWXA41RNGAB"
  - "FACT-01KXF7A3S6C0KZ81NZ9DV465KK"
  - "FACT-01KXF7A3S67WFG09ZGX400K8FY"
  - "FACT-01KXF7A3S6SVWBT4PNHW195543"
  - "FACT-01KXF7A3S632WSB1XAW95QJX67"
  - "FACT-01KXF7A3S6P1WH24BNP9ZB0CSV"
  - "FACT-01KXF7A3S6Q2W8S58Z9500S3KK"
  - "FACT-01KXFAT5BD3G62M863T8Q5XQRA"
  - "FACT-01KXFAT5BDCEXFGDDSCAYC5W23"
  - "FACT-01KXFAT5BDNJD9MYM531NRTF6T"
  - "FACT-01KXFAT5BDV443926K5EEMFMNS"
  - "FACT-01KXFAT5BD02PA33Y2NX7KKXJQ"
  - "FACT-01KXFAT5BDZ1V6EE26GTMD8XK8"
  - "FACT-01KXFAT5BD8K2BS9JWCZMZG5Z9"
  - "FACT-01KXFAT5BDDD96PTA43SPBSNPN"
reading_order:
  - "FACT-01KXF42THT7V7DE5VMS003MAQN"
  - "FACT-01KXF42THT2RGTV4EE3WAGB4BP"
  - "FACT-01KXF42THT7C21G3B6D9JYZASB"
  - "FACT-01KXF42THT3370VJG893ATCB0Z"
  - "FACT-01KXF42THTKJW3GVZH4MT9DZR3"
  - "FACT-01KXF42THTTEN8JJ8JKQ6H0ZZS"
  - "FACT-01KXF42THT4KGH1MNPTYD0YB1Z"
  - "FACT-01KXF42THTTS4HWPGWFX1ADSNT"
  - "FACT-01KXF42THTDRB05QMJXFBFE9KS"
  - "FACT-01KXF42THT2ZW0AJVM9MA7KW23"
  - "FACT-01KXF7A3S6QG684GPCBTZKYA7Y"
  - "FACT-01KXF7A3S6RQPGBBF7MS1CWDBE"
  - "FACT-01KXF7A3S6CQF1FE0VXWV9GKDB"
  - "FACT-01KXF7A3S6GWXRWXWXA41RNGAB"
  - "FACT-01KXF7A3S6C0KZ81NZ9DV465KK"
  - "FACT-01KXF7A3S67WFG09ZGX400K8FY"
  - "FACT-01KXF7A3S6SVWBT4PNHW195543"
  - "FACT-01KXF7A3S632WSB1XAW95QJX67"
  - "FACT-01KXF7A3S6P1WH24BNP9ZB0CSV"
  - "FACT-01KXF7A3S6Q2W8S58Z9500S3KK"
  - "FACT-01KXFAT5BD3G62M863T8Q5XQRA"
  - "FACT-01KXFAT5BDCEXFGDDSCAYC5W23"
  - "FACT-01KXFAT5BDNJD9MYM531NRTF6T"
  - "FACT-01KXFAT5BDV443926K5EEMFMNS"
  - "FACT-01KXFAT5BD02PA33Y2NX7KKXJQ"
  - "FACT-01KXFAT5BDZ1V6EE26GTMD8XK8"
  - "FACT-01KXFAT5BD8K2BS9JWCZMZG5Z9"
  - "FACT-01KXFAT5BDDD96PTA43SPBSNPN"
filters: {service_id: "SERVICE-01KXB0H9ZMFN9JW1GNN614Q1BJ", statuses: ["confirmed"]}
inclusion_criteria: "Include confirmed Looker Studio architecture, connector, credential, modeling, blending, interactivity, sharing, embedding, publishing and governance boundaries."
updated_at: "2026-07-14"
---

# Primary flow

External dataset → connector → data source and field schema → report components → viewer interaction → published or embedded delivery.

# Asset and data boundaries

A report is the presentation asset. A data source is the semantic and connection layer between an
external dataset and report components. A connector retrieves data for the data source. Asset roles
control what users may do with reports and data sources; data credentials independently determine
whether the underlying data can be viewed.

# Connection and lifecycle modes

Most data sources query the underlying system through a live connection. Extracted data creates a
stored snapshot that can be refreshed. Uploaded files are imported rather than maintained as live
connections. Embedded data sources travel with their report, while reusable data sources can serve
multiple reports and centralize field definitions.

# Credential boundary

Owner's credentials authorize queries through the data-source owner and can expose results to viewers
without direct dataset access. Viewer's credentials require each viewer to have their own dataset
access. Service-account credentials use a non-human Google identity. These modes must be selected as a
governance decision rather than treated as a report-format preference.

# Modeling boundary

Calculated fields create derived dimensions or metrics. Data-source calculated fields are reusable but
do not operate on blended data. Chart-specific calculated fields can use blended data but remain local
to one chart and cannot reference another chart-specific field.

# Blending boundary

A blend is embedded in one report and can combine up to five data sources. It inherits freshness and
credentials from its component sources. Each blend table is grouped and aggregated before the join,
and join conditions support field equality only. Therefore blend output is not guaranteed to match a
row-level SQL join unless grain and unique identifiers are explicitly preserved.

# Filters and viewer interaction

Editor-defined filters inherit from report to page to component. Controls allow viewers to filter,
provide parameter values, change timeframes or select datasets. Cross-source filtering depends on
internal field IDs rather than display names. Cross-filtering can convert chart selections into filters
for other report components.

# Sharing and governance

Viewer, Editor and Owner roles govern asset operations. Sharing a reusable data source does not grant
access to the underlying dataset, and only its owner can change the connection. Private embeds preserve
sign-in and authorization requirements. Embedded reports remain interactive but do not expose edit,
copy or share actions.

# Publishing and change control

Report publishing separates an editor draft from the viewer-facing published version. This boundary is
not complete: edits to reusable data sources can affect both draft and published reports without a new
report publication. Production governance must therefore version and review both reports and reusable
sources.

# Measurement boundary

Looker Studio is a presentation, semantic-modeling and interaction layer. It does not repair source
quality, establish metric grain automatically, grant dataset access through asset sharing, or guarantee
SQL-equivalent blend results. Reliable dashboards require explicit ownership of source definitions,
credentials, field IDs, join grain, publication state and reusable-source changes.
