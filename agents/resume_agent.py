from ai.client import ask_ai


def optimize_resume(job_description: str, master_resume: str) -> str:
    instructions = """
You are an ATS resume optimization specialist. Optimize the candidate's
resume for the supplied job description. Never invent skills, experience,
achievements, employers, dates, or certifications. Only reorganize and
emphasize factual information already present in the master resume.
"""
    prompt = f"""
JOB DESCRIPTION:
{job_description}

MASTER RESUME:
{master_resume}

Return the optimized resume as plain text.
"""
    return ask_ai(prompt, instructions)
