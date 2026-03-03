import yaml
from scraper import parse_eightfold_jobs, fetch_all_eightfold_jobs
from filter import filter_jobs_by_keywords


def load_config():
    """
    Load company configuration from YAML file.
    """
    with open("config/companies.yaml", "r") as file:
        return yaml.safe_load(file)


def run():
    """
    Main execution pipeline:
    - Load config
    - Fetch jobs via API
    - Parse jobs
    - Filter by keywords
    - Print results
    """

    config = load_config()

    for company in config["companies"]:
        print("\n" + "=" * 60)
        print(f"Fetching jobs from {company['name']}...")
        print("=" * 60 + "\n")

        # Route based on platform
        if company["platform"] == "eightfold":
            raw_jobs = fetch_all_eightfold_jobs()
            jobs = parse_eightfold_jobs({"positions": raw_jobs})
        else:
            print(f"Unsupported platform: {company['platform']}")
            continue

        print(f"Total jobs fetched: {len(jobs)}")

        # Apply keyword filtering
        filtered_jobs = filter_jobs_by_keywords(
            jobs,
            company.get("keywords", [])
        )

        print(f"Jobs matching your keywords: {len(filtered_jobs)}\n")

        # Print first 5 matches
        for job in filtered_jobs[:5]:
            print(job)


if __name__ == "__main__":
    run()