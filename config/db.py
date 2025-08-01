from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGODb")
client = MongoClient(MONGO_URI)
db = client["discord_bot"]
games_collection = db["games"]