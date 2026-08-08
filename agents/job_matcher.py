import json

from ai.client import ask_ai
from ai.prompts import JOB_MATCHER_INSTRUCTIONS


def match_job(job: dict, profile: dict) -> dict:
    prompt = f"""
Candidate profile:
{json.dumps(profile, indent=2)}

Job:
{json.dumps(job, indent=2)}

Return JSON only:
{{
  "match_score": 0,
  "decision": "APPLY",
  "reason": "",
  "strengths": [],
  "gaps": [],
  "required_skills": [],
  "matched_skills": []
}}
"""
    raw = ask_ai(prompt, JOB_MATCHER_INSTRUCTIONS)
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"AI matcher returned invalid JSON: {raw}") from exc
