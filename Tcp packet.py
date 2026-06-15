from scapy.all import *


packet = IP(dst="8.8.8.8") / TCP(
    sport=12345,
    dport=80,
    flags="S"
)


packet.show()


send(packet)
