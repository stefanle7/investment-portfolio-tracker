from fastapi import FastAPI
from routes import transactions, portfolio

app = FastAPI()

app.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])
app.include_router(portfolio.router, prefix="/portfolio", tags=["Portfolio"])

@app.get("/")
def root():
    return {"message": "Portfolio Tracker API is running"}