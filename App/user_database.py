from pymongo import MongoClient
from dotenv import load_dotenv
import os


def db_init():
    load_dotenv()
    CONNECTION_STRING = os.getenv("CONNECTION_STRING")
    client = MongoClient(CONNECTION_STRING)
    db = client["Sellcom"]
    user_collection = db["user_Sellcom"]
    return user_collection
