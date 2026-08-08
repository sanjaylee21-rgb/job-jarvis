from database.supabase_client import get_supabase


def insert_job(job: dict):
    return (
        get_supabase()
        .table("jobs")
        .upsert(job, on_conflict="source,external_id")
        .execute()
        .data
    )


def get_jobs(limit: int = 100):
    return (
        get_supabase()
        .table("jobs")
        .select("*")
        .order("discovered_at", desc=True)
        .limit(limit)
        .execute()
        .data
    )
