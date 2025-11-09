import pandas as pd

def clean_solar_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean solar dataset."""
    df = df.copy()
    df = df.dropna(subset=["GHI", "DNI", "DHI"])
    df = df[df["GHI"] >= 0]
    return df
