# CbS13 — Detection and Anomalies: Execution Runbook

Preparation status: **complete**. Practical status: **execution pending** unless a task below is explicitly marked solved.

This guide converts the supplied School 21 brief into a later execution checklist. Expected values are not evidence; copy only observed results into final deliverables.

## Inputs needed later

Provided `file1.bin`–`file3.bin`, `malicious_traffic.pcap`, YARA, Suricata, Python, pynput, and an isolated VM.

## Task-by-task plan

### Task 1 — YARA

Hash samples, extract candidate strings/hex sequences without executing files, select one unique text string and one unique hex sequence per rule, and include filesize in one rule. Test each rule against all three samples plus benign controls; one rule must match exactly one target.

### Task 2 — Suricata

Identify four suspicious packets with frame numbers and stable payload/header indicators. Write distinct SIDs in `peer.rules`, run Suricata offline with the supplied PCAP/rules, and confirm all four intended alerts in `fast.log` without broad false positives.

### Task 3 — UBA

Record inter-key timing for two entries of the same string, compare interval arrays, define and document mean deviation, and print the exact required message above/below threshold 0.1. Handle backspace, mismatch, empty/one-character input, and cleanup.

## Required deliverables

`file1_rule.yar`, `file2_rule.yar`, `file3_rule.yar`, `peer.rules`, and `UBA.py`.

## Verification gate

Create a 3×3 YARA match matrix plus benign tests, count four Suricata alert groups, compile/test Python, and document timing formula/units.

## Evidence record

For every practical task record input filename/hash, lab version, exact command/configuration, expected result, observed result, screenshot/frame/log evidence, and final GitLab filename.

## Troubleshooting

Record **symptom → diagnostic → interpretation → change → retest**. Keep failed attempts when they explain the final fix. Never replace an observed value with an AI-generated value.

## Repository hygiene

Never publish real credentials, recovery keys, production private keys, personal data, or third-party scan results. Testing stays in an isolated authorized lab. The assigned GitLab repository, **develop** branch, **src** path, and exact filenames take precedence. A project is not complete until evidence and peer review confirm it.
