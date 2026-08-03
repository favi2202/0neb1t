# CbS18 — Social Engineering and OSINT: Execution Runbook

Preparation status: **complete**. Practical status: **execution pending** unless a task below is explicitly marked solved.

This guide converts the supplied School 21 brief into a later execution checklist. Expected values are not evidence; copy only observed results into final deliverables.

## Inputs needed later

`osint1-5.jpg`, `no_sniff_dump.pcap`, Wireshark/tshark, and official repository.

## Task-by-task plan

### Task 1 — OSINT

Preserve hashes/metadata for each image, then use visible language, road signs, architecture, terrain, transit, storefront, and map clues. Record country, region, locality, evidence, confidence, and alternative hypothesis. Do not identify private people or expose personal data.

### Task 2 — Phishing awareness

Create a clearly labeled training simulation with fictional names and no working links, credentials, QR codes, or real access workflow. Highlight at least two indicators such as urgency and false authority, and add reviewer notes explaining them. Keep it inside School 21 review context.

### Task 3 — Sniffer detection

Analyze PCAP offline. Start with endpoint/MAC statistics, ARP anomalies, duplicate IP-to-MAC mappings, unsolicited/probe patterns, and stream direction. Compare suspicious behavior against routers/bridges before deciding. Record MAC plus frame-based justification.

## Required deliverables

`I_am_osinter.txt`, `email_for_you.md`, AI dialogue, `sniffer_detector.txt`, and analysis notes.

## Verification gate

Require two independent clues per image, label confidence, preserve simulation warning, and cite exact frames/filters for suspected sniffer. Conclusions remain input pending.

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

1. Gather: The supplied images and PCAP, offline analysis tools, and the official repository.
2. Clone the official School 21 GitLab repository, create/use `develop`, and work only under `src` unless the official task says otherwise.
3. Copy supplied inputs before editing and record SHA-256 hashes when evidence integrity matters.
4. Take a VM/GNS3 snapshot or copy the working project before each major change.
5. Keep a scratch evidence note: **step → why → command/action → observed result → proof filename/frame**.

### Task 1 — Image OSINT

**Why:** Geolocation should rely on multiple independent clues and calibrated confidence.

**Do this:**

1. Hash/preserve each image and inspect available metadata.
2. List visible language, signs, road markings, architecture, terrain, transit, and storefront clues.
3. Form at least two hypotheses.
4. Use maps/search only for public-place comparison; do not identify private people.
5. Require two independent clues before selecting country/region/locality.
6. Record alternatives and confidence.

**Verification gate:**

- Two independent clues support each conclusion.
- Private individuals are not identified.
- Uncertainty is explicit.

**Save:** `I_am_osinter.txt`.

**AI prompt (paste your real output after it):**

> Analyze only the public-place clues I describe from this classroom image. Build a clue table with observation, possible meaning, alternative, confidence, and a safe public source to verify. Do not identify people, homes, or expose personal data.

### Task 2 — Phishing-awareness simulation

**Why:** A clearly labeled fictional example teaches warning signs without creating a usable credential-harvesting message.

**Do this:**

1. Use fictional organization/names and a visible TRAINING SIMULATION label.
2. Include no working links, QR codes, credential form, attachment payload, or real login workflow.
3. Demonstrate at least two warning signs such as urgency and false authority.
4. Add reviewer notes explaining each indicator and the safe response.
5. Proofread so nobody can mistake it for a real message.

**Verification gate:**

- Training label is prominent.
- No functional harmful element exists.
- At least two indicators and defensive actions are explained.

**Save:** `email_for_you.md` and required AI dialogue.

**AI prompt (paste your real output after it):**

> Review this clearly labeled fictional phishing-awareness example. Confirm it cannot collect credentials or direct users to a live site, identify the warning signs, and improve the defensive teaching notes without making the message more operational.

### Task 3 — Sniffer detection from PCAP

**Why:** ARP/MAC and traffic patterns can suggest promiscuous hosts, but evidence must distinguish them from routers or bridges.

**Do this:**

1. Hash and analyze `no_sniff_dump.pcap` offline.
2. Review endpoints, conversations, MAC mappings, ARP behavior, and unusual probes.
3. Build candidate list with exact frame evidence.
4. Test alternative explanations such as router, bridge, broadcast receiver, or duplicate IP.
5. Choose a MAC only when evidence supports it and record confidence.

**Verification gate:**

- Every indicator cites frames/filters.
- Normal infrastructure explanations are considered.
- Conclusion and confidence match evidence strength.

**Save:** `sniffer_detector.txt` and analysis notes.

**AI prompt (paste your real output after it):**

> Analyze only the sanitized Wireshark fields I paste from this authorized PCAP. Build a candidate table with MAC, frames, behavior, why it may indicate sniffing, benign alternatives, and confidence. Do not claim certainty without packet evidence.

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

