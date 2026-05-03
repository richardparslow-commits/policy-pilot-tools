import streamlit as st
from datetime import datetime, timedelta

# 1. Page Configuration & Branding
st.set_page_config(page_title="Life Policy Pilot | Navigation Tool", page_icon="✈️", layout="wide")
PRIMARY_RED = "#CC0700" 
SILVER_GRAY = "#E2E8F0"

st.markdown(f"""
    <style>
    h1, h2, h3 {{ color: {PRIMARY_RED} !important; }}
    .stTabs [data-baseweb="tab-list"] {{ gap: 24px; }}
    .stTabs [data-baseweb="tab"] {{ height: 50px; background-color: {SILVER_GRAY}; border-radius: 4px 4px 0 0; padding: 10px 20px; }}
    .stTabs [aria-selected="true"] {{ background-color: {PRIMARY_RED}; color: white; }}
    .metric-container {{ background-color: {SILVER_GRAY}; padding: 20px; border-radius: 10px; border-left: 5px solid {PRIMARY_RED}; }}
    </style>
    """, unsafe_allow_html=True)

# 2. Header
st.title("✈️ The Pilot's Navigation Tool")
st.info("As your fiduciary advocate, we use precise analysis to ensure your flight path is secure and transparent.")

# 3. Navigation Tabs
tab1, tab2 = st.tabs(["Step 1: Pre-Flight Check (Needs)", "Phase One: Smooth Landing (Checklist)"])

# --- TAB 1: PRE-FLIGHT CHECK (Step 1) ---
with tab1:
    st.subheader("Financial Altitude Analysis")
    st.write("Calculate the coverage required to clear your financial obligations and protect your beneficiaries.")
    
    col_in, col_out = st.columns([1, 1], gap="large")
    
    with col_in:
        st.markdown("#### 🛠️ Obligations")
        mortgage = st.number_input("Mortgage & Large Debts ($)", value=250000, step=10000)
        education = st.number_input("Education/College Fund Goals ($)", value=100000, step=5000)
        final_exp = st.number_input("Final Expenses & Legal ($)", value=15000, step=1000)
        
        st.markdown("#### 💰 Income Replacement")
        income = st.number_input("Annual Income to Protect ($)", value=75000, step=5000)
        years = st.slider("Years of Protection Needed", 5, 30, 20)
        
        st.markdown("#### ⚓ Existing Assets (Offsets)")
        assets = st.number_input("Liquid Savings & Current Insurance ($)", value=50000, step=5000)

    # Calculation Logic
    total_obligation = mortgage + education + final_exp + (income * years)
    net_gap = max(0, total_obligation - assets)

    with col_out:
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric("Total Projected Need", f"${total_obligation:,.0f}")
        st.metric("Net Coverage Gap", f"${net_gap:,.0f}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.write("### Flight Analysis")
        st.write(f"To clear your **${mortgage+education+final_exp:,.0f}** in fixed obligations and replace your income for **{years} years**, your baseline 'Altitude' is **${total_obligation:,.0f}**.")
        st.write(f"Accounting for your current assets, we recommend exploring options to bridge the **${net_gap:,.0f}** gap.")

# --- TAB 2: PHASE ONE (Smooth Landing) ---
with tab2:
    st.subheader("The 30-Day Post-Purchase Administration Checklist")
    st.write("Ensuring your policy is properly filed and your 'Free Look' period is protected.")

    col_check, col_date = st.columns(2)

    with col_check:
        st.markdown("#### ✅ Critical Checkpoints")
        st.checkbox("Confirm physical or digital policy delivery.")
        st.checkbox("Verify beneficiary names and social security numbers are correct.")
        st.checkbox("Secure the policy in a known location (The 'Pilot's Log').")
        st.checkbox("Notify beneficiaries of policy location and agent contact.")
        st.checkbox("Set up automated premium payments to prevent lapse.")

    with col_date:
        st.markdown("#### ⏳ Free Look Period Tracker")
        effective_date = st.date_input("Policy Effective Date", datetime.now())
        look_days = st.selectbox("Free Look Period (Days)", [10, 20, 30], index=2)
        
        deadline = effective_date + timedelta(days=look_days)
        days_left = (deadline - datetime.now().date()).days
        
        if days_left > 0:
            st.warning(f"Your Free Look Period expires on **{deadline.strftime('%B %d, %Y')}**.")
            st.write(f"You have **{days_left} days** remaining to review your contract without penalty.")
        else:
            st.error(f"The standard Free Look Period for this date has likely passed ({deadline.strftime('%B %d, %Y')}).")

st.divider()
st.caption("Note: This tool provides objective simulations. All 'Flight Plans' are subject to final contract terms and professional advocacy review.")
