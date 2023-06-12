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
document_to_delete = \
    {"_id": ObjectId(
        "6485440295883d3e714b2e2d")}

print("Searching for target document before delete: ")
pprint(accounts_collection.find_one(document_to_delete))

result = accounts_collection.delete_one(
    document_to_delete)

print("Searching for target document after delete: ")
pprint(accounts_collection.find_one(document_to_delete))
print("Documents deleted: " + str(result.deleted_count))

# delete many
documents_to_delete = {
    'balance': {"$lt": 300000000}
}

print("\nSearching for sample target document before delete: ")
pprint(accounts_collection.find(
    documents_to_delete))

result = accounts_collection.delete_many(
    documents_to_delete)
print("Searching for sample target document after delete: ")
pprint(accounts_collection.find(documents_to_delete))

print("Documents deleted: " + str(result.deleted_count))

client.close()
