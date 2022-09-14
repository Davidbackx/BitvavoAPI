from datetime import date
from python_bitvavo_api.bitvavo import Bitvavo
from datetime import datetime
import schedule
import time

bitvavo = Bitvavo()
response = bitvavo.ticker24h({})

with open("D:\\David\\cryptomarket_dataset\\crypto-dataset\\dataset.txt","r+") as output:
     crypto_data = output.read()
     for market in response:
        if '-BTC' not in market["market"]:
            output.write(f'{market}\n')



    