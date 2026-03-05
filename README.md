# Investment Portfolio Tracker

A Python-based REST API that lets users log stock and crypto transactions, track their holdings, and view real-time portfolio performance — all backed by MongoDB and powered by live market data.

---

## Motivation

Many students invest in stocks and crypto but don't have a clear, centralized way to track what they own, what they paid, and how their portfolio is performing over time. Most tools are either overly complex or locked behind expensive subscriptions.

This project solves that by building a practical, open-source portfolio tracker that:
- Logs buy/sell transactions and stores them in a database
- Calculates real-time gain/loss using live market prices
- Provides historical performance data for any holding
- Is fully queryable via a clean REST API

---

## Tech Stack

| Layer | Technology |
|---|---|
| **Backend Framework** | FastAPI (Python) |
| **Database** | MongoDB Atlas via PyMongo |
| **Market Data** | yfinance (Yahoo Finance) |

---
