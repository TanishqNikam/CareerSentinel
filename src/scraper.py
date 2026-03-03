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

import json

def fetch_jobs_api(api_url):
    """
    Fetch jobs data from the Eightfold API endpoint.
    """

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    response = requests.get(api_url, headers=headers, timeout=10)
    response.raise_for_status()

    return response.json()

def parse_eightfold_jobs(api_data):
    """
    Extract relevant job details from Eightfold API response.
    """

    jobs = []

    positions = api_data.get("positions", [])

    for job in positions:
        job_info = {
            "id": job.get("id"),
            "title": job.get("name"),
            "location": job.get("location"),
            "url": job.get("canonicalPositionUrl")
        }

        jobs.append(job_info)

    return jobs

import time

def fetch_all_eightfold_jobs():
    """
    Fetch all paginated job listings from Eightfold API.
    """

    base_url = "https://aexp.eightfold.ai/api/apply/v2/jobs"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    all_jobs = []
    start = 0
    page_size = 10

    while True:
        params = {
            "domain": "aexp.com",
            "start": start,
            "num": page_size,
            "exclude_pid": "40416958",
            "location": "any",
            "pid": "40416958",
            "sort_by": "relevance"
        }

        response = requests.get(base_url, headers=headers, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        positions = data.get("positions", [])

        if not positions:
            break

        print(f"Fetched {len(positions)} jobs (start={start})")

        all_jobs.extend(positions)
        start += page_size

        time.sleep(0.5)  # polite rate limiting

    return all_jobs