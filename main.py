import streamlit as st
from resume_parser import parse_resume
from analyzer import analyze_resume

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")
st.title("📄 AI-Powered Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])
job_description = st.text_area("Paste the job description (optional)", height=200)

if uploaded_file:
    resume_text = parse_resume(uploaded_file)

    if resume_text:
        st.subheader("📋 Extracted Resume Text")
        st.text_area("Text", resume_text[:3000], height=300)

        st.subheader("📊 Resume Analysis")
        results = analyze_resume(resume_text, job_description)

        st.markdown("**Entities Extracted:**")
        for key, value in results["entities"].items():
            st.write(f"**{key.title()}:**", value)

        st.markdown("**Matching Score:**")
        st.metric("Relevance Score", f"{results['score']}%")

        if results.get("missing_keywords"):
            st.markdown("**🔍 Suggested Improvements:**")
            st.warning(f"Missing keywords: {', '.join(results['missing_keywords'])}")
