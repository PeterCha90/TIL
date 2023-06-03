from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI()

USER_DB = {}
NAME_NOT_FOUND = HTTPException(
    status_code=400,
    detail="Name not found."
)
