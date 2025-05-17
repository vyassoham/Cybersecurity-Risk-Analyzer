def generate_recommendations(data, score):
    recs = []
    if data.get('reuse_passwords'):
        recs.append("Avoid reusing passwords.")
    if not data.get('uses_2fa'):
        recs.append("Enable 2FA for all accounts.")
    if not data.get('https_check'):
        recs.append("Check for HTTPS before submitting sensitive data.")
    if not data.get('updates_regularly'):
        recs.append("Update your OS and apps regularly.")
    if data.get('clicks_unknown_links') != 'Never':
        recs.append("Avoid clicking on suspicious email or website links.")
    if not data.get('uses_password_manager'):
        recs.append("Use a password manager to generate and store strong passwords.")
    return recs
