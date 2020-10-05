from sqlalchemy import func

from models import *
from models.User import User

stock_types = Enum('t', 'r', 'CS', 'ETF', 'EUSOV', 'FOR', 'PS', name='type')


class Stock(Base):
    __tablename__ = 'stocks'
    ticker = Column(String(15), primary_key=True)
    name = Column(String(255))
    type = Column(stock_types)
    exchange = Column(Enum('MOEX', 'SPBX', name='type'))
    rating = Column(Integer)
    volatility = Column(Float)
    last_price = Column(Float)
    followed_by = Column(SmallInteger, ForeignKey('users.id'), default=None)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    follower: User = relationship("User", back_populates="stocks")
    trades = relationship("Trade", back_populates="stock")

    def __init__(self, ticker, name, type, exchange, rating, volatility, last_price=0):
        self.ticker = ticker
        self.name = name
        self.type = type
        self.exchange = exchange
        self.rating = rating
        self.volatility = volatility
        self.last_price = last_price
