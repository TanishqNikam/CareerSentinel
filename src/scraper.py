import requests
from bs4 import BeautifulSoup


def fetch_page(url):
    """
    Fetch raw HTML from a given URL.
    """

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    return response.text

def parse_jobs(html, company_name):
    """
    Parse HTML and extract job listings.
    """

    soup = BeautifulSoup(html, "html.parser")

    jobs = []

    # TEMPORARY generic parsing logic
    for link in soup.find_all("a"):
        title = link.get_text(strip=True)
        href = link.get("href")

        if title and href:
            jobs.append({
                "company": company_name,
                "title": title,
                "link": href
            })

    return jobs