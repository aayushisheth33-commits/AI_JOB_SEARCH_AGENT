import streamlit as st
from backend.api_handler import search_jobs_api
from utils.resume_parser import extract_text_from_pdf
from backend.job_matcher import match_jobs

st.set_page_config(page_title="AI Career Agent")

st.title("AI Career Agent ")

# Upload resume
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

# Job input
keyword = st.text_input("Enter Job Role", placeholder="e.g. Python Developer")

if st.button("Search Jobs"):

    if not keyword:
        st.warning("Please enter a job role")
    else:
        jobs = search_jobs_api(keyword)

        if uploaded_file:
            resume_text = extract_text_from_pdf(uploaded_file)
            jobs = match_jobs(resume_text, jobs)

        if jobs:
            st.success(f"Found {len(jobs)} jobs ")

            for job in jobs:
                st.subheader(job["title"])
                st.write("Company:", job["company"])
                st.write("Location:", job["location"])

                if "score" in job:
                    st.write(f"Match Score: {job['score']} ")

                st.write("---")
        else:
            st.error("No jobs found. Try another keyword.")