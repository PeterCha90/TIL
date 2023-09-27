import json
import tables

from models import *
from typing import List, Annotated
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from fastapi_offline import FastAPIOffline
from fastapi import Depends, HTTPException

app = FastAPIOffline()
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
    ppr_key = ocr_result['ppr_key']
    ocr_json = ocr_result['reply']
    ocr_start = ocr_result['time']['start']
    ocr_end = ocr_result['time']['end']

    ocr_json = json.dumps(ocr_json)
    ocr_data = tables.OcrResult(ppr_key=ppr_key,
                                result=ocr_json,
                                start=ocr_start,
                                end=ocr_end)
    db.add(ocr_data)
    db.commit()
    db.refresh(ocr_data)


@app.get("/ocr_result/{ppr_key}")
async def read_result(ppr_key: str, db: db_dependency):
    result = db.query(tables.OcrResult).filter(
        tables.OcrResult.ppr_key == ppr_key).all()
    if not result:
        raise HTTPException(status_code=404,
                            detail='Result is not found')
    return result
