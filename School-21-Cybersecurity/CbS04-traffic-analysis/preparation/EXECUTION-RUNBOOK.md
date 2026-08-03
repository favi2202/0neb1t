# CbS4 — Traffic Analysis: Execution Runbook

Preparation status: **complete**. Practical status: **execution pending** unless a task below is explicitly marked solved.

This guide converts the supplied School 21 brief into a later execution checklist. Expected values are not evidence; copy only observed results into final deliverables.

## Inputs needed later

Supplied SMB and reverse-shell captures, Wireshark/tshark, Python, Scapy, and a disposable lab.

## Task-by-task plan

### Task 1 — Packet investigation

Hash the PCAP before analysis. Identify endpoints with Conversations, then filter `smb || smb2`. Record overall sequence, exact SMB dialect, Session ID, authenticated account, and both endpoint MAC addresses. Cite frame numbers in `report.docx`.

### Task 2 — Reverse-shell trace

Inspect `some_troubled_traffic.pcapng`, unusual long-lived TCP streams, and Follow TCP Stream. Record initiating IP, destination IP, protocol, and commands exactly as observed. Do not execute extracted commands.

### Task 3 — Scapy

Prepare a localhost-only packet to 127.0.0.1 TCP/12345 with the required Raw payload. Capture with `tcp port 12345`, retain exactly the intended message packet in `sent_message.pcapng`, and verify packet count/payload.

## Required deliverables

`report.docx`, `answers.txt`, `main.py`, and `sent_message.pcapng`.

## Verification gate

Reopen PCAPs, confirm frame numbers/stream direction, run `python3 -m py_compile main.py`, and verify the final capture contains one intended packet.

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

1. Gather: The supplied packet captures, Wireshark, Python 3, Scapy, and a disposable/local-only test environment.
2. Clone the official School 21 GitLab repository, create/use `develop`, and work only under `src` unless the official task says otherwise.
3. Copy supplied inputs before editing and record SHA-256 hashes when evidence integrity matters.
4. Take a VM/GNS3 snapshot or copy the working project before each major change.
5. Keep a scratch evidence note: **step → why → command/action → observed result → proof filename/frame**.

### Task 1 — SMB packet investigation

**Why:** Frame-based evidence teaches you to turn packets into a defensible timeline.

**Do this:**

1. Copy the original PCAP and calculate its SHA-256 before analysis.
2. Use Statistics → Endpoints/Conversations to identify the two systems.
3. Filter `smb || smb2`; follow the relevant stream/session.
4. Record dialect, Session ID, authenticated account, and both MAC addresses with exact frame numbers.
5. Write the report in your own words and insert only necessary screenshots.
6. Reopen the report and confirm every value against the capture.

**Verification gate:**

- Every conclusion cites a frame number.
- MAC/IP direction is consistent across Ethernet and IP layers.
- The report opens correctly and contains all requested answers.

**Save:** `report.docx`.

**AI prompt (paste your real output after it):**

> Analyze only the packet fields I paste from this authorized capture. Build a table with claim, exact value, frame number, and Wireshark field path. Mark anything not proven as unknown. Then ask me to verify each row in Wireshark.

### Task 2 — Reverse-shell trace

**Why:** Following a TCP stream reveals who initiated a session and what observable commands crossed the network.

**Do this:**

1. Hash `some_troubled_traffic.pcapng` and never execute extracted content.
2. Review conversations and unusually long or interactive TCP streams.
3. Use Follow TCP Stream and determine client/server direction from the first SYN.
4. Record initiating IP, destination IP, protocol, and commands exactly as visible.
5. Cross-check stream bytes with original frames and save concise answers.

**Verification gate:**

- The first SYN proves the initiator.
- Each command can be located in the stream and an exact frame.
- No command from the capture was executed.

**Save:** `answers.txt`.

**AI prompt (paste your real output after it):**

> I am analyzing an authorized training PCAP offline. From the TCP summary and sanitized stream text I paste, identify the likely interactive session, initiator, destination, protocol, and observable commands. Cite only provided frames and do not suggest executing payloads.

### Task 3 — Scapy localhost message

**Why:** Creating and capturing one local packet connects packet construction with Wireshark decoding.

**Do this:**

1. Write `main.py` to send the exact required Raw payload only to `127.0.0.1:12345/TCP`.
2. Compile it with `python3 -m py_compile main.py`.
3. Start capture on the loopback interface with `tcp port 12345`.
4. Run the script once, stop capture, and locate the intended payload packet.
5. Remove unrelated packets from the saved capture or recapture cleanly.
6. Reopen and verify payload and packet count.

**Verification gate:**

- Destination is exactly 127.0.0.1 TCP/12345.
- The required message is visible in Raw/TCP payload.
- Final capture contains exactly the evidence required by the task.

**Save:** `main.py` and `sent_message.pcapng`.

**AI prompt (paste your real output after it):**

> Review my Scapy script for a localhost-only lab. Check destination, TCP port, exact byte payload, accidental retransmission, and whether it sends more than intended. Explain corrections; do not change the task message.

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

