import json
from datetime import datetime
from python_bitvavo_api.bitvavo import Bitvavo

def read_data():
    with open ('bitvavo_api\\dataset.txt','r') as data:
        data = data.readlines()
        return data
    
def average_from_coin(coin):    
    data = read_data()
    count = 0
    total = 0
    for i in range(len(data)):
        item = json.loads(data[i])
        if item["market"] == coin:
            count += 1
            total += float(item['last'])
    return total/count

def get_min_from_coin(coin):
    data = read_data()
    minimum = 1000000000
    for i in range(len(data)):
        item = json.loads(data[i])
        if item["market"] == coin:
            if float(item['last']) < minimum:
                minimum = float(item['last'])
    return minimum

def get_max_from_coin(coin):
    data = read_data()
    maximum = 0
    for i in range(len(data)):
        item = json.loads(data[i])
        if item["market"] == coin:
            if float(item['last']) > maximum:
                maximum = float(item['last'])
    return maximum

def length_dataset():
    data = read_data()
    first = int(json.loads(data[0])['timestamp'])
    last = int(json.loads(data[len(data)-1])['timestamp'])
    first_date = datetime.fromtimestamp(first/1000)    
    last_date = datetime.fromtimestamp(last/1000)

    length = last_date-first_date
    return length.days
def last_pull():
    data = read_data()   
    last = int(json.loads(data[len(data)-1])['timestamp'])  
    last_date = datetime.fromtimestamp(last/1000)
    return last_date.date()

def perc_coin_above_average(coin): # for percentage beneath the average -> 1 - this function
    data = read_data()
    avg = average_from_coin(coin)
    count_coin = 0
    count = 0
    for i in range(len(data)):
        item = json.loads(data[i])
        if item['market'] == coin:
            count_coin += 1
            if float(item['last']) > avg:
                count += 1
    return count/count_coin

def avg_price_if_price_above_avg(coin):
    data = read_data()
    avg = average_from_coin(coin)
    total = 0
    count = 0
    for i in range(len(data)):
        item = json.loads(data[i])
        if item['market'] == coin:
            if float(item['last']) > avg:
                total += float(item['last'])
                count += 1
    return total/count

def avg_price_if_price_beneath_avg(coin):
    data = read_data()
    avg = average_from_coin(coin)
    total = 0
    count = 0
    for i in range(len(data)):
        item = json.loads(data[i])
        if item['market'] == coin:
            if float(item['last']) < avg:
                total += float(item['last'])
                count += 1
    return total/count
def all_currencies():
    data = read_data()
    currencies = []
    for i in range(len(data)):
        item = json.loads(data[i])
        if item['market'] not in currencies:
            currencies.append(item['market'])
    return currencies
def current_price(coin):
    bitvavo = Bitvavo()
    response = bitvavo.tickerPrice({})
    for market in response:
        if market['market'] == coin:
            return float(market['price'])
        
def overview_currency(currency):
    if currency not in all_currencies():
        return []
    overview = {
            'currency':currency,
            'current':round(current_price(currency),3),
            'average': round(average_from_coin(currency),3),
            'minimum': round(get_min_from_coin(currency),3),
            'maximum': round(get_max_from_coin(currency),3),
            'perc_above_avg': round(perc_coin_above_average(currency)*100,3),
            'perc_beneath_avg':round((1-perc_coin_above_average(currency))*100,3),
            'avg_price_above_avg': round(avg_price_if_price_above_avg(currency),3),
            'avg_price_beneath_avg': round(avg_price_if_price_beneath_avg(currency),3)
        }
    return overview
    
def overview():
    currencies = all_currencies()
    overview_data = []
    for currency in currencies:
        overview = overview_currency(currency)
        overview_data.append(overview)
    return overview_data

general_data = overview()
timespan = length_dataset()
last_update = last_pull()

# print(average_from_coin("ADA-EUR"))
# print(avg_price_if_price_beneath_avg("ADA-EUR"))
# print(perc_coin_above_average("ADA-EUR"))
