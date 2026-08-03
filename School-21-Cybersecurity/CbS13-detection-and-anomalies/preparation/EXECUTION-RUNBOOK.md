# CbS13 — Detection and Anomalies: Execution Runbook

Preparation status: **complete**. Practical status: **execution pending** unless a task below is explicitly marked solved.

This guide converts the supplied School 21 brief into a later execution checklist. Expected values are not evidence; copy only observed results into final deliverables.

## Inputs needed later

Provided `file1.bin`–`file3.bin`, `malicious_traffic.pcap`, YARA, Suricata, Python, pynput, and an isolated VM.

## Task-by-task plan

### Task 1 — YARA

Hash samples, extract candidate strings/hex sequences without executing files, select one unique text string and one unique hex sequence per rule, and include filesize in one rule. Test each rule against all three samples plus benign controls; one rule must match exactly one target.

### Task 2 — Suricata

Identify four suspicious packets with frame numbers and stable payload/header indicators. Write distinct SIDs in `peer.rules`, run Suricata offline with the supplied PCAP/rules, and confirm all four intended alerts in `fast.log` without broad false positives.

### Task 3 — UBA

Record inter-key timing for two entries of the same string, compare interval arrays, define and document mean deviation, and print the exact required message above/below threshold 0.1. Handle backspace, mismatch, empty/one-character input, and cleanup.

## Required deliverables

`file1_rule.yar`, `file2_rule.yar`, `file3_rule.yar`, `peer.rules`, and `UBA.py`.

## Verification gate

Create a 3×3 YARA match matrix plus benign tests, count four Suricata alert groups, compile/test Python, and document timing formula/units.

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

1. Gather: Supplied samples/PCAP, YARA, Suricata, Python, and an isolated disposable VM.
2. Clone the official School 21 GitLab repository, create/use `develop`, and work only under `src` unless the official task says otherwise.
3. Copy supplied inputs before editing and record SHA-256 hashes when evidence integrity matters.
4. Take a VM/GNS3 snapshot or copy the working project before each major change.
5. Keep a scratch evidence note: **step → why → command/action → observed result → proof filename/frame**.

### Task 1 — YARA rules

**Why:** Good signatures use stable, distinctive evidence and are tested against both target and benign files.

**Do this:**

1. Hash samples and never execute them.
2. Extract printable strings/hex sequences offline.
3. Choose one unique text and one unique hex indicator per requested rule; add filesize where required.
4. Write rules with metadata and clear conditions.
5. Test a 3×3 sample matrix plus benign controls.
6. Tune until the required selectivity is achieved.

**Verification gate:**

- Each rule matches its intended target(s) only.
- Rule syntax validates.
- Indicators can be located in the corresponding file.

**Save:** `file1_rule.yar`, `file2_rule.yar`, and `file3_rule.yar`.

**AI prompt (paste your real output after it):**

> Review these YARA rules against the sanitized match matrix and extracted indicators. Check syntax, uniqueness, condition logic, filesize use, false positives, and explain why each string is stable. Do not execute samples.

### Task 2 — Suricata offline rules

**Why:** Network signatures should match stable malicious indicators without alerting on unrelated traffic.

**Do this:**

1. Hash and open `malicious_traffic.pcap` offline.
2. Identify four suspicious packets with frame numbers.
3. Select stable header/payload indicators.
4. Write distinct SIDs and descriptive messages in `peer.rules`.
5. Run Suricata offline with the supplied PCAP.
6. Confirm four intended alert groups and tune broad rules.

**Verification gate:**

- Suricata loads rules without error.
- `fast.log` shows intended alerts/SIDs.
- Benign packets are not matched by overly broad conditions.

**Save:** `peer.rules`.

**AI prompt (paste your real output after it):**

> Audit these Suricata rules for an offline classroom PCAP. Check direction, protocol, ports, content modifiers, flow, SID uniqueness, and false-positive scope. Tie each rule to the exact packet evidence I paste.

### Task 3 — Typing-behavior anomaly

**Why:** Inter-key timing is a simple behavioral feature whose reliability depends on consistent measurement.

**Do this:**

1. Record timestamps for two entries of the same expected string.
2. Convert them into interval arrays.
3. Implement and document the exact mean-deviation formula.
4. Handle backspace, mismatch, empty, and one-character cases.
5. Compare to threshold 0.1 and print exact required messages.
6. Test with deterministic sample intervals plus real input.

**Verification gate:**

- Both arrays use the same units and alignment.
- Edge cases do not crash.
- Threshold branches print exact required text.

**Save:** `UBA.py`.

**AI prompt (paste your real output after it):**

> Review my typing-timing anomaly script for privacy and correctness. Check timestamp source, interval alignment, units, deviation formula, threshold 0.1, backspace/mismatch/short-input handling, and exact output messages. Do not store actual typed content beyond the lab need.

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

