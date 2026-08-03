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


<!-- independent-guide-v2 -->
## Independent step-by-step guide

Use this section when no assistant is available. Work on **one task at a time** and do not move forward until its verification gate passes.

### Before starting

1. Gather: Disposable Linux VM(s), Nginx, OpenSSL/Wireshark, OpenVPN tools, and authorized CryptoPro/NGate media if supplied.
2. Clone the official School 21 GitLab repository, create/use `develop`, and work only under `src` unless the official task says otherwise.
3. Copy supplied inputs before editing and record SHA-256 hashes when evidence integrity matters.
4. Take a VM/GNS3 snapshot or copy the working project before each major change.
5. Keep a scratch evidence note: **step → why → command/action → observed result → proof filename/frame**.

### Task 1 — HTTPS/TLS capture

**Why:** TLS protects HTTP in transit after certificate and key negotiation.

**Do this:**

1. Create a snapshot and install Nginx/OpenSSL.
2. Generate a lab-only certificate/key with task fields.
3. Configure Nginx HTTPS on 443 and run `nginx -t`.
4. Test locally with a browser and `openssl s_client`.
5. Capture only the lab client/server TLS flow.
6. Reopen capture and identify handshake plus encrypted application data.

**Verification gate:**

- Nginx config validates.
- Certificate subject/issuer and dates are correct.
- Capture shows TLS handshake and encrypted data, not plaintext HTTP content.

**Save:** `my_website.pcapng` and any required config/evidence; do not publish a reusable private key.

**AI prompt (paste your real output after it):**

> Review my lab Nginx TLS configuration and sanitized handshake fields. Check certificate/key paths, protocol/port, validation output, capture filter, and which frames prove negotiation and encrypted application data.

### Task 2 — OpenVPN tunnel

**Why:** A VPN creates an encrypted virtual interface and routes selected traffic through it.

**Do this:**

1. Create lab CA/server/client materials with exact subject fields.
2. Generate DH/required parameters and configs.
3. Start server, then client; read logs before changing anything.
4. Verify tunnel interfaces, assigned addresses, routes, and ping.
5. Capture only the lab exchange if required.
6. Archive only assignment materials and clearly label private lab keys.

**Verification gate:**

- Client log reports successful initialization.
- Tunnel interfaces/routes exist.
- Traffic crosses the intended tunnel subnet.

**Save:** Required `server/` and `client/` materials.

**AI prompt (paste your real output after it):**

> Troubleshoot this isolated OpenVPN lab using my sanitized server/client logs and configs. Check certificates, time, cipher/auth compatibility, ports, routes, and firewall in that order. Explain one test at a time.

### Task 3 — CryptoPro NGate

**Why:** This task depends on licensed vendor software and official installation steps.

**Do this:**

1. Do not download unofficial installers or bypass licensing.
2. Obtain the exact authorized media, license, and official guide from School 21.
3. Snapshot before installation and record product/version.
4. Follow the required steps and exact OU/subject values.
5. Export only the required certificate/container artifacts.
6. Remove license identifiers and unrelated personal information from screenshots.

**Verification gate:**

- Product/service status is healthy.
- Certificate fields match the assignment.
- Required exports open and are not empty.

**Save:** `root.cer`, `admin.cer`, `mcradmin.000`, and required evidence.

**AI prompt (paste your real output after it):**

> I am following the authorized CryptoPro NGate classroom guide. Using only the installation step/output I paste, explain what the step does, what success looks like, and what non-sensitive evidence to save. Do not suggest unofficial downloads, license bypasses, or invented results.

### Task 4 — Bonus administrator linkage

**Why:** Linking the administrator workstation proves certificate-based management works end to end.

**Do this:**

1. Attempt only after the licensed core installation works.
2. Follow the official bonus sequence.
3. Verify certificate enrollment and management access.
4. Capture only required UI sections.
5. Record failure honestly if the environment/license is unavailable.

**Verification gate:**

- Certificate details are visible and valid.
- Control panel proves the required connection.
- Screenshots contain no unrelated personal data.

**Save:** `admin_cert.png` and `control_panel.png` when completed.

**AI prompt (paste your real output after it):**

> Review these sanitized bonus-task screenshots and certificate fields against the stated requirements. List what is proven, what is missing, and the next official-guide step; never fabricate a successful connection.

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

