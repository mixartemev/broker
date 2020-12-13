from models import *
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

    def __init__(self, id, source, dest, val, cur, date, user_id=1):
        self.id = id
        self.source = source
        self.dest = dest
        self.val = val
        self.cur = cur
        self.date = date
        self.user_id = user_id
