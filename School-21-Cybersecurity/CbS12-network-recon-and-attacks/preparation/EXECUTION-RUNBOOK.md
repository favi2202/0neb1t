# CbS12 — Network Reconnaissance and Attack Analysis: Execution Runbook

Preparation status: **complete**. Practical status: **execution pending** unless a task below is explicitly marked solved.

This guide converts the supplied School 21 brief into a later execution checklist. Expected values are not evidence; copy only observed results into final deliverables.

## Inputs needed later

Strictly isolated authorized lab, supplied PCAP/files, test MongoDB instance with no real data, and local mitmproxy endpoints.

## Task-by-task plan

### Task 1 — MITRE ATT&CK

Map eight scenarios to tactic/technique IDs in `my_mitre.txt`. Use the official current MITRE Enterprise matrix during execution because IDs/relationships can change; explain each primary mapping and omit sub-techniques.

### Task 2 — MongoDB scanner

Build `scan.py` for an explicitly supplied private lab CIDR only. Require a target argument, reject public ranges by default, use bounded timeouts/concurrency, test TCP/27017, and report only anonymous lab instances. Include instructions.

### Task 3 — MITM lab

Use mitmproxy only between your own local test client and form server. Log field names and redact password/token values; do not collect real credentials. Confirm with synthetic data.

### Task 4 — Detection

Analyze `good_traffic.pcap` offline, identify malicious sequence and flag, and name the defensive control. Cite frame numbers and observed indicators.

### Task 5 — Bonus

Document FOFA query syntax conceptually. Do not interact with or publish a live third-party vulnerable host; use an authorized lab/example reserved address if reviewer permits.

## Required deliverables

`my_mitre.txt`, `scan.py` plus instructions, `interceptor.py`, `solution.txt`, and optional `i_found_it.txt`.

## Verification gate

Unit-test CIDR validation, scan only owned lab, use synthetic forms, reopen PCAP evidence, and validate mappings against official MITRE pages.

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

1. Gather: Only a strictly isolated, authorized lab; supplied PCAP/files; a local test MongoDB; and synthetic mitmproxy endpoints.
2. Clone the official School 21 GitLab repository, create/use `develop`, and work only under `src` unless the official task says otherwise.
3. Copy supplied inputs before editing and record SHA-256 hashes when evidence integrity matters.
4. Take a VM/GNS3 snapshot or copy the working project before each major change.
5. Keep a scratch evidence note: **step → why → command/action → observed result → proof filename/frame**.

### Task 1 — MITRE ATT&CK mapping

**Why:** MITRE gives a consistent language for describing attacker goals and methods.

**Do this:**

1. Read each scenario and highlight the observable action.
2. Select the primary Enterprise tactic and technique from the official matrix.
3. Record ID, name, and one-sentence evidence mapping.
4. Do not add sub-techniques if prohibited.
5. Recheck all eight mappings against the current official matrix.

**Verification gate:**

- Each mapping is supported by exact scenario evidence.
- Tactic and technique roles are not confused.
- All required cases are present.

**Save:** `my_mitre.txt`.

**AI prompt (paste your real output after it):**

> Map these classroom scenarios to current MITRE Enterprise ATT&CK. For each, provide primary tactic, primary technique ID/name, and one-sentence evidence. Mark ambiguity and do not invent sub-techniques when the task excludes them.

### Task 2 — Private-lab MongoDB scanner

**Why:** A bounded scanner teaches service discovery without touching unauthorized systems.

**Do this:**

1. Require an explicit target CIDR argument.
2. Reject public/non-lab ranges by default; allow only the exact owned lab network.
3. Use short timeouts and bounded concurrency.
4. Check TCP/27017 and only the anonymous-access condition required by the task.
5. Test against your own configured lab service and a closed-port control.
6. Document authorization and usage.

**Verification gate:**

- Public targets are rejected.
- Lab open/closed controls are reported correctly.
- Errors/timeouts do not crash the script.

**Save:** `scan.py` plus instructions.

**AI prompt (paste your real output after it):**

> Review this network scanner strictly for an owned RFC1918 lab. Check target validation, public-range rejection, timeouts, concurrency bounds, error handling, and proof that it cannot scan arbitrary Internet ranges. Do not expand its scope.

### Task 3 — Synthetic MITM exercise

**Why:** A controlled proxy shows why unencrypted or improperly trusted traffic can expose form data.

**Do this:**

1. Run a local test form with fake values only.
2. Place mitmproxy between your own client and server.
3. Write `interceptor.py` to log required field names while redacting password/token values.
4. Submit synthetic form data and verify the proxy event.
5. Stop the proxy and delete temporary fake secrets.

**Verification gate:**

- Only local lab endpoints appear.
- Sensitive values are redacted.
- Expected synthetic request is observed.

**Save:** `interceptor.py`.

**AI prompt (paste your real output after it):**

> Review this local-only mitmproxy addon. Ensure it handles only my synthetic lab traffic, redacts credential values, records required metadata, and does not persist sensitive headers or bodies.

### Task 4 — Offline malicious-traffic analysis

**Why:** PCAP evidence can reveal attack stages and the control that would detect or prevent them.

**Do this:**

1. Hash `good_traffic.pcap` and analyze offline.
2. Use endpoints/conversations/protocol hierarchy to find anomalies.
3. Build a frame-numbered sequence of suspicious events.
4. Extract the flag only from observed bytes.
5. Name a defensive control and tie it to the exact indicator.

**Verification gate:**

- Every claim has a frame/filter.
- Direction and timing are consistent.
- Flag is copied exactly from evidence.

**Save:** `solution.txt`.

**AI prompt (paste your real output after it):**

> Analyze only the sanitized packet fields I paste from this authorized PCAP. Build a timeline with frame, source, destination, protocol, observable, interpretation, and confidence. Separate detection from prevention and never invent a flag.

### Task 5 — Bonus search syntax

**Why:** Search-engine syntax can be documented without probing third-party vulnerable systems.

**Do this:**

1. Describe FOFA query components conceptually.
2. Use reserved/example addresses or your owned lab.
3. Do not contact or publish a live third-party vulnerable target.
4. Record why authorization matters.

**Verification gate:**

- Example is non-routable or owned.
- No third-party host is tested.
- Syntax explanation matches the task.

**Save:** Optional `i_found_it.txt` only if completed within authorization.

**AI prompt (paste your real output after it):**

> Explain the requested FOFA query syntax using placeholders and reserved example addresses only. Do not identify or test a real vulnerable third-party system.

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

