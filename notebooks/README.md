#  Notebooks – Solar Challenge Week 1

This folder contains all Jupyter notebooks created for **Task 2: Data Profiling, Cleaning, and Exploratory Data Analysis (EDA)**.  
Each notebook focuses on one country's solar dataset and follows the same analysis structure defined in the project rubric.

---

## 📘 Notebook Overview

| Notebook | Description | Branch |
|-----------|--------------|--------|
| **benin_eda.ipynb** | Full exploratory data analysis for the **Benin** dataset. Includes data profiling (`df.describe()` and missing values), outlier detection using Z-scores, cleaning of negative irradiance values, and multiple visual analyses (time-series, correlation, wind distribution, temperature–humidity relationships, and bubble chart). | `eda-benin` |
| **sierra_leone_eda.ipynb** | (To be added) – EDA for the **Sierra Leone** dataset following the same structure as Benin. | `eda-sierra` |
| **togo_eda.ipynb** | (To be added) – EDA for the **Togo** dataset following the same structure as Benin. | `eda-togo` |

---

##  Standard EDA Workflow

Each notebook follows these steps:

1. **Data Profiling**
   - Summary statistics using `df.describe()`
   - Missing-value report using `df.isna().sum()`

2. **Data Cleaning**
   - Handle invalid or negative irradiance values (`GHI`, `DNI`, `DHI`)
   - Impute missing values with median
   - Compute and filter outliers using Z-scores

3. **Time-Series Analysis**
   - Plot `GHI`, `DNI`, `DHI`, and `Tamb` against timestamps
   - Observe daily and seasonal solar trends

4. **Correlation & Relationship Analysis**
   - Heatmap of `GHI`, `DNI`, `DHI`, `TModA`, `TModB`
   - Scatter plots (`WS` vs `GHI`, `RH` vs `Tamb`)
   - Bubble chart: `GHI` vs `Tamb` with bubble size = `RH`

5. **Wind & Distribution Analysis**
   - Histograms of `GHI`, `DNI`, `Tamb`, and `WS`
   - Wind direction histogram (or wind rose)

6. **Cleaning Impact**
   - Compare average `ModA` & `ModB` before and after cleaning events




##  Notes

- Cleaned datasets are saved locally in `data/<country>_clean.csv` but **not committed** to GitHub (as specified in `.gitignore`).
- Each notebook can be executed independently after installing requirements with:
  ```bash
  pip install -r requirements.txt
