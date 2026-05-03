import streamlit as st

# 1. Page Configuration & Branding
st.set_page_config(page_title="Life Policy Pilot | Financial Altitude Analysis", page_icon="✈️", layout="wide")
PRIMARY_RED = "#CC0700" 
SILVER_GRAY = "#E2E8F0"

st.markdown(f"""
    <style>
    /* 1. App-wide Background */
    .stApp {{
        background: linear-gradient(180deg, {SILVER_GRAY} 0%, #FFFFFF 100%);
    }}

    /* 2. Content Container (Makes the 'Flight Deck' stand out) */
    .block-container {{
        background-color: white;
        padding: 40px !important;
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.05);
        margin-top: 30px;
    }}

    /* 3. Branding Colors & Metrics */
    h1, h2, h3 {{ color: {PRIMARY_RED} !important; }}
    
    .metric-container {{ 
        background-color: #f8fafc; 
        padding: 25px; 
        border-radius: 12px; 
        border-left: 8px solid {PRIMARY_RED}; 
        margin-bottom: 20px;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);
    }}
    
    /* 4. Input Styling */
    .stNumberInput, .stSlider {{ border-bottom: 1px solid {SILVER_GRAY}; padding-bottom: 15px; }}
    </style>
    """, unsafe_allow_html=True)

# 2. Header
st.title("✈️ Financial Altitude Analysis")
st.subheader("Step 1: The Pre-Flight Check")
st.info("As your fiduciary advocate, we use precise analysis to identify the coverage 'Altitude' required to clear your financial obligations and protect your beneficiaries.")

# 3. Input & Analysis Layout
col_in, col_out = st.columns([1, 1.2], gap="large")

with col_in:
    st.markdown("### 🛠️ Fixed Obligations")
    st.write("Liabilities that must be cleared to ensure a 'Smooth Landing'.")
    mortgage = st.number_input("Mortgage & Large Debt Balances ($)", value=250000, step=10000)
    education = st.number_input("Education/College Fund Goals ($)", value=100000, step=5000)
    final_exp = st.number_input("Final Expenses & Legal Costs ($)", value=15000, step=1000)
    
    st.markdown("---")
    st.markdown("### 💰 Income Replacement")
    st.write("Capital required to maintain your family's standard of living.")
    income = st.number_input("Annual Income to Protect ($)", value=75000, step=5000)
    years = st.slider("Years of Protection Needed", 5, 30, 20)
    
    st.markdown("---")
    st.markdown("### ⚓ Asset Offsets")
    st.write("Existing resources that reduce total coverage requirements.")
    assets = st.number_input("Liquid Savings & Current Insurance ($)", value=50000, step=5000)

# 4. Calculation Logic
income_requirement = income * years
total_liabilities = mortgage + education + final_exp + income_requirement
net_gap = max(0, total_liabilities - assets)

with col_out:
    st.markdown("### 📊 Analysis Dashboard")
    
    # Visualizing the Gap
    st.markdown('<div class="metric-container">', unsafe_allow_html=True)
    st.metric("Total Projected Need", f"${total_liabilities:,.0f}")
    st.metric("Net Coverage Gap", f"${net_gap:,.0f}")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("#### Flight Path Summary")
    summary_text = (
        f"* **Fixed Obligations:** ${mortgage+education+final_exp:,.0f} in immediate debt.\n"
        f"* **Income Security:** ${income_requirement:,.0f} needed for {years} years.\n"
        f"* **The Gap:** Your current 'Altitude' is short by **${net_gap:,.0f}**."
    )
    st.write(summary_text)
    
    st.divider()
    st.markdown("#### 🧭 Next Steps")
    st.write("Your objective analysis suggests a strategic gap that requires professional advocacy.")
    st.button("Request Full Pre-Flight Consultation")

# 5. Professional Footer
st.divider()
st.caption("Note: This tool provides objective simulations based on the D.I.M.E. method. All results are projections for educational purposes and do not represent a final offer. Final underwriting depends on carrier-specific guidelines.")
