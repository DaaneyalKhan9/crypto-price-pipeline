import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import altair as alt

st.set_page_config(
    page_title="Crypto Dashboard",
    layout="wide",
    page_icon="📈"
)

# -------------------------------
# Database connection
# -------------------------------
engine = create_engine("postgresql://crypto_user:pass@localhost:5432/crypto_pipeline")

# -------------------------------
# Load latest prices
# -------------------------------
latest_query = """
SELECT DISTINCT ON (coin)
    coin, price_usd, loaded_at
FROM crypto_prices
ORDER BY coin, loaded_at DESC;
"""

df_latest = pd.read_sql(latest_query, engine)


# -------------------------------
# Sidebar – coin selection
# -------------------------------
st.sidebar.title("⚙️ Controls")
selected_coin = st.sidebar.selectbox("Choose a coin", df_latest["coin"].tolist())


# -------------------------------
# Page Title
# -------------------------------
st.title("📊 Crypto Price Dashboard")

# -------------------------------
# Latest Prices Table
# -------------------------------
st.subheader("Latest Prices")
st.dataframe(df_latest, use_container_width=True)


# -------------------------------
# Historical Data for Selected Coin
# -------------------------------
hist_query = f"""
SELECT coin, price_usd, loaded_at
FROM crypto_prices
WHERE coin = '{selected_coin}'
ORDER BY loaded_at ASC;
"""

df_hist = pd.read_sql(hist_query, engine)
df_hist["loaded_at"] = pd.to_datetime(df_hist["loaded_at"])


# -------------------------------
# Price Trend Chart
# -------------------------------
st.subheader(f"Price Trend – {selected_coin.capitalize()}")

if df_hist.empty:
    st.warning("No historical data available yet.")
else:
    chart = (
        alt.Chart(df_hist)
        .mark_line()
        .encode(
            x=alt.X("loaded_at:T", title="Time"),
            y=alt.Y("price_usd:Q", title="Price (USD)"),
            tooltip=["loaded_at", "price_usd"]
        )
        .properties(height=400)
    )

    st.altair_chart(chart, use_container_width=True)
