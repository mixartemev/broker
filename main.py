from models.Stock import Stock
from models.User import User
from models.Trade import Trade
from db import session
from req import get
import pandas
from trades import get_trades

session.merge(User('artemiev'))

res = get('securities/SPBX')
g = [(r['symbol'], r['shortname'], r['type'], r['exchange'], r['rating'], r['volatility']) for r in res]  # last_price
for i in g:
    session.merge(Stock(*i))
print(pandas.DataFrame(g[0:60], columns=('symb', 'name', 'type', 'rating', 'volatile')))

session.commit()

for trade in get_trades():
    session.merge(Trade(*trade.values()))

session.commit()
