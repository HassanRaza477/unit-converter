import streamlit as st
import math
import re

# Modern 3D Neumorphic Design CSS
st.markdown("""
<style>
    :root {
        --primary: #0052CC;  /* High contrast blue */
        --secondary: #FF6B00; /* High contrast orange */
        --background: #FFFFFF;
        --text: #2D3748;
        --error: #CC0000;
    }

    .stApp {
        background: var(--background);
        color: var(--text);
        font-family: system-ui;
    }

    .stTextInput input {
        background: var(--background) !important;
        color: var(--text) !important;
        border: 3px solid var(--primary) !important;
        border-radius: 12px;
        font-size: 2.5rem !important;
        padding: 24px 30px !important;
        margin-bottom: 2rem;
        font-weight: 700;
        height:100% !important;
    }

    button {
        background: var(--background) !important;
        color: var(--primary) !important;
        border: 3px solid var(--primary) !important;
        padding: 1.5rem 0 !important;
        margin: 8px !important;
        width:100% !important;
        border-radius: 12px !important;
        font-size: 1.6rem !important;
        font-weight: 700;
        transition: all 0.2s ease;
    }

    button:hover {
        background: var(--primary) !important;
        color: var(--background) !important;
        transform: scale(1.05);
    }

    button:active {
        transform: scale(0.95);
    }

    /* Operator Buttons */
    button[data-testid="baseButton-secondary"]:has(div:contains("/")),
    button[data-testid="baseButton-secondary"]:has(div:contains("*")),
    button[data-testid="baseButton-secondary"]:has(div:contains("-")),
    button[data-testid="baseButton-secondary"]:has(div:contains("+"))) {
        color: var(--secondary) !important;
        border-color: var(--secondary) !important;
    }

    /* Error Messages */
    .stAlert {
        background: #FFEBEE !important;
        color: var(--error) !important;
        border: 2px solid var(--error) !important;
    }

    /* History Panel */
    .history-item {
        background: #F7FAFC;
        color: var(--text);
        border: 2px solid #E2E8F0;
        border-radius: 8px;
        padding: 12px;
        margin: 8px 0;
    }

    @media (max-width: 768px) {
        button {
            padding: 1.2rem 0 !important;
            font-size: 1.4rem !important;
        }
        
        .stTextInput input {
            font-size: 2rem !important;
            padding: 20px 16px !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# Session State Management
if 'equation' not in st.session_state:
    st.session_state.equation = ''
if 'history' not in st.session_state:
    st.session_state.history = []

# Evaluation Function
def safe_eval(expr):
    expr = expr.replace('^', '**').replace('π', str(math.pi))
    expr = re.sub(r'(\d+)!', r'math.factorial(\1)', expr)
    return eval(expr, {'math': math, '__builtins__': None})

# Main App Layout
def main():
    st.title("🌟 NeoCalc Pro")
    
    # Main Display
    display = st.empty()
    display.text_input("", value=st.session_state.equation, 
                     key="input", label_visibility="collapsed")

    # Button Grid
    btn_layout = [
        ['C', '(', ')', '/'],
        ['7', '8', '9', '*'],
        ['4', '5', '6', '-'],
        ['1', '2', '3', '+'],
        ['0', '.', 'π', '=']
    ]

    for row in btn_layout:
        cols = st.columns([1.2 if btn == '0' else 1 for btn in row])
        for i, btn in enumerate(row):
            with cols[i]:
                if st.button(btn, key=f"btn_{btn}"):
                    handle_click(btn)

    # Scientific Functions
    with st.expander("🚀 Advanced Functions", expanded=True):
        sci_cols = st.columns(4)
        sci_btns = ['sin(', 'cos(', 'tan(', 'log(']
        for col, btn in zip(sci_cols, sci_btns):
            with col:
                if st.button(btn):
                    st.session_state.equation += btn

    # History Sidebar
    with st.sidebar:
        st.header("📜 History")
        for item in reversed(st.session_state.history[-6:]):
            st.markdown(f'<div class="history-item">✨ {item}</div>', 
                       unsafe_allow_html=True)
        if st.button("🧹 Clear History", use_container_width=True):
            st.session_state.history = []

def handle_click(btn):
    if btn == 'C':
        st.session_state.equation = ''
    elif btn == '=':
        try:
            result = safe_eval(st.session_state.equation)
            st.session_state.history.append(
                f"{st.session_state.equation} = {result:.4f}"
            )
            st.session_state.equation = f"{result:.6f}"
        except Exception as e:
            st.session_state.equation = "🚨 Error"
    else:
        st.session_state.equation += btn

if __name__ == "__main__":
    main()