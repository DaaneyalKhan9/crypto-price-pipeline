import pandas as pd
from datetime import datetime


def transform_current_data(raw_records):
    """
    Turn list of dicts from fetch_top10_current_prices() into a DataFrame
    and add a loaded_at timestamp.
    """
    df = pd.DataFrame(raw_records)
    df["loaded_at"] = datetime.utcnow()
    return df
