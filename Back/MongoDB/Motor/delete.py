import os
import asyncio

from pprint import pprint
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

MONGODB_URL = os.environ["MONGODB_URL"]
client = AsyncIOMotorClient(MONGODB_URL)
collection = client.bank.test_collection


async def delete_one():
    n = await collection.count_documents({})
    print('%s docs before delete_one()' % n)
    result = await collection.delete_one(
        {'i': {'$gte': 2010}}
    )
    print('%s docs after' % (
        await collection.count_documents({})))


async def delete_many():
    n = await collection.count_documents({})
    print('%s docs before delete_many()' % n)
    result = await collection.delete_many(
        {'i': {'$gte': 2010}}
    )
    print('%s docs after' % (
        await collection.count_documents({})))


loop = asyncio.get_event_loop()
loop.run_until_complete(delete_one())
print()
loop.run_until_complete(delete_many())
