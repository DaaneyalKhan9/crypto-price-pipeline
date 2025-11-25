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

### Features

###🔍 1. Real-Time Price Extraction

- Live price data pulled from CoinGecko API

- Configured for top 10 cryptocurrencies

- Handles inconsistent API responses gracefully

### 🧮 2. Data Transformation

- Cleans API responses

- Converts timestamps

- Normalizes dataset into a consistent schema

### 🗄️ 3. PostgreSQL Data Warehouse
Database table: crypto_prices
| column    | type      | description        |
| --------- | --------- | ------------------ |
| coin      | text      | crypto symbol/name |
| price_usd | numeric   | USD price          |
| loaded_at | timestamp | Time of extraction |

📉 4. Historical Backfill

- Fetches 30-day history for all top 10 coins

- Automatic 429 error handling (rate limits)

- Exponential backoff + cooldown to ensure data completeness

### 📊 5. Interactive Streamlit Dashboard

- Latest prices table

- A coin selector

- Line chart with historical + live price trends

- Clean and modern UI theme

### 🤖 6. Automation

- Optional extras:

- Scheduler (scheduler.py) to run pipeline automatically

- Docker PostgreSQL instance for isolated local storage

# 🛠️ Tech Stack

| Component      | Technology                   |
| -------------- | ---------------------------- |
| **Language**   | Python 3.13                  |
| **API**        | CoinGecko REST API           |
| **Database**   | PostgreSQL (Docker optional) |
| **Libraries**  | Pandas, SQLAlchemy, Requests |
| **Dashboard**  | Streamlit                    |
| **Automation** | Cron / Python Scheduler      |


# 📊 Dashboard Preview

![Dashboard](https://raw.githubusercontent.com/DaaneyalKhan9/crypto-price-pipeline/main/images/dashboard.png)

### 🎯 What I've Learned / Key Takeaways

- Building production-style ETL pipelines

- Handling API rate limits and 429 automatic retries

- Designing a clean SQL schema

- Using Dockerized PostgreSQL

- Creating an interactive analytics dashboard

- Automating data workflows using Python

