import requests
from refresh_token import ref_tok

auth = {'Authorization': f"Bearer {ref_tok()}"}


def get(url: str, params: dict = None, host: str = 'https://api.alor.ru/md/v2/'):
    res = requests.get(host+url, params, headers=auth)
    return res.json()


def get_trades(offset: int = 0):
    res: list = get('/stats/SPBX/D70657/history/trades', {'from': offset}, 'https://api.alor.ru/md')
    deals = []
    for d in res:
        qty = int(d['qty']) * (1 if d['side'] == 'sell' else -1)
        deals.append({'id': d['id'], 'symbol': d['symbol'], 'price': d['price'], 'qty': qty, 'date': d['date']})
    return deals
