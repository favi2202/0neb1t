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


<!-- independent-guide-v2 -->
## Independent step-by-step guide

Use this section when no assistant is available. Work on **one task at a time** and do not move forward until its verification gate passes.

### Before starting

1. Gather: `task1.png`, `task_3.txt`, `measures.xlsx`, a spreadsheet editor, and exact assignment files.
2. Clone the official School 21 GitLab repository, create/use `develop`, and work only under `src` unless the official task says otherwise.
3. Copy supplied inputs before editing and record SHA-256 hashes when evidence integrity matters.
4. Take a VM/GNS3 snapshot or copy the working project before each major change.
5. Keep a scratch evidence note: **step → why → command/action → observed result → proof filename/frame**.

### Task 1 — Security zones

**Why:** Zoning applies stronger physical controls to more critical or exposed areas.

**Do this:**

1. Inventory every room/door from the plan.
2. Define A/B/C criteria before assigning zones.
3. Assign each room with one-sentence reasoning.
4. Mark doors needing access control.
5. Select the emergency exit using the plan and safety constraints.
6. Reconcile labels with the image.

**Verification gate:**

- Every room appears once.
- Critical areas receive stronger zones.
- Emergency route does not rely on a locked/unsafe path.

**Save:** `security_zones.txt`.

**AI prompt (paste your real output after it):**

> Using only the floor-plan labels and constraints I paste, audit my A/B/C zone assignments. Check completeness, criticality, door controls, emergency egress, and unsupported assumptions.

### Task 2 — Equipment buying list

**Why:** Physical controls must cover unauthorized access, fire, power, water, environment, and monitoring.

**Do this:**

1. List five servers and one administrator workstation.
2. Map hazards to controls before selecting equipment.
3. Choose quantities for access control, fire detection/suppression, UPS/power, leak detection, racks, CCTV, and environment monitoring.
4. Avoid adding cooling if the task states it already exists.
5. Build formulas and notes in the spreadsheet.

**Verification gate:**

- Every hazard has a control.
- Quantities match assets/doors/rooms.
- Workbook formulas and units are consistent.

**Save:** `buying_list.xlsx` and required AI log.

**AI prompt (paste your real output after it):**

> Audit this physical-security buying list. Map each item to hazard, protected asset, quantity rationale, dependency, and evidence from the floor plan. Flag duplicates, missing hazards, and unnecessary cooling.

### Task 3 — Organizational measures

**Why:** Policies and procedures complement physical equipment and must fit the scenario.

**Do this:**

1. Read every option in `task_3.txt`.
2. Classify as effective, unsuitable, redundant, or non-physical.
3. Choose at least ten effective and at least three unsuitable measures.
4. Give a short scenario-specific reason for each.
5. Check counts and exact wording.

**Verification gate:**

- Minimum counts are satisfied.
- Reasons explain context, not only definitions.
- Selected items exist in source.

**Save:** `I_4m_the_security.txt`.

**AI prompt (paste your real output after it):**

> Review my selections against the supplied option list. For each, classify effective/unsuitable/redundant/non-physical, explain why for this scenario, and verify minimum counts without inventing options.

### Task 4 — Budget optimization

**Why:** Budgeting requires arithmetic plus threat coverage, not simply buying the cheapest controls.

**Do this:**

1. Import every measure and one-time/recurring cost.
2. Normalize recurring costs to the required period.
3. List required threats and candidate controls.
4. Select within 2,500,000 RUB with at least two partial-equivalent controls per required threat.
5. Show formulas and total.
6. Run a second independent total check.

**Verification gate:**

- Total is at or below budget.
- Recurring costs use the same period.
- Coverage matrix meets the task requirement.

**Save:** `answer.txt`.

**AI prompt (paste your real output after it):**

> Audit this security budget from the supplied measures table. Recalculate annualized cost and total, then build a threat-to-control coverage matrix. Flag any threat lacking two qualifying controls and do not invent prices.

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

