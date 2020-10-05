from db import session
from filler import trades_update
from models.Trade import Trade
from req import get_trades

last_trade = session.query(Trade).order_by(Trade.id.desc()).first().id
trades_update(get_trades(last_trade))

