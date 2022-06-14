from pydantic import BaseModel


class EquityEOD(BaseModel):
    ticker: str
    price: float
    market_date: str


class EquityMinuteBar(BaseModel):
    ticker: str
    bar_start_time: str
    bar_end_time: str
    first_price: float
    last_price: float
    first_volume: int
    last_volume: int