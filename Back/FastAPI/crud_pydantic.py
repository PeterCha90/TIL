from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI()

USER_DB = {}
NAME_NOT_FOUND = HTTPException(
    status_code=400,
    detail="Name not found."
)


class CreateIn(BaseModel):
    name: str
    nickname: str


class CreateOut(BaseModel):
    status: str
    id: int


@app.post("/users", response_model=CreateOut)
def create_user(user: CreateIn) -> CreateOut:
    USER_DB[user.name] = user.nickname
    user_dict = user.dict()
    user_dict['status'] = 'success'
    user_dict['id'] = len(USER_DB)
    return user_dict


@app.get("/users")
def get_user(name: str):
    if name not in USER_DB:
        raise NAME_NOT_FOUND
    return {'nickname': USER_DB[name]}
