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


<!-- independent-guide-v2 -->
## Independent step-by-step guide

Use this section when no assistant is available. Work on **one task at a time** and do not move forward until its verification gate passes.

### Before starting

1. Gather: All scripts supplied by the task, Python 3, and an isolated virtual environment.
2. Clone the official School 21 GitLab repository, create/use `develop`, and work only under `src` unless the official task says otherwise.
3. Copy supplied inputs before editing and record SHA-256 hashes when evidence integrity matters.
4. Take a VM/GNS3 snapshot or copy the working project before each major change.
5. Keep a scratch evidence note: **step → why → command/action → observed result → proof filename/frame**.

### Task 1 — Block cipher script

**Why:** Block structure, padding, and key handling determine the correct inverse.

**Do this:**

1. Hash and preserve `crypto_alphabet.py`.
2. Trace alphabet/encoding, block size, key use, padding, and output format.
3. Reproduce one known block before writing a full decryptor.
4. Decrypt, remove padding correctly, and round-trip the plaintext.

**Verification gate:**

- Re-encryption exactly reproduces ciphertext.
- Padding is validated, not merely stripped.
- Recovered text decodes without ignored errors.

**Save:** `solution.txt`.

**AI prompt (paste your real output after it):**

> Trace this supplied block-cipher script. Make a table of input type, block size, key operation, padding, output encoding, and inverse operation. Do not guess the flag; require a round-trip test.

### Task 2 — Stream cipher correction

**Why:** A stream cipher depends on correct state and keystream generation.

**Do this:**

1. Preserve the original script and identify the intended algorithm.
2. Compare state initialization/update/output against the standard.
3. List every deviation with exact line numbers.
4. Fix a copy, generate the keystream, decrypt, and verify by re-encryption.

**Verification gate:**

- Corrected implementation passes a known test vector when available.
- Line-number explanations match the supplied file.
- Round-trip succeeds.

**Save:** `solution_stream.txt` and any correction notes requested.

**AI prompt (paste your real output after it):**

> Compare this educational stream-cipher code to the named standard. Identify deviations with exact line numbers, explain their effect on state/keystream, and propose the smallest correction. Require a test vector and round-trip.

### Task 3 — AES decryption

**Why:** AES mode, key, IV/nonce, padding, and encoding must all match.

**Do this:**

1. Inspect `4es.py` for key size, mode, IV/nonce, ciphertext encoding, and padding.
2. Decode the ciphertext representation before decrypting.
3. Use the exact inverse mode.
4. Validate and remove padding.
5. Write plaintext and mode, then re-encrypt to confirm.

**Verification gate:**

- Key/IV lengths match the mode.
- Re-encryption reproduces ciphertext.
- Mode is named and justified from code.

**Save:** `solution_aes.txt`.

**AI prompt (paste your real output after it):**

> Review this supplied AES script and extract key length, mode, IV/nonce, encoding, and padding. Build a safe local decrypt-and-reencrypt check. Do not infer missing values.

### Task 4 — Modes and vulnerability

**Why:** Mode behavior and nonce/IV reuse explain recognizable ciphertext patterns and practical failures.

**Do this:**

1. Classify each supplied mode script by its dependency pattern.
2. Use repeated plaintext blocks to observe whether ciphertext blocks repeat.
3. Document operator/mode mapping.
4. For `crypto_crack.py`, identify the concrete misuse, reproduce it only on supplied data, and recover the flag.
5. Record the faulty line and why it breaks security.

**Verification gate:**

- Mode classification matches code and experiment.
- The vulnerability is demonstrated on supplied inputs.
- Recovered text round-trips or otherwise satisfies an exact check.

**Save:** `operator.txt` and `crack.txt`.

**AI prompt (paste your real output after it):**

> Using only these supplied classroom scripts, classify each block mode from code/data dependencies and analyze the cryptographic misuse in `crypto_crack.py`. Cite exact lines, explain the security consequence, and require a reproducible local verification.

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

