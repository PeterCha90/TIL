import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGODB_URL = os.environ["MONGODB_URL"]

client = MongoClient(MONGODB_URL)


def callback(
    session,
    transfer_id=None,
    receiver=None,
    sender=None,
    amount=None
):
    accounts_collection = session.client.bank.accounts
    transfers_collection = session.client.bank.transfers

    transfer = {
        "transfer_id": transfer_id,
        "to_account": receiver,
        "from_account": sender,
        "amount": {"$numberDecimal": amount}
    }

    accounts_collection.update_one(
        {"account_id": sender},
        {
            "$inc": {"balance": -amount},
            "$push": {"transfers_complete": transfer_id}
        },
        session=session
    )

    accounts_collection.update_one(
        {"account_id": receiver},
        {
            "$inc": {"balance": amount},
            "$push": {"transfers_complete": transfer_id}
        },
        session=session
    )

    transfers_collection.insert_one(transfer, session=session)
    print("Transaction successful")

    return


def callback_wrapper(s): return callback(
    s,
    transfer_id="TR2131342",
    receiver="MDB333332222",
    sender="MDB93929292",
    amount=100
)


with client.start_session() as session:
    session.with_transaction(callback_wrapper)

client.close()
