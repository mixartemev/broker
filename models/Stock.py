from sqlalchemy import func

from models import *

stock_types = Enum('t', 'r', 'CS', 'ETF', 'EUSOV', 'FOR', 'PS', 'RDR', name='type')


class Stock(Base):
    __tablename__ = 'stocks'
    ticker = Column(String(15), primary_key=True)
    name = Column(String(255))
    type = Column(stock_types)
    exchange = Column(Enum('MOEX', 'SPBX', name='type'))
    lot = Column(Integer)
    rating = Column(Integer)
    volatility = Column(Float)
    last_price = Column(Float)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    followers: [] = relationship("Follow", back_populates="stock")
    trades: [] = relationship("Trade", back_populates="stock")

    def __init__(self, ticker, name, type, exchange, lot, rating, volatility, last_price=0):
        self.ticker = ticker
        self.name = name
        self.type = type
        self.exchange = exchange
        self.lot = lot
        self.rating = rating
        self.volatility = volatility
        self.last_price = last_price
