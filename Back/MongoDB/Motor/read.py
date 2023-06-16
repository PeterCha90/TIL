import os
import asyncio

from pprint import pprint
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

MONGODB_URL = os.environ["MONGODB_URL"]
client = AsyncIOMotorClient(MONGODB_URL)
collection = client.bank.test_collection


async def find_one():
    doc = await collection.find_one(
        {'i': {'$lt': 2002}})
    pprint(doc)


async def find():
    cursor = collection.find(
        {'i': {'$lt': 2006}})
    for doc in await cursor.to_list(length=100):
        pprint(doc)

loop = asyncio.get_event_loop()
print("Find one:")
loop.run_until_complete(find_one())
print("Find:")
loop.run_until_complete(find())
