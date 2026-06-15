from scapy.all import *

# TCP SYN Packet
packet = IP(dst="8.8.8.8") / TCP(
    sport=12345,
    dport=80,
    flags="S"
)

# Packet details
packet.show()

# Send packet
send(packet)
