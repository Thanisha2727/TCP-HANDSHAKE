# Scapy TCP Networking Project

A Python-based networking project built using Scapy to demonstrate TCP packet creation, analysis, TCP three-way handshake, and basic TCP port scanning.

##  Features

- TCP SYN Packet Generation
- TCP Three-Way Handshake
- TCP Packet Analysis
- TCP Header Inspection
- TCP Port Scanning
- Network Traffic Learning
- Scapy Packet Crafting

##  About

This project helps beginners understand how TCP communication works at the packet level using Scapy. It demonstrates how packets are crafted, transmitted, and analyzed in a network environment.

##  Technologies Used

- Python 3
- Scapy
- TCP/IP Protocol
- Networking Concepts

##  Installation

Clone the repository:

```bash
git clone https://github.com/your-username/scapy-tcp-project.git
cd scapy-tcp-project
```

Install dependencies:

```bash
pip install scapy
```

##  Project Structure

```text
scapy-tcp-project/
│
├── tcp_syn.py
├── tcp_handshake.py
├── tcp_port_scan.py
├── requirements.txt
└── README.md
```

##  TCP SYN Packet Example

```python
from scapy.all import *

packet = IP(dst="8.8.8.8") / TCP(
    sport=12345,
    dport=80,
    flags="S"
)

packet.show()
send(packet)
```

##  TCP Three-Way Handshake

```text
Client                      Server

SYN ---------------------->

      <------------------ SYN-ACK

ACK ---------------------->
```

This process establishes a reliable TCP connection between client and server.

##  TCP Port Scanning

The scanner sends TCP SYN packets and checks whether ports are open based on the response received.

##  Learning Outcomes

After completing this project, you will understand:

- TCP/IP Fundamentals
- TCP Flags (SYN, ACK, FIN, RST)
- Packet Crafting
- Network Communication
- Port Scanning Concepts
- Packet Analysis Techniques

##  Disclaimer

This project is intended strictly for educational and research purposes.

Only test systems and networks that you own or have explicit authorization to assess.

Unauthorized network scanning may violate organizational policies or local laws.

##  Future Improvements

- Multi-threaded Scanning
- Banner Grabbing
- Packet Sniffing Module
- Service Detection
- Network Visualization Dashboard

##  Author

Jenit Akash

##  License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a star.
