# CbS14 — Secure Network Design: Execution Runbook

Preparation status: **complete**. Practical status: **execution pending** unless a task below is explicitly marked solved.

This guide converts the supplied School 21 brief into a later execution checklist. Expected values are not evidence; copy only observed results into final deliverables.

## Inputs needed later

pfSense CE 2.6.0 image, hypervisor with isolated networks, two disposable VMs, and official repository.

## Task-by-task plan

### Task 1 — NGFW

Deploy with specified resources, assign WAN/LAN correctly, restrict management to lab LAN, create `school21` in admins, sign in, and capture `pfweb.png` plus `proof.png` showing only required information.

### Task 2 — IPsec VPN

Clone after cleaning identifiers, use distinct LAN subnets, configure matching phase 1/2 proposals/selectors, add rules, bring up tunnel, and verify cross-site traffic. Export `pfsense1.xml`, `pfsense2.xml`, and `site-to-site.png`; backups are sensitive.

### Task 3 — Firewall rules

On lab LAN block RDP, block SSH, and allow SMTP only through schedule 07:00–22:59 on chosen day. Order before broad allows, test allowed/denied cases, and export `fw_rules.xml`.

### Task 4 — Bonus iptables

Translate policies into commented lab-only iptables commands in `iptables_rules.txt`. Use stateful matches and time module; test on disposable host to avoid lockout.

## Required deliverables

`pfweb.png`, `proof.png`, `site-to-site.png`, `pfsense1.xml`, `pfsense2.xml`, `fw_rules.xml`, and optional `iptables_rules.txt`.

## Verification gate

Inspect interfaces, user rights, IPsec SA/status, rule order, schedule timezone, positive/negative tests, and sanitized exports.

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

1. Gather: pfSense CE 2.6.0, an isolated hypervisor lab, two disposable test VMs, snapshots, and no production networks.
2. Clone the official School 21 GitLab repository, create/use `develop`, and work only under `src` unless the official task says otherwise.
3. Copy supplied inputs before editing and record SHA-256 hashes when evidence integrity matters.
4. Take a VM/GNS3 snapshot or copy the working project before each major change.
5. Keep a scratch evidence note: **step → why → command/action → observed result → proof filename/frame**.

### Task 1 — pfSense deployment

**Why:** Correct interface assignment and restricted management are the base of a secure firewall.

**Do this:**

1. Create isolated WAN/LAN networks and snapshot before configuration.
2. Deploy pfSense with required resources and carefully map WAN/LAN.
3. Set LAN management address and verify access only from lab LAN.
4. Create the exact `school21` administrator account.
5. Capture only the required UI/proof without secrets.

**Verification gate:**

- WAN/LAN addresses are not swapped.
- Web UI is reachable only from intended lab segment.
- Required account/role is visible without password disclosure.

**Save:** `pfweb.png` and `proof.png`.

**AI prompt (paste your real output after it):**

> Review this sanitized pfSense interface/user summary. Check WAN/LAN mapping, management exposure, administrator role, and what screenshots prove. Do not ask for passwords or real public network details.

### Task 2 — Site-to-site IPsec

**Why:** Matching phase settings and traffic selectors create an encrypted path between distinct LANs.

**Do this:**

1. Clone only after cleaning identifiers and use different LAN subnets.
2. Configure matching phase 1 proposals/authentication.
3. Configure mirrored phase 2 local/remote selectors.
4. Add only required firewall rules.
5. Bring up tunnel and test cross-site ping.
6. Export sanitized configs and capture status.

**Verification gate:**

- IPsec SA is established.
- Selectors are mirrored correctly.
- Cross-site traffic succeeds while unrelated traffic stays blocked.

**Save:** `pfsense1.xml`, `pfsense2.xml`, and `site-to-site.png`; sanitize sensitive material.

**AI prompt (paste your real output after it):**

> Troubleshoot this isolated pfSense IPsec lab from sanitized phase 1/2 settings and logs. Compare proposals, IDs, selectors, routes, rules, and time. Give one verification step at a time.

### Task 3 — Scheduled firewall policy

**Why:** Rule order, direction, state, and time zone decide what traffic is actually allowed.

**Do this:**

1. Create blocks for RDP and SSH from the specified lab side.
2. Create SMTP allow rule with the exact 07:00–22:59 schedule/day.
3. Place rules before broad allows.
4. Test each deny and both inside/outside the schedule.
5. Check active states and time zone.
6. Export only required rules.

**Verification gate:**

- RDP/SSH tests are blocked.
- SMTP works only during the required window.
- Rule order and interface are correct.

**Save:** `fw_rules.xml`.

**AI prompt (paste your real output after it):**

> Audit these pfSense rules for interface, source/destination, protocol/port, order, schedule/time zone, and default-policy interaction. Produce an allowed/blocked test matrix from my sanitized configuration.

### Task 4 — Bonus iptables translation

**Why:** Translating policy shows how stateful firewall concepts map to Linux rules.

**Do this:**

1. Write commented rules in a file before applying anything.
2. Include established/related handling and loopback.
3. Translate RDP/SSH blocks and scheduled SMTP using the time module.
4. Add a rollback plan to prevent lockout.
5. Test only on a disposable VM.

**Verification gate:**

- Syntax is valid for the chosen iptables version.
- Tests match the pfSense policy.
- Rollback restores connectivity.

**Save:** `iptables_rules.txt`.

**AI prompt (paste your real output after it):**

> Review these lab-only iptables rules without broadening scope. Check state handling, direction, ports, time-zone/time match, order, default policy, and rollback safety before I test in a disposable VM.

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

