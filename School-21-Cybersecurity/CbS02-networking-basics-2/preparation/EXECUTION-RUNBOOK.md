# CbS2 — Networking Basics Part 2: Execution Runbook

Preparation status: **complete**. Practical status: **execution pending** unless a task below is explicitly marked solved.

This guide converts the supplied School 21 brief into a later execution checklist. Expected values are not evidence; copy only observed results into final deliverables.

## Inputs needed later

Authorized Cisco 3745 image, GNS3, Wireshark, and official GitLab checkout.

## Task-by-task plan

### Task 1 — Static routing

Build R1–R2–R3. Suggested links: R1 10.10.10.1/24 ↔ R2 10.10.10.2/24 and R2 10.10.20.1/24 ↔ R3 10.10.20.2/24. Configure R1 route to 10.10.20.0/24 via 10.10.10.2 and R3 return route to 10.10.10.0/24 via 10.10.20.1. Verify both directions and capture ICMP.

### Task 2 — NTP

Make one router the lab time source, deliberately set the peer clock incorrectly, configure the NTP server address, and wait for synchronization. Record the transport protocol, observed source/destination ports, and first Transmit Timestamp from the capture.

### Task 3 — DNS

Configure a loopback and record for `my.site`, enable the lab DNS service, and point the neighbor at it. Ping by name, then inspect `dns` packets. Expected query is usually type A/class IN; confirm from the real PCAP. Prepare `ai-logs/dns.md`.

### Task 4 — DHCP

Attach a VPC on 10.10.30.0/24. Reserve the gateway and all but a 50-address range; for example leave 10.10.30.2–10.10.30.51 leasable. Capture DORA. The first packet is expected to target 255.255.255.255; verify it.

### Task 5 — SSH

Create a local user, domain name, RSA host key, SSH v2, and VTY `login local`/`transport input ssh`. Check TCP/22, complete one login, exit, and analyze TCP handshake plus SSH version exchange. Save `ai-logs/ssh.md`.

## Required deliverables

Per task: required `.gns3project`; `static`, `ntp`, `dns`, `dhcp`, and `ssh` PCAP/text files; DNS and SSH AI logs.

## Verification gate

Use `show ip route`, `show ntp associations`, `show hosts`, DHCP bindings, `show ip ssh`, bidirectional ping, and protocol-specific Wireshark filters.

## Evidence record

For every practical task record input filename/hash, lab version, exact command/configuration, expected result, observed result, screenshot/frame/log evidence, and final GitLab filename.

## Troubleshooting

Record **symptom → diagnostic → interpretation → change → retest**. Keep failed attempts when they explain the final fix. Never replace an observed value with an AI-generated value.

## Repository hygiene

Never publish real credentials, recovery keys, production private keys, personal data, or third-party scan results. Testing stays in an isolated authorized lab. The assigned GitLab repository, **develop** branch, **src** path, and exact filenames take precedence. A project is not complete until evidence and peer review confirm it.
