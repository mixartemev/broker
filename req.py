import requests
from refresh_token import ref_tok

auth = {'Authorization': f"Bearer {ref_tok()}"}


def get(url: str, params: dict = None, host: str = 'https://api.alor.ru/md/v2/'):
    return requests.get(host+url, params, headers=auth).json()
