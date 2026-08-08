import json

from ai.client import ask_ai
from ai.prompts import APPLICATION_INSTRUCTIONS


def prepare_application(job: dict, profile: dict, resume: str = "") -> dict:
    prompt = f"""
Candidate:
{json.dumps(profile, indent=2)}

Resume:
{resume}

Job:
{json.dumps(job, indent=2)}

Return JSON only with:
{{
  "why_this_role": "",
  "why_suitable": "",
  "relevant_experience": "",
  "career_goals": "",
  "relocation_answer": "",
  "salary_response": "",
  "cover_letter": ""
}}
"""
    raw = ask_ai(prompt, APPLICATION_INSTRUCTIONS)
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError("Application agent returned invalid JSON") from exc
