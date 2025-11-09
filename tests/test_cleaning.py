


import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.data_cleaning import clean_data
import pandas as pd

def test_clean_data():
    data = {
        "GHI": [100, 250, None],
        "DNI": [50, 70, 80],
        "DHI": [20, 30, 40]
    }
    df = pd.DataFrame(data)
    cleaned = clean_data(df)
    assert "GHI" in cleaned.columns
    assert cleaned.shape[0] > 0
