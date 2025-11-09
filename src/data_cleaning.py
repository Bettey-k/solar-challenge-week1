"""
data_cleaning.py
----------------
This module provides reusable data-cleaning functions for the Solar Data Discovery project.

Each function includes docstrings and handles:
- Missing values
- Outlier removal
- Data validation for solar irradiance datasets (GHI, DNI, DHI)
"""

import pandas as pd
import numpy as np

def load_data(file_path: str) -> pd.DataFrame:
    """Load dataset and return a DataFrame."""
    return pd.read_csv(file_path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean data by handling missing values and removing outliers."""
    df = df.dropna(subset=["GHI", "DNI", "DHI"])
    z = np.abs((df[["GHI","DNI","DHI"]] - df[["GHI","DNI","DHI"]].mean()) / df[["GHI","DNI","DHI"]].std())
    df_clean = df[(z < 3).all(axis=1)]
    return df_clean

def summarize_data(df: pd.DataFrame) -> pd.DataFrame:
    """Generate descriptive statistics for solar variables."""
    return df[["GHI","DNI","DHI","Tamb","RH","WS"]].describe()
