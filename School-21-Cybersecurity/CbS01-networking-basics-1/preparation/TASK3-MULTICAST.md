# CbS1 Task 3 — Multicast runbook

Status: **Prepared; execution and packet verification pending**.

## Goal

Connect two Cisco 3745 routers, configure a shared IPv4 subnet, make one router join a multicast group, send ICMP to that group, capture the traffic, and identify the Ethernet destination MAC.

## Lab plan

- R1 `FastEthernet0/0`: `10.10.10.1/24`
- R2 `FastEthernet0/0`: `10.10.10.2/24`
- Multicast group: `239.1.1.1`
- Expected multicast destination MAC for that chosen group: `01:00:5e:01:01:01`

The MAC above is a theoretical expectation. It must be confirmed in the real capture before placing it in the final answer file.

## Configuration outline

R1:

```text
enable
configure terminal
hostname R1
ip multicast-routing
interface FastEthernet0/0
 ip address 10.10.10.1 255.255.255.0
 no shutdown
end
write memory
```

R2:

```text
enable
configure terminal
hostname R2
ip multicast-routing
interface FastEthernet0/0
 ip address 10.10.10.2 255.255.255.0
 ip igmp join-group 239.1.1.1
 no shutdown
end
write memory
```

The actual interface name may differ. Confirm it with `show ip interface brief` and substitute the real name.

## Verification sequence

1. Confirm both interfaces are up/up:
   ```text
   show ip interface brief
   ```
2. Confirm ordinary connectivity from R1:
   ```text
   ping 10.10.10.2
   ```
3. Confirm R2 joined the group:
   ```text
   show ip igmp groups
   ```
4. Start a GNS3 capture on the R1–R2 link.
5. From R1:
   ```text
   ping 239.1.1.1
   ```
6. Stop the capture after the request/reply packets appear.

Some IOS versions may require an extended ping or an explicitly selected source interface. Use IOS help (`?`) rather than guessing if the short command does not work.

## Wireshark analysis

Use this display filter:

```text
icmp || igmp
```

Select the ICMP Echo Request and expand:

- **Ethernet II:** source and destination MAC
- **Internet Protocol Version 4:** source `10.10.10.1`, destination `239.1.1.1`
- **Internet Control Message Protocol:** Echo Request, normally Type 8

IPv4 multicast MAC addresses begin with `01:00:5e`. The lower 23 bits of the multicast IPv4 address become the lower 23 bits of the Ethernet MAC. Because different IPv4 multicast addresses can map to the same MAC, the mapping is not one-to-one.

For `239.1.1.1`, the expected mapping is:

```text
239.1.1.1 -> 01:00:5e:01:01:01
```

## Required outputs

- `multicast.pcap` using the classic PCAP format requested by the README
- `multicast` text file containing the destination-MAC answer

Suggested final wording after capture verification:

> The ICMP Echo Request sent to multicast group 239.1.1.1 used Ethernet destination MAC 01:00:5e:01:01:01. This is an IPv4 multicast MAC derived from the lower 23 bits of the multicast IPv4 address.

## Evidence

- GNS3 topology with R1 and R2
- R1/R2 interface configurations
- `show ip interface brief`
- `show ip igmp groups`
- Successful multicast ping output
- Wireshark packet with Ethernet, IPv4, and ICMP sections expanded
- Save-As window or file listing confirming `multicast.pcap`

## Troubleshooting

- **No response:** confirm R2 joined the group and both interfaces are up.
- **No packets:** make sure capture started on the correct link before the ping.
- **Only IGMP appears:** verify the ICMP command and display filter.
- **Wrong MAC expectation:** confirm the actual group address; changing the group changes the lower MAC bytes.
- **Saved as PCAPNG:** use Save As and explicitly select classic PCAP.

## Reviewer questions

- **Broadcast vs multicast?** Broadcast targets every host in a broadcast domain; multicast targets interested group members.
- **What does ICMP do?** It carries network-control and error information; ping uses Echo Request/Reply.
- **Why does the MAC start with 01:00:5e?** That prefix is reserved for IPv4 multicast Ethernet mapping.