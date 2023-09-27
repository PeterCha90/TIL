from database import Base
from sqlalchemy import Column, Integer, String, JSON


class OcrResult(Base):
    __tablename__ = 'ocr_result'
    id = Column(Integer, primary_key=True, index=True)
    ppr_key = Column(String, nullable=False)
    start = Column(String, nullable=False)
    end = Column(String, nullable=False)
    result = Column(JSON, nullable=True)
