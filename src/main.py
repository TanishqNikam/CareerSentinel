import yaml
from scraper import fetch_jobs_api, fetch_page, parse_jobs


def load_config():
    with open("config/companies.yaml", "r") as file:
        return yaml.safe_load(file)


def run():
    # hardcode the endpoint for now
    url = "https://aexp.eightfold.ai/api/apply/v2/jobs/40416958/jobs?domain=aexp.com"

    print("Calling API:", url)
    data = fetch_jobs_api(url)

    print("API response keys:", data.keys())
    print("Sample data:", data)


if __name__ == "__main__":
    run()