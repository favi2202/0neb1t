#!/usr/bin/env python3
"""Send the School 21 training message to localhost TCP/12345 with Scapy.

Run only in the local disposable lab. Capture with a filter such as:
    tcp port 12345
"""

from scapy.all import IP, TCP, Raw, send

DESTINATION = "127.0.0.1"
PORT = 12345
MESSAGE = b"Dear Steel Cat! This is no attack, it's my humster Pinkie you should track"


def main() -> None:
    packet = IP(dst=DESTINATION) / TCP(dport=PORT, flags="PA") / Raw(load=MESSAGE)
    send(packet, verbose=False)
    print(f"Sent {len(MESSAGE)} bytes to {DESTINATION}:{PORT}")


if __name__ == "__main__":
    main()
