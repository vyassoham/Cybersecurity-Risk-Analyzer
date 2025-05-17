import streamlit as st

def show_results(score, recs):
    st.subheader(f"📊 Risk Score: {score}/100")

    if score >= 80:
        st.success("Low Risk. Well done!")
    elif score >= 50:
        st.warning("Medium Risk. Room for improvement.")
    else:
        st.error("High Risk. Take action now!")

    st.markdown("---")
    st.write("### Recommendations:")
    for r in recs:
        st.write(f"- {r}")
