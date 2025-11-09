

# ⚙️ Source Code – Modular Python Functions

This folder contains **reusable, well-documented Python modules** that power the Solar Data Discovery project.

---

## 📂 Files Overview
| File | Description |
|------|--------------|
| `data_cleaning.py` | Functions for loading, cleaning, and preparing solar data (handles NaNs and outliers). |
| `data_analysis.py` | Functions for descriptive statistics, correlation heatmaps, and visualizations. |
| `__init__.py` | Package initializer so `src/` can be imported as a module. |

---

## 🧱 How to Use

Example usage inside a notebook:
```python
from src.data_cleaning import clean_solar_data
from src.data_analysis import summarize_solar_data, plot_correlation_heatmap

df = clean_solar_data("data/benin.csv")
summary = summarize_solar_data(df)
plot_correlation_heatmap(df, title="Benin Solar Variable Correlations")

🧮 Functions Summary
data_cleaning.py

load_data(file_path) → loads CSV data

handle_missing_values(df, cols) → fills NaN values with median

remove_outliers(df, cols, z_thresh) → filters rows using Z-scores

clean_solar_data(file_path) → combines all cleaning steps

data_analysis.py

summarize_solar_data(df) → descriptive stats

plot_correlation_heatmap(df) → correlation plot

plot_time_series(df, column, title) → line plot for irradiance or temperature

🧪 Testing

Run tests from the project root:

pytest -q


Expected output:

2 passed in 0.5s

🧠 Notes

All functions include docstrings and type hints.

Designed for easy re-use across notebooks and future dashboards.

Tested automatically via GitHub Actions.


---
