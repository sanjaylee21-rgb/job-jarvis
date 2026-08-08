from utils.dedupe import job_hash
from utils.text import clean_text


def test_job_hash_is_stable():
    assert job_hash("Analyst", "ABC", "Chennai") == job_hash("Analyst", "ABC", "Chennai")


def test_job_hash_changes_with_company():
    assert job_hash("Analyst", "ABC", "Chennai") != job_hash("Analyst", "XYZ", "Chennai")


def test_clean_text():
    assert clean_text("  hello   world\n") == "hello world"
