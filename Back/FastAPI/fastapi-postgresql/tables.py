from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Float, JSON


class OcrResult(Base):
    __tablename__ = 'ocr_result'
    id = Column(Integer, primary_key=True, index=True)
    result = Column(JSON, nullable=False)
