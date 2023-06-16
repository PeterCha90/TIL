import os
import asyncio

from pprint import pprint
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

MONGODB_URL = os.environ["MONGODB_URL"]
client = AsyncIOMotorClient(MONGODB_URL)
collection = client.bank.test_collection


async def aggregate():
    pipeline = [
        {'$project':
         {'money':
          {'$multiply': ['$i', 0.5]}}}
    ]
    async for doc in collection.aggregate(pipeline):
        print(doc)

loop = asyncio.get_event_loop()
loop.run_until_complete(aggregate())
