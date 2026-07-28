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
