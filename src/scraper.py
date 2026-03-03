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