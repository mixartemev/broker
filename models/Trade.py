from models import *
from models.Stock import Stock
from models.User import User


class Trade(Base):
    __tablename__ = 'trades'
    id = Column(Integer, primary_key=True)
    symbol = Column(String(15), ForeignKey('stocks.ticker'))
    price = Column(Float)
    qty = Column(SmallInteger)
    date = Column(Date)
    user_id = Column(SmallInteger, ForeignKey('users.id'))
    user: User = relationship("User", back_populates="trades")
    stock: Stock = relationship("Stock", back_populates="trades")

    def __init__(self, id, symbol, price, qty, date, user_id=1):
        self.id = id
        self.symbol = symbol
        self.price = price
        self.qty = qty
        self.date = date
        self.user_id = user_id
