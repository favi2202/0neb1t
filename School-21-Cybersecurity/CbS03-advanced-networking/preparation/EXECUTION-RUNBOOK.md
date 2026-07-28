# CbS3 — Advanced Networking: Execution Runbook

Preparation status: **complete**. Practical status: **execution pending** unless a task below is explicitly marked solved.

This guide converts the supplied School 21 brief into a later execution checklist. Expected values are not evidence; copy only observed results into final deliverables.

## Inputs needed later

Cisco 3745 EtherSwitch-compatible image/module, GNS3, four VPCs, and official repository.

## Task-by-task plan

### Task 1 — VLAN and trunk

Use SW1 with PC1 in VLAN 10 and PC2 in VLAN 20; SW2 with PC3 in VLAN 10 and PC4 in VLAN 20. Give each VLAN its own subnet, configure access ports, create an 802.1Q trunk, label addresses, and verify same-VLAN success/cross-VLAN failure. Harden negotiation/native VLAN when supported.

### Task 2 — EtherChannel

Replace the single trunk with two physical links grouped into one port-channel. Use the same channel mode on both sides, make the logical port-channel the trunk, and verify member links are bundled rather than suspended.

### Task 3 — OSPF

Build R1–R2–R3 with two /30 transit networks and one loopback/free subnet on R1 and R3. Advertise all four networks in area 0. Verify FULL neighbors, OSPF routes, and loopback-to-loopback pings. Add authentication only after routing works.

### Task 4 — HSRP

Put R1, R2, and one VPC in the same LAN. Configure a shared virtual IP as the VPC gateway, assign different priorities, enable preemption deliberately, and verify failover by stopping the active router.

## Required deliverables

Four verified GNS3 project files, plus required AI dialogue/configuration evidence.

## Verification gate

Use `show vlan brief`, `show interfaces trunk`, `show etherchannel summary`, `show ip ospf neighbor`, `show ip route ospf`, and `show standby brief`.

## Evidence record

For every practical task record input filename/hash, lab version, exact command/configuration, expected result, observed result, screenshot/frame/log evidence, and final GitLab filename.

## Troubleshooting

Record **symptom → diagnostic → interpretation → change → retest**. Keep failed attempts when they explain the final fix. Never replace an observed value with an AI-generated value.

## Repository hygiene

Never publish real credentials, recovery keys, production private keys, personal data, or third-party scan results. Testing stays in an isolated authorized lab. The assigned GitLab repository, **develop** branch, **src** path, and exact filenames take precedence. A project is not complete until evidence and peer review confirm it.
