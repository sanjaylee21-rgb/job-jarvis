import pandas as pd
import streamlit as st
from dotenv import load_dotenv

from config.settings import EXCLUDED_ROLES, TARGET_LOCATIONS, TARGET_ROLES
from database.queries import get_jobs
from job_sources.aggregator import collect_jobs
from services.job_service import ingest_jobs

load_dotenv()

st.set_page_config(page_title="Job Jarvis", page_icon="🤖", layout="wide")

PROFILE = {
    "name": "Sanjay",
    "education": "MBA Finance",
    "experience_years": 0,
    "target_locations": TARGET_LOCATIONS,
    "target_roles": TARGET_ROLES,
    "excluded_roles": EXCLUDED_ROLES,
}

st.title("🤖 Job Jarvis")
st.caption("AI-powered job discovery, matching, application preparation and tracking")

with st.sidebar:
    st.header("⚙️ Search profile")
    st.write(f"**Candidate:** {PROFILE['name']}")
    st.write(f"**Education:** {PROFILE['education']}")
    st.write("**Locations:** " + ", ".join(TARGET_LOCATIONS))
    st.divider()
    st.write("**Target roles**")
    for role in TARGET_ROLES:
        st.write(f"• {role}")
    st.divider()
    st.write("**Excluded**")
    for role in EXCLUDED_ROLES:
        st.write(f"• {role}")

    if st.button("🔄 Ingest jobs", use_container_width=True):
        try:
            count = ingest_jobs()
            st.success(f"Ingested {count} jobs")
            st.rerun()
        except Exception as exc:
            st.error(f"Could not ingest jobs: {exc}")

try:
    jobs = get_jobs()
    data_source = "Supabase"
except Exception:
    jobs = collect_jobs()
    data_source = "Demo data"

if not jobs:
    jobs = collect_jobs()
    data_source = "Demo data"

df = pd.DataFrame(jobs)
if "match_score" not in df.columns:
    df["match_score"] = pd.NA

numeric_scores = pd.to_numeric(df["match_score"], errors="coerce")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Jobs", len(df))
c2.metric("Strong matches", int((numeric_scores >= 80).sum()))
c3.metric("Applications", 0)
c4.metric("Interviews", 0)

st.caption(f"Data source: {data_source}")
st.divider()

st.subheader("🔥 Opportunities")

location_filter = st.multiselect("Location", sorted(df["location"].dropna().unique()), default=[])
score_filter = st.slider("Minimum match score", 0, 100, 0)

filtered = df.copy()
if location_filter:
    filtered = filtered[filtered["location"].isin(location_filter)]
filtered = filtered[pd.to_numeric(filtered["match_score"], errors="coerce").fillna(0) >= score_filter]

if filtered.empty:
    st.info("No jobs match the current filters.")
else:
    for _, job in filtered.iterrows():
        score = job.get("match_score")
        score_text = f"{int(score)}%" if pd.notna(score) else "Not scored"
        with st.container(border=True):
            left, right = st.columns([5, 1])
            with left:
                st.markdown(f"### {job.get('title', 'Untitled role')}")
                st.write(f"**{job.get('company', 'Unknown')}** · {job.get('location', 'Unknown')}")
                st.write(f"**AI Match:** {score_text}")
            with right:
                if job.get("url"):
                    st.link_button("View Job", job["url"], use_container_width=True)
            with st.expander("Description"):
                st.write(job.get("description", "No description available."))
