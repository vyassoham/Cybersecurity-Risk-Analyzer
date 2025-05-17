# core/data_scheme.py

"""
Defines the schema for user cybersecurity input data.
"""

from typing import Dict, List

def get_data_schema() -> List[Dict]:
    """
    Returns the full schema of user data fields used in the risk analyzer.

    Returns:
        List[Dict]: List of field definitions with labels, types, options, and help text.
    """
    return [
        {
            "key": "reuse_passwords",
            "label": "Do you reuse the same passwords across multiple sites?",
            "type": "boolean",
            "help": "Reusing passwords increases risk if one account is compromised.",
        },
        {
            "key": "uses_password_manager",
            "label": "Do you use a password manager?",
            "type": "boolean",
            "help": "Password managers generate and store strong passwords.",
        },
        {
            "key": "uses_2fa",
            "label": "Do you enable Two-Factor Authentication (2FA) where available?",
            "type": "boolean",
            "help": "2FA provides an extra security layer to prevent unauthorized access.",
        },
        {
            "key": "https_check",
            "label": "Do you check for HTTPS before entering personal info?",
            "type": "boolean",
            "help": "HTTPS ensures secure communication with websites.",
        },
        {
            "key": "updates_regularly",
            "label": "Do you regularly update your OS and applications?",
            "type": "boolean",
            "help": "Updates patch security vulnerabilities in your system.",
        },
        {
            "key": "clicks_unknown_links",
            "label": "How often do you click on unknown or suspicious links?",
            "type": "choice",
            "options": ["Often", "Sometimes", "Never"],
            "help": "Clicking unknown links may lead to phishing or malware.",
        }
    ]
