# CbS1 — Networking Basics Part 1: Execution Runbook

Preparation status: **complete**. Practical status: **execution pending** unless a task below is explicitly marked solved.

This guide converts the supplied School 21 brief into a later execution checklist. Expected values are not evidence; copy only observed results into final deliverables.

## Inputs needed later

Authorized Cisco 3745 image, GNS3, Wireshark, and the assigned GitLab repository.

## Task-by-task plan

### Task 1 — Address calculations

Completed and independently checked. Use `src/ip-1` as the prepared answer; copy it to the official repository only after checking the required path.

### Task 2 — GNS3

Follow `TASK2-GNS3.md`: import the authorized image, boot the router, verify with `show version`, save the configuration, and preserve screenshots.

### Task 3 — Multicast

Follow `TASK3-MULTICAST.md`: build the isolated two-router lab, capture IGMP/ICMP, compare group 239.1.1.1 with expected MAC 01:00:5e:01:01:01, and record only observed packet values.

### Task 4 — ARP

Follow `TASK4-ARP.md`: clear dynamic ARP state, capture the first request and reply, distinguish Ethernet destination from the ARP target-hardware field, and record the reply MAC from the genuine capture.

## Required deliverables

`src/ip-1`; GNS3 projects; `multicast`, `multicast.pcap`; `arp`, `arp.pcap`; required AI logs.

## Verification gate

Recalculate Task 1; use `show version`, `show ip igmp groups`, `show ip arp`, and Wireshark display filters. Practical tasks remain execution pending.

## Evidence record

For every practical task record input filename/hash, lab version, exact command/configuration, expected result, observed result, screenshot/frame/log evidence, and final GitLab filename.

## Troubleshooting

Record **symptom → diagnostic → interpretation → change → retest**. Keep failed attempts when they explain the final fix. Never replace an observed value with an AI-generated value.

## Repository hygiene

Never publish real credentials, recovery keys, production private keys, personal data, or third-party scan results. Testing stays in an isolated authorized lab. The assigned GitLab repository, **develop** branch, **src** path, and exact filenames take precedence. A project is not complete until evidence and peer review confirm it.
