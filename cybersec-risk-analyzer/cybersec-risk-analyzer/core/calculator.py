def calculate_score(data):
    score = 100
    if data.get('reuse_passwords'): 
        score -= 25
    if not data.get('uses_2fa'): 
        score -= 20
    if not data.get('https_check'): 
        score -= 10
    if not data.get('updates_regularly'): 
        score -= 15
    if data.get('clicks_unknown_links') == 'Often': 
        score -= 20
    elif data.get('clicks_unknown_links') == 'Sometimes': 
        score -= 10
    if not data.get('uses_password_manager'): 
        score -= 10
    return max(score, 0)
