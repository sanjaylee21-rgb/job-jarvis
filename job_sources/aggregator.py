from job_sources.sample_jobs import get_sample_jobs
from utils.dedupe import job_hash


def normalize_job(job: dict) -> dict:
    normalized = dict(job)
    normalized["title"] = str(normalized.get("title", "")).strip()
    normalized["company"] = str(normalized.get("company", "")).strip()
    normalized["location"] = str(normalized.get("location", "")).strip()
    normalized["description"] = str(normalized.get("description", "")).strip()
    normalized["dedupe_hash"] = job_hash(
        normalized["title"], normalized["company"], normalized["location"]
    )
    return normalized


def collect_jobs() -> list[dict]:
    # Real connectors are deliberately isolated behind JobSource. This keeps
    # the pipeline stable while individual portals are added using permitted
    # APIs, feeds, or user-controlled browser workflows.
    return [normalize_job(job) for job in get_sample_jobs()]
