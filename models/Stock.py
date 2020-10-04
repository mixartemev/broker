from sqlalchemy import func
from models import *


class Stock(Base):
    __tablename__ = 'stocks'
    ticker = Column(String(15), primary_key=True)
    name = Column(String(127))
    type = Column(Enum('t', 'r', name='type'))
    exchange = Column(Enum('MOEX', 'SPBX', name='type'))
    rating = Column(Integer)
    volatility = Column(Float)
    last_price = Column(Float)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    trades = relationship("Trade", back_populates="stock")

    def __init__(self, ticker, name, type, exchange, rating, volatility, last_price=0):
        self.ticker = ticker
        self.name = name
        self.type = type
        self.exchange = exchange
        self.rating = rating
        self.volatility = volatility
        self.last_price = last_price
