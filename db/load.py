from sqlalchemy import create_engine
import pandas as pd  # only needed for the __main__ test


def get_engine():
    return create_engine("postgresql://crypto_user:pass@localhost:5432/crypto_pipeline")


def load_to_db(df: pd.DataFrame):
    """
    Append a DataFrame to the crypto_prices table.
    If the table does not exist yet, it will be created automatically.
    """
    engine = get_engine()
    df.to_sql("crypto_prices", engine, if_exists="append", index=False)
    print(f"Loaded {len(df)} rows into crypto_prices")


if __name__ == "__main__":
    # Quick test
    test_df = pd.DataFrame(
        {
            "coin": ["bitcoin", "ethereum"],
            "symbol": ["BTC", "ETH"],
            "price_usd": [12345.0, 2345.0],
            "market_cap_rank": [1, 2],
            "loaded_at": [pd.Timestamp.utcnow(), pd.Timestamp.utcnow()],
        }
    )
    load_to_db(test_df)
