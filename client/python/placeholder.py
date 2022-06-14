from typing import List, Dict


class OptionQuotes:
    def __init__(self, tickers: List[str], date: str):
        self.tickers = tickers
        self.date = date

    def get(self) -> List[Dict]:
        return model.get(self.tickers, self.date)


class OptionEod:
    def __init__(self, tickers: List[str], date: str):
        self.tickers = tickers
        self.date = date

    def get(self) -> List[Dict]:
        return model.get(self.tickers, self.date)
