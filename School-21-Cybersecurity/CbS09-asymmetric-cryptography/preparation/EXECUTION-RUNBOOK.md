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
