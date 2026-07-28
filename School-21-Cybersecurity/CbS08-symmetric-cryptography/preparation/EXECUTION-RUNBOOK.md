# CbS8 — Symmetric Cryptography: Execution Runbook

Preparation status: **complete**. Practical status: **execution pending** unless a task below is explicitly marked solved.

This guide converts the supplied School 21 brief into a later execution checklist. Expected values are not evidence; copy only observed results into final deliverables.

## Inputs needed later

All supplied Python scripts and a disposable Python environment.

## Task-by-task plan

### Task 1 — Block encryption

Read `crypto_alphabet.py` to determine key, alphabet/encoding, padding, and how the two outputs relate. Write a decryptor only after reproducing one known block; record the recovered flag in `solution.txt`.

### Task 2 — Stream cipher

Identify the state-update/keystream algorithm, list every deviation from the standard implementation with line references, correct a copy, and decrypt into `solution_stream.txt`.

### Task 3 — AES

Inspect `4es.py` for key, IV, encoding, and padding; decrypt the ciphertext using the required inverse mode and place plaintext plus mode in `solution_aes.txt`.

### Task 4 — Modes

Classify each mode script by dependency pattern: ECB independent blocks, CBC previous ciphertext, CFB/OFB feedback, CTR nonce/counter. Confirm with repeated-block tests, then write `operator.txt`.

### Task 5 — Vulnerability

Inspect `crypto_crack.py` for nonce/IV/key misuse or another flaw. Reproduce it, recover the flag, and identify the faulty line in `crack.txt`.

## Required deliverables

`solution.txt`, `solution_stream.txt`, `solution_aes.txt`, `operator.txt`, and `crack.txt`.

## Verification gate

Every recovered plaintext must round-trip through the supplied implementation; record source hashes and exact line references. All answers remain source pending.

## Evidence record

For every practical task record input filename/hash, lab version, exact command/configuration, expected result, observed result, screenshot/frame/log evidence, and final GitLab filename.

## Troubleshooting

Record **symptom → diagnostic → interpretation → change → retest**. Keep failed attempts when they explain the final fix. Never replace an observed value with an AI-generated value.

## Repository hygiene

Never publish real credentials, recovery keys, production private keys, personal data, or third-party scan results. Testing stays in an isolated authorized lab. The assigned GitLab repository, **develop** branch, **src** path, and exact filenames take precedence. A project is not complete until evidence and peer review confirm it.
