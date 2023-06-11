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

# update one
document_to_update = \
    {"_id": ObjectId(
        "648546177d2f3251320d2e75")}

add_to_balance = {"$inc": {"balance": 100}}

pprint("Original: " + str(
       accounts_collection.find_one(
           document_to_update)))

result = accounts_collection.update_one(
    document_to_update, add_to_balance)

print("Documents updated:\n" + str(
    result.modified_count))

pprint(accounts_collection.find_one(
    document_to_update
))

pprint(result)

# update many
select_accounts = {"account_type": "checking"}

set_field = {"$set": {"minimum_balance": 100}}

result = accounts_collection.update_many(
    select_accounts, set_field
)

print("Documents matched: " + str(result.matched_count))
print("Documents updated: " + str(result.modified_count))
pprint(accounts_collection.find_one(select_accounts))

client.close()
