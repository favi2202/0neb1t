# CbS11 — Enterprise IT Infrastructure: Execution Runbook

Preparation status: **complete**. Practical status: **execution pending** unless a task below is explicitly marked solved.

This guide converts the supplied School 21 brief into a later execution checklist. Expected values are not evidence; copy only observed results into final deliverables.

## Inputs needed later

`typical_org.xlsx`, `not_really_typical_org`, diagrams.net, spreadsheet editor, and official repository.

## Task-by-task plan

### Task 1 — Topology

Extract every supplied asset, group endpoints/network/server/security devices, use standard icons, draw actual connections, and save editable `result_topology.drawio`. Do not invent IPs or ports unless necessary.

### Task 2 — Inventory

Create `My_inventory.xlsx` with device, OS/version, software/version, IPv4/mask, domain/local accounts, and domain. Include function-appropriate software for non-network devices. Add checks for missing values and duplicate IPs.

### Task 3 — Protection

Place at least endpoint protection, firewalls, and VPN; consider EDR, backups, segmentation, logging, and MFA. Add a protection column and export protected topology/inventory.

### Task 4 — Bonus

Add three remote workers, a terminal server, and an isolated two-server segment reachable only through protected remote access. Explicitly deny all other access.

## Required deliverables

`result_topology.drawio`, `My_inventory.xlsx`, optional `check_inventory.py`, protected topology/inventory, AI logs/justification, and `new_result_topology`.

## Verification gate

Reconcile asset counts, open/re-save drawio, validate XLSX formulas/filters, check required fields, and trace permitted/denied paths.

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

1. Gather: The supplied inventories, diagrams.net, a spreadsheet editor, and exact source files from the official repository.
2. Clone the official School 21 GitLab repository, create/use `develop`, and work only under `src` unless the official task says otherwise.
3. Copy supplied inputs before editing and record SHA-256 hashes when evidence integrity matters.
4. Take a VM/GNS3 snapshot or copy the working project before each major change.
5. Keep a scratch evidence note: **step → why → command/action → observed result → proof filename/frame**.

### Task 1 — Current topology

**Why:** A topology turns an asset list into visible trust boundaries and dependencies.

**Do this:**

1. Open every supplied source and list each unique asset.
2. Classify endpoints, network, servers, and security devices.
3. Draw actual connections with standard icons; mark assumptions distinctly.
4. Save editable drawio and reopen it to test integrity.
5. Reconcile the diagram asset count with the source.

**Verification gate:**

- Every supplied asset appears once.
- Connections/labels trace back to source data.
- The `.drawio` file reopens and remains editable.

**Save:** `result_topology.drawio`.

**AI prompt (paste your real output after it):**

> Using the supplied asset table I paste, create a reconciliation checklist for my topology. Separate facts from assumptions and flag missing, duplicate, or impossible connections; do not invent IP addresses.

### Task 2 — Asset inventory

**Why:** A structured inventory supports ownership, patching, vulnerability management, and incident response.

**Do this:**

1. Create required columns exactly.
2. Enter one row per asset and use source values first.
3. Add function-appropriate software only where the task requires design work; label assumptions.
4. Check missing mandatory fields and duplicate IPs.
5. Apply filters/freeze panes and reopen the workbook.

**Verification gate:**

- Row count matches topology.
- No unexplained duplicate IPs.
- Required OS/software/account/domain fields are populated or marked unknown.

**Save:** `My_inventory.xlsx`.

**AI prompt (paste your real output after it):**

> Audit this inventory table for required columns, missing values, duplicate IPs, inconsistent OS/software versions, and assets absent from the topology. Return a correction list, not invented values.

### Task 3 — Protection design

**Why:** Controls should map to assets, threats, and the CIA triad rather than being decorative icons.

**Do this:**

1. Identify confidentiality, integrity, and availability needs per segment.
2. Place endpoint protection, firewall, VPN, backups, logging, MFA, and segmentation where justified.
3. Add protection/owner columns to inventory.
4. Draw permitted trust paths and blocked paths.
5. Explain each major control in one sentence.

**Verification gate:**

- Every major risk has at least one control.
- Controls exist in both topology and inventory.
- No control blocks required business traffic without explanation.

**Save:** Protected topology/inventory and required AI justification.

**AI prompt (paste your real output after it):**

> Review my enterprise protection design using CIA, least privilege, segmentation, backups, logging, and remote access. For each proposed control, state protected asset, threat reduced, placement, and how I can verify it. Mark overengineering.

### Task 4 — Remote-worker bonus

**Why:** A terminal server and isolated server segment centralize and restrict remote access.

**Do this:**

1. Add three remote users and one protected remote-access path.
2. Add terminal server and isolated two-server segment.
3. Allow only required flows; show explicit deny boundaries.
4. Trace one permitted and one denied path.
5. Update both topology and inventory.

**Verification gate:**

- Remote users cannot directly reach isolated servers.
- Only the designed protected path works.
- All new assets appear in inventory.

**Save:** `new_result_topology` and updated supporting files.

**AI prompt (paste your real output after it):**

> Check this remote-access design. Trace source, authentication point, VPN, terminal server, isolated segment, and firewall decision for allowed and denied cases. Identify any bypass path.

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

