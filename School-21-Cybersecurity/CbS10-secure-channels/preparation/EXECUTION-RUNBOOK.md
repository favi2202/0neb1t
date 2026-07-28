# CbS10 — Secure Channels: Execution Runbook

Preparation status: **complete**. Practical status: **execution pending** unless a task below is explicitly marked solved.

This guide converts the supplied School 21 brief into a later execution checklist. Expected values are not evidence; copy only observed results into final deliverables.

## Inputs needed later

Disposable Linux VM, Nginx, Wireshark, OpenVPN tooling, and licensed CryptoPro/NGate media if supplied.

## Task-by-task plan

### Task 1 — TLS

Install Nginx, create a lab certificate, configure HTTPS on 443, open the local page, capture the handshake, and trim to client↔server traffic. Verify handshake and encrypted application data in `my_website.pcapng`.

### Task 2 — OpenVPN

Build lab CA/server/client materials with O=School-21 and OU=cryptoProf, generate DH parameters, configure local server/client, connect, and verify tunnel addressing plus logs. Never reuse published private keys.

### Task 3 — CryptoPro NGate

Requires authorized media/license and official guide. Follow through step 15, use OU=MCPeer, export `root.cer`, `admin.cer`, and `mcradmin.000`, and keep the private container restricted to the assignment.

### Task 4 — Bonus

Complete administrator-workstation linkage only when the licensed environment exists. Capture `admin_cert.png` and `control_panel.png` with required details while excluding unrelated personal data.

## Required deliverables

`my_website.pcapng`; `server/` and `client/` OpenVPN materials; NGate certificate/container files; optional screenshots.

## Verification gate

Use `nginx -t`, `openssl s_client`, Wireshark TLS filters, OpenVPN logs/routes/ping, and certificate-detail inspection. CryptoPro tasks are license/environment pending.

## Evidence record

For every practical task record input filename/hash, lab version, exact command/configuration, expected result, observed result, screenshot/frame/log evidence, and final GitLab filename.

## Troubleshooting

Record **symptom → diagnostic → interpretation → change → retest**. Keep failed attempts when they explain the final fix. Never replace an observed value with an AI-generated value.

## Repository hygiene

Never publish real credentials, recovery keys, production private keys, personal data, or third-party scan results. Testing stays in an isolated authorized lab. The assigned GitLab repository, **develop** branch, **src** path, and exact filenames take precedence. A project is not complete until evidence and peer review confirm it.
