# CbS11 — Enterprise IT Infrastructure: Execution Runbook

Preparation status: **complete**. Practical status: **execution pending** unless a task below is explicitly marked solved.

This guide converts the supplied School 21 brief into a later execution checklist. Expected values are not evidence; copy only observed results into final deliverables.

## Inputs needed later

`typical_org.xlsx`, `not_really_typical_org`, diagrams.net, spreadsheet editor, and official repository.

## Task-by-task plan

### Task 1 — Topology

Extract every supplied asset, group endpoints/network/server/security devices, use standard icons, draw actual connections, and save editable `result_topology.drawio`. Do not invent IPs or ports unless necessary.

### Task 2 — Inventory

Create `My_inventory.xlsx` with device, OS/version, software/version, IPv4/mask, domain/local accounts, and domain. Include function-appropriate software for non-network devices. Add checks for missing values and duplicate IPs.

### Task 3 — Protection

Place at least endpoint protection, firewalls, and VPN; consider EDR, backups, segmentation, logging, and MFA. Add a protection column and export protected topology/inventory.

### Task 4 — Bonus

Add three remote workers, a terminal server, and an isolated two-server segment reachable only through protected remote access. Explicitly deny all other access.

## Required deliverables

`result_topology.drawio`, `My_inventory.xlsx`, optional `check_inventory.py`, protected topology/inventory, AI logs/justification, and `new_result_topology`.

## Verification gate

Reconcile asset counts, open/re-save drawio, validate XLSX formulas/filters, check required fields, and trace permitted/denied paths.

## Evidence record

For every practical task record input filename/hash, lab version, exact command/configuration, expected result, observed result, screenshot/frame/log evidence, and final GitLab filename.

## Troubleshooting

Record **symptom → diagnostic → interpretation → change → retest**. Keep failed attempts when they explain the final fix. Never replace an observed value with an AI-generated value.

## Repository hygiene

Never publish real credentials, recovery keys, production private keys, personal data, or third-party scan results. Testing stays in an isolated authorized lab. The assigned GitLab repository, **develop** branch, **src** path, and exact filenames take precedence. A project is not complete until evidence and peer review confirm it.
