# CbS4 — Traffic Analysis: Execution Runbook

Preparation status: **complete**. Practical status: **execution pending** unless a task below is explicitly marked solved.

This guide converts the supplied School 21 brief into a later execution checklist. Expected values are not evidence; copy only observed results into final deliverables.

## Inputs needed later

Supplied SMB and reverse-shell captures, Wireshark/tshark, Python, Scapy, and a disposable lab.

## Task-by-task plan

### Task 1 — Packet investigation

Hash the PCAP before analysis. Identify endpoints with Conversations, then filter `smb || smb2`. Record overall sequence, exact SMB dialect, Session ID, authenticated account, and both endpoint MAC addresses. Cite frame numbers in `report.docx`.

### Task 2 — Reverse-shell trace

Inspect `some_troubled_traffic.pcapng`, unusual long-lived TCP streams, and Follow TCP Stream. Record initiating IP, destination IP, protocol, and commands exactly as observed. Do not execute extracted commands.

### Task 3 — Scapy

Prepare a localhost-only packet to 127.0.0.1 TCP/12345 with the required Raw payload. Capture with `tcp port 12345`, retain exactly the intended message packet in `sent_message.pcapng`, and verify packet count/payload.

## Required deliverables

`report.docx`, `answers.txt`, `main.py`, and `sent_message.pcapng`.

## Verification gate

Reopen PCAPs, confirm frame numbers/stream direction, run `python3 -m py_compile main.py`, and verify the final capture contains one intended packet.

## Evidence record

For every practical task record input filename/hash, lab version, exact command/configuration, expected result, observed result, screenshot/frame/log evidence, and final GitLab filename.

## Troubleshooting

Record **symptom → diagnostic → interpretation → change → retest**. Keep failed attempts when they explain the final fix. Never replace an observed value with an AI-generated value.

## Repository hygiene

Never publish real credentials, recovery keys, production private keys, personal data, or third-party scan results. Testing stays in an isolated authorized lab. The assigned GitLab repository, **develop** branch, **src** path, and exact filenames take precedence. A project is not complete until evidence and peer review confirm it.
