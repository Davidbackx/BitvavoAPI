from ast import Lambda
from functools import total_ordering
from inspect import currentframe
import json
from random import weibullvariate

def read_data():
    with open ('D:\\David\\bitvavoApi\\crypto_api_site\\dataset\\dataset_raw.txt','r') as data:
        data = data.readlines()
        return data

data = read_data()

def get_all_max_points(currency):
    working_data = []
    max = []
    for i in range(len(data)):
        item = json.loads(data[i])
        if item["market"] == currency:
            working_data.append(item)
    while len(max) < 5:
        i = 0
        highest = {}
        for item in working_data:
            if float(item["high"]) > i:
                highest = item
        max.append(highest)
        working_data.remove(highest)
    max = sorted(max,key=lambda x:x["timestamp"],reverse=True)
    return max
def get_all_min_points(currency):
    working_data = []
    min = []
    for i in range(len(data)):
        item = json.loads(data[i])
        if item["market"] == currency:
            working_data.append(item)
    while len(min) < 5:
        i = 999999999
        lowest = {}
        for item in working_data:
            if float(item["low"]) < i:
                lowest = item
        min.append(lowest)
        working_data.remove(lowest)
    min = sorted(min,key=lambda x:x["timestamp"],reverse=True)
    return min
def trend_calc(currency):
    max_values = ([item["high"] for item in get_all_max_points(currency)])
    min_values = ([item["low"] for item in get_all_min_points(currency)])
    averages = []
    for i in range(len(max_values)):
        averages.append(round(((float(max_values[i])+float(min_values[i]))/2),4))
    total = 0
    for avg in averages:
        total += avg
    average = total/len(averages)
    if average > averages[0]:
        return 1
    elif average < averages[0]:
        return -1
    else:
        return 0

def current_trend(currency):
    value = trend_calc(currency)
    if value == 1:
        return f"{currency} zit in een stijgende trend"
    elif value == -1:
        return f"{currency} zit in een dalende trend"
    else:
        return f"{currency} zit op een constante trend"

def avg(currency):
    total = 0
    n = 0
    for i in range(len(data)):
        item = json.loads(data[i])
        if item["market"] == currency:
            n += 1
            total += float(item["last"])
    return total/n

def ema(currency,period):
    ema = []
    n:int = period
    weight = 2/(n+1)
    average = avg(currency)
    currency_data = []
    for i in range(len(data)):
        item = json.loads(data[i])
        if item["market"] == currency:
            currency_data.append(item)
    
    for idx,item in enumerate(currency_data):
        if idx+1 > n:
            if len(ema) == 0:
                ema.append(round((average+weight*(float(item["last"]))-average),4))
            else:
                ema.append(round(ema[idx-n-1]+weight*(float(item["last"])-ema[idx-n-1]),4))
    return ema

def ema2(currency,period):
    ema = []
    n:int = period
    weight = 2/(n+1)
    average = avg(currency)
    currency_data = []
    for i in range(len(data)):
        item = json.loads(data[i])
        if item["market"] == currency:
            currency_data.append(item)
    
    for idx,item in enumerate(currency_data):
        if idx+1 > n:
            if len(ema) == 0:
                ema_val = (float(item["last"])*weight)+(average*(1-weight))
                value = {
                    "ema":round(ema_val,4),
                    "time":item["timestamp"]
                }
                ema.append(value)
            else:
                ema_val = (float(item["last"])*weight)+(ema[idx-n-1]["ema"]*(1-weight))
                value ={
                    "ema":round(ema_val,4),
                    "time":item["timestamp"]
                } 
                ema.append(value)
    return ema
# def macd(currency):
#     ema_12 = ema2(currency,12)
#     ema_26 = ema2(currency,26)
#     min = 0
#     if len(ema_12) > len(ema_26):
#         min = len(ema_26)
#     else:
#         min = len(ema_12)
#     macd = []
#     for i in range(min):
#         value = ema_12[i] - ema_26[i]
#         macd.append(round(value,4))
#     return macd
# print(macd("ADA-EUR"))

