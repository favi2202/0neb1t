# CbS12 — Network Reconnaissance and Attack Analysis: Execution Runbook

Preparation status: **complete**. Practical status: **execution pending** unless a task below is explicitly marked solved.

This guide converts the supplied School 21 brief into a later execution checklist. Expected values are not evidence; copy only observed results into final deliverables.

## Inputs needed later

Strictly isolated authorized lab, supplied PCAP/files, test MongoDB instance with no real data, and local mitmproxy endpoints.

## Task-by-task plan

### Task 1 — MITRE ATT&CK

Map eight scenarios to tactic/technique IDs in `my_mitre.txt`. Use the official current MITRE Enterprise matrix during execution because IDs/relationships can change; explain each primary mapping and omit sub-techniques.

### Task 2 — MongoDB scanner

Build `scan.py` for an explicitly supplied private lab CIDR only. Require a target argument, reject public ranges by default, use bounded timeouts/concurrency, test TCP/27017, and report only anonymous lab instances. Include instructions.

### Task 3 — MITM lab

Use mitmproxy only between your own local test client and form server. Log field names and redact password/token values; do not collect real credentials. Confirm with synthetic data.

### Task 4 — Detection

Analyze `good_traffic.pcap` offline, identify malicious sequence and flag, and name the defensive control. Cite frame numbers and observed indicators.

### Task 5 — Bonus

Document FOFA query syntax conceptually. Do not interact with or publish a live third-party vulnerable host; use an authorized lab/example reserved address if reviewer permits.

## Required deliverables

`my_mitre.txt`, `scan.py` plus instructions, `interceptor.py`, `solution.txt`, and optional `i_found_it.txt`.

## Verification gate

Unit-test CIDR validation, scan only owned lab, use synthetic forms, reopen PCAP evidence, and validate mappings against official MITRE pages.

## Evidence record

For every practical task record input filename/hash, lab version, exact command/configuration, expected result, observed result, screenshot/frame/log evidence, and final GitLab filename.

## Troubleshooting

Record **symptom → diagnostic → interpretation → change → retest**. Keep failed attempts when they explain the final fix. Never replace an observed value with an AI-generated value.

## Repository hygiene

Never publish real credentials, recovery keys, production private keys, personal data, or third-party scan results. Testing stays in an isolated authorized lab. The assigned GitLab repository, **develop** branch, **src** path, and exact filenames take precedence. A project is not complete until evidence and peer review confirm it.
