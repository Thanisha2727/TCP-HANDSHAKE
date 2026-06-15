from scapy.all import *

target = "192.168.1.1"

for port in range(1, 1025):
    pkt = IP(dst=target) / TCP(dport=port, flags="S")

    resp = sr1(pkt, timeout=0.5, verbose=0)

    if resp:
        if resp.haslayer(TCP):
            if resp[TCP].flags == 0x12: 
                print(f"Port {port} OPEN")

                rst = IP(dst=target) / TCP(
                    dport=port,
                    flags="R"
                )
                send(rst, verbose=0)
