import time
import requests
import pandas as pd


# -----------------------------
# Fetch top 10 coins by market cap
# -----------------------------
def fetch_top10_current_prices():
    """Fetch top 10 cryptocurrencies (CoinGecko API)."""
    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
    }

    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    top10 = [{"coin": c["id"], "price_usd": c["current_price"]} for c in data]
    return top10


# -----------------------------
# Fetch live prices for ANY coin list
# -----------------------------
def fetch_current_prices(coins):
    """Fetch current price dictionary for a list of coins."""
    ids = ",".join(coins)
    url = (
        f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"
    )
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.json()


# -----------------------------
# Fetch historical data with retries (429-safe)
# -----------------------------
def fetch_historical_prices(coin: str, days: int = 30, retries: int = 5):
    """
    Fetch historical OHLC/price chart data for 1 coin.
    Includes retry support for 429 Too Many Requests.
    """

    url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"
    params = {"vs_currency": "usd", "days": str(days)}

    for attempt in range(1, retries + 1):
        try:
            resp = requests.get(url, params=params, timeout=10)

            # Hit rate-limit → wait exponentially
            if resp.status_code == 429:
                wait = min(120, 5 * attempt)  
                print(f"⚠️ 429 rate limit for {coin}. Waiting {wait}s...")
                time.sleep(wait)
                continue

            resp.raise_for_status()
            data = resp.json()

            # Build list of records
            records = [
                {
                    "coin": coin,
                    "price_usd": float(price),
                    "loaded_at": pd.to_datetime(ts, unit="ms"),
                }
                for ts, price in data.get("prices", [])
            ]

            return records

        except Exception as e:
            print(f"❌ Error fetching history for {coin}: {e}")
            time.sleep(2)

    print(f"❌ Failed to fetch history for {coin} after {retries} retries.")
    return []
