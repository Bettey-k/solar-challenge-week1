
📍 *Path: `solar-challenge-week1/scripts/README.md`*

```markdown
# 🧰 Scripts Folder

This folder is reserved for **automation scripts** and **workflow extensions** that complement the Solar Data Discovery project.

---

## 🧩 Purpose
- Automate daily data-cleaning tasks.
- Schedule summary report generation.
- Integrate modular functions from `/src/` for batch processing.

---

## 🧱 Example Future Script (planned)
`automate_cleaning.py`
```python
from src.data_cleaning import clean_solar_data
from src.data_analysis import summarize_solar_data

countries = ["benin", "sierra_leone", "togo"]
for country in countries:
    df = clean_solar_data(f"data/{country}.csv")
    summary = summarize_solar_data(df)
    print(f"{country.title()} summary:\n", summary)

🧭 How to Run Scripts

From the project root:

python scripts/<script_name>.py

🧾 Notes

The folder currently includes __init__.py for module compatibility.

Scripts are optional but demonstrate how to operationalize the analysis pipeline.


---

✅ **After adding these:**
1. Copy each README.md into its folder.  
2. Commit and push:
   ```bash
   git add README.md notebooks/README.md src/README.md scripts/README.md
   git commit -m "docs: add detailed READMEs for root, notebooks, src, and scripts"
   git push origin main