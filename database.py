from pymongo import MongoClient
from dotenv import load_dotenv
import os

# This is where MongoDB is used. transactions_collections(MongoDB function) reads & writes to the database 

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["portfolio_db"]

transactions_collection = db["transactions"]