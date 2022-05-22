import requests
import time
import datetime

from db import DB
from common_types import Config


class Bot:
    def __init__(self, config: Config, db: DB):
        self.config = config
        self.db = db

        r = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BNBUSDT').json()
        self.bnb = int(float(r['price']))
        r = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT').json()
        self.eth = int(float(r['price']))

    def start(self):
        cursor = 1
        while True:
            r = requests.get(f'https://www.binance.com/bapi/nft/v1/public/nft/homepage/announce?cursor={cursor}').json()
            data = r['data']['orderSuccessAnnounces'][0]

            data["priceBUSD"] = None

            if data['currency'] == 'BNB':
                data["priceBUSD"] = float(self.bnb) * float(data['price'])
            elif data['currency'] == 'ETH':
                data["priceBUSD"] = float(self.eth) * float(data['price'])
            elif data['currency'] == 'BUSD':
                data["priceBUSD"] = float(data['price'])

            element_id = self.db.insert_document(data)
            if element_id:
                print(data)
                print('\n')
            time.sleep(self.config.request_time_delay)
            if cursor < 30:
                cursor += 1
            else:
                cursor = 1

    def stop(self):
        pass

