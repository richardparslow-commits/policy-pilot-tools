import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Life Policy Pilot | Flight Simulator", page_icon="✈️")

# 2. Branding Colors
PRIMARY_RED = "#CC0700"
SILVER_GRAY = "#E2E8F0"

# Custom CSS for Professional Branding
st.markdown(f"""
    <style>
    /* Heading Colors */
    h1, h2, h3 {{ color: {PRIMARY_RED} !important; }}
    
    /* Button Styling */
    .stButton>button {{ 
        background-color: {PRIMARY_RED}; 
        color: white; 
        border: none;
        border-radius: 4px;
    }}
    
    /* Metric Display Styling */
    [data-testid="stMetricValue"] {{
        background-color: {SILVER_GRAY};
        padding: 10px;
        border-radius: 8px;
        color: #1a202c;
    }}
    </style>
    """, unsafe_allow_html=True)

# 3. Header and Introduction
st.title("✈️ The Pilot's Navigation Tool")
st.subheader("Simulating Your Financial Flight Path")

st.info("As your fiduciary advocate, this tool provides projections based on the data you provide. It is designed for analysis and does not represent a final offer.")

# 4. Input Controls (Sidebar)
with st.sidebar:
    st.header("Flight Data Inputs")
    income = st.number_input("Annual Income to Protect ($)", min_value=0, value=75000, step=5000)
    years = st.slider("Years of Protection Needed", 5, 40, 20)
    debt = st.number_input("Existing Debt/Mortgages ($)", min_value=0, value=250000)

# 5. Simulation Logic
total_need = (income * years) + debt

# 6. Results Display
col1, col2 = st.columns(2)

with col1:
    st.metric("Suggested Coverage Altitude", f"${total_need:,.0f}")

with col2:
    st.write("### Your Flight Path Analysis")
    st.write(f"To maintain your current standard of living for **{years} years** while clearing **${debt:,.0f}** in debt, a coverage amount of **${total_need:,.0f}** is the projected baseline.")

st.divider()

# 7. Professional Disclaimer
st.caption("Note: This simulation is for educational purposes. Final underwriting depends on carrier-specific guidelines and individual health profiles. We prioritize objective analysis to find the most efficient path for your unique needs.")
