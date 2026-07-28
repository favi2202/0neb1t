# CbS5 — Linux Security: Execution Runbook

Preparation status: **complete**. Practical status: **execution pending** unless a task below is explicitly marked solved.

This guide converts the supplied School 21 brief into a later execution checklist. Expected values are not evidence; copy only observed results into final deliverables.

## Inputs needed later

Disposable Linux VM with snapshot, root access for the lab, and a test email account or local mail sink.

## Task-by-task plan

### Task 1 — Inventory script

Create `get_all_info.sh` with root check, package-manager detection, package/process/listening-port/kernel/OS collection, installation of `cowsay` and `sl`, creation of `info`, and `OS_RESULT.tar`. Keep stderr useful and quote variables.

### Task 2 — Users and permissions

Make operations idempotent. Create both groups and all requested users, assign memberships, set group-controlled home access, install/check Apache, and validate sudoers with `visudo -cf`. The broad `/var` requirement is unsafe on a real system; reproduce it only in the disposable VM and document the risk.

### Task 3 — Monitoring

Configure logwatch and Postfix at maximum detail, test mail delivery, then add the exact midnight cron entry to `cron.txt`. Never commit mail passwords or provider tokens.

### Task 4 — Built-in protection

Create a lab-only SSH key pair, test public-key login before disabling passwords, and block inbound TCP/80 with INPUT. Export sanitized `sshd_config`, the lab public key in `authorized_keys`, and relevant iptables output.

## Required deliverables

`get_all_info.sh`, `OS_RESULT.tar`, setup `.sh`, `main.cf`, `cron.txt`, `sshd_config`, `authorized_keys`, and `iptables.txt`.

## Verification gate

Run ShellCheck when available; test scripts twice; inspect `tar -tf`; use `id`, `getent`, `systemctl`, `visudo -cf`, a second SSH session, and iptables counters.

## Evidence record

For every practical task record input filename/hash, lab version, exact command/configuration, expected result, observed result, screenshot/frame/log evidence, and final GitLab filename.

## Troubleshooting

Record **symptom → diagnostic → interpretation → change → retest**. Keep failed attempts when they explain the final fix. Never replace an observed value with an AI-generated value.

## Repository hygiene

Never publish real credentials, recovery keys, production private keys, personal data, or third-party scan results. Testing stays in an isolated authorized lab. The assigned GitLab repository, **develop** branch, **src** path, and exact filenames take precedence. A project is not complete until evidence and peer review confirm it.
