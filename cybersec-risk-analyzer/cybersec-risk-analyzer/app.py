import streamlit as st
from components.inputs import collect_inputs
from core.calculator import calculate_score
from core.recommender import generate_recommendations
from components.results import show_results
from core.password_strength import estimate_crack_time

st.set_page_config(
    page_title="Cybersecurity Risk Analyzer",
    layout="centered",
)

st.title("🔐 Personalized Cybersecurity Risk Analyzer")
st.markdown(
    "Answer the questions below to find out your **cyber risk score** "
    "and get personalized recommendations."
)
st.markdown("---")

with st.form(key="risk_form"):
    user_data = collect_inputs()
    submitted = st.form_submit_button("🔍 Analyze My Risk")

if submitted:
    try:
        score = calculate_score(user_data)
        recommendations = generate_recommendations(user_data, score)
        show_results(score, recommendations)

        # Password crack time estimate
        crack_time = estimate_crack_time(user_data.get('password_input', ''))
        st.info(crack_time)

    except Exception as e:
        st.error(f"⚠️ An error occurred during analysis:\n\n`{e}`")

st.markdown("---")
st.markdown(
    "<center><sub>© 2025 Soham Vyas | CyberSec Risk Analyzer</sub></center>",
    unsafe_allow_html=True
)
