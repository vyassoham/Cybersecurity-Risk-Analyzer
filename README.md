# Personalized Cybersecurity Risk Analyzer

🔐 **A comprehensive Streamlit web app to evaluate your cybersecurity habits, provide a risk score, and give personalized recommendations — including password crack time estimation!**

---

## Overview

This app helps users understand their cybersecurity risk based on their online habits such as password reuse, two-factor authentication (2FA) usage, software update frequency, and browsing behavior. It calculates a **risk score** out of 100, offers actionable security recommendations, and estimates how long it would take to crack a password you enter.

Built with modular Python code and Streamlit for an interactive, user-friendly interface.

---

## Features

- **Risk Assessment:** Analyze your security posture with a detailed questionnaire.
- **Personalized Recommendations:** Get specific advice based on your responses.
- **Password Strength Checker:** Enter any password and see an estimate of how long it would take to crack.
- **Modern Streamlit UI:** Clean, responsive design with sidebar information and error handling.
- **Modular Architecture:** Easy to maintain and extend with clear separation of UI, logic, and utils.

---

## Demo

![Demo Screenshot](docs/demo-screenshot.png)  
*(Add a screenshot of your app here)*

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/cybersecurity-risk-analyzer.git
    cd cybersecurity-risk-analyzer
    ```

2. Create and activate a Python virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the app:
    ```bash
    streamlit run app.py
    ```

---

## Usage

- Answer the cybersecurity habits questionnaire.
- Submit to get your risk score and tailored security recommendations.
- Navigate to the Password Strength Checker section to test any password.
- Improve your security based on insights provided.

---

## Project Structure

cybersecurity-risk-analyzer/
│
├── app.py # Main Streamlit app
├── components/ # UI components (inputs, results)
├── core/ # Core logic (calculations, recommendations)
├── utils/ # Utility modules (logging, pdf export, password analysis)
├── config/ # App configuration and constants
├── requirements.txt # Python dependencies
├── README.md
└── .gitignore


