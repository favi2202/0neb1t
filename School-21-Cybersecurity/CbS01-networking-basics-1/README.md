# CbS1 — Networking Basics Part 1

Status: **In progress** (15%). Task 1 is solved and verified. Tasks 2–4 are fully prepared but require the official image/environment and genuine packet captures.

## Scope

IPv4, OSI/TCP-IP, GNS3, Cisco IOS, Wireshark, ICMP, multicast, ARP

## Tasks

1. Address calculations — solution prepared in `src/ip-1`
2. GNS3 introduction — runbook prepared; execution pending
3. Multicast requests — runbook prepared; packet verification pending
4. ARP analysis — runbook prepared; packet verification pending

## Preparation guides

- [Task 2 — GNS3](preparation/TASK2-GNS3.md)
- [Task 3 — Multicast](preparation/TASK3-MULTICAST.md)
- [Task 4 — ARP](preparation/TASK4-ARP.md)
- [Track-wide preparation-first workflow](../PREPARATION-FIRST-WORKFLOW.md)

## Expected deliverables

- `src/ip-1`
- GNS3 project containing the imported Cisco 3745 device
- `multicast.pcap`
- `multicast`
- GNS3 project for the ARP lab
- `arp.pcap`
- `arp`
- `ai-logs/arp.md`

Exact filenames in the official task and assigned GitLab repository take precedence. Supplied inputs are not deliverables unless the README explicitly says to return them.

## Working rules

- Complete official submission work in the assigned GitLab repository on `develop`.
- Keep required work under `src`.
- Use an isolated, authorized lab for security testing.
- Do not commit credentials, real private keys, personal data, unauthorized scan results, or fabricated evidence.
- Verify every artifact with an appropriate command, test, capture, parser, or configuration check.
- Preserve required AI dialogue/log files, but review and explain every result independently.

## Task 1 verification

- `178.101.89.7` → `10110010.01100101.01011001.00000111`
- `201.57.153.161` → `11001001.00111001.10011001.10100001`
- 3 hosts → `/29` (`255.255.255.248`, 6 usable)
- 16 hosts → `/27` (`255.255.255.224`, 30 usable)
- 32 hosts → `/26` (`255.255.255.192`, 62 usable)

The host formula is `2^h - 2`: one address is reserved for the network and one for broadcast.

## Current next step

No resource-dependent action is required now. When the official Cisco 3745 image and project repository become available, follow the Task 2 runbook and return the GNS3 screenshot or error output for verification.