import os
import asyncio

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

MONGODB_URL = os.environ["MONGODB_URL"]
client = AsyncIOMotorClient(MONGODB_URL)
collection = client.bank.test_collection


async def insert():
    doc = {'key': 'value'}
    result = await collection.insert_one(doc)
    print('result %s' % repr(result.inserted_id))


async def insert_many():
    result = await collection.insert_many(
        [{'i': i} for i in range(2001, 3001)])
    print('inserted %d docs' %
          (len(result.inserted_ids)))


loop = asyncio.get_event_loop()
loop.run_until_complete(insert())
loop.run_until_complete(insert_many())
