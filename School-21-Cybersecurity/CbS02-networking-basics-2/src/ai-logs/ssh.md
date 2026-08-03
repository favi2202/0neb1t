# SSH traffic analysis

## Lab result

The SSH server is `R1-SSH-Server` at `10.10.10.1`. The client is `R2-SSH-Client` at `10.10.10.2`. The capture proves that TCP port 22 is reachable and that an SSH session was established.

## TCP three-way handshake

The main SSH connection uses client source port `25400` and server destination port `22`.

1. Client → server: `SYN`, sequence number `1506267677`.
2. Server → client: `SYN, ACK`, sequence number `1018374606`, acknowledgment `1506267678`.
3. Client → server: `ACK`, sequence number `1506267678`, acknowledgment `1018374607`.

The acknowledgment values are one greater than the received initial sequence numbers because a TCP SYN consumes one sequence number. This completes the TCP connection before SSH begins.

## SSH connection stages

1. **Protocol identification:** the server sends `SSH-2.0-Cisco-1.25`; the client responds with `SSH-1.99-Cisco-1.25`, which indicates compatibility with SSH version 2.
2. **Algorithm negotiation:** both sides exchange SSH key-exchange proposals. The visible proposals include `diffie-hellman-group1-sha1` for key exchange, `ssh-rsa` for the host key, AES/3DES CBC ciphers, and HMAC algorithms for integrity.
3. **Key exchange:** Diffie-Hellman messages establish a shared session secret without sending that secret directly across the network. The RSA host key identifies the server.
4. **New keys:** the peers switch to the negotiated encryption and integrity keys.
5. **Encrypted session:** authentication and terminal data appear only as encrypted SSH packets in Wireshark; the password and commands are not readable from the capture.
6. **Connection close:** FIN/ACK packets close the tested TCP connection cleanly.

## Port test and the second TCP stream

The capture also contains a shorter connection from client source port `43725` to server port `22`. It completes a TCP handshake, receives the server SSH banner, and then closes. This is consistent with using a Telnet-style client only to test whether TCP port 22 is open; it is not a Telnet service on port 23.

## Telnet compared with SSH

- **Telnet:** normally uses TCP port 23 and sends terminal data without encryption, so usernames, passwords, and commands can be exposed to anyone able to capture the traffic.
- **SSH:** normally uses TCP port 22 and provides server authentication, encryption, and integrity protection. After key negotiation, the useful session contents are not readable in a normal packet capture.

## Verification commands

```cisco
show ip interface brief
show ip ssh
show users
show running-config | section line vty
show running-config | include username|ip ssh|ip domain
copy running-config startup-config
```

`copy running-config startup-config` saves the active configuration from RAM into NVRAM so it will be loaded again after a router restart.
