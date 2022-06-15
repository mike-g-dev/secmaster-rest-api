from fastapi import FastAPI
from src.python_server import db

# TODO: sophisticated creation of this object
app = FastAPI()


# TODO: add proper routing
@app.get("/tickers")
async def get_all_tickers(as_of: str = ""):
    return db.get_all_tickers(as_of=as_of)


# @app.post("/equity/eod/{ticker}", response_model=EquityEOD)
# async def get_equity_eod(ticker: str, market_date: str):
#     return db.get_equity_records(ticker=ticker, date=market_date)
