def estimate_crack_time(password: str) -> str:
    import math

    if not password:
        return "No password entered."

    length = len(password)
    charset_size = 0

    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(not c.isalnum() for c in password):
        charset_size += 32  # Approximate special characters count

    if charset_size == 0:
        return "Password must contain valid characters."

    combinations = charset_size ** length

    guesses_per_second = 1e9  # 1 billion guesses/sec (example attacker speed)
    seconds = combinations / guesses_per_second

    if seconds < 60:
        return f"Estimated crack time: {int(seconds)} seconds"
    elif seconds < 3600:
        return f"Estimated crack time: {int(seconds / 60)} minutes"
    elif seconds < 86400:
        return f"Estimated crack time: {int(seconds / 3600)} hours"
    elif seconds < 31536000:
        return f"Estimated crack time: {int(seconds / 86400)} days"
    else:
        years = seconds / 31536000
        return f"Estimated crack time: {years:.2f} years"
