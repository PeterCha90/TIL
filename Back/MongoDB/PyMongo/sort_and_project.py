import os

from pprint import pprint
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGODB_URL = os.environ["MONGODB_URL"]

client = MongoClient(MONGODB_URL)
db = client.bank
accounts_collection = db.accounts

conversion_rate = 1.3

select = {"$match": {"account_type": "checking",
                     "balance": {"$lt": 1000}}}
organize = {"$sort": {"balance": -1}}
fields = {
    "$project": {
        "account_type": 1,
        "balance": 1,
        "gbp_balance": {"$divide":
                        ["$balance", conversion_rate]},
        "_id": 0
    }
}

pipeline = [
    select,
    organize,
    fields
]
results = accounts_collection.aggregate(pipeline)

for item in results:
    pprint(item)

client.close()
