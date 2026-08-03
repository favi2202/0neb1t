# 0neb1t — School 21 Cybersecurity

This repository organizes preparation and verified work for the School 21 cybersecurity track (CbS1–CbS18).

The official task text remains on the School 21 platform. Each project folder now contains an original README plus a detailed `preparation/EXECUTION-RUNBOOK.md` with task steps, required inputs, deliverables, verification, evidence, troubleshooting, and public-repository safety notes.

## Rules

- Complete official submissions in the assigned GitLab repository and required `develop` branch.
- Work only in `src` when the project requires it and preserve exact filenames.
- Never fabricate screenshots, captures, command output, flags, or test results.
- Keep credentials, recovery keys, production private keys, personal data, real phishing data, and unauthorized scan results out of this public repository.
- Network security exercises stay inside isolated, authorized labs.
- **Preparation complete** does not mean the practical project is complete.

## Track

| Project | Topic | Preparation status | Practical status |
|---|---|---|---|
| CbS1 | Addressing, GNS3, multicast, ARP | Complete | **Complete — all 4 tasks verified** |
| CbS2 | Routing, NTP, DNS, DHCP, SSH | Complete | **Complete — all 5 tasks verified** |
| CbS3 | VLAN, EtherChannel, OSPF, HSRP | Complete | **Next — detailed execution guide ready** |
| CbS4 | Traffic analysis and Scapy | Complete | `main.py` prepared; captures pending |
| CbS5 | Linux security | Complete | VM execution pending |
| CbS6 | Windows security (optional) | Complete | Windows VM execution pending |
| CbS7 | Introductory cryptography | Complete | Tasks 1–2 solved; sources needed for remaining tasks |
| CbS8 | Symmetric cryptography | Complete | Supplied scripts required |
| CbS9 | Asymmetric cryptography and PKI | Complete | RSA Task 1 solved; remaining sources/lab pending |
| CbS10 | TLS, VPN, secure channels | Complete | VM/license execution pending |
| CbS11 | Enterprise infrastructure | Complete | Supplied spreadsheets required |
| CbS12 | Reconnaissance, attack analysis, defenses | Complete | Isolated lab and supplied files required |
| CbS13 | YARA, Suricata, anomaly detection | Complete | Samples/PCAP execution pending |
| CbS14 | pfSense, IPsec, firewall rules | Complete | pfSense lab execution pending |
| CbS15 | Information-security legislation | Complete | Supplied document versions required |
| CbS16 | Threat modelling and documentation | Complete | Diagram/document production pending |
| CbS17 | Physical security | Complete | Supplied image/tables required |
| CbS18 | Social engineering, OSINT, detection | Complete | Images/PCAP execution pending |

## Work completed from embedded data

- CbS1 `src/ip-1`: verified address and subnet calculations.
- CbS4 `src/main.py`: localhost-only Scapy packet sender prepared; capture still pending.
- CbS7 `src/encoding.txt` and `src/XorXor.txt`: independently calculated.
- CbS9 `src/RSA_cracked.txt`: exact fifth-root RSA result independently verified.

See [PREPARATION-FIRST-WORKFLOW.md](School-21-Cybersecurity/PREPARATION-FIRST-WORKFLOW.md) for the missing-input policy.


## Work without an assistant

Use [INDEPENDENT-EXECUTION-GUIDE.md](School-21-Cybersecurity/INDEPENDENT-EXECUTION-GUIDE.md) for the universal workflow, evidence template, troubleshooting loop, AI prompts, submission checks, and peer-review preparation. Every CbS3–CbS18 execution runbook now includes task-specific step-by-step instructions.
