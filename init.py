from models.Stock import Stock
from models.User import User
from models.Trade import Trade
from db import session
from req import get, get_trades
from filler import stocks_update, trades_update

session.merge(User('artemiev'))

stocks_update(get('securities/MOEX'))
stocks_update(get('securities/SPBX'))

trades_update(get_trades())
