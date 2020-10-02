import requests
from refresh_token import ref_tok


def get_trades():
    res: list = requests.get(
        'https://api.alor.ru/md/stats/SPBX/D70657/history/trades',
        headers={'Authorization': f"Bearer {ref_tok()}"}
    ).json()
    deals = []
    for d in res:
        sell = -1 if d['side'] == 'sell' else 1
        deals.append({'id': d['id'], 'symbol': d['symbol'], 'qty': int(d['qty'])*sell,  'price': d['price']})
    return deals
