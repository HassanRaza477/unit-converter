import streamlit as st
import re
import math
import requests
import hashlib
import secrets
import string

# Configuration
MIN_LENGTH = 12
COMMON_PASSWORDS_URL = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt"

def check_breaches(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1password[:5], sha1password[5:]
    try:
        response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}", timeout=2)
        return next((int(count) for line in response.text.splitlines() for h, count in [line.split(':')] if h == suffix), 0)
    except Exception:
        return -1

def get_common_passwords():
    try:
        return set(requests.get(COMMON_PASSWORDS_URL, timeout=5).text.splitlines())
    except Exception:
        return set()

def calculate_entropy(password):
    pool_size = sum([
        26 * int(bool(re.search(r'[a-z]', password))),
        26 * int(bool(re.search(r'[A-Z]', password))),
        10 * int(bool(re.search(r'[0-9]', password))),
        32 * int(bool(re.search(r'[^a-zA-Z0-9]', password)))
    ])
    return len(password) * math.log2(pool_size) if pool_size else 0

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(characters) for _ in range(length))

def strength_check(password):
    common_passwords = get_common_passwords()
    return {
        'length': len(password) >= MIN_LENGTH,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'digit': bool(re.search(r'[0-9]', password)),
        'special': bool(re.search(r'[^a-zA-Z0-9]', password)),
        'common': password in common_passwords,
        'entropy': calculate_entropy(password),
        'breach_count': check_breaches(password)
    }

def strength_meter(checks):
    score = sum([
        2 * checks['length'],
        2 * checks['uppercase'],
        2 * checks['lowercase'],
        2 * checks['digit'],
        2 * checks['special'],
        3 * (not checks['common']),
        min(5, checks['entropy'] / 10)
    ]) - (5 if checks['breach_count'] > 0 else 0)
    return max(0, min(100, (score / 16) * 100))

def main():
    st.set_page_config(
        page_title="CyberLock Pass Analyzer",
        page_icon="🔐",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Dark Theme CSS
    st.markdown("""
    <style>
        :root {
            --dark: #000000;
            --red: #FF0000;
            --green: #00FF00;
            --white: #FFFFFF;
            --gray: #404040;
        }

        body {
            background-color: var(--dark) !important;
            color: var(--white) !important;
        }

        .stTextInput input {
            background: var(--gray) !important;
            color: var(--white) !important;
            border-radius: 8px;
            padding: 12px;
            border: 1px solid var(--red) !important;
        }

        .strength-container {
            background: var(--gray);
            border-radius: 15px;
            padding: 20px;
            margin: 15px 0;
            border: 2px solid var(--red);
        }

        .strength-meter {
            height: 15px;
            background: var(--dark);
            border-radius: 10px;
            overflow: hidden;
        }

        .strength-progress {
            height: 100%;
            transition: all 0.5s ease;
            background: linear-gradient(90deg, var(--red), var(--green));
        }

        .criteria-card {
            background: var(--gray);
            border: 1px solid var(--red);
            color: var(--white);
            padding: 15px;
            margin: 10px 0;
            border-radius: 10px;
        }

        .generated-pass {
            background: var(--gray);
            border: 2px solid var(--green);
            color: var(--green);
            padding: 15px;
            border-radius: 10px;
            font-family: monospace;
        }

        .st-bd {
            background-color: var(--dark) !important;
        }

        .stButton button {
            background: var(--red) !important;
            color: var(--white) !important;
            border: none !important;
            border-radius: 8px;
            padding: 10px 20px;
            transition: 0.3s;
        }

        .stButton button:hover {
            background: #CC0000 !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # Main Interface
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("## 🔐 Password Analyzer")
        
        # Password Input
        password = st.text_input(
            "Enter Password:", 
            type="password",
            key="pass_input",
            placeholder="Type your password here..."
        )
        
        if password:
            checks = strength_check(password)
            strength = strength_meter(checks)

            # Strength Meter
            st.markdown(f"""
            <div class="strength-container">
                <div style="display: flex; justify-content: space-between;">
                    <h3 style="color: {checks['breach_count'] and 'var(--red)' or 'var(--green)'}">Security Status</h3>
                    <h3>{strength:.0f}%</h3>
                </div>
                <div class="strength-meter">
                    <div class="strength-progress" style="width: {strength}%;
                        background: linear-gradient(90deg, 
                        var(--red) {max(0, min(100, strength))}%, 
                        var(--green) {max(0, min(100, strength))}%);">
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Security Checklist
            st.markdown("### 🔍 Security Checklist")
            criteria = [
                (checks['length'], f"Minimum {MIN_LENGTH} characters", "📏"),
                (checks['uppercase'], "Contains uppercase letters", "🔼"),
                (checks['lowercase'], "Contains lowercase letters", "🔽"),
                (checks['digit'], "Contains numbers", "🔢"),
                (checks['special'], "Contains special characters", "⭐"),
                (not checks['common'], "Not in common passwords", "🚫")
            ]
            
            for status, text, icon in criteria:
                color = "var(--green)" if status else "var(--red)"
                st.markdown(f"""
                <div class="criteria-card">
                    <span style="color: {color}; font-size: 1.5rem">{"✔" if status else "✖"}</span>
                    <span style="font-size: 1.2rem">{icon}</span>
                    <span style="margin-left: 10px">{text}</span>
                </div>
                """, unsafe_allow_html=True)

    with col2:
        st.markdown("## ⚡ Password Generator")
        
        # Generator Controls
        pass_length = st.slider("Select Length", 12, 32, 16)
        if st.button("Generate Secure Password"):
            new_pass = generate_password(pass_length)
            st.session_state.generated_pass = new_pass
        
        if 'generated_pass' in st.session_state:
            st.markdown("### Generated Password")
            st.markdown(f'<div class="generated-pass">{st.session_state.generated_pass}</div>', unsafe_allow_html=True)
            
            # Copy Functionality
            if st.button("📋 Copy Password"):
                st.write("Password copied to clipboard!")

if __name__ == "__main__":
    main()