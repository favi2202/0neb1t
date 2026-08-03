# CbS9 — Asymmetric Cryptography and PKI: Execution Runbook

Preparation status: **complete**. Practical status: **execution pending** unless a task below is explicitly marked solved.

This guide converts the supplied School 21 brief into a later execution checklist. Expected values are not evidence; copy only observed results into final deliverables.

## Inputs needed later

Provided `dh.py`, `crypto.py`, `ciphertext.txt`, Kali/OpenSSL, and official repository.

## Task-by-task plan

### Task 1 — RSA

Solved from the embedded values: because e=5 and the plaintext power is smaller than n, the exact integer fifth root of c is the message. Verified result: `S21{b1663r_15_n07_4lw4y5_b3773r}`. Exact fifth-power equality was checked.

### Task 2 — Diffie–Hellman

Inspect `dh.py`; compare both parties’ shared-secret formulas and modular exponent order. Record each faulty line number and full corrected line in `dh_answer.txt`. Source is required for exact line numbers.

### Task 3 — Fermat factorization

Set a=ceil(sqrt(N)), increment until a²−N is a square, obtain p=a−b and q=a+b, calculate d, and decrypt. Verify p×q=N and re-encryption. Save `fermat_attack.py`, `solution.txt`, and notes.

### Task 4 — OpenSSL tools

Generate a lab-only RSA-2048 key, convert to PEM, create CSR with O=School-21 and OU=CoolPeer, and issue a self-signed X.509 certificate. Never reuse the published lab private key.

### Task 5 — PKI

Create `pki/{certs,private,newcerts}`; generate AES-256-protected CA/server keys; create CA cert with School-21/RootCertificate; create server CSR with OtherSchool/SomeServer; sign and archive. Use passphrase `school21` only for this lab.

## Required deliverables

`RSA_cracked.txt`, `dh_answer.txt`, `solution.txt`, `fermat_attack.py`, lab PEM key/certificate, archived `pki`, AI logs, and optional `check_pki.sh`.

## Verification gate

Use exact-root checks, p×q=N, re-encryption, `openssl rsa -check`, `openssl req -text`, `openssl x509 -text`, and `openssl verify`.

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

1. Gather: Supplied `dh.py`, `crypto.py`, `ciphertext.txt`, Python 3, OpenSSL, and a lab-only workspace.
2. Clone the official School 21 GitLab repository, create/use `develop`, and work only under `src` unless the official task says otherwise.
3. Copy supplied inputs before editing and record SHA-256 hashes when evidence integrity matters.
4. Take a VM/GNS3 snapshot or copy the working project before each major change.
5. Keep a scratch evidence note: **step → why → command/action → observed result → proof filename/frame**.

### Task 1 — RSA exact-root case

**Why:** Small-exponent RSA fails when no modular wrap occurs; exact arithmetic proves the result.

**Do this:**

1. Recheck the supplied n, e, and c.
2. Calculate the exact integer fifth root.
3. Verify `m^5 == c` and `m < n`.
4. Convert integer to bytes/text and save the verified result.

**Verification gate:**

- Exact power equality holds.
- Byte conversion is reversible.
- Prepared flag matches the recomputation.

**Save:** `RSA_cracked.txt`.

**AI prompt (paste your real output after it):**

> Independently verify this educational RSA small-exponent result using integer arithmetic only. Show the exact-root check, integer-to-bytes step, and re-encryption equality; reject approximate floating-point roots.

### Task 2 — Diffie–Hellman code review

**Why:** Both parties must compute the same modular shared secret with correct exponentiation order.

**Do this:**

1. Hash/preserve `dh.py`.
2. Trace public values and each side’s shared-secret formula.
3. Compare both formulas mathematically.
4. Record faulty line numbers and corrected full lines.
5. Run a local equality test.

**Verification gate:**

- Alice and Bob produce exactly the same secret.
- Corrections reference real source lines.
- No secret is assumed without execution.

**Save:** `dh_answer.txt`.

**AI prompt (paste your real output after it):**

> Review this supplied Diffie–Hellman classroom script. Map each variable to private key, public value, modulus, generator, and shared secret. Find faulty lines, provide corrected full lines, and require both sides to produce identical output.

### Task 3 — Fermat factorization

**Why:** Close primes can make RSA factorization much easier than intended.

**Do this:**

1. Parse N and ciphertext from supplied files.
2. Implement integer-only ceil(sqrt(N)) and the a²−N square test.
3. Recover p/q and verify `p*q == N`.
4. Compute phi and private exponent d.
5. Decrypt and re-encrypt to verify.

**Verification gate:**

- Factor product equals N.
- `e*d mod phi == 1`.
- Re-encryption reproduces ciphertext.

**Save:** `fermat_attack.py` and `solution.txt`.

**AI prompt (paste your real output after it):**

> Review my Fermat-factorization script for an authorized RSA exercise. Check integer square tests, loop termination, p/q verification, modular inverse, byte conversion, and re-encryption. Do not provide an unverified plaintext.

### Task 4 — OpenSSL and PKI

**Why:** Certificates bind identities to public keys; a CA signs and enables verification.

**Do this:**

1. Use lab-only keys and the exact subject fields required by the task.
2. Generate RSA key, PEM conversion, CSR, and self-signed certificate for the tool task.
3. Build required `pki` directory and CA database files.
4. Generate encrypted CA/server keys with the assignment passphrase only in this disposable lab.
5. Sign the server CSR and archive exactly required files.
6. Inspect every key/CSR/cert and run certificate verification.

**Verification gate:**

- `openssl rsa -check` succeeds.
- CSR/certificate subjects match required O/OU/CN fields.
- `openssl verify` succeeds against the lab CA.

**Save:** Required PEM/CSR/certificate files, archived `pki`, AI logs, and optional checker; never reuse these keys elsewhere.

**AI prompt (paste your real output after it):**

> Audit these lab OpenSSL commands. Explain what each file contains, verify subject/issuer/key sizes/extensions, identify missing CA database steps, and provide inspection commands. Treat all keys as disposable classroom material.

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

