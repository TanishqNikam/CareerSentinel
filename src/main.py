import yaml
from scraper import fetch_jobs_api, parse_eightfold_jobs


def load_config():
    with open("config/companies.yaml", "r") as file:
        return yaml.safe_load(file)


def run():
    config = load_config()

    for company in config["companies"]:
        print(f"\nFetching jobs from {company['name']}...\n")

        if company["platform"] == "eightfold":
            data = fetch_jobs_api(company["api_url"])
            jobs = parse_eightfold_jobs(data)

            print(f"Total jobs fetched: {len(jobs)}")

            for job in jobs[:5]:
                print(job)


if __name__ == "__main__":
    run()