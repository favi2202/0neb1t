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
