from req import get


def get_trades():
    res: list = get('/stats/SPBX/D70657/history/trades', {'from': 600}, 'https://api.alor.ru/md')
    deals = []
    for d in res:
        qty = int(d['qty']) * (1 if d['side'] == 'sell' else -1)
        deals.append({'id': d['id'], 'symbol': d['symbol'], 'price': d['price'], 'qty': qty, 'date': d['date']})
    return deals
