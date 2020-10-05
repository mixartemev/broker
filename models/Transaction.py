from datetime import datetime
from models import *
from models.Stock import Stock
from models.User import User


class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    source = Column(String(15))
    dest = Column(String(15))
    val = Column(Float)
    cur = Column(SmallInteger)
    date = Column(Date)
    user_id = Column(SmallInteger, ForeignKey('users.id'))
    user: User = relationship("User", back_populates="transactions")

    def __init__(self, id, symbol, price, qty, date, user_id=1):
        self.id = id
        self.symbol = symbol
        self.price = price
        self.qty = qty
        self.date = date.split('T')[0]
        self.user_id = user_id
