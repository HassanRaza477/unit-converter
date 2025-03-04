import streamlit as st
import time
import pandas as pd

# Custom CSS for modern design
st.set_page_config(page_title="Professional Unit Converter", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@300;500;700&display=swap');
    
    * {
        font-family: 'Roboto Mono', monospace;
    }
    
    .main {
        background: linear-gradient(45deg, #0f0c29, #302b63, #24243e);
        color: #fff !important;
    }
    
    .stSelectbox [data-testid='stSelectbox'] > div {
        background: rgba(255,255,255,0.1) !important;
        border-radius: 15px !important;
        border: 2px solid #6366f1 !important;
    }
    
    .metric-box {
        border: 2px solid #3b82f6;
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        background: rgba(255,255,255,0.05);
    }
    
    .glowing-text {
        animation: glow 1.5s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { text-shadow: 0 0 10px #3b82f6; }
        to { text-shadow: 0 0 20px #3b82f6, 0 0 30px #3b82f6; }
    }
</style>
""", unsafe_allow_html=True)

# Unit database with multipliers
UNIT_SYSTEM = {
    "📏 Length": {
        "Nanometers": 1e-9,
        "Micrometers": 1e-6,
        "Millimeters": 0.001,
        "Centimeters": 0.01,
        "Meters": 1.0,
        "Kilometers": 1000.0,
        "Inches": 0.0254,
        "Feet": 0.3048,
        "Miles": 1609.34
    },
    "⚖️ Weight": {
        "Milligrams": 0.001,
        "Grams": 1.0,
        "Kilograms": 1000.0,
        "Metric Tons": 1e6,
        "Ounces": 28.3495,
        "Pounds": 453.592
    },
    "🧪 Chemistry": {
        "Moles": 1.0,
        "Millimoles": 1e-3,
        "Atoms": 6.022e23,
        "Molecules": 6.022e23,
        "Formula Units": 6.022e23
    },
    "💡 Energy": {
        "Joules": 1.0,
        "Kilojoules": 1000.0,
        "Calories": 4.184,
        "Kilocalories": 4184.0,
        "Electronvolts": 1.602e-19
    }
}

# Conversion logic
def convert_units(value, from_unit, to_unit, category):
    try:
        base_value = value * UNIT_SYSTEM[category][from_unit]
        converted_value = base_value / UNIT_SYSTEM[category][to_unit]
        return round(converted_value, 6)
    except:
        return None

# Main UI
st.title("🔬 Professional Unit Converter")
st.markdown("<h3 class='glowing-text'>Precision Conversions for Science & Engineering</h3>", unsafe_allow_html=True)

# Session state initialization
if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=["Time", "From", "To", "Value", "Result"])

# Main converter
with st.container():
    col1, col2 = st.columns([1, 1])
    with col1:
        category = st.selectbox("Select Category", list(UNIT_SYSTEM.keys()))
    with col2:
        units = list(UNIT_SYSTEM[category].keys())
        from_unit = st.selectbox("From Unit", units)
        to_unit = st.selectbox("To Unit", [u for u in units if u != from_unit])

value = st.number_input("Enter Value", min_value=0.0, value=1.0, step=0.1)

# Conversion with animation
if st.button("🚀 Convert Now", type="primary"):
    with st.spinner("Converting..."):
        time.sleep(0.5)
        result = convert_units(value, from_unit, to_unit, category)
        
        if result is not None:
            st.markdown(f"""
            <div class="metric-box">
                **{value} {from_unit}**  
                =  
                **{result} {to_unit}**  
            </div>
            """, unsafe_allow_html=True)
            
            # Add to history
            new_entry = pd.DataFrame([{
                "Time": pd.Timestamp.now(),
                "From": f"{value} {from_unit}",
                "To": f"{result} {to_unit}",
                "Value": value,
                "Result": result
            }])
            
            st.session_state.history = pd.concat([st.session_state.history, new_entry], ignore_index=True)
        else:
            st.error("Invalid conversion attempt!")

# History and analytics
with st.expander("📈 Conversion Analytics", expanded=True):
    tab1, tab2 = st.tabs(["History", "Statistics"])
    
    with tab1:
        if not st.session_state.history.empty:
            st.dataframe(st.session_state.history.style.format({"Value": "{:.4f}", "Result": "{:.4f}"}))
        else:
            st.info("No conversion history available")
    
    with tab2:
        if not st.session_state.history.empty:
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Total Conversions", len(st.session_state.history))
                st.line_chart(st.session_state.history.set_index("Time")["Value"])
            with col2:
                avg_speed = (st.session_state.history["Result"] / st.session_state.history["Value"]).mean()
                st.metric("Average Conversion Rate", f"{avg_speed:.4f}")
                st.bar_chart(st.session_state.history["Result"].value_counts())
        else:
            st.warning("No data for statistics")

# Unit reference table
with st.sidebar:
    st.subheader("🔍 Unit Reference")
    selected_category = st.selectbox("Category Reference", list(UNIT_SYSTEM.keys()))
    
    df = pd.DataFrame({
        "Unit": UNIT_SYSTEM[selected_category].keys(),
        "Base Multiplier": UNIT_SYSTEM[selected_category].values()
    })
    
    st.dataframe(df.style.format({"Base Multiplier": "{:.2e}"}), height=300)

# Responsive design
st.markdown("""
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
@media (max-width: 768px) {
    .stSelectbox [data-testid='stSelectbox'] > div {
        font-size: 14px !important;
    }
    .metric-box {
        padding: 15px !important;
    }
}
</style>
""", unsafe_allow_html=True)