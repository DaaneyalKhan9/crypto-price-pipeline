from extract import fetch_top10_current_prices, fetch_historical_prices
from db.load import load_to_db
import pandas as pd
import time


def backfill_history(days: int = 30):
    print(f"📊 Backfilling {days} days of history for top 10 coins...")

    top10 = fetch_top10_current_prices()
    coins = [r["coin"] for r in top10]

    all_records = []

    for coin in coins:
        print(f"\n⏳ Fetching history for {coin}...")
        hist_records = fetch_historical_prices(coin, days=days)
        all_records.extend(hist_records)

        # Avoid rapid-fire requests
        time.sleep(6)

    df_hist = pd.DataFrame(all_records)
    print(f"\n📦 Total historical rows: {len(df_hist)}")

    load_to_db(df_hist)
    print("✅ Historical backfill completed.")


if __name__ == "__main__":
    backfill_history(days=30)
