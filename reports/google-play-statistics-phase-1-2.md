---
id: "REPORT-01KXB8RT71BTSMJHWYV6R8NAC7"
title: "Google Play Console Statistics Phase 1.2"
research_question: "How does Google Play Console distinguish statistics for installs, users, devices, events, and installed audience?"
created_at: "2026-07-12"
as_of: "2026-07-12"
author: "google-analytics-knowledge-project"
status: "issued"
fact_ids:
  - "FACT-01KXB8RT717CVN07FCD0T1D3JD"
  - "FACT-01KXB8RT7168XAFT7A5EKN31Z9"
  - "FACT-01KXB8RT71CR4V1DHN4SVTTK44"
  - "FACT-01KXB8RT712M3QGSAM75HJX9Y5"
  - "FACT-01KXB8RT71DD20FY7Y5RXWKCWZ"
  - "FACT-01KXB8RT71HMCQP17QZTDDVND3"
  - "FACT-01KXB8RT71S8JB2WCRR7NACD9Q"
  - "FACT-01KXB8RT71FAR8H0WAHBMRFCZ0"
  - "FACT-01KXB8RT715RNJFQBE3S2GFMZ1"
  - "FACT-01KXB8RT71ZWV587X5ZR8FV9FQ"
  - "FACT-01KXB8RT71PQEA7HYS6D3MTEEQ"
  - "FACT-01KXB8SE2VWPHRNGKME92ACFE6"
  - "FACT-01KXB8SE2VBAX0WBKD15JGC330"
  - "FACT-01KXB8SE2VDMCKDP410XFDYTR7"
  - "FACT-01KXB8SE2VH5DSRBE6GJH120GJ"
  - "FACT-01KXB8SE2V52GYNZRJ0EYMD6VN"
  - "FACT-01KXB8SE2VH92PWGWRQNXAVTH8"
  - "FACT-01KXB98FWKBNYAXSPMJPGVMJVY"
evidence_ids:
  - "EVID-01KXB8P28ES4MWKKG9V34H0R8Q"
  - "EVID-01KXB8P28EBC0C80EJVZWBMY4K"
  - "EVID-01KXB8P28EVPX3D6H511GGKRCG"
  - "EVID-01KXB8P28EKVCXQSGE1SW20RHC"
  - "EVID-01KXB8P28E5H5YNYD68GQ7EH8H"
  - "EVID-01KXB8P28EN6EYSHKFQ5FSEK08"
  - "EVID-01KXB8P28EMTVKWMCB22YRMQNP"
  - "EVID-01KXB8P28E35C1KVSDRMJNEGYC"
  - "EVID-01KXB8P28E8CNPS7BD0A67DBG1"
  - "EVID-01KXB8P28EDHGV2K4NDGGVAR23"
  - "EVID-01KXB8P28EDE2HE9FZV99CB7FW"
  - "EVID-01KXB8P28EZJK01D04W8SY0D1D"
  - "EVID-01KXB8P28EWNTYA3VSVB4WRG09"
  - "EVID-01KXB8P28EA6T0DMA6EGK100WC"
  - "EVID-01KXB98FWK5Y2Z84MVRVW4DMT5"
concept_ids:
  - "CONCEPT-01KXB0H9ZM2J36209PV7RXPCD3"
  - "CONCEPT-01KXB0H9ZMB53TZPK3Q8N6XDVB"
  - "CONCEPT-01KXB0H9ZMY0Z31MBFPCDF5Y3Q"
  - "CONCEPT-01KXB0H9ZMX4S975N077EGM94N"
  - "CONCEPT-01KXB0H9ZM410EY10Q7A190K5X"
  - "CONCEPT-01KXB0H9ZM80395EP8SM7W6T0Z"
  - "CONCEPT-01KXB0H9ZMBPTYGA7SHR0K94VE"
  - "CONCEPT-01KXB0H9ZMYRQ1M9SS0TJR22Z6"
  - "CONCEPT-01KXB0H9ZMXPT1ZMXS689KRCTK"
service_ids: ["SERVICE-01KXB0H9ZM3Z8V674FKJP8T657"]
method: "Review current official Google documentation, create section-level Evidence, extract candidate Facts, then review atomicity, grain, status, confidence, and links."
limitations: "No live account was inspected; UI freshness, complete historical start, lifetime availability, direct API availability, and the defective Uninstall events definition remain unresolved."
---

# Scope

This dated report covers only Google Play Console Statistics for installs, users, devices, events,
installed audience, time aggregation, dimensions, UI export, and aggregated Statistics exports.

# Official sources

The Evidence IDs in front matter point to four official Google documents and exact section paths.

# Established Facts

- UI and dimensions: `FACT-01KXB8RT717CVN07FCD0T1D3JD`, `FACT-01KXB8RT71CR4V1DHN4SVTTK44`
- Users and devices: `FACT-01KXB8RT712M3QGSAM75HJX9Y5`, `FACT-01KXB8RT71FAR8H0WAHBMRFCZ0`
- Installed audience and install base: `FACT-01KXB8RT71HMCQP17QZTDDVND3`, `FACT-01KXB8RT715RNJFQBE3S2GFMZ1`
- Install events and first opens: `FACT-01KXB8RT71ZWV587X5ZR8FV9FQ`, `FACT-01KXB8RT71PQEA7HYS6D3MTEEQ`
- Export and timing: `FACT-01KXB8SE2VBAX0WBKD15JGC330`, `FACT-01KXB8SE2VDMCKDP410XFDYTR7`

# Key distinctions

- Acquisition versus Install: `FACT-01KXB8SE2V52GYNZRJ0EYMD6VN`
- User versus Device: `FACT-01KXB8RT71DD20FY7Y5RXWKCWZ`, `FACT-01KXB8RT71FAR8H0WAHBMRFCZ0`
- Install event versus Installed audience: `FACT-01KXB8RT71ZWV587X5ZR8FV9FQ`, `FACT-01KXB8RT71HMCQP17QZTDDVND3`
- Install versus First open: `FACT-01KXB8SE2VH92PWGWRQNXAVTH8`
- Per-interval versus cumulative: `FACT-01KXB8RT7168XAFT7A5EKN31Z9`, `FACT-01KXB8SE2VWPHRNGKME92ACFE6`

# Uncertainties and open questions

The current official help row for Uninstall events appears to repeat First opens text, so no
definition was canonized. UI freshness, full history start, lifetime aggregation, a direct
Statistics API, and direct BigQuery export were not confirmed.

# Coverage and next phase

The scoped Statistics topics are covered to the extent supported by official documentation. The
recommended next stage is Phase 1.3 — Google Play Console Ratings & Reviews Research.
