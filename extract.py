import time
import requests
import pandas as pd

def fetch_top10_current_prices():
    """Fetch the current top 10 coins by market cap from CoinGecko."""
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 10, "page": 1}

    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        return [{"coin": c["id"], "price_usd": c["current_price"]} for c in data]

    except Exception as e:
        print(f"❌ Error fetching top 10 coins: {e}")
        return []


def fetch_historical_prices(coin: str, days: int = 30, retries: int = 5):
    """Fetch historical price data with rate limiting + retry for 429 errors."""
    url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"
    params = {"vs_currency": "usd", "days": days}

    for attempt in range(retries):
        try:
            resp = requests.get(url, params=params, timeout=10)

            # Handle 429 rate limits
            if resp.status_code == 429:
                wait_time = 2 ** attempt  # exponential backoff
                print(f"Rate limit hit for {coin}. Waiting {wait_time} seconds...")
                time.sleep(wait_time)
                continue

            resp.raise_for_status()

            data = resp.json()
            records = [
                {
                    "coin": coin,
                    "price_usd": float(price),
                    "loaded_at": pd.to_datetime(ts, unit="ms"),
                }
                for ts, price in data["prices"]
            ]
            return records

        except Exception as e:
            print(f"Error fetching history for {coin}: {e}")
            time.sleep(2)

    print(f"Failed to fetch history for {coin} after {retries} retries.")
    return []
