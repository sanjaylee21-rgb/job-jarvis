import hashlib


def job_hash(title: str, company: str, location: str) -> str:
    value = "|".join(
        part.lower().strip() for part in (title, company, location)
    )
    return hashlib.sha256(value.encode("utf-8")).hexdigest()
