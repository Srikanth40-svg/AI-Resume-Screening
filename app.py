import streamlit as st
import pandas as pd
from pathlib import Path
from resume_parser import analyze_job_description, process_resume

st.set_page_config(
    page_title="AI Resume Screening",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #9ca3af;
    margin-bottom: 30px;
}

.section-title {
    font-size: 25px;
    font-weight: 600;
    margin-top: 25px;
}

.candidate-card {
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #333;
    margin-bottom: 15px;
}

.score {
    font-size: 30px;
    font-weight: 700;
}

.skill {
    padding: 6px 10px;
    border-radius: 6px;
    margin: 4px;
    display: inline-block;
}

</style>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="main-title">🤖 AI Resume Screening & Job Matching</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-powered resume analysis and candidate ranking using LLMs.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


st.markdown(
    '<div class="section-title">📋 Job Description</div>',
    unsafe_allow_html=True
)

job_description = st.text_area(
    "Paste the job description",
    height=220,
    placeholder="Paste the complete job description here...",
    label_visibility="collapsed"
)


st.markdown(
    '<div class="section-title">📄 Candidate Resumes</div>',
    unsafe_allow_html=True
)

uploaded_files = st.file_uploader(
    "Upload PDF or DOCX resumes",
    type=["pdf", "docx"],
    accept_multiple_files=True
)


if uploaded_files:
    st.success(
        f"{len(uploaded_files)} resume(s) uploaded successfully."
    )


st.write("")

analyze_button = st.button(
    "🚀 Analyze Resumes",
    type="primary",
    use_container_width=True
)


if analyze_button:

    if not job_description.strip():

        st.warning(
            "Please enter a job description before analyzing."
        )

    elif not uploaded_files:

        st.warning(
            "Please upload at least one resume."
        )

    else:

        with st.spinner(
            "🤖 AI is analyzing the candidates..."
        ):

            job = analyze_job_description(
                job_description
            )

            results = []

            for uploaded_file in uploaded_files:

                temp_path = Path(
                    "temp_" + uploaded_file.name
                )

                with open(temp_path, "wb") as f:
                    f.write(
                        uploaded_file.getbuffer()
                    )

                try:

                    result = process_resume(
                        temp_path,
                        job
                    )

                    if result:

                        result["filename"] = (
                            uploaded_file.name
                        )

                        results.append(result)

                finally:

                    if temp_path.exists():
                        temp_path.unlink()


        results.sort(
            key=lambda candidate: candidate["score"],
            reverse=True
        )


        if results:

            st.divider()

            st.markdown(
                '<div class="section-title">'
                '🏆 Candidate Rankings'
                '</div>',
                unsafe_allow_html=True
            )
            csv_data = []

            for candidate in results:

                details = candidate["details"]

                csv_data.append({
                    "Candidate": candidate["name"],
                    "Score": candidate["score"],
                    "Matching Skills": ", ".join(
                        details.get("matching_skills", [])
                    ),
                    "Missing Skills": ", ".join(
                        details.get(
                            "missing_important_skills",
                            []
                        )
                    ),
                    "Experience Requirement": details.get(
                        "experience_requirement_met",
                        "Not specified"
                    ),
                    "Verdict": details.get(
                        "verdict",
                        details.get(
                            "final_verdict",
                            ""
                        )
                    )
                })

            df = pd.DataFrame(csv_data)

            csv_file = df.to_csv(index=False)

            st.download_button(
                label="📥 Download Results as CSV",
                data=csv_file,
                file_name="candidate_screening_results.csv",
                mime="text/csv"
            )

            st.write("")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Candidates Analyzed",
                    len(results)
                )

            with col2:
                st.metric(
                    "Top Score",
                    f"{results[0]['score']}%"
                )

            with col3:
                average_score = sum(
                    candidate["score"]
                    for candidate in results
                ) / len(results)

                st.metric(
                    "Average Score",
                    f"{average_score:.1f}%"
                )


            st.write("")


            for index, candidate in enumerate(
                results,
                start=1
            ):

                details = candidate["details"]

                name = candidate["name"]
                score = candidate["score"]

                if index == 1:
                    rank = "🥇"
                elif index == 2:
                    rank = "🥈"
                elif index == 3:
                    rank = "🥉"
                else:
                    rank = f"#{index}"


                with st.expander(
                    f"{rank}  {name}  —  {score:.1f}%",
                    expanded=(index == 1)
                ):

                    st.progress(
                        min(max(score / 100, 0.0), 1.0),
                        text=f"Match Score: {score:.1f}%"
                    )


                    st.write("")


                    col1, col2 = st.columns(2)


                    with col1:

                        st.subheader(
                            "✅ Matching Skills"
                        )

                        matching_skills = details.get(
                            "matching_skills",
                            []
                        )

                        if matching_skills:

                            for skill in matching_skills:
                                st.markdown(
                                    f"• {skill}"
                                )

                        else:

                            st.write(
                                "No matching skills identified."
                            )


                    with col2:

                        st.subheader(
                            "❌ Missing Skills"
                        )

                        missing_skills = details.get(
                            "missing_important_skills",
                            []
                        )

                        if missing_skills:

                            for skill in missing_skills:
                                st.markdown(
                                    f"• {skill}"
                                )

                        else:

                            st.write(
                                "No major missing skills identified."
                            )


                    st.divider()


                    st.subheader(
                        "💼 Experience Requirement"
                    )

                    experience = details.get(
                        "experience_requirement_met",
                        "Not specified"
                    )

                    if experience is True:

                        st.success(
                            "Experience requirement met"
                        )

                    elif experience is False:

                        st.error(
                            "Experience requirement not met"
                        )

                    else:

                        st.info(
                            str(experience)
                        )


                    st.subheader(
                        "🧠 AI Verdict"
                    )

                    verdict = details.get(
                        "verdict",
                        details.get(
                            "final_verdict",
                            "No verdict available"
                        )
                    )

                    st.info(verdict)


        else:

            st.error(
                "No candidates could be processed."
            )