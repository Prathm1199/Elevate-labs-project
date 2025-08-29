# Network Packet Sniffer with Alert System

## Overview
This project is a real-time network packet sniffer with anomaly detection.
It monitors live network traffic, detects suspicious patterns (e.g., flooding, port scanning),
logs data into SQLite, and raises alerts.

## Features
- Capture live packets using Scapy
- Log headers (IP, port, protocol, flags, length)
- Detect anomalies (flooding, scanning)
- Store traffic data in SQLite database
- Generate alerts on threshold breach

## Requirements
- Python 3.x
- Scapy
- SQLite
- Matplotlib

## Usage
```bash
python sniffer.py
```