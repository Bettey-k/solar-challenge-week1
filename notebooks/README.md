# 🧠 Exploratory Data Analysis (EDA) – Solar Data Discovery

This folder contains all the **Exploratory Data Analysis (EDA)** notebooks for the **KAIM / 10 Academy Solar Data Discovery Challenge**.  
Each notebook explores solar radiation and environmental parameters for one country: **Benin**, **Sierra Leone**, and **Togo**.

---

## 🌍 Purpose of the EDA

The goal of this analysis is to:
1. **Understand** the characteristics of solar irradiance and weather parameters across regions.  
2. **Clean** the data by handling missing values and outliers.  
3. **Explore relationships** between solar variables (GHI, DNI, DHI, Tamb, RH, WS, etc.).  
4. **Visualize** patterns and trends across time to identify potential for solar power generation.  
5. **Generate insights** for each country to support future dashboard and ranking analysis.

---

## 📘 Available Notebooks

| Notebook | Description |
|-----------|-------------|
| **`benin_eda.ipynb`** | Step-by-step profiling, cleaning, and visualization for Benin dataset. Includes time-series, correlations, humidity–temperature relationships, and cleaning impact. |
| **`sierra_leone_eda.ipynb`** | Similar pipeline for Sierra Leone dataset. Analyzes irradiance patterns and how humidity affects solar radiation. |
| **`togo_eda.ipynb`** | Full EDA for Togo dataset focusing on temperature fluctuations, wind speed, and irradiance intensity. |
| **`interim_summary.ipynb`** | Aggregates cleaned results from all three countries, computes summary tables, and generates cross-country comparison plots. |

---

## ⚙️ How to Run the Notebooks

### 1️⃣ Activate Environment
```bash
# From project root
.venv\Scripts\activate   # Windows
# or
source .venv/bin/activate   # macOS / Linux
  2️⃣ Launch Jupyter
jupyter notebook notebooks/

  3️⃣ Open and Run

Open one notebook (e.g. benin_eda.ipynb) → click “Run All”.
Ensure that you have the cleaned or raw dataset for that country inside /data/.

🧩 EDA Workflow (Summary)

Load Data → using src.data_cleaning.load_data()

Profile & Describe → df.describe(), df.isna().sum()

Clean Data → fill NaNs with median; remove outliers (|Z| > 3)

Visualize Trends → time-series for GHI, DNI, DHI, Tamb

Analyze Correlations → heatmap of solar variables

Cleaning Impact → compare ModA & ModB before/after cleaning

Distributions → histograms for irradiance, scatter for WS vs GHI

Temperature–Humidity → scatter plots and bubble charts

Save Results → export cleaned data as data/<country>_clean.csv

🧠 Tools Used

pandas, numpy → data cleaning

matplotlib, seaborn → visualization

scipy.stats → Z-score filtering

Jupyter Notebook → documentation & exploration

🏁 Key Outcomes

Clean, validated datasets for all three countries.

Identified links between temperature, humidity, and solar performance.

Produced visuals for irradiance distribution and correlations.

Prepared data for cross-country comparison and dashboards.