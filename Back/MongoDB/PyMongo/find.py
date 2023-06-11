import os

from pprint import pprint
from datetime import datetime
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId

load_dotenv()
MONGODB_URL = os.environ["MONGODB_URL"]

client = MongoClient(MONGODB_URL)

db = client.bank
accounts_collection = db.accounts

# find one
document_to_find = \
    {"_id": ObjectId(
        "648546177d2f3251320d2e73")}

result = accounts_collection.find_one(
    document_to_find)
pprint(result)

# find with Query
documents_to_find = {
    'balance': {"$gt": 4700}
}

cursor = accounts_collection.find(documents_to_find)

for i, doc in enumerate(cursor):
    pprint(doc)
    print()

print("# of docs found: " + str(i+1))

client.close()
