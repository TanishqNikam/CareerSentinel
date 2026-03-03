import yaml
from scraper import fetch_jobs_api, parse_eightfold_jobs


def load_config():
    with open("config/companies.yaml", "r") as file:
        return yaml.safe_load(file)


def run():
    # TEMP: still hardcoding endpoint for Amex
    url = "https://aexp.eightfold.ai/api/apply/v2/jobs/40416958/jobs?domain=aexp.com"

    print("Fetching jobs from American Express...\n")

    data = fetch_jobs_api(url)
    jobs = parse_eightfold_jobs(data)

    print(f"Total jobs fetched: {len(jobs)}\n")

    for job in jobs[:5]:
        print(job)


if __name__ == "__main__":
    run()