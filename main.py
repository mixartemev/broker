from db import session
from history import history
from models.Stock import Stock
from models.Trade import Trade
from req import get

# h = history('INTC')
# o = get('orderbooks/MOEX/SBER')
# print(h)
stocks = ('INTC', 'IBM', 'GTX', 'ZM', 'AAPL', 'TSLA', 'SBER', 'YNDX')

q = get('securities/MOEX%3ASBER%2CMOEX%3AGAZP/quotes')
print(q)
