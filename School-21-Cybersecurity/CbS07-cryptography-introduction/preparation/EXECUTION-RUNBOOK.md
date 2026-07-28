# CbS7 — Introduction to Cryptography: Execution Runbook

Preparation status: **complete**. Practical status: **execution pending** unless a task below is explicitly marked solved.

This guide converts the supplied School 21 brief into a later execution checklist. Expected values are not evidence; copy only observed results into final deliverables.

## Inputs needed later

Provided `crypto.py`, any supplied wordlist, Python, and official repository.

## Task-by-task plan

### Task 1 — Encodings

Prepared results: decimal ASCII → `School-21`; hexadecimal UTF-8 → `съешь ещё этих мягких французских булок, да выпей чаю`; Base64 of `Ехал Грека через реку` → `0JXRhdCw0Lsg0JPRgNC10LrQsCDRh9C10YDQtdC3INGA0LXQutGD`. Recheck byte-for-byte before submission.

### Task 2 — XOR

Prepared principles: a value XOR itself produces zero bits; `1010 XOR 0000 = 1010` is a valid four-bit example where the result equals an operand; `(A XOR B) XOR A = B`. The Russian phrase is UTF-8, not ASCII, although identical byte sequences still XOR to zero.

### Task 3 — Hashing

The digest has 128 hexadecimal characters, consistent with SHA-512. The password still requires authorized dictionary testing or supplied learning resources; do not invent it. Record tested method, wordlist, and result.

### Task 4 — Encryption

Inspect supplied `crypto.py`, identify the reversible XOR-based transformation, reproduce it in a separate checker, recover `flag`, and explain the inverse in `solution.txt`.

## Required deliverables

`encoding.txt`, `XorXor.txt`, optional AI dialogue/scripts, `password.txt`, and `solution.txt`.

## Verification gate

Decode/encode independently, test XOR algebra on bytes, recompute the recovered password hash, and run the original algorithm forward on the recovered flag.

## Evidence record

For every practical task record input filename/hash, lab version, exact command/configuration, expected result, observed result, screenshot/frame/log evidence, and final GitLab filename.

## Troubleshooting

Record **symptom → diagnostic → interpretation → change → retest**. Keep failed attempts when they explain the final fix. Never replace an observed value with an AI-generated value.

## Repository hygiene

Never publish real credentials, recovery keys, production private keys, personal data, or third-party scan results. Testing stays in an isolated authorized lab. The assigned GitLab repository, **develop** branch, **src** path, and exact filenames take precedence. A project is not complete until evidence and peer review confirm it.
