from datetime import date
from python_bitvavo_api.bitvavo import Bitvavo
from datetime import datetime
import schedule
import time

bitvavo = Bitvavo()
response = bitvavo.ticker24h({})

with open("D:\\David\\bitvavoApi\\crypto_api_site\\dataset\\dataset_raw.txt","r+") as output:
     crypto_data = output.read()
     for market in response:
        if '-BTC' not in market["market"]:
            has_none_values = False
            for item in market.items():
                if item == None:
                    has_none_values = True
                    break
            if not has_none_values:
                str_market = str(market)
                changed = str_market.replace("'","\"")
                output.write(f"{changed}\n")



    