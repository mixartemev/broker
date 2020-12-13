from models import *
from models.Stock import Stock
from models.User import User


class Follow(Base):
    __tablename__ = 'follows'
    code = Column(String(15), ForeignKey('stocks.ticker'), primary_key=True)
    followed_by = Column(SmallInteger, ForeignKey('users.id'), primary_key=True)

    follower: User = relationship("User", back_populates="follows")
    stock: Stock = relationship("Stock", back_populates="followers")

    def __init__(self, code, followed_by):
        self.code = code
        self.followed_by = followed_by
