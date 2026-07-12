---
id: "VIEW-01KXB8RT713ZPZ7T0TQP56XX0S"
title: "Google Play acquisition-to-install route"
question: "Which canonical entities distinguish acquisition, install, user, device, installed audience, and first open?"
audience: "Analytics researchers and AI agents"
owner: "knowledge-architecture"
status: "published"
entity_ids:
  - "CONCEPT-01KXB0H9ZM80395EP8SM7W6T0Z"
  - "CONCEPT-01KXB0H9ZMBPTYGA7SHR0K94VE"
  - "CONCEPT-01KXB0H9ZMX4S975N077EGM94N"
  - "CONCEPT-01KXB0H9ZM410EY10Q7A190K5X"
  - "CONCEPT-01KXB0H9ZMY0Z31MBFPCDF5Y3Q"
  - "CONCEPT-01KXB0H9ZMYRQ1M9SS0TJR22Z6"
  - "FACT-01KXB1T830G58R2GC21G593MVP"
  - "FACT-01KXB8RT71S8JB2WCRR7NACD9Q"
  - "FACT-01KXB8RT71ZWV587X5ZR8FV9FQ"
  - "FACT-01KXB8RT71HMCQP17QZTDDVND3"
  - "FACT-01KXB8RT71FAR8H0WAHBMRFCZ0"
  - "FACT-01KXB8RT71PQEA7HYS6D3MTEEQ"
  - "FACT-01KXB8SE2VWPHRNGKME92ACFE6"
reading_order:
  - "CONCEPT-01KXB0H9ZM80395EP8SM7W6T0Z"
  - "FACT-01KXB1T830G58R2GC21G593MVP"
  - "CONCEPT-01KXB0H9ZMBPTYGA7SHR0K94VE"
  - "FACT-01KXB8RT71S8JB2WCRR7NACD9Q"
  - "FACT-01KXB8RT71ZWV587X5ZR8FV9FQ"
  - "CONCEPT-01KXB0H9ZMX4S975N077EGM94N"
  - "FACT-01KXB8RT71HMCQP17QZTDDVND3"
  - "CONCEPT-01KXB0H9ZM410EY10Q7A190K5X"
  - "FACT-01KXB8RT71FAR8H0WAHBMRFCZ0"
  - "CONCEPT-01KXB0H9ZMY0Z31MBFPCDF5Y3Q"
  - "CONCEPT-01KXB0H9ZMYRQ1M9SS0TJR22Z6"
  - "FACT-01KXB8RT71PQEA7HYS6D3MTEEQ"
  - "FACT-01KXB8SE2VWPHRNGKME92ACFE6"
filters:
  service_id: "SERVICE-01KXB0H9ZM3Z8V674FKJP8T657"
  statuses: ["confirmed"]
inclusion_criteria: "Include only canonical distinctions required to traverse acquisition to installation grain; Firebase first open remains out of scope."
updated_at: "2026-07-12"
---

# Reading route

Acquisition → Install → User / Device → Installed audience → First open.

This View provides identifiers and order only. Follow each Fact to its Evidence for definitions and
scope. Firebase event semantics remain an open transition for a later service phase.
