from agents.application_agent import prepare_application
from agents.qa_agent import validate_application


def prepare_and_validate(job: dict, profile: dict, resume: str = "") -> dict:
    application = prepare_application(job, profile, resume)
    application["qa"] = validate_application(application)
    return application
