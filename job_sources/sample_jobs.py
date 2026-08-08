def get_sample_jobs() -> list[dict]:
    return [
        {
            "source": "sample",
            "external_id": "sample-001",
            "title": "Junior Financial Analyst",
            "company": "ABC Finance",
            "location": "Chennai",
            "url": "https://example.com/jobs/sample-001",
            "description": """
We are looking for a Junior Financial Analyst.
Responsibilities include financial analysis, Excel reporting,
management reporting, financial modelling and data analysis.
Requirements: MBA Finance or equivalent, strong Excel skills,
and 0-2 years experience.
""".strip(),
        },
        {
            "source": "sample",
            "external_id": "sample-002",
            "title": "Sales Executive",
            "company": "XYZ Insurance",
            "location": "Chennai",
            "url": "https://example.com/jobs/sample-002",
            "description": """
Responsible for selling insurance products, generating leads,
telecalling prospects and achieving sales targets.
""".strip(),
        },
    ]
