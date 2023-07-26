import os
import asyncio

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

MONGODB_URL = os.environ["MONGODB_URL"]
client = AsyncIOMotorClient(MONGODB_URL)


async def ping_server():
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        db_list = await client.list_database_names()
        print("Successfully connected to MongoDB!")
        print("Your DB list:")
        print("\t" + str(db_list))
    except Exception as e:
        print(e)

loop = asyncio.get_event_loop()
loop.run_until_complete(ping_server())
loop.close()