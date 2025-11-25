from extract import fetch_top10_current_prices
from transform import transform_current_data
from db.load import load_to_db


def run_pipeline():
    print("Running crypto ETL pipeline (top 10 by market cap)...")

    raw = fetch_top10_current_prices()
    print(f"Extracted {len(raw)} records")

    df = transform_current_data(raw)
    print("Transformed data:")
    print(df)

    load_to_db(df)
    print("Pipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()
