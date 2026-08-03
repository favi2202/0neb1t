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


<!-- independent-guide-v2 -->
## Independent step-by-step guide

Use this section when no assistant is available. Work on **one task at a time** and do not move forward until its verification gate passes.

### Before starting

1. Gather: A disposable Linux VM snapshot, sudo/root access inside that VM, and no production credentials.
2. Clone the official School 21 GitLab repository, create/use `develop`, and work only under `src` unless the official task says otherwise.
3. Copy supplied inputs before editing and record SHA-256 hashes when evidence integrity matters.
4. Take a VM/GNS3 snapshot or copy the working project before each major change.
5. Keep a scratch evidence note: **step → why → command/action → observed result → proof filename/frame**.

### Task 1 — System inventory script

**Why:** A repeatable inventory is the foundation for hardening and incident response.

**Do this:**

1. Snapshot the VM and identify its package manager.
2. Write `get_all_info.sh` with a root check and clear error handling.
3. Collect packages, processes, listening ports, kernel, and OS information.
4. Install/check the requested packages, write output to `info`, and archive it as `OS_RESULT.tar`.
5. Run ShellCheck if available and execute the script twice to test idempotency.
6. Inspect the archive before submission.

**Verification gate:**

- Script refuses unsafe non-root execution when required.
- `tar -tf OS_RESULT.tar` lists `info`.
- Output contains every category requested by the task.

**Save:** `get_all_info.sh` and `OS_RESULT.tar`.

**AI prompt (paste your real output after it):**

> Audit this Bash inventory script line by line. Check root detection, quoting, package-manager handling, command failures, repeat runs, output redirection, and archive contents. Explain each issue before proposing a minimal fix.

### Task 2 — Users and permissions

**Why:** Correct ownership and least privilege prevent users from reading or changing unrelated data.

**Do this:**

1. Create the required users/groups exactly as named in the assignment.
2. Add memberships and confirm with `id`/`getent group`.
3. Apply group-controlled home permissions; test access as both allowed and disallowed users.
4. Install/check Apache if requested and validate its service state.
5. Edit sudoers only through a drop-in or `visudo`, then run `visudo -cf`.
6. Perform the broad `/var` permission requirement only in the disposable VM, record why it is unsafe in real systems, and test the script twice.

**Verification gate:**

- Allowed users can access only what the task permits.
- Disallowed users receive permission denied.
- Sudoers validates with no syntax errors.

**Save:** One setup `.sh` script with the exact filename permitted by the task.

**AI prompt (paste your real output after it):**

> I am working in a disposable School 21 Linux VM. Review my user/group/permission script for idempotency and least privilege. Flag destructive or overly broad commands, especially changes under `/var`, explain the real-world risk, and show how to verify each assignment requirement safely.

### Task 3 — Daily monitoring

**Why:** Automated reports make configuration drift and system problems visible.

**Do this:**

1. Install/configure Logwatch and Postfix using the assignment settings.
2. Use a local mail sink or test account; never store a real password/token in the repository.
3. Generate one report manually before scheduling.
4. Verify mail logs and receipt.
5. Create the exact daily cron entry and copy only that entry to `cron.txt`.
6. Export the sanitized Postfix configuration.

**Verification gate:**

- Manual report succeeds.
- Mail logs show successful local/test delivery.
- `crontab -l` contains the intended schedule.

**Save:** `main.cf` and `cron.txt`.

**AI prompt (paste your real output after it):**

> Check my Logwatch/Postfix/cron lab configuration. Explain the mail flow, validate cron syntax, identify secrets that must be removed, and give verification commands using only a local or test mailbox.

### Task 4 — SSH keys and firewall

**Why:** Key authentication and an explicit firewall reduce exposed attack surface.

**Do this:**

1. Generate a new lab-only SSH key pair.
2. Install the public key and prove a second key-based session works.
3. Back up `sshd_config`; disable password authentication only after the key test.
4. Validate with `sshd -t` before restarting/reloading SSH.
5. Add the requested INPUT rule for TCP/80 without locking out SSH.
6. Test allowed SSH and blocked HTTP, then export sanitized evidence.

**Verification gate:**

- A new key-based SSH session succeeds.
- `sshd -t` returns no error.
- iptables counters increase when the blocked test is attempted.

**Save:** `sshd_config`, lab public `authorized_keys`, and `iptables.txt`; never submit the private key.

**AI prompt (paste your real output after it):**

> Review my sanitized SSH and iptables configuration for a disposable VM. Check lockout risk, rule order, key permissions, and whether password login is truly disabled. Give a rollback command before any risky change.

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

