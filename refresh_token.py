import requests
from env import REFRESH_TOKEN


def ref_tok():
    return requests.post(f"https://oauth.alor.ru/refresh?token={REFRESH_TOKEN}").json()['AccessToken']
