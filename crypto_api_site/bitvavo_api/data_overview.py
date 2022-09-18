import json
from datetime import datetime

def read_data():
    with open ('D:\\David\\bitvavoApi\\crypto_api_site\\dataset\\dataset_raw.txt','r') as data:
        data = data.readlines()
        return data
def get_overview():
    data_overview = []
    with open("D:\\David\\bitvavoApi\\crypto_api_site\\bitvavo_api\\calculated_dataset.txt","r") as input:
        data = input.readlines()
        for i in range(len(data)):
            item = json.loads(data[i])
            data_overview.append(item)
    return data_overview

def get_overview_currency(currency):
    with open("D:\\David\\bitvavoApi\\crypto_api_site\\bitvavo_api\\calculated_dataset.txt","r") as input:
        data = input.readlines()
        for i in range(len(data)):
            item = json.loads(data[i])
            if item['currency'] == currency:
                return item

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
def test():
    with open("calculated_dataset.txt","r") as output:
        data = output.readlines()
        for i in range(len(data)):
            item = json.loads(data[i])
            print(item["current"])

def date_from_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp/1000)
def last_days_coin(coin,days):
    data = read_data()
    coin_data = []
    for i in range(len(data)-1,0,-1):
        item = json.loads(data[i])
        if item["market"] == coin and len(coin_data) != days:
            coin_data.append(item)
    return coin_data
coin_data = last_days_coin("ADA-EUR",7)
overview = get_overview()
last_update = last_pull()
length = length_dataset()
