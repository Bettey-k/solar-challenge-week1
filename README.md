# ☀️ Solar Data Discovery – KAIM / 10 Academy Week 1

### 👩🏽‍💻 Author: Betelhem Kibret Getu  
**Program:** KAIM / 10 Academy – Week 1  
**Challenge:** Solar Data Discovery  
**Repository:** [https://github.com/Bettey-k/solar-challenge-week1](https://github.com/Bettey-k/solar-challenge-week1)

---

## 🌍 Project Overview
This project focuses on **cleaning, profiling, and analyzing solar energy datasets** from three West African countries — **Benin**, **Sierra Leone**, and **Togo**.  
It was developed as part of **10 Academy’s KAIM Week 1 Challenge** to demonstrate skills in:
- Data cleaning and preprocessing  
- Exploratory Data Analysis (EDA)  
- Python modularization and documentation  
- Version control and CI/CD automation

---

## 🧩 Objectives
1. Load, profile, and clean raw solar datasets.  
2. Handle missing values and remove outliers using Z-score filtering.  
3. Perform descriptive statistics and correlation analysis.  
4. Visualize solar patterns across time and environmental variables.  
5. Build reusable Python modules for data cleaning and analysis.  
6. Maintain version control best practices (branches, commits, CI tests).

---

## 🛠️ Setup Instructions

### 1️⃣ Clone and create environment
```bash
git clone https://github.com/Bettey-k/solar-challenge-week1.git
cd solar-challenge-week1
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run tests
pytest -q


You should see something like:

2 passed in 0.5s

4️⃣ Launch Jupyter Notebooks
jupyter notebook notebooks/

5️⃣ Optional: Run functions directly
python src/data_cleaning.py


or import in notebooks:

from src.data_cleaning import clean_solar_data

🧱 Repository Structure
solar-challenge-week1/
│
├── .github/workflows/ci.yml        → Continuous Integration (pytest + flake8)
├── src/                            → Modular code (cleaning + analysis)
├── notebooks/                      → EDA and visual analysis per country
├── tests/                          → Unit tests for validation
├── scripts/                        → Placeholder for future automation
├── output/                         → Generated figures and summaries
├── data/                           → Local data (ignored in .gitignore)
├── requirements.txt                → Project dependencies
└── README.md                       → Main documentation (this file)

📊 Steps in the Project
Step 1. Environment & Git Setup

Created virtual environment and requirements file.

Added CI workflow in .github/workflows/ci.yml to verify builds.

Initialized repository with .gitignore and folder structure.

Step 2. Data Profiling & Cleaning

Loaded raw datasets from the data/ folder.

Used functions in src/data_cleaning.py to:

Replace missing values with median.

Remove outliers using Z-scores.

Validate column consistency.

Step 3. Exploratory Data Analysis (EDA)

Conducted analysis in separate notebooks:

benin_eda.ipynb

sierra_leone_eda.ipynb

togo_eda.ipynb

Visualized time-series, correlations, humidity-temperature relations, and cleaning impact.

Step 4. Modularization

Abstracted core cleaning and visualization functions into:

src/data_cleaning.py

src/data_analysis.py

Added detailed docstrings for clarity and reusability.

Step 5. Testing & CI

Added tests/test_cleaning.py to verify functions.

Enabled GitHub Actions to run automatic tests.

Step 6. Documentation

Added detailed README files across folders.

Ensured clear structure and instructions for reproducibility.
