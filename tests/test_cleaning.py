import os
import sys
import pandas as pd
from src.data_cleaning import clean_solar_data

# Add project root to sys.path for imports
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


def test_clean_solar_data():
    """Test cleaning pipeline."""
    data = {
        "GHI": [100, 200, None],
        "DNI": [50, 70, 80],
        "DHI": [20, 30, 40]
    }
    df = pd.DataFrame(data)
    cleaned = clean_solar_data(df)

    # Check that the function returns expected columns
    assert "GHI" in cleaned.columns
