# CbS16 — Security Project Lifecycle and Documentation: Execution Runbook

Preparation status: **complete**. Practical status: **execution pending** unless a task below is explicitly marked solved.

This guide converts the supplied School 21 brief into a later execution checklist. Expected values are not evidence; copy only observed results into final deliverables.

## Inputs needed later

Task 1 network image, FSTEC methodology/templates, document editor, and selected game/application.

## Task-by-task plan

### Task 1 — Assessment boundary

Starting from DC2, include target and every connected/dependency segment that can affect it according to the supplied diagram. Record complete list in `answer.txt`; exact names remain image pending.

### Task 2 — Threat model

Prepare `Threat_site.docx` for a public e-commerce site with account/payment flows. Skip sections 1–2 and create seven methodology-aligned tables covering assets/context, consequences, threat objects, sources, methods/capabilities, scenarios, and relevance/controls. Mark invented assumptions.

### Task 3 — User guide

Choose one application and build `I_am_user.docx` with introduction, purpose/conditions, preparation, operations, emergency situations, and learning recommendations. Keep a draft, validate steps, and revise for business style.

## Required deliverables

`answer.txt`, `Threat_site.docx`, AI dialogue/fixes, `I_am_user.docx`, optional draft, and AI notes.

## Verification gate

Trace boundary on source diagram, count seven tables, cross-reference assumptions/controls, and run every guide procedure exactly as written.

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

1. Gather: The Task 1 network image, supplied methodology/templates, a document editor, and a chosen application/game.
2. Clone the official School 21 GitLab repository, create/use `develop`, and work only under `src` unless the official task says otherwise.
3. Copy supplied inputs before editing and record SHA-256 hashes when evidence integrity matters.
4. Take a VM/GNS3 snapshot or copy the working project before each major change.
5. Keep a scratch evidence note: **step → why → command/action → observed result → proof filename/frame**.

### Task 1 — Assessment boundary

**Why:** A correct boundary includes the target and dependencies that can affect its security.

**Do this:**

1. Open the source diagram at full resolution.
2. Start at DC2 and trace every connected/dependent segment.
3. Record why each segment is included or excluded.
4. Use exact source labels in `answer.txt`.
5. Recheck every edge on the diagram.

**Verification gate:**

- Every included segment has a dependency path to DC2.
- Names match the image exactly.
- No disconnected segment is added without justification.

**Save:** `answer.txt`.

**AI prompt (paste your real output after it):**

> Using only the network labels and connections I paste from the source image, help trace the assessment boundary starting at DC2. Return included segment, path/dependency, reason, and confidence; do not invent hidden connections.

### Task 2 — E-commerce threat model

**Why:** Threat modeling connects assets, consequences, sources, scenarios, and controls.

**Do this:**

1. State the e-commerce scope and mark assumptions.
2. Follow the supplied methodology and skip only sections explicitly excluded.
3. Create the seven required tables.
4. Keep identifiers consistent across assets, threats, scenarios, and controls.
5. Map each relevant scenario to at least one practical control.
6. Review completeness and business language.

**Verification gate:**

- Exactly seven required tables exist.
- Cross-references are consistent.
- Every conclusion is supported by methodology or labeled assumption.

**Save:** `Threat_site.docx` and required AI dialogue/fixes.

**AI prompt (paste your real output after it):**

> Review this threat-model table one section at a time against the supplied methodology headings. Check asset/scenario/control traceability, missing assumptions, contradictions, and business wording. Do not invent organization-specific facts.

### Task 3 — User guide

**Why:** A usable guide lets a new person complete tasks and recover from predictable problems.

**Do this:**

1. Choose one application and define target reader/version.
2. Write introduction, purpose/conditions, preparation, operations, emergency cases, and learning recommendations.
3. Perform every procedure exactly as written.
4. Add screenshots only where they reduce ambiguity.
5. Revise failed steps and keep terminology consistent.

**Verification gate:**

- A fresh reader can follow the guide.
- Every command/menu path was tested.
- Emergency/recovery steps are clear and safe.

**Save:** `I_am_user.docx`, optional draft, and AI review notes.

**AI prompt (paste your real output after it):**

> Act as a technical editor for this user guide. Check prerequisites, sequence, missing clicks/commands, expected results, recovery steps, consistent terminology, and whether a beginner can reproduce it. Return issues by section, not a rewritten fantasy procedure.

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

