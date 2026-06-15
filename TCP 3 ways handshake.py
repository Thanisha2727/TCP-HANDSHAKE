from scapy.all import *

target_ip = "8.8.8.8"
target_port = 80


ip = IP(dst=target_ip)
syn = TCP(sport=RandShort(), dport=target_port, flags="S", seq=1000)


syn_ack = sr1(ip/syn, timeout=2)

if syn_ack:
  
    ack = TCP(
        sport=syn.sport,
        dport=target_port,
        flags="A",
        seq=syn_ack.ack,
        ack=syn_ack.seq + 1
    )

    send(ip/ack)
    print("TCP Handshake Completed")
else:
    print("No Response")
