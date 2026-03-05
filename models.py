from pydantic import BaseModel
from datetime import datetime
from typing import Literal

class Transaction(BaseModel):
    ticker: str
    type: Literal["buy", "sell"]
    quantity: float
    price: float
    date: datetime = datetime.now()

