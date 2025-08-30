# Elevate Labs Projects  

This repository contains **two projects**:  

1. **Web Application Vulnerability Scanner**  
2. **Network Packet Sniffer with Anomaly Detection & Alert System**  

Both projects are implemented in Python and demonstrate core concepts of **offensive security** and **network monitoring**.  


##  1. Web Application Vulnerability Scanner  

A Python-based scanner that detects common web application vulnerabilities like **XSS, SQL Injection, Command Injection, Path Traversal, and misconfigured CORS**.  

###  Features  
- Crawls target websites to discover forms and inputs.  
- Injects payloads to test for vulnerabilities:  
  - XSS (Cross-Site Scripting)  
  - SQL Injection  
  - Command Injection  
  - Path Traversal  
- Detects **CORS misconfigurations**.  
- Provides results with payload used, evidence, and severity.  
- Includes a **Flask-based web interface** to manage scans and view results.  

###  Usage  
- **Console mode:** run `scanner.py` and enter a target URL.  
- **Web interface:** run `app.py` and open `http://127.0.0.1:5000` in your browser.  

Detailed guide available in [`web_scanner/README.md`](https://github.com/Prathm1199/Elevate-labs-project/blob/main/web_scanner/README.md)  


##  2. Network Packet Sniffer with Anomaly Detection  

A **real-time network traffic sniffer** built with Python and `scapy`. It captures live packets, stores logs, and detects anomalies like flooding.  

###  Features  
- Captures live packets with headers:  
  - Source IP, Destination IP  
  - Ports (TCP/UDP)  
  - Protocol  
  - Packet length  
  - TCP flags  
- Detects anomalies (flooding, suspicious activity).  
- Stores data in **SQLite database**.  
- Generates **traffic summary reports**.  
- Alerts on threshold breaches (via CLI, extendable to email).  

###  Usage  
1. Navigate to the project folder:  
   ```bash
   cd packet_sniffer
   python -m venv venv
   venv\Scripts\activate   # Windows
   ```
   OR
   ``` 
   source venv/bin/activate   # Linux/Mac  
   pip install -r requirements.txt
   python sniffer.py
   ```
Detailed guide available in [`packet_sniffer/README.md`](https://github.com/Prathm1199/Elevate-labs-project/blob/main/packet%20sniffer/README.md)


## Note:
These projects are for educational purposes only.  
Do not run them against systems or networks you do not own or have explicit permission to test.

