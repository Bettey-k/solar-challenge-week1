# ☀️ Solar Data Discovery – KAIM / 10 Academy Week 1

### 👩🏽‍💻 Author: Betelhem Kibret Getu  
**Program:** KAIM / 10 Academy – Week 1  
**Challenge:** Solar Data Discovery  
**Repository:** [https://github.com/Bettey-k/solar-challenge-week1](https://github.com/Bettey-k/solar-challenge-week1)

---

## 🌍 Project Overview

This repository explores **solar irradiance data** from three West African countries — **Benin**, **Sierra Leone**, and **Togo** — as part of the **KAIM / 10 Academy Week 1 Challenge**.

The project demonstrates:
- Data profiling, cleaning, and analysis using Python  
- Statistical and visual comparison of solar patterns  
- Modular, reusable code design  
- Git-based version control, CI/CD integration, and documentation best practices  

---

## 🎯 Objectives

1. Load and profile raw solar datasets from multiple regions.  
2. Handle missing values and detect outliers using **Z-score filtering**.  
3. Compute summary statistics (mean, median, std) and correlations.  
4. Visualize irradiance patterns (GHI, DNI, DHI) and weather impacts.  
5. Build reusable modules for data cleaning and analysis.  
6. Develop an **interactive Streamlit dashboard** for cross-country comparison.  

---

## 🛠️ Setup & Execution Guide

### 1️⃣ Clone Repository & Create Environment
```bash
git clone https://github.com/Bettey-k/solar-challenge-week1.git
cd solar-challenge-week1
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Tests
pytest -q

You should see output similar to:

2 passed in 0.5s

4️⃣ Launch Jupyter Notebooks
jupyter notebook notebooks/

5️⃣ un Streamlit Dashboard
streamlit run app/main.py

🧱 Repository Structure
solar-challenge-week1/
│
├── .github/workflows/ci.yml         → CI/CD pipeline (pytest + flake8)
├── app/                             → Streamlit dashboard
│   ├── main.py                      → Interactive comparison dashboard
│   ├── utils.py                     → Helper functions
│   └── __init__.py
│
├── src/                             → Core Python modules
│   ├── data_cleaning.py             → Handles missing values, outliers
│   ├── data_analysis.py             → Statistical and visual analysis
│   └── __init__.py
│
├── notebooks/                       → Country-specific EDA notebooks
│   ├── benin_eda.ipynb
│   ├── sierra_leone_eda.ipynb
│   ├── togo_eda.ipynb
│   └── compare_countries.ipynb
│
├── tests/                           → Unit tests (pytest)
│   ├── test_cleaning.py
│   └── __init__.py
│
├── scripts/                         → Placeholder for automation
│   ├── README.md
│   └── __init__.py
│
├── data/                            → Local data (ignored by .gitignore)
├── output/                          → Generated plots & cleaned files
├── requirements.txt                 → Project dependencies
└── README.md                        → Main documentation (this file)
📊 Project Workflow
Step 1 – Environment & Version Control Setup

Initialized repo with .gitignore, requirements.txt, and CI workflow.

Used branch-per-task structure (setup-task, eda-benin, compare-countries, etc.).

Followed conventional commit style: feat:, fix:, chore:, etc.

Step 2 – Data Profiling & Cleaning

Loaded datasets from data/ folder.

Applied src/data_cleaning.py functions:

Fill missing values using median

Remove outliers using |Z| > 3 threshold

Validate data types and consistency

Step 3 – Exploratory Data Analysis (EDA)

Conducted visual and statistical EDA per country (notebooks/*.ipynb).

Produced time-series, correlations, and distribution plots.

Compared temperature, humidity, and irradiance trends.

Step 4 – Cross-Country Comparison

Combined cleaned datasets into one summary.

Created side-by-side boxplots, summary tables, and ANOVA tests.

Highlighted significant differences in solar potential.

Step 5 – Interactive Dashboard

Developed a Streamlit dashboard under app/main.py.

Added:

Sidebar controls (country & metric)

Boxplots, summary tables, ANOVA results

Ranking bar chart of average GHI

CSV download option

Step 6 – Testing & CI/CD

Added lightweight unit tests for data cleaning functions.

Configured GitHub Actions for automated linting and testing.

🧩 Key Insights

Benin exhibits the highest average GHI (solar potential).

Sierra Leone has high humidity and moderate irradiance.

Togo shows stable daily irradiance but lower peaks.

ANOVA confirms statistically significant variance between regions.

🧠 Tools Used
Category	Tools
Data Handling	pandas, numpy
Visualization	matplotlib, seaborn
Statistics	scipy.stats
Testing	pytest, flake8
Dashboard	Streamlit
Version Control	Git, GitHub Actions
🏆 Outcome

Fully cleaned and validated solar datasets for three regions.

Insightful visual and statistical comparison across countries.

Reusable, modular code with CI pipeline and Streamlit dashboard.

Well-documented repository for reproducibility and review.