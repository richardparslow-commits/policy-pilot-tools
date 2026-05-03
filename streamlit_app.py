import streamlit as st

# Branding & Layout
st.set_page_config(page_title="Life Policy Pilot | Advanced Navigator", layout="wide")
PRIMARY_RED = "#CC0700" #
SILVER_GRAY = "#E2E8F0" #

st.title("✈️ Step 1: The Pre-Flight Check") #
st.markdown("### Advanced Fiduciary Needs Analysis")

# Sidebar: Detailed Needs
with st.sidebar:
    st.header("1. Financial Liabilities")
    mortgage = st.number_input("Mortgage Balance ($)", value=250000)
    other_debt = st.number_input("Other Debt (Auto, Student, CC) ($)", value=25000)
    education = st.number_input("Education Fund Goals ($)", value=100000)
    final_expenses = st.number_input("Final Expenses/Legal ($)", value=15000)

    st.header("2. Income Replacement")
    income_replace = st.number_input("Annual Income to Replace ($)", value=75000)
    years = st.slider("Years of Replacement", 5, 30, 20)

    st.header("3. Existing Assets (Offsets)")
    savings = st.number_input("Liquid Assets/Savings ($)", value=50000)
    current_life = st.number_input("Existing Life Insurance ($)", value=100000)

# Calculations
total_liabilities = mortgage + other_debt + education + final_expenses + (income_replace * years)
net_need = max(0, total_liabilities - (savings + current_life))

# Results
st.info("As your fiduciary advocate, we identify the specific 'Altitude' required to clear your financial obligations.") #

col1, col2 = st.columns(2)
with col1:
    st.metric("Total Projected Need", f"${total_liabilities:,.0f}")
with col2:
    st.metric("Net Coverage Gap", f"${net_need:,.0f}", delta_color="inverse")

# Pre-Underwriting Teaser
st.divider()
st.subheader("🛠️ Pre-Underwriting Indicators")
st.write("Health and lifestyle (e.g., tobacco use or hobbies like Jiu-Jitsu) influence carrier selection.")
# This reinforces the "Carrier Match" logic from your site
