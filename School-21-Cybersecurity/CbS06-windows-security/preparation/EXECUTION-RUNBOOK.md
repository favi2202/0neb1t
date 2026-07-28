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
