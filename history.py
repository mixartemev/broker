from datetime import timedelta, datetime
from req import get

start = int((datetime.now() - timedelta(days=90)).timestamp())


def history(ticker: str):
    h = get('history', {
        'symbol': ticker,
        'exchange': 'SPBX',
        'tf': 86400,
        'from': start,
        'to': int(datetime.now().timestamp())
    })['history']
    for i in h:
        i['time'] = datetime.fromtimestamp(i['time']).date().isoformat()
    return h
