import os

from pprint import pprint
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGODB_URL = os.environ["MONGODB_URL"]

client = MongoClient(MONGODB_URL)
db = client.bank
accounts_collection = db.accounts


select = {"$match": {"balance": {"$lt": 1000}}}

group_and_avg = {
    "$group": {"_id": "$account_type",
               "avg_balance": {"$avg": "$balance"}}
}

pipeline = [
    select,
    group_and_avg
]
results = accounts_collection.aggregate(pipeline)

for item in results:
    pprint(item)

client.close()
