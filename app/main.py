"""
Executable FastApi REST API script.
"""
from fastapi import FastAPI
from pydantic import BaseModel


INDICIES = [
    {
        "ticker": "SPY",
        "open_price": 123.4,
        "close_price": 124.0
    },
    {
        "ticker": "QQQ",
        "open_price": 123.4,
        "close_price": 124.0
    },
    {
        "ticker": "SPX",
        "open_price": 123.4,
        "close_price": 124.0
    }
]


class Equity(BaseModel):
    ticker: str
    open_price: float
    close_price: float


EQUITIES = [
    Equity(**{
        "ticker": "AAPL",
        "open_price": 123.4,
        "close_price": 124.0
    }),
    Equity(**{
        "ticker": "MSFT",
        "open_price": 123.4,
        "close_price": 124.0
    }),
    Equity(**{
        "ticker": "TSLA",
        "open_price": 123.4,
        "close_price": 124.0
    })
]


def get_application() -> FastAPI:
    """
    Returns a configured instance of FastAPI application
    :return:
    """
    return FastAPI()


app = get_application()


@app.get("/")
async def root():
    return {"message": "Welcome to secmaster api!"}


@app.get("/eod")
async def get_all_eod_data(skip: int = 0, limit: int = 10):
    """
    Sends GET to /eod/?skip=0&limit=10 URL
    Declaring python types is the first layer of validation as these parameters are
    passed in as strings but are converted to ints in this method.

    :param skip:
    :param limit:
    :return:
    """
    data = INDICIES + EQUITIES
    return {
        "data": data[skip:skip + limit],
        "response_code": 200 if data else 404
    }


@app.get("/eod/equity/{ticker}")
async def get_eod_ticker(ticker: str):
    data = [row for row in EQUITIES if row.ticker == ticker]
    return {
        "data": data,
        "response_code": 200 if data else 404
    }


@app.get("/eod/indicies/{ticker}")
async def get_eod_ticker(ticker: str):
    data = [row for row in INDICIES if row.ticker == ticker]
    return {
        "data": data,
        "response_code": 200 if data else 404
    }


@app.put("/eod/equity/")
async def create_equity_record(equity: Equity):
    EQUITIES.append(equity)
    return equity


@app.put("/eod/indicies/")
async def create_index_record(equity: Equity):
    INDICIES.append(equity)
    return equity