import json
import tables

from models import *
from typing import List, Annotated
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()
tables.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/save_result/")
async def save_result(result: OcrResult,
                      db: db_dependency):
    ocr_result = result.dict()
    ocr_json = json.dumps(ocr_result)
    ocr_json = tables.OcrResult(result=ocr_json)
    db.add(ocr_json)
    db.commit()
    db.refresh(ocr_json)


@app.get("/ocr_result/{result_id}")
async def read_result(result_id: int, db: db_dependency):
    result = db.query(tables.OcrResult).filter(
        tables.OcrResult.id == result_id).all()
    if not result:
        raise HTTPException(status_code=404,
                            detail='Result is not found')
    return result
