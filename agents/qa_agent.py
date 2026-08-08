def validate_application(application: dict) -> dict:
    required = [
        "why_this_role",
        "why_suitable",
        "relevant_experience",
        "career_goals",
        "cover_letter",
    ]
    missing = [key for key in required if not application.get(key)]
    return {
        "ready": not missing,
        "missing_fields": missing,
    }
