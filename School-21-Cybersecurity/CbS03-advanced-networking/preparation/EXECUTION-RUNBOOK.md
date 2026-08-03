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


<!-- independent-guide-v2 -->
## Independent step-by-step guide

Use this section when no assistant is available. Work on **one task at a time** and do not move forward until its verification gate passes.

### Before starting

1. Gather: GNS3, Cisco 3745 EtherSwitch module, four VPCS nodes, and the official task repository.
2. Clone the official School 21 GitLab repository, create/use `develop`, and work only under `src` unless the official task says otherwise.
3. Copy supplied inputs before editing and record SHA-256 hashes when evidence integrity matters.
4. Take a VM/GNS3 snapshot or copy the working project before each major change.
5. Keep a scratch evidence note: **step → why → command/action → observed result → proof filename/frame**.

### Task 1 — VLAN 10/20 and 802.1Q trunk

**Why:** VLANs separate broadcast domains while a trunk carries several VLANs over one link.

**Do this:**

1. Create SW1, SW2, and PC1–PC4; label every cable and IP/mask.
2. Use one subnet for VLAN 10 and a different subnet for VLAN 20.
3. Create VLANs 10 and 20 on both switches.
4. Put PC1/PC3 access ports in VLAN 10 and PC2/PC4 access ports in VLAN 20.
5. Make the inter-switch link a static 802.1Q trunk and allow VLANs 10,20.
6. Test same-VLAN pings first; cross-VLAN pings should fail without routing.
7. Save configs with `copy running-config startup-config` and export the project.

**Verification gate:**

- `show vlan brief` or `show vlan-switch brief` places access ports correctly.
- `show interfaces trunk` shows the inter-switch link forwarding VLANs 10 and 20.
- PC1↔PC3 and PC2↔PC4 work; PC1↔PC2 does not.

**Save:** One `.gns3`/`.gns3project` file, AI dialogue, final configs, and a short note comparing your manual result with AI.

**AI prompt (paste your real output after it):**

> I am configuring two Cisco 3745 EtherSwitch nodes in GNS3. VLAN 10 contains PC1/PC3 and VLAN 20 contains PC2/PC4. First explain the access-port and trunk logic. Then review the outputs I paste from `show vlan brief`, `show interfaces trunk`, and `show running-config`. Do not invent interface names or evidence; identify one check at a time and explain why.

### Task 2 — EtherChannel trunk

**Why:** EtherChannel combines physical links into one logical link and keeps connectivity if one member fails.

**Do this:**

1. Copy Task 1 into a new project; do not destroy the working VLAN version.
2. Add a second physical link between switches.
3. Configure identical speed/duplex/trunk settings on all member ports.
4. Create the same channel group and supported mode on both ends.
5. Apply trunk settings to the Port-channel interface, not inconsistently to individual members.
6. Verify bundling, then stop one member link and repeat the same-VLAN ping.
7. Save both switches and export a separate project.

**Verification gate:**

- `show etherchannel summary` marks both links bundled, not suspended.
- `show interfaces port-channel` shows the logical trunk.
- Traffic still passes after one member link is stopped.

**Save:** A second GNS3 project containing the same VLAN topology with a two-link trunk EtherChannel.

**AI prompt (paste your real output after it):**

> Review this Cisco EtherChannel lab output from an isolated GNS3 topology. Tell me whether both physical ports are actually bundled, which exact field proves it, and the smallest manual fix. Explain mode compatibility and do not assume LACP/PAgP support that is not visible in my IOS output.

### Task 3 — OSPF and authentication

**Why:** OSPF learns routes dynamically; authentication prevents an untrusted router from forming a legitimate adjacency.

**Do this:**

1. Build R1–R2–R3 with two /30 transit networks and one loopback/free subnet on R1 and R3.
2. Configure and verify every interface before enabling OSPF.
3. Advertise all four networks in area 0 with correct wildcard masks.
4. Set stable router IDs and wait for FULL neighbors.
5. Verify OSPF routes and ping between the two free-subnet addresses.
6. Only after basic routing works, enable matching OSPF authentication settings/keys on both sides of every link.
7. Recheck neighbors, routes, pings, then save and export.

**Verification gate:**

- `show ip ospf neighbor` shows FULL adjacencies.
- `show ip route ospf` contains the remote free subnet.
- Both end-to-end pings succeed before and after authentication.

**Save:** Final authenticated OSPF GNS3 project, AI log/commentary, and one sentence explaining what AI changed in your approach.

**AI prompt (paste your real output after it):**

> I built R1–R2–R3 in GNS3. Use only the pasted interface table, OSPF config, `show ip ospf neighbor`, and `show ip route ospf`. Check addressing, masks, area, wildcard, passive interfaces, timers, and authentication in that order. Explain each hypothesis and ask me to verify it instead of fabricating the result.

### Task 4 — HSRP gateway redundancy

**Why:** HSRP gives a host one stable virtual gateway while two routers provide active/standby redundancy.

**Do this:**

1. Connect R1, R2, and one VPCS through a switch in one subnet.
2. Assign unique real IPs to R1/R2 and reserve a third IP as the HSRP virtual gateway.
3. Configure the same HSRP group and virtual IP on both routers.
4. Give R1 the higher priority and enable preempt only after understanding its effect.
5. Set the VPCS gateway to the virtual IP.
6. Verify normal ping, stop the active router/interface, and measure failover.
7. Restart R1, observe role recovery, save configs, and export.

**Verification gate:**

- `show standby brief` shows one Active and one Standby.
- VPCS reaches the virtual IP before and after failover.
- The default gateway on VPCS never changes.

**Save:** One HSRP GNS3 project with saved router configs.

**AI prompt (paste your real output after it):**

> Explain this HSRP output for a beginner. Identify active, standby, virtual IP, priority, preempt behavior, and why failover did or did not occur. Use only my pasted `show standby brief`, interface status, and VPCS gateway. Give one safe test at a time.

### If something fails

1. Stop changing several things at once.
2. Write the exact symptom.
3. Collect the smallest relevant status/config/log output.
4. Form one hypothesis and run one test.
5. Record the result, revert if necessary, and retest the original goal.

### Final submission gate

- Exact filenames match the official task.
- Every generated answer is backed by real output, a source line, a packet frame, or a screenshot.
- Project/config files reopen after devices/VMs are stopped cleanly.
- Secrets, private keys not explicitly required, recovery keys, licenses, and personal data are removed.
- Only required files are inside the official repository `src` directory.
- You can explain **what each command/action did, why it was needed, and how you proved it worked**.

