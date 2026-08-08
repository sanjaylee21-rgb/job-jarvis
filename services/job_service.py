from database.queries import insert_job
from job_sources.aggregator import collect_jobs


def ingest_jobs() -> int:
    count = 0
    for job in collect_jobs():
        payload = {k: v for k, v in job.items() if k != "dedupe_hash"}
        insert_job(payload)
        count += 1
    return count
