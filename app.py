import streamlit as st

from src.matching import match_resume_to_job
from src.pdf_text import PDFTextError, extract_pdf_text

MAX_UPLOAD_BYTES = 5 * 1024 * 1024

st.set_page_config(page_title="SkillLens", layout="centered")
st.title("SkillLens")
st.caption("Explainable resume-to-role matching")
st.info(
    "Skill overlap only. This is not a hiring decision or candidate ranking. "
    "A human must make every hiring decision."
)

st.session_state.setdefault("widget_generation", 0)
generation = st.session_state["widget_generation"]

with st.form("analysis"):
    resume_file = st.file_uploader(
        "Upload resume PDF (max 5 MB)",
        type=["pdf"],
        key=f"resume_{generation}",
    )
    job_description = st.text_area(
        "Paste job description",
        height=220,
        key=f"job_description_{generation}",
    )
    submitted = st.form_submit_button("Analyze match", type="primary")

if submitted:
    st.session_state.pop("result", None)
    st.session_state.pop("analysis_error", None)

    if resume_file is None:
        st.session_state["analysis_error"] = "Upload a PDF resume to continue."
    elif not job_description.strip():
        st.session_state["analysis_error"] = "Paste a job description to continue."
    elif resume_file.size > MAX_UPLOAD_BYTES:
        st.session_state["analysis_error"] = "The PDF is larger than the 5 MB upload limit."
    else:
        try:
            with st.spinner("Reading the PDF and comparing skills..."):
                resume_text = extract_pdf_text(resume_file.getvalue())
                st.session_state["result"] = match_resume_to_job(resume_text, job_description)
        except (PDFTextError, ValueError) as error:
            st.session_state["analysis_error"] = str(error)

if st.button("Delete uploaded data and results"):
    st.session_state.pop("result", None)
    st.session_state.pop("analysis_error", None)
    st.session_state["widget_generation"] += 1
    st.rerun()

if error := st.session_state.get("analysis_error"):
    st.error(error, title="Analysis could not run")

if result := st.session_state.get("result"):
    st.subheader("Match summary")
    st.metric("Skill overlap", f"{result['score']}%")
    st.caption(
        f"{result['matched_count']} of {result['requested_count']} identified job skills "
        "were found in the resume. This score uses skill overlap only."
    )

    st.subheader("Matched skills")
    if result["matched"]:
        for item in result["matched"]:
            with st.container(border=True):
                st.markdown(f"**{item['skill']}**")
                st.caption("Resume evidence")
                st.text(item["resume_evidence"])
                st.caption("Job description evidence")
                st.text(item["job_evidence"])
    else:
        st.write("No supported job skills were found in the resume.")

    st.subheader("Skills to develop")
    if result["missing"]:
        for item in result["missing"]:
            with st.container(border=True):
                st.markdown(f"**{item['skill']}**")
                st.caption("Requested in the job description")
                st.text(item["job_evidence"])
    else:
        st.write("All identified job skills were found in the resume.")

st.caption("Files and results stay in this session and are not saved by SkillLens.")