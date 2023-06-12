import os

from datetime import datetime
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGODB_URL = os.environ["MONGODB_URL"]

client = MongoClient(MONGODB_URL)

db = client.bank
accounts_collection = db.accounts

# insert one
new_account = {
    "account_holder": "Peter Cha",
    "account_id": "MDB93929292",
    "account_type": "checking",
    "balance": 900,
    "last_updated": datetime.utcnow(),
}

result = accounts_collection.insert_one(new_account)

document_id = result.inserted_id
print(f"_id of inerted document: {document_id}")

# insert many
new_accounts = [
    {
        "account_id": "MDB011235813",
        "account_holder": "Ada Lovelace",
        "account_type": "savings",
        "balance": 100,
    },
    {
        "account_id": "MDB829000001",
        "account_holder": "Muhammad ibn Musa al-Khwarizmi",
        "account_type": "savings",
        "balance": 300,
    },
]

result = accounts_collection.insert_many(new_accounts)
document_ids = result.inserted_ids
print("# of documents inserted: " + str(len(document_ids)))
print(f"_ids of inserted documents: {document_ids}")

client.close()
