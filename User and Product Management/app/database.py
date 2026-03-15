from pymongo import MongoClient


MONGO_URL=""

client=MongoClient(MONGO_URL)

db=client["ecommerce_db"]

users_collection=db["User"]
products_Collection=db["products"]

