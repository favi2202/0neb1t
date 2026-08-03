# CbS6 — Windows Security: Execution Runbook

Preparation status: **complete**. Practical status: **execution pending** unless a task below is explicitly marked solved.

This guide converts the supplied School 21 brief into a later execution checklist. Expected values are not evidence; copy only observed results into final deliverables.

## Inputs needed later

Windows Pro/Enterprise-capable disposable VM, administrator account, snapshot, and a non-production volume for BitLocker.

## Task-by-task plan

### Task 1 — Security policy

Configure minimum password length 8, complexity enabled, and maximum age 30 days. Build `get_sec_pol.ps1` with an administrator check and export the effective policy to `secpol.txt`.

### Task 2 — BitLocker

Encrypt only the designated lab volume with a password protector, save the recovery key outside the repository, and export `manage-bde -status` to `crypt.txt`. Never publish the recovery key.

### Task 3 — User rights

Create/enable Guest if required; deny network logon to Guest; limit backup rights to Administrators; disable shutdown without logon; and deny RDP to Users. Export effective result to `secpol_2.txt`.

### Task 4 — Firewall

Create exactly `Block_http_conn`, `Allow_rdp_conn`, `Block_ftp_conn`, and `Block_ping_conn`. Build `get_fw_rules.ps1` to select only these names and print requested fields into `result.txt`.

## Required deliverables

`get_sec_pol.ps1`, `secpol.txt`, `crypt.txt`, `secpol_2.txt`, `get_fw_rules.ps1`, and `result.txt`.

## Verification gate

Use `secedit /export`, `net accounts`, `manage-bde -status`, `Get-NetFirewallRule`, and `Get-NetFirewallPortFilter`; do not claim settings applied before real VM output exists.

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

1. Gather: A disposable Windows Pro/Enterprise VM, administrator access, a snapshot, and a non-production volume.
2. Clone the official School 21 GitLab repository, create/use `develop`, and work only under `src` unless the official task says otherwise.
3. Copy supplied inputs before editing and record SHA-256 hashes when evidence integrity matters.
4. Take a VM/GNS3 snapshot or copy the working project before each major change.
5. Keep a scratch evidence note: **step → why → command/action → observed result → proof filename/frame**.

### Task 1 — Password/security policy

**Why:** Local policy establishes a minimum authentication baseline.

**Do this:**

1. Snapshot the VM and open the correct local security policy tools.
2. Set minimum length 8, complexity enabled, and maximum age 30 days.
3. Run policy refresh if needed.
4. Write `get_sec_pol.ps1` with an administrator check and an effective-policy export.
5. Run it from an elevated PowerShell session and save `secpol.txt`.
6. Compare GUI settings with exported values.

**Verification gate:**

- `net accounts`/exported policy shows the requested values.
- The script clearly stops when not elevated.
- `secpol.txt` contains real VM output.

**Save:** `get_sec_pol.ps1` and `secpol.txt`.

**AI prompt (paste your real output after it):**

> Review this PowerShell security-policy export script. Check elevation detection, reliable command output, file encoding, error handling, and whether it proves the effective values rather than only desired settings.

### Task 2 — BitLocker lab volume

**Why:** Volume encryption protects data if the storage device is lost.

**Do this:**

1. Use only the designated non-production lab volume.
2. Enable BitLocker with the assignment protector.
3. Store the recovery key outside Git and verify it is readable.
4. Wait for encryption to complete.
5. Run `manage-bde -status` and save the complete status as `crypt.txt`.
6. Test unlock/recovery only according to the official VM guide.

**Verification gate:**

- Correct lab volume is encrypted.
- Protection status is On and conversion is complete.
- No recovery key appears in repository files/screenshots.

**Save:** `crypt.txt` only; never publish the recovery key.

**AI prompt (paste your real output after it):**

> Interpret this sanitized `manage-bde -status` output. Explain conversion status, encryption method, protection status, and protectors. Tell me what is still incomplete without asking for or exposing the recovery key.

### Task 3 — User rights

**Why:** User-right assignments enforce who may log on, back up, shut down, or use RDP.

**Do this:**

1. Apply each requested local user-right rule one at a time.
2. Record the before/after policy name and assigned group.
3. Refresh policy and test with safe lab accounts when possible.
4. Run the Task 1 export script again.
5. Save the resulting effective policy as `secpol_2.txt`.
6. Check that UAC remains enabled.

**Verification gate:**

- Guest/network logon, backup rights, shutdown, and RDP rights match the task.
- The export proves the change.
- Normal administrator access remains available.

**Save:** `secpol_2.txt` plus the existing script.

**AI prompt (paste your real output after it):**

> Check this Windows user-rights export against these requirements: deny Guest network logon, backup rights only for Administrators, no shutdown without logon, and deny RDP to Users. Map each requirement to the exact policy and flag conflicts.

### Task 4 — Named firewall rules

**Why:** Windows Firewall rules demonstrate explicit allow/deny policy and reproducible reporting.

**Do this:**

1. Create exactly the four rule names required by the assignment.
2. Set direction, action, protocol, ports, and profiles carefully.
3. Test each rule in the disposable VM.
4. Write `get_fw_rules.ps1` to select only those exact names.
5. Join rule data with port-filter data and export requested fields to `result.txt`.
6. Rerun and confirm no unrelated rules appear.

**Verification gate:**

- All four rules exist and are enabled as required.
- Protocol/ports/actions/profiles are correct.
- `result.txt` contains only the four rules.

**Save:** `get_fw_rules.ps1` and `result.txt`.

**AI prompt (paste your real output after it):**

> Review my four Windows Firewall rules and reporting script. Verify exact names, direction, protocol, local/remote ports, action, profile, and enabled state. Explain any mismatch and give a safe test for each rule.

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

