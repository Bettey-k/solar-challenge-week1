# app/main.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import os

# Configure Streamlit page
st.set_page_config(page_title="Solar Comparison Dashboard", page_icon="☀️", layout="wide")

# ---- HEADER ----
st.title("☀️ Solar Data Comparison Dashboard")
st.caption("KAIM / 10 Academy – Week 1 Task 3: Cross-Country Solar Potential Analysis")

# ---- FILE PATHS ----
COUNTRY_FILES = {
    "Benin": "data/benin_clean.csv",
    "Sierra Leone": "data/sierra_leone_clean.csv",
    "Togo": "data/togo_clean.csv",
}

# ---- SIDEBAR ----
st.sidebar.header("⚙️ Dashboard Controls")

selected_countries = st.sidebar.multiselect(
    "Select countries to include:",
    list(COUNTRY_FILES.keys()),
    default=list(COUNTRY_FILES.keys())
)

selected_metric = st.sidebar.selectbox(
    "Select solar metric to compare:",
    ["GHI", "DNI", "DHI"]
)

# ---- LOAD DATA ----
data_frames = []
for country in selected_countries:
    file_path = COUNTRY_FILES[country]
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df["Country"] = country
        data_frames.append(df)
    else:
        st.warning(f"⚠️ Missing file: {file_path}")

if not data_frames:
    st.error("No data available. Ensure your cleaned CSV files are in the data/ folder.")
    st.stop()

df_all = pd.concat(data_frames, ignore_index=True)

# ---- BOXPLOT ----
st.subheader(f"📊 {selected_metric} Distribution by Country")

fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x="Country", y=selected_metric, data=df_all, palette="Set2", ax=ax)
ax.set_xlabel("")
ax.set_ylabel(f"{selected_metric} (W/m²)")
ax.set_title(f"{selected_metric} Comparison")
st.pyplot(fig)

# ---- SUMMARY TABLE ----
st.subheader("📋 Summary Statistics")
summary = (
    df_all.groupby("Country")[[selected_metric]]
    .agg(["mean", "median", "std"])
    .round(2)
)
st.dataframe(summary)

# ---- DOWNLOAD BUTTON ----
csv_data = summary.to_csv().encode("utf-8")
st.download_button(
    label="⬇️ Download Summary as CSV",
    data=csv_data,
    file_name=f"solar_summary_{selected_metric.lower()}.csv",
    mime="text/csv",
)

# ---- ANOVA TEST ----
st.subheader("🔬 One-way ANOVA Test")

groups = [df_all[df_all["Country"] == c][selected_metric].dropna() for c in selected_countries]

if len(groups) >= 2:
    f_stat, p_val = stats.f_oneway(*groups)
    st.write(f"**F-statistic:** {f_stat:.3f}")
    st.write(f"**p-value:** {p_val:.6f}")
    if p_val < 0.05:
        st.success("✅ Statistically significant difference found (p < 0.05).")
    else:
        st.info("ℹ️ No significant difference found (p ≥ 0.05).")
else:
    st.warning("Select at least two countries for ANOVA test.")

# ---- RANKING BAR CHART ----
st.subheader("🏆 Average Solar Irradiance (GHI) Ranking")

ghi_means = (
    df_all.groupby("Country")["GHI"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

fig, ax = plt.subplots(figsize=(6, 4))
sns.barplot(x=ghi_means.values, y=ghi_means.index, palette="YlOrBr", ax=ax)
ax.set_xlabel("Average GHI (W/m²)")
ax.set_ylabel("")
ax.set_title("Average GHI by Country")
st.pyplot(fig)

# ---- INSIGHTS ----
st.markdown("---")
st.subheader("💡 Observations / Insights")
st.markdown("""
- Countries with **higher average GHI** have stronger solar potential.  
- The **boxplot spread** indicates variability and consistency in solar exposure.  
- **ANOVA** helps verify if observed differences are statistically meaningful.  
""")

