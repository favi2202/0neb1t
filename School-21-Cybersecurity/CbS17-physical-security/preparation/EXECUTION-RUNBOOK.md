# CbS17 — Physical Security: Execution Runbook

Preparation status: **complete**. Practical status: **execution pending** unless a task below is explicitly marked solved.

This guide converts the supplied School 21 brief into a later execution checklist. Expected values are not evidence; copy only observed results into final deliverables.

## Inputs needed later

`task1.png`, `task_3.txt`, `measures.xlsx`, spreadsheet editor, and official repository.

## Task-by-task plan

### Task 1 — Security zones

Inventory rooms from floor plan, rank A/B/C by criticality/exposure, identify doors requiring access control, and select an emergency exit using plan/safety constraints. Exact answers remain image pending.

### Task 2 — Equipment

Build `buying_list.xlsx` for five servers and one admin workstation. Cover access control, fire detection/suppression, UPS/power, water leakage, locked rack, CCTV/environment monitoring, and dust where appropriate. Cooling already exists.

### Task 3 — Organizational measures

From `task_3.txt`, choose at least ten effective physical-security measures and at least three unsuitable/redundant/non-physical measures. Give a short reason in `I_4m_the_security.txt`; exact selection remains source pending.

### Task 4 — Budget

From `measures.xlsx`, select within 2,500,000 RUB, annualize recurring cost, provide at least two partial-equivalent controls for each required threat, and show arithmetic in `answer.txt`.

## Required deliverables

`security_zones.txt`, `buying_list.xlsx`, AI logs, `I_4m_the_security.txt`, and budget `answer.txt`.

## Verification gate

Reconcile rooms/items with source files, ensure hazards covered, verify quantities/cost formulas, and confirm total stays within budget.

## Evidence record

For every practical task record input filename/hash, lab version, exact command/configuration, expected result, observed result, screenshot/frame/log evidence, and final GitLab filename.

## Troubleshooting

Record **symptom → diagnostic → interpretation → change → retest**. Keep failed attempts when they explain the final fix. Never replace an observed value with an AI-generated value.

## Repository hygiene

Never publish real credentials, recovery keys, production private keys, personal data, or third-party scan results. Testing stays in an isolated authorized lab. The assigned GitLab repository, **develop** branch, **src** path, and exact filenames take precedence. A project is not complete until evidence and peer review confirm it.
