from pydantic import BaseModel, Field
from typing import List, Tuple, Optional, Any


class DictList(BaseModel):
    DRAWE_CPHN_NO: Optional[str] = None
    LOC_NATNL_CD: Optional[str] = None
    ERROR_CD: Optional[str] = None
    RELAY_BNK_NAME: Optional[str] = None
    IMPRT_USAG_DSTC: Optional[str] = None
    PYBNK_NAME: Optional[str] = None
    RMTANC_DTLIST_CTNT: Optional[str] = None
    PYBNK_ADDR: Optional[str] = None
    DRAWE_ADDR_TELNO: Optional[str] = None
    PYBNK_NO: Optional[str] = None
    PYBNK_BIC: Optional[str] = None
    RMTR_TELNO: Optional[str] = None
    DRAWE_FNAME: Optional[str] = None
    IMPRT_RPRT_NO: Optional[str] = None
    RMTR_ENG_NAME: Optional[str] = None
    HS_CD: Optional[str] = None
    buyer: Optional[
        List[Optional[Any]]
    ] = None
    seller: Optional[
        List[Optional[Any]]
    ] = None
    consignee: Optional[
        List[Optional[Any]]
    ] = None

    commodity: Optional[
        List[Optional[Any]]
    ] = None
    quantity: Optional[
        List[Optional[Any]]
    ] = None
    unit_price: Optional[
        List[Optional[Any]]
    ] = None
    amount: Optional[
        List[Optional[Any]]
    ] = None
    description_of_goods: Optional[
        List[Optional[Any]]
    ] = None
    origin: Optional[
        List[Optional[Any]]
    ] = None
    time_of_shipment: Optional[
        List[Optional[Any]]
    ] = None
    Beneficiary_name: Optional[
        List[Optional[Any]]
    ] = None
    AccountNo: Optional[
        List[Optional[Any]]
    ] = None
    Beneficiary_Bank: Optional[
        List[Optional[Any]]
    ] = None


class TimeEntry(BaseModel):
    start: Optional[str]
    end: Optional[str]


class OcrData(BaseModel):
    reply_dict: DictList


class OcrResult(BaseModel):
    reply: List[OcrData]
    time: TimeEntry
    ppr_key: str
