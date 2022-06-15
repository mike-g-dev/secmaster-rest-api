from typing import List, Dict

ALL_TICKERS = [
    "AAPL",
    "MSFT",
    "SPX",
    "VIX",
    "FB",
    "QQQ"
]

FAKE_EQUITY_EOD_DB = [
    {
        "ticker": "AAPL",
        "price": "132.5",
        "market_date": "2022-06-09"
    },
    {
        "ticker": "AAPL",
        "price": "132.5",
        "market_date": "2022-06-10"
    },
    {
        "ticker": "MSFT",
        "price": "132.5",
        "market_date": "2022-06-10"
    }
]


def get_equity_records(ticker: str, date: str) -> List[Dict]:
    return [
        record for record in FAKE_EQUITY_EOD_DB
        if record["ticker"] == ticker and record["market_date"] == date
    ]


def get_all_tickers(as_of: str = "") -> List[str]:
    return ALL_TICKERS
