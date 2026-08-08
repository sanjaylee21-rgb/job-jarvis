from agents.job_matcher import match_job
from config.settings import EXCLUDED_ROLES, TARGET_LOCATIONS, TARGET_ROLES
from job_sources.aggregator import collect_jobs

PROFILE = {
    "name": "Sanjay",
    "education": "MBA Finance",
    "experience_years": 0,
    "target_locations": TARGET_LOCATIONS,
    "target_roles": TARGET_ROLES,
    "excluded_roles": EXCLUDED_ROLES,
}


def run_matching(jobs: list[dict]) -> list[dict]:
    results = []
    for job in jobs:
        scored = dict(job)
        scored.update(match_job(job, PROFILE))
        results.append(scored)
    return results


def run_demo() -> list[dict]:
    return run_matching(collect_jobs())
