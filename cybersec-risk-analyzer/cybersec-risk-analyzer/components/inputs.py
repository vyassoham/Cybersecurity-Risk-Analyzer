import streamlit as st

def collect_inputs():
    st.subheader("📝 Online Habits Assessment")

    data = {}

    st.markdown("#### 🔐 Password Practices")
    data['reuse_passwords'] = st.radio(
        "Do you reuse the same passwords across multiple sites?",
        [True, False],
        help="Using the same password increases vulnerability if one site is compromised."
    )

    data['uses_password_manager'] = st.radio(
        "Do you use a password manager?",
        [True, False],
        help="Password managers help create and store strong, unique passwords for each site."
    )

    st.markdown("#### 🧾 Security Measures")
    data['uses_2fa'] = st.radio(
        "Do you enable Two-Factor Authentication (2FA) where available?",
        [True, False],
        help="2FA adds an extra layer of security to your accounts."
    )

    data['https_check'] = st.radio(
        "Do you check for HTTPS before entering personal information?",
        [True, False],
        help="HTTPS ensures encrypted communication with websites."
    )

    st.markdown("#### 🖥️ Device & Browsing Behavior")
    data['updates_regularly'] = st.radio(
        "Do you regularly update your OS and software?",
        [True, False],
        help="Regular updates patch security vulnerabilities."
    )

    data['clicks_unknown_links'] = st.radio(
        "How often do you click on unknown or suspicious links?",
        ["Often", "Sometimes", "Never"],
        help="Clicking on unknown links can lead to phishing or malware."
    )

    st.markdown("#### 🔒 Password Strength Estimator")
    data['password_input'] = st.text_input(
        "Type a password to check how strong it is:",
        type="password",
        help="Enter any password to see estimated crack time."
    )

    return data
