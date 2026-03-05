from fastapi import APIRouter
import yfinance as yf
from database import transactions_collection

router = APIRouter()

@router.get("/")
def get_portfolio():
    holdings = {}

    for t in transactions_collection.find():
        ticker = t["ticker"].upper()
        qty = t["quantity"] if t["type"] == "buy" else -t["quantity"]
        cost = t["price"] * t["quantity"] if t["type"] == "buy" else 0

        if ticker not in holdings:
            holdings[ticker] = {"quantity": 0, "total_cost": 0}

        holdings[ticker]["quantity"] += qty
        holdings[ticker]["total_cost"] += cost

    portfolio = []
    for ticker, data in holdings.items():
        if data["quantity"] <= 0:
            continue
        stock = yf.Ticker(ticker)
        current_price = stock.fast_info["last_price"]
        avg_buy_price = data["total_cost"] / data["quantity"]
        gain_loss = (current_price - avg_buy_price) * data["quantity"]

        portfolio.append({
            "ticker": ticker,
            "quantity": data["quantity"],
            "avg_buy_price": round(avg_buy_price, 2), #2decimal
            "current_price": round(current_price, 2), #2decimal
            "gain_loss": round(gain_loss, 2), #2decimal
        })

    return portfolio