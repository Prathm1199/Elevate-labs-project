# Web Application Vulnerability Scanner

A Python-based web application vulnerability scanner that detects common vulnerabilities like XSS, SQL Injection, Command Injection, Path Traversal, and misconfigured CORS. Includes a web interface built with Flask.

## Features

- Crawls web pages to find forms and input fields.
- Injects payloads for:
  - XSS (Cross-Site Scripting)
  - SQL Injection
  - Command Injection
  - Path Traversal
- Detects CORS misconfiguration.
- Logs vulnerabilities with:
  - **Payload used**
  - **Evidence**
  - **Severity level**
- Web interface to manage scans and view results in the browser.

  ## Setup and Installation (Linux)

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
### Create a Python virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
### Install dependencies
```
pip install -r requirements.txt
```
### Running the Scanner
Option 1: Console Scanner
```
python3 scanner.py
```
Enter the target URL when prompted.
The scanner will print vulnerabilities with payload, evidence, and severity in the terminal.

Option 2: Web Interface (Flask)
```
python3 app.py
```
Flask will start and show:
```
Running on http://127.0.0.1:5000
```
Open your browser and go to http://127.0.0.1:5000.
Enter the target URL in the form and view scan results directly in the browser.

### Notes
Always test against your own applications or safe testing sites (e.g., DVWA or testphp.vulnweb.com).
Do not use this tool against systems you do not have permission to test.

### Screenshorts
<img width="1816" height="752" alt="Screenshot 2025-08-29 041849" src="https://github.com/user-attachments/assets/febe9d12-3e65-416b-bc4c-6c89c96e89da" />
<img width="1714" height="626" alt="Screenshot 2025-08-29 041744" src="https://github.com/user-attachments/assets/c86066ac-199b-42fc-8a14-9c7abd441c81" />

