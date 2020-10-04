from sqlalchemy.orm import relationship
from models import Base, Column, SmallInteger, String


class User(Base):
    __tablename__ = 'users'
    id = Column(SmallInteger, primary_key=True, autoincrement=True)
    name = Column(String(255))
    trades = relationship("Trade", back_populates="user")

    def __init__(self, name):
        self.name = name