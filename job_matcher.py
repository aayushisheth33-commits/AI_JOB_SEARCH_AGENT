def match_jobs(resume_text, jobs):

    resume_text = resume_text.lower()
    matched_jobs = []

    for job in jobs:
        title = job["title"].lower()

        score = 0
        for word in title.split():
            if word in resume_text:
                score += 1

        if score > 0:
            job["score"] = score
            matched_jobs.append(job)

    # if nothing matched, return all jobs
    if not matched_jobs:
        return jobs

    return sorted(matched_jobs, key=lambda x: x["score"], reverse=True)