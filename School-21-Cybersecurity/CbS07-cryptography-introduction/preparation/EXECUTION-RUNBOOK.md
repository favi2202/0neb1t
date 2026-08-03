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


<!-- independent-guide-v2 -->
## Independent step-by-step guide

Use this section when no assistant is available. Work on **one task at a time** and do not move forward until its verification gate passes.

### Before starting

1. Gather: The official repository, supplied `crypto.py` and wordlist if present, and Python 3.
2. Clone the official School 21 GitLab repository, create/use `develop`, and work only under `src` unless the official task says otherwise.
3. Copy supplied inputs before editing and record SHA-256 hashes when evidence integrity matters.
4. Take a VM/GNS3 snapshot or copy the working project before each major change.
5. Keep a scratch evidence note: **step → why → command/action → observed result → proof filename/frame**.

### Task 1 — Encodings

**Why:** Encoding changes representation, not secrecy; byte accuracy matters.

**Do this:**

1. Solve decimal ASCII, hexadecimal UTF-8, and Base64 parts manually first.
2. Use a small independent Python check only after writing your answer.
3. Compare byte-for-byte, including spaces and Cyrillic encoding.
4. Record both method and final result in the required file.

**Verification gate:**

- Decoding the result recreates the exact original text.
- UTF-8 is used for Cyrillic.
- No invisible newline changes the Base64 value.

**Save:** `encoding.txt` and any required AI log.

**AI prompt (paste your real output after it):**

> Verify these encoding answers independently. Show the byte sequence, transformation, and reverse check. Do not replace my work silently; point out the first differing byte or character.

### Task 2 — XOR properties

**Why:** XOR is reversible and operates on bits/bytes, which explains many simple ciphers.

**Do this:**

1. Write the truth table and solve each property manually.
2. Demonstrate self-XOR, XOR with zero, and cancellation.
3. For text, explicitly encode to bytes before XOR.
4. Reverse every example to prove it.

**Verification gate:**

- Each example has equal-length bit/byte operands.
- The inverse operation recovers the input.
- The explanation distinguishes characters from UTF-8 bytes.

**Save:** `XorXor.txt`.

**AI prompt (paste your real output after it):**

> Check my XOR reasoning using bit-level examples and UTF-8 bytes. Verify each equality in both directions and explain any confusion between a character and its encoded bytes.

### Task 3 — Hash identification and authorized cracking

**Why:** Hash length/format suggests an algorithm, while verification requires recomputing the digest.

**Do this:**

1. Record digest length and identify plausible algorithm(s).
2. Use only the supplied/authorized wordlist and local hash-checking method.
3. Log the method and candidate count; do not use unrelated leaked credentials.
4. Recompute the digest of the recovered candidate and compare exactly.

**Verification gate:**

- Candidate digest exactly equals the target.
- Algorithm and text encoding are documented.
- No invented password is submitted.

**Save:** `password.txt`.

**AI prompt (paste your real output after it):**

> I have an authorized School 21 hash exercise. From the digest format and the supplied wordlist details I paste, help identify the algorithm and design a local verification workflow. Do not use external leaked credentials or claim a password without an exact digest match.

### Task 4 — Reverse supplied crypto.py

**Why:** Understanding the forward transformation tells you how to construct its inverse.

**Do this:**

1. Hash/copy the supplied script before editing.
2. Trace input, encoding, key, loop/order, and output format line by line.
3. Write a separate inverse/checker rather than damaging the original.
4. Recover the flag, then run the forward algorithm on it.
5. Explain the inverse operations in plain language.

**Verification gate:**

- Forward(recovered plaintext) reproduces original ciphertext.
- Every inverse step corresponds to a visible source line.
- The original source remains unchanged.

**Save:** `solution.txt` and required script/log evidence.

**AI prompt (paste your real output after it):**

> Analyze only this supplied educational `crypto.py`. Describe the data flow line by line, identify reversible operations, and help me build an inverse checker. Mark assumptions and require a forward round-trip before accepting the recovered flag.

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

