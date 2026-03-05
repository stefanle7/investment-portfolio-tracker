from fastapi import APIRouter
from models import Transaction
from database import transactions_collection
from bson import ObjectId

router = APIRouter()

@router.post("/")
def add_transaction(transaction: Transaction):
    data = transaction.dict()
    result = transactions_collection.insert_one(data)
    return {"id": str(result.inserted_id), "message": "Transaction added"}

@router.get("/")
def get_transactions():
    txns = []
    for t in transactions_collection.find():
        t["_id"] = str(t["_id"])
        txns.append(t)
    return txns