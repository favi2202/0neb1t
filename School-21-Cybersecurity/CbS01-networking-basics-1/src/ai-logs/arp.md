# AI-assisted ARP analysis log

## Scope

AI assistance was used to interpret a genuine packet capture produced in the
GNS3 lab. It was not used to fabricate packets, command output, MAC addresses,
or project evidence.

## Lab procedure performed by the student

1. Connected two Cisco 3745 routers through FastEthernet0/0.
2. Configured R1 as `10.10.10.1/24` and R2 as `10.10.10.2/24`.
3. Cleared the ARP cache so the next ping would require address resolution.
4. Started a Wireshark capture on the R1-R2 link.
5. Sent ICMP Echo Requests from R1 to `10.10.10.2`.
6. Saved the complete capture as classic PCAP in `arp.pcap`.

## Question presented to AI

Analyze the real capture, identify the first ARP destination MAC address and
its name, explain the MAC addresses in the request and reply, and explain the
security logic of ARP spoofing.

## AI-supported interpretation

- Frame 10 is an ARP Request from `10.10.10.1`.
- Its Ethernet destination is `ff:ff:ff:ff:ff:ff`, the broadcast address.
- R1's sender MAC is `c4:01:53:7c:00:00`.
- The ARP target hardware field is `00:00:00:00:00:00` because R2's MAC was
  unknown at that moment.
- Frame 11 is an ARP Reply from `10.10.10.2`.
- R2 reports its MAC as `c4:02:36:58:00:00`.
- The reply is unicast to R1 at `c4:01:53:7c:00:00`.
- The subsequent ICMP frames confirm that both routers use the resolved
  unicast MAC addresses.

## Security explanation

ARP has no built-in authentication. A forged ARP reply can claim a false
IP-to-MAC association, and a host may cache it. This can redirect or disrupt
local traffic. Defensive measures include Dynamic ARP Inspection, DHCP
Snooping, monitoring IP-to-MAC changes, segmentation, and encryption.

## Independent verification

The student can reproduce the conclusion in Wireshark using the display filter:

```text
arp || icmp
```

Expand `Ethernet II` and `Address Resolution Protocol` in frames 10 and 11.
The values recorded above must match the packet fields in `arp.pcap`.

PCAP SHA-256:
`c6ac8939b0c4591ba0f265139bd7c5fa8423b55682a5ea21fc122bc4bf5c04fe`
