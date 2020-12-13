from models.Stock import Stock
from models.User import User
from models.Follow import Follow
from models.Trade import Trade
from models.Transaction import Transaction
from db import session
from req import get, get_trades
from filler import stocks_update, trades_update

session.merge(User('artemiev'))
#
m = get('securities/MOEX')
stocks_update(m)
# stocks_update(get('securities/SPBX'))

trades = get_trades()
trades_update(trades)

trades = session.query(Trade).distinct().values(Trade.symbol)
trades = set(t['symbol'] for t in trades)
trades = [{'code': s[0], 'followed_by': 1} for s in trades]
for f in trades:
    session.merge(Follow(*f.values()))
session.commit()
