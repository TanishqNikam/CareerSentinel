import os
import pandas as pd

DATA_FILE = "data/jobs.csv"


def load_existing_jobs():
    """
    Load previously stored jobs from CSV.
    """
    if not os.path.exists(DATA_FILE):
        return pd.DataFrame(columns=["id", "title", "location", "url"])

    return pd.read_csv(DATA_FILE)


def save_new_jobs(new_jobs):
    """
    Save only new jobs (based on job id).
    Returns list of jobs that were newly added.
    """

    existing_df = load_existing_jobs()

    if existing_df.empty:
        new_df = pd.DataFrame(new_jobs)
        new_df.to_csv(DATA_FILE, index=False)
        return new_jobs

    existing_ids = set(existing_df["id"].astype(str))

    truly_new_jobs = [
        job for job in new_jobs
        if str(job["id"]) not in existing_ids
    ]

    if truly_new_jobs:
        updated_df = pd.concat(
            [existing_df, pd.DataFrame(truly_new_jobs)],
            ignore_index=True
        )
        updated_df.to_csv(DATA_FILE, index=False)

    return truly_new_jobs