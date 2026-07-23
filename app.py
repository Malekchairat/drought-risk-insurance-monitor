import pandas as pd
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="France Drought Risk Monitor", page_icon="🌧️", layout="wide"
)

# 2. Header & Title
st.title("🌧️ Insurance Drought & Claim Risk Monitoring Dashboard")
st.markdown(
    "Automated risk scoring tool for **Catastrophe Naturelle (Sécheresse / RGA)** monitoring and underwriting decisions."
)

# 3. Load Processed Data
@st.cache_data
def load_data():
    return pd.read_csv("drought_processed.csv")


df = load_data()

# 4. Sidebar Controls
st.sidebar.header("🔍 Filtering & Options")
selected_region = st.sidebar.selectbox(
    "Select Target Region:", options=["All Regions"] + list(df["Region"].unique())
)

# Filter dataframe based on selection
if selected_region != "All Regions":
    filtered_df = df[df["Region"] == selected_region]
else:
    filtered_df = df

# 5. Top Metric Cards (KPIs)
col1, col2, col3, col4 = st.columns(4)

with col1:
    avg_temp = filtered_df["Max_Temp_C"].mean()
    st.metric("Avg Max Temp (°C)", f"{avg_temp:.1f} °C")

with col2:
    total_precip = filtered_df["Precipitation_mm"].sum()
    st.metric("Total Rainfall (mm)", f"{total_precip:.1f} mm")

with col3:
    high_risk_days = (filtered_df["Risk_Level"] == 2).sum()
    st.metric(
        "High Drought Alerts",
        f"{high_risk_days} Days",
        delta="Risk Flagged" if high_risk_days > 0 else "Normal",
        delta_color="inverse",
    )

with col4:
    avg_claim_prob = filtered_df["Predicted_Risk_Score"].mean() * 100
    st.metric("Avg Claim Probability", f"{avg_claim_prob:.1f}%")

st.divider()

# 6. Charts & Visualizations
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("🌡️ Temperature Trends")
    st.line_chart(filtered_df.pivot(index="Date", columns="Region", values="Max_Temp_C"))

with chart_col2:
    st.subheader("💧 Precipitation Levels (mm)")
    st.bar_chart(filtered_df.pivot(index="Date", columns="Region", values="Precipitation_mm"))

st.divider()

# 7. ML Risk Model Outputs Table
st.subheader("📋 Regional ML Drought Risk Assessment Table")

# Format Risk Level for display
def highlight_risk(val):
    if val == 2:
        return "background-color: #ff4b4b; color: white; font-weight: bold;"
    elif val == 1:
        return "background-color: #ffa726; color: black;"
    return "background-color: #66bb6a; color: white;"

st.dataframe(
    filtered_df.style.map(highlight_risk, subset=["Risk_Level"]),
    use_container_width=True,
)