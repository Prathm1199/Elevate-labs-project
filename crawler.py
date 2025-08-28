import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            print(f"[!] Failed to access {url}, status code: {response.status_code}")
            return None

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract all links
        links = []
        for link in soup.find_all("a", href=True):
            full_url = urljoin(url, link["href"])
            links.append(full_url)

        # Extract all forms
        forms = []
        for form in soup.find_all("form"):
            action = form.get("action")
            method = form.get("method", "get").lower()
            inputs = []
            for input_tag in form.find_all("input"):
                input_type = input_tag.get("type", "text")
                input_name = input_tag.get("name")
                inputs.append({"type": input_type, "name": input_name})
            forms.append({"action": action, "method": method, "inputs": inputs})

        return {"url": url, "links": links, "forms": forms}

    except Exception as e:
        print(f"[!] Error: {e}")
        return None

# For quick testing
if __name__ == "__main__":
    test_url = input("Enter a URL to crawl: ")
    results = crawl(test_url)
    if results:
        print("\n[+] Links found:")
        for link in results["links"]:
            print("   ", link)

        print("\n[+] Forms found:")
        for form in results["forms"]:
            print(f"   Action: {form['action']} | Method: {form['method']}")
            for inp in form["inputs"]:
                print(f"      Input: {inp['name']} (type={inp['type']})")
