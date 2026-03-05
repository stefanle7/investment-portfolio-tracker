from fastapi import FastAPI
from routes import transactions, portfolio
from fastapi.middleware.cors import CORSMiddleware # I need this if I want to connext to a frontend (React)

# used to run FastAPI

app = FastAPI()

app.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])
app.include_router(portfolio.router, prefix="/portfolio", tags=["Portfolio"])

@app.get("/")
def root():
    return {"message": "Portfolio Tracker API is running"}