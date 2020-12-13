from db import session
from models.Stock import Stock, stock_types
from models.Trade import Trade


def stocks_update(arr: list):
    arr = filter(lambda x: x['type'] in stock_types.enums, arr)
    g = [(r['symbol'], r['description'], r['type'], r['exchange'], r['lotsize'], r['rating'], r['volatility'], r.get('last_price')) for r in arr]
    for i in g:
        session.merge(Stock(*i))
    session.commit()


def trades_update(arr: list):
    for trade in arr:
        session.merge(Trade(*trade.values()))
    session.commit()
