# 📈 Crypto Price Pipeline

A fully automated data engineering project with real-time + historical crypto price tracking.

# 🚀 Overview

This project is a complete end-to-end data pipeline that:

Extracts live crypto prices for the top 10 cryptocurrencies

Collects historic price data (30-day backfill)

Loads everything into a PostgreSQL database

Automates daily updates with a scheduler

Displays insights via an interactive Streamlit dashboard

This is a production-grade project designed to demonstrate data engineering, ETL architecture, and dashboard analytics.

# 💡Features
🔹 Top 10 Crypto Live Prices

Fetched via CoinGecko JSON API.

🔹 30-Day Historical Price Loader

With automatic rate-limit handling & exponential backoff.

🔹 PostgreSQL Storage

Database schema includes:

coin

price_usd

loaded_at (timestamp)

🔹 Interactive Dashboard

Built with Streamlit:

Live price table

Line chart of historical trends

Coin selector

🔹 Automation

Optional:

Scheduler to run pipeline automatically

Dockerized PostgreSQL instance

# 📊 Dashboard Preview

![Dashboard](assets/dashboard.png)

🧱 Tech Stack
Component -> Technology
Language ->	Python 3.13
API -> CoinGecko
DB	-> PostgreSQL (Docker)
Libraries -> Pandas, SQLAlchemy, Requests
Dashboard -> Streamlit
Automation -> Cron / Custom scheduler