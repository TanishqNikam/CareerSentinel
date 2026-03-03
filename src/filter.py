def filter_jobs_by_keywords(jobs, keywords):
    filtered = []

    for job in jobs:
        title = job["title"]

        if any(keyword.lower() in title.lower() for keyword in keywords):
            filtered.append(job)

    return filtered