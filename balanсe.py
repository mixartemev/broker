from req import get

m = get('Clients/MOEX/D70657/positions')
s = get('Clients/SPBX/D70657/positions', None, 'https://api.alor.ru/md/')
