# CbS1 Task 4 — ARP runbook

Status: **Prepared; execution and packet verification pending**.

## Goal

Capture the ARP resolution that occurs before a ping, confirm the new ARP-table entry, identify the first request's destination MAC, inspect the reply, and document the security implications.

## Expected protocol behavior

When R1 knows R2's IP but not its MAC, R1 sends an ARP Request inside an Ethernet broadcast frame.

- Expected Ethernet destination: `ff:ff:ff:ff:ff:ff`
- Name: Ethernet broadcast address
- ARP target hardware address inside the request is commonly `00:00:00:00:00:00` because it is unknown.

Do not confuse the Ethernet destination MAC with the ARP payload's target hardware address.

The ARP Reply should normally be unicast. Its Ethernet source MAC is the real interface MAC of the neighbor answering the request. That value cannot be filled in until the lab generates it.

## Procedure

1. Reuse two routers in the same subnet, for example:
   - R1: `10.10.10.1/24`
   - R2: `10.10.10.2/24`
2. Confirm both interfaces are up:
   ```text
   show ip interface brief
   ```
3. Display the current cache:
   ```text
   show ip arp
   ```
4. If necessary, clear the dynamic cache using the appropriate IOS command so the next ping forces resolution.
5. Start a capture on the R1–R2 link.
6. From R1:
   ```text
   ping 10.10.10.2
   ```
7. Display the cache again:
   ```text
   show ip arp
   ```
8. Stop the capture.

Use IOS help if the cache-clear command differs in the supplied image. Do not clear unrelated production caches—this is only for the isolated lab.

## Wireshark analysis

Display filter:

```text
arp || icmp
```

For the first ARP Request, inspect:

- Ethernet destination: expected `ff:ff:ff:ff:ff:ff`
- ARP opcode: request (1)
- Sender MAC/IP: R1
- Target IP: R2
- Target MAC: unknown/zeros in the request

For the ARP Reply, inspect:

- Ethernet source: R2's actual interface MAC
- Ethernet destination: R1's MAC
- ARP opcode: reply (2)
- Sender IP/MAC: R2's claimed mapping

Then confirm the same mapping appears in `show ip arp`.

## Required outputs

- GNS3 project
- `arp.pcap`
- `arp` text answer
- `ai-logs/arp.md`

Suggested main answer after real verification:

> The first ARP Request was sent to ff:ff:ff:ff:ff:ff, the Ethernet broadcast address, because the sender did not yet know the destination host's MAC address.

Add the actual reply source MAC observed in the capture.

## Security explanation

ARP has no built-in authentication. A forged ARP Reply can claim that a trusted IP address is associated with an attacker's MAC address. The fields involved in that false claim are primarily the sender protocol address (claimed IP) and sender hardware address (claimed MAC). This may poison a host's cache and redirect traffic.

Keep this explanation conceptual; the assignment explicitly does not require an attack script.

Defensive measures include:

- Dynamic ARP Inspection on supported switches
- DHCP Snooping as a trusted IP–MAC binding source
- Static mappings for a very small set of critical systems
- Segmentation and monitoring for unexpected IP–MAC changes
- End-to-end encryption so intercepted traffic remains protected

## AI log structure

`ai-logs/arp.md` should later contain:

1. The actual ARP-table output and explanation of each column.
2. Why entries may be dynamic or static.
3. Security risks of unauthenticated ARP.
4. Conceptual ARP-spoofing field logic based on the captured packet.
5. The improved final wording of the broadcast-MAC answer.
6. Your own verification comments.

## Evidence

- GNS3 topology
- ARP table before and after ping
- First ARP Request with Ethernet and ARP fields expanded
- ARP Reply with source MAC visible
- ICMP request/reply following resolution
- File listing showing `arp.pcap`, `arp`, and the GNS3 project

## Troubleshooting

- **No ARP Request:** the cache already contains the mapping; clear the dynamic entry and capture again.
- **Ping fails:** verify addressing, masks, interface state, and direct connectivity.
- **Only ARP, no ICMP:** resolution may fail or an interface may be down.
- **Capture is empty:** capture the correct GNS3 link.
- **Wrong address reported:** distinguish Ethernet destination from ARP target hardware address.

## Reviewer questions

- **Why is ARP Layer 2/Layer 3 adjacent?** It resolves an IPv4 address to the link-layer address needed for local Ethernet delivery.
- **Why broadcast the request?** The sender knows the IP but not which local MAC owns it.
- **Why is the reply usually unicast?** The requester MAC is already present in the ARP Request.