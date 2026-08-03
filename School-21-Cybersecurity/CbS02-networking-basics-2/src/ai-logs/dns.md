# DNS packet analysis

## 1. Request and response from `dns.pcap`

The capture contains one DNS request and its matching response.

### Request — frame 3

- Source: `10.10.10.2:56521`
- Destination: `10.10.10.1:53/UDP`
- Transaction ID: `0xD821`
- Flags: `0x0100` — standard query with Recursion Desired set
- Questions: 1
- Answers: 0
- Name: `my.site`
- Type: `A` (IPv4 host address)
- Class: `IN` (Internet)

### Response — frame 4

- Source: `10.10.10.1:53`
- Destination: `10.10.10.2:56521/UDP`
- Transaction ID: `0xD821`, matching the request
- Flags: `0x8180` — response, Recursion Desired and Recursion Available, no error
- Questions: 1
- Answers: 1
- Answer: `my.site A 10.10.100.1`
- TTL: 10 seconds

The Transaction ID lets the client associate the response with its request. Matching the ID and question is also important because an unexpected response may indicate stale traffic or an attempted forged DNS reply. Flags describe whether the packet is a query or response, whether recursion is requested or available, and whether an error occurred. The Questions counter identifies how many names are being requested, while Answers identifies how many resource records the server returned.

### Encoding of `my.site`

DNS encodes a domain as length-prefixed labels rather than as one ordinary string:

```text
02 6d 79 04 73 69 74 65 00
```

- `02` — the next label is 2 bytes long
- `6d 79` — ASCII `my`
- `04` — the next label is 4 bytes long
- `73 69 74 65` — ASCII `site`
- `00` — end of the domain name

The response uses the compression pointer `c0 0c`, which points back to the already encoded name at byte offset 12 in the DNS message. This avoids repeating the full name.

## 2. Recursive DNS lookup

If this router only knows the local `my.site` record and has no usable upstream resolver, a request for `www.google.com` will not be resolved successfully. With a recursive resolver configured, the normal path is:

1. The client asks its recursive DNS server for `www.google.com`.
2. The resolver asks a root server which servers handle `.com`.
3. It asks a `.com` TLD server which authoritative servers handle `google.com`.
4. It asks a `google.com` authoritative server for the `www.google.com` record.
5. The resolver caches the result and returns it to the client.

## 3. Three DNS record types other than A

- `AAAA` — maps a hostname to an IPv6 address. Example response: `host.example AAAA 2001:db8::10`.
- `MX` — identifies the mail server for a domain and includes a preference value. Example: `example MX 10 mail.example`.
- `CNAME` — makes one hostname an alias of another canonical hostname. Example: `www.example CNAME web.example`.
