import os
import asyncio

from pprint import pprint
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

MONGODB_URL = os.environ["MONGODB_URL"]
client = AsyncIOMotorClient(MONGODB_URL)
collection = client.bank.test_collection


async def replace():
    old = await collection.find_one({'i': 2003})
    print('Old doc: %s' % repr(old))
    _id = old['_id']
    result = await collection.replace_one(
        {'i': 2003}, {'replace': 'everything'}
    )
    print('Replaced %s' % result.modified_count)
    new = await collection.find_one(
        {'_id': _id})
    print('Now %s' % repr(new))


async def update():
    result = await collection.update_one(
        {'i': 2003},
        {'$set': {'key': 'value'}}
    )
    print('Updated %s doc' % result.modified_count)


async def update_many():
    result = await collection.update_many(
        {'i': {'$lt': 2005}},
        {'$set': {'status': 'updated'}}
    )
    print('Updated %s docs' % result.modified_count)


loop = asyncio.get_event_loop()
loop.run_until_complete(replace())
print()
loop.run_until_complete(update())
print()
loop.run_until_complete(update_many())
