from typing import List, Dict
import yfinance as yf
import datetime
import pandas as pd
from dataclasses import dataclass

# TODO: Come up with better way to have global ticker knowledge on per request basis where necissary
ALL_TICKERS = ["AAPL", "MSFT", "SPX", "FB"]


# TODO: refactor this into a way that cleanly converts types from results
# into serializable JSON payload to return from REST API call
@dataclass
class EquityEodRecord:
    market_date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    dividends: int
    stock_splits: int

    def __post_init__(self):
        self.market_date = str(self.market_date)
        self.open = float(self.open)
        self.high = float(self.high)
        self.low = float(self.low)
        self.close = float(self.close)
        self.volume = int(self.volume)
        self.dividends = int(self.dividends)
        self.stock_splits = int(self.stock_splits)


def get_end_date(start_date: str) -> str:
    date_range = pd.bdate_range(start=start_date, periods=2)
    end_date = date_range[-1]
    return datetime.datetime.strftime(end_date, "%Y-%m-%d")


def get_equity_records(ticker: str, date: str) -> List[EquityEodRecord]:
    ticker = yf.Ticker(ticker)
    end_date = get_end_date(date)

    # TODO: cache these responses
    results = ticker.history(start=date, end=end_date)
    return [EquityEodRecord(*r) for r in results.to_records()]


def get_all_tickers(as_of: str = "") -> List[str]:
    return ALL_TICKERS
