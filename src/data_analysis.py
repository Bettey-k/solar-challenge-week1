"""
data_analysis.py
----------------
Reusable functions for descriptive statistics, correlations,
and visualization in the Solar Data Discovery project.

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def summarize_solar_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate descriptive statistics for key solar metrics.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned solar dataset.

    Returns
    -------
    pd.DataFrame
        Summary statistics (count, mean, std, min, max).
    """
    return df[["GHI", "DNI", "DHI", "Tamb", "RH", "WS"]].describe()


def plot_correlation_heatmap(df: pd.DataFrame, title: str = "Solar Variable Correlations"):
    """
    Plot a heatmap of correlations among solar variables.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned solar dataset.
    title : str
        Title for the plot.

    Returns
    -------
    None
    """
    plt.figure(figsize=(6, 5))
    sns.heatmap(df.corr(), annot=True, cmap="YlOrBr", fmt=".2f")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(f"output/{title.replace(' ', '_').lower()}.png")
    plt.close()


def plot_time_series(df: pd.DataFrame, column: str, title: str):
    """
    Plot a time-series visualization of a chosen variable.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset containing a 'Timestamp' column.
    column : str
        Column name to plot.
    title : str
        Title for the plot.

    Returns
    -------
    None
    """
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    plt.figure(figsize=(10, 4))
    plt.plot(df["Timestamp"], df[column], linewidth=1, color="orange")
    plt.title(title)
    plt.xlabel("Timestamp")
    plt.ylabel(column)
    plt.tight_layout()
    plt.savefig(f"output/{column.lower()}_timeseries.png")
    plt.close()
