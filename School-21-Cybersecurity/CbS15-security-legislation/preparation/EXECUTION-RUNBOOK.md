# CbS15 — Information-Security Legislation: Execution Runbook

Preparation status: **complete**. Practical status: **execution pending** unless a task below is explicitly marked solved.

This guide converts the supplied School 21 brief into a later execution checklist. Expected values are not evidence; copy only observed results into final deliverables.

## Inputs needed later

Supplied versions of 187-FZ, GOST R 56546-2015, FSTEC tables/orders, and official repository.

## Task-by-task plan

### Task 1 — Legislation

For each case, identify exact duty, locate corresponding article/part in the supplied 187-FZ version, quote only a short identifying phrase, and record article numbers in `legal_cases.txt`. Do not rely on memory because amendments and source versions matter.

### Task 2 — Standards

Search the supplied GOST document itself for the embedded flag and save it verbatim in `i_am_attentive.txt`. Record document hash/page for verification.

### Task 3 — Classification

Determine whether each scenario is a personal-data system, state information system, or KII object; derive impact/scale/threat inputs from supplied tables; assign class/level with one-sentence justification in `my_cases.txt`.

## Required deliverables

`legal_cases.txt`, `i_am_attentive.txt`, and `my_cases.txt`.

## Verification gate

Every answer must cite the supplied document/table row and version. Treat this as educational classification, not legal advice; source documents remain pending.

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

1. Gather: The exact supplied versions of 187-FZ, GOST, FSTEC tables/orders, and the official repository.
2. Clone the official School 21 GitLab repository, create/use `develop`, and work only under `src` unless the official task says otherwise.
3. Copy supplied inputs before editing and record SHA-256 hashes when evidence integrity matters.
4. Take a VM/GNS3 snapshot or copy the working project before each major change.
5. Keep a scratch evidence note: **step → why → command/action → observed result → proof filename/frame**.

### Task 1 — Legislation cases

**Why:** Legal conclusions are version-sensitive and must be tied to exact articles rather than memory.

**Do this:**

1. Record the title/date/version/hash of the supplied law.
2. For each case, identify the action/obligation in plain language.
3. Search the supplied text and locate the exact article/part.
4. Use only a short identifying phrase and record the citation.
5. Cross-check that the article answers the scenario.

**Verification gate:**

- Every case has article/part and justification.
- All citations come from the supplied version.
- No unsupported legal conclusion is presented as advice.

**Save:** `legal_cases.txt`.

**AI prompt (paste your real output after it):**

> Using only the supplied version excerpt I paste, map each educational case to the exact article and part. Quote only a short identifying phrase, explain the connection, and mark uncertainty. Do not rely on current-law memory.

### Task 2 — Attention flag in standard

**Why:** Document provenance and page-level evidence make the extracted result reproducible.

**Do this:**

1. Hash the supplied GOST file.
2. Search text/OCR and inspect surrounding page manually.
3. Copy the embedded flag exactly.
4. Record page and document version for your own verification.
5. Reopen the final answer and compare character by character.

**Verification gate:**

- Flag exists visibly in the supplied document.
- Page/version/hash are recorded.
- No OCR substitution changed characters.

**Save:** `i_am_attentive.txt`.

**AI prompt (paste your real output after it):**

> Check this extracted flag against the short supplied document excerpt/page metadata. Identify likely OCR confusions and require a character-by-character visual confirmation.

### Task 3 — System classification

**Why:** Classification follows decision criteria and supplied tables, not intuition.

**Do this:**

1. For each scenario determine whether it is a personal-data system, state information system, or KII object.
2. Extract impact, scale, data, users, and threat conditions from the scenario.
3. Walk through the supplied classification table row by row.
4. Assign class/level/category and write one-sentence justification.
5. Record table/order/version reference.

**Verification gate:**

- Inputs map to explicit table criteria.
- Class/level is reproducible from the cited row.
- Ambiguous assumptions are labeled.

**Save:** `my_cases.txt`.

**AI prompt (paste your real output after it):**

> Walk through this educational classification case using only the supplied FSTEC table excerpt. Separate scenario facts, assumptions, decision criteria, selected row, and resulting class/level. Flag missing facts instead of guessing.

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

