import os

import pandas as pd
import streamlit as st
from dotenv import load_dotenv

from database.queries import get_jobs
from job_sources.sample_jobs import get_sample_jobs

load_dotenv()

st.set_page_config(
    page_title="Job Jarvis",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 Job Jarvis")
st.caption("AI-powered job discovery, matching and application management")

profile = {
    "name": "Sanjay",
    "education": "MBA Finance",
    "experience_years": 0,
    "target_locations": [
        "Chennai",
        "Coimbatore",
        "Bangalore",
        "Hyderabad",
        "Pune",
        "Gurgaon",
    ],
    "target_roles": [
        "Financial Analyst",
        "Investment Analyst",
        "Equity Research Analyst",
        "Research Associate",
        "Portfolio Analyst",
        "Finance Analyst",
        "Pricing Analyst",
        "Investment Banking Analyst",
    ],
    "excluded_roles": [
        "Sales",
        "Field Sales",
        "Telecalling",
        "Direct Marketing",
        "Insurance Sales",
    ],
}

with st.sidebar:
    st.header("⚙️ Profile")
    st.write(f"**Candidate:** {profile['name']}")
    st.write(f"**Education:** {profile['education']}")
    st.write("**Target roles:**")
    for role in profile["target_roles"]:
        st.write(f"- {role}")

    st.divider()
    st.info(
        "V0.1 is a foundation. Real job-source connectors and controlled "
        "application automation will be added in later versions."
    )

try:
    jobs = get_jobs()
except Exception as exc:
    jobs = []
    st.warning(
        "Supabase is not configured yet. Showing sample jobs. "
        f"Connection detail: {exc}"
    )

if not jobs:
    jobs = get_sample_jobs()

# Sample jobs do not have AI scores until the matcher is run.
df = pd.DataFrame(jobs)

if "match_score" not in df.columns:
    df["match_score"] = None

col1, col2, col3, col4 = st.columns(4)
col1.metric("Jobs Found", len(df))
col2.metric(
    "Strong Matches",
    int((pd.to_numeric(df["match_score"], errors="coerce") >= 80).sum()),
)
col3.metric("Applications", 0)
col4.metric("Interviews", 0)

st.divider()
st.subheader("🔥 Job Opportunities")

for _, job in df.iterrows():
    score = job.get("match_score")
    score_text = f"{int(score)}%" if pd.notna(score) else "Not scored"

    with st.container(border=True):
        left, right = st.columns([4, 1])
        with left:
            st.markdown(f"### {job.get('title', 'Untitled role')}")
            st.write(
                f"**{job.get('company', 'Unknown company')}** · "
                f"{job.get('location', 'Location not specified')}"
            )
            st.write(f"**AI Match:** {score_text}")
        with right:
            url = job.get("url")
            if url:
                st.link_button("View Job", url)

        with st.expander("Job description"):
            st.write(job.get("description", "No description available."))
