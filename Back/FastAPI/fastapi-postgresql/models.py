from pydantic import BaseModel
from typing import List, Tuple, Optional


class DictList(BaseModel):
    DRAWE_CPHN_NO: Optional[str]
    LOC_NATNL_CD: Optional[str]
    ERROR_CD: Optional[str]
    RELAY_BNK_NAME: Optional[str]
    IMPRT_USAG_DSTC: Optional[str]
    PYBNK_NAME: Optional[str]
    RMTANC_DTTuple_CTNT: Optional[str]
    PYBNK_ADDR: Optional[str]
    DRAWE_ADDR_TELNO: Optional[str]
    PYBNK_NO: Optional[str]
    PYBNK_BIC: Optional[str]
    RMTR_TELNO: Optional[str]
    DRAWE_FNAME: Optional[str]
    IMPRT_RPRT_NO: Optional[str]
    RMTR_ENG_NAME: Optional[str]
    HS_CD: Optional[str]


class DictEntry(BaseModel):
    dictionary: Optional[DictList]


class BboxList(BaseModel):
    buyer: Optional[
        Tuple[str, List[Tuple[float, float]], float]]
    seller: Optional[
        Tuple[str, List[Tuple[float, float]], float]]
    consignee: Optional[
        Tuple[str, List[Tuple[float, float]], float]]
    commodity: Optional[
        Tuple[str, List[Tuple[float, float]], float]]
    quantity: Optional[
        Tuple[str, List[Tuple[float, float]], float]]
    unit_price: Optional[
        Tuple[str, List[Tuple[float, float]], float]]
    amount: Optional[
        Tuple[str, List[Tuple[float, float]], float]]
    description_of_goods: Optional[
        Tuple[str, List[Tuple[float, float]], float]]
    origin: Optional[
        Tuple[str, List[Tuple[float, float]], float]]
    time_of_shipment: Optional[
        Tuple[str, List[Tuple[float, float]], float]]
    Beneficiary_name: Optional[
        Tuple[str, List[Tuple[float, float]], float]]
    AccountNo: Optional[
        Tuple[str, List[Tuple[float, float]], float]]
    Beneficiary_Bank: Optional[
        Tuple[str, List[Tuple[float, float]], float]]


class BboxesEntry(BaseModel):
    bboxes: Optional[BboxList]


class TimeEntry(BaseModel):
    start: Optional[str]
    end: Optional[str]


class OcrResult(BaseModel):
    reply: Optional[List[Tuple[DictEntry, BboxesEntry]]]
    time: Optional[TimeEntry]
