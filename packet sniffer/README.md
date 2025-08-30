# Network Packet Sniffer with Alert System

## Overview
This project is a real-time network packet sniffer with anomaly detection.
It monitors live network traffic, detects suspicious patterns (e.g., flooding, port scanning),
logs data into SQLite, and raises alerts.

## Features
- Capture live packets using **Scapy**  
- Extract and log headers:  
  - Source IP, Destination IP  
  - Source/Destination Ports  
  - Protocol (TCP/UDP/ICMP)  
  - Packet length  
  - TCP flags  
- Detect anomalies:  
  - Flooding detection (sudden packet spikes)  
  - Port scanning detection (multiple port hits)  
- Store traffic data in an **SQLite database**  
- Generate **traffic summary reports**  
- Raise **real-time alerts** (console, extendable to email)  

## Requirements
- Python 3.x
- [Scapy](https://scapy.net/)
- SQLite
- Matplotlib

## Usage
Install and run:  
```bash
pip install -r requirements.txt
cd packet_sniffer
python sniffer.py
```
Output looks like:
```
192.168.1.10:50427 -> 104.18.5.247:443 | proto=6 | len=1424 | flags=A  
ALERT: Flooding detected from 192.168.1.10 (195 packets in 10s)  
```

## Note:
Run with administrator/root privileges for capturing packets.  
For learning and demo purposes only — do not sniff traffic on networks without permission.

## Screenshots:
<img width="1861" height="927" alt="Screenshot 2025-08-29 223204" src="https://github.com/user-attachments/assets/68706cb6-0760-4af9-9927-3516d899f7f0" />
