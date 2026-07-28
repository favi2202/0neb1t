# CbS18 — Social Engineering and OSINT: Execution Runbook

Preparation status: **complete**. Practical status: **execution pending** unless a task below is explicitly marked solved.

This guide converts the supplied School 21 brief into a later execution checklist. Expected values are not evidence; copy only observed results into final deliverables.

## Inputs needed later

`osint1-5.jpg`, `no_sniff_dump.pcap`, Wireshark/tshark, and official repository.

## Task-by-task plan

### Task 1 — OSINT

Preserve hashes/metadata for each image, then use visible language, road signs, architecture, terrain, transit, storefront, and map clues. Record country, region, locality, evidence, confidence, and alternative hypothesis. Do not identify private people or expose personal data.

### Task 2 — Phishing awareness

Create a clearly labeled training simulation with fictional names and no working links, credentials, QR codes, or real access workflow. Highlight at least two indicators such as urgency and false authority, and add reviewer notes explaining them. Keep it inside School 21 review context.

### Task 3 — Sniffer detection

Analyze PCAP offline. Start with endpoint/MAC statistics, ARP anomalies, duplicate IP-to-MAC mappings, unsolicited/probe patterns, and stream direction. Compare suspicious behavior against routers/bridges before deciding. Record MAC plus frame-based justification.

## Required deliverables

`I_am_osinter.txt`, `email_for_you.md`, AI dialogue, `sniffer_detector.txt`, and analysis notes.

## Verification gate

Require two independent clues per image, label confidence, preserve simulation warning, and cite exact frames/filters for suspected sniffer. Conclusions remain input pending.

## Evidence record

For every practical task record input filename/hash, lab version, exact command/configuration, expected result, observed result, screenshot/frame/log evidence, and final GitLab filename.

## Troubleshooting

Record **symptom → diagnostic → interpretation → change → retest**. Keep failed attempts when they explain the final fix. Never replace an observed value with an AI-generated value.

## Repository hygiene

Never publish real credentials, recovery keys, production private keys, personal data, or third-party scan results. Testing stays in an isolated authorized lab. The assigned GitLab repository, **develop** branch, **src** path, and exact filenames take precedence. A project is not complete until evidence and peer review confirm it.
