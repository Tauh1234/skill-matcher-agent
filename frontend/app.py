import streamlit as st
import requests

st.title("Skill Matcher Agent")

resume = st.text_area("Paste Resume")

jd = st.text_area("Paste Job Description")

if st.button("Match Skills"):

    response = requests.post(
        "http://127.0.0.1:8000/match",
        json={
            "resume_text": resume,
            "job_description": jd
        }
    )

    result = response.json()

    st.write("Resume Skills:")
    st.write(result["resume_skills"])

    st.write("JD Skills:")
    st.write(result["jd_skills"])

    st.success(
        f"Match Percentage: {result['match_percentage']}%"
    )