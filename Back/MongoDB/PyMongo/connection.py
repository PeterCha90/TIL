import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGODB_URL = os.environ["MONGODB_URL"]

client = MongoClient(MONGODB_URL)

for db in client.list_database_names():
    print(db)

client.close()
