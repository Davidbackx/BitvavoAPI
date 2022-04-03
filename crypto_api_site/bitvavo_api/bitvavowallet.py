from python_bitvavo_api.bitvavo import Bitvavo
import numpy as np
import math
from datetime import datetime
#from bitvavovariables import bitvavo_api,bitvavo_secret_api

bitvavo = Bitvavo()
response = bitvavo.tickerPrice({})
assets = bitvavo.assets({})
PricesLatest24h = bitvavo.ticker24h({})
api_key = '30477b338507ae0f02edf1d363ad7b28cc2c6ec19934b393a0940fb9f9ff6151'
api_secret_key ='33ae1f6ad81423f557d8203a7305aa96d0da2a30c9d95765619ebfa5e41063dae4649eaa2ff811db19b407e7d85f12cc0546821677cebd316906e026abfba956'

#help functions
def get_max_price_from_name(currencyname):
    symbols = list()
    names = list()
    for symbol in assets:
        symbols.append(symbol['symbol'])
    for name in assets:
        names.append(name['name'])
    if currencyname is None:
        return None
    else:
        if currencyname in symbols:
            abrev = currencyname
        else:
            abrev = get_abrev_from_fullName(currencyname)
        for minPrice in PricesLatest24h:
            if abrev+'-EUR' in minPrice['market']:
                return minPrice['high']

def get_min_price_from_name(currencyname):
    symbols = list()
    names = list()
    for symbol in assets:
        symbols.append(symbol['symbol'])
    for name in assets:
        names.append(name['name'])
    if currencyname is None:
        return None
    else:
        if currencyname in symbols:
            abrev = currencyname
        else:
            abrev = get_abrev_from_fullName(currencyname)
        for minPrice in PricesLatest24h:
            if abrev+'-EUR' in minPrice['market']:
                return minPrice['low']
        
def get_current_value_from_currency(currencyname):
    symbols = list()
    names = list()
    abrev =''
    for symbol in assets:
        symbols.append(symbol['symbol'])
    for name in assets:
        names.append(name['name'])

    if currencyname in symbols:
        abrev = currencyname
    else:
        abrev = get_abrev_from_fullName(currencyname)
    for price in response:
        if abrev+'-EUR' in price['market']:
            currentPrice = price['price']
            return currentPrice
        
def get_fullName_from_abrev(currencyname):
    currencyname = currencyname
    for symbol in assets:
        if symbol['symbol'] == currencyname:
            return symbol['name']

def get_abrev_from_fullName(currencyname):
    currencyname = currencyname
    for symbol in assets:
        if symbol['name'] == currencyname:
            return symbol['symbol']

#account functions
def get_account_currencys(apiKey,apiSecretKey): #['ADA', 'NANO', 'RSR', 'VET', 'XRP']
    apiKey = api_key
    apiSecretKey = api_secret_key
    bitvavo = Bitvavo({"apikey":apiKey,"apisecret":apiSecretKey})
    response = bitvavo.balance({})
    abrevs =list()
    for item in response:
        abrevs.append(item['symbol'])
    abrevs.pop(0)
    return [item for item in abrevs]

    
def get_total_account_deposits_in_eur(apiKey,apiSecretKey): #700
    apiKey = api_key
    apiSecretKey = api_secret_key
    bitvavo = Bitvavo({"apikey":apiKey,"apisecret":apiSecretKey})
    response = bitvavo.depositHistory({})
    totalAmount = 0
    for item in response:
        totalAmount += int(item['amount'])
    return (totalAmount) 
def get_total_account_balance(apiKey,apiSecretKey): #710.7
    apiKey = api_key
    apiSecretKey = api_secret_key

    bitvavo = Bitvavo({"apikey":apiKey,"apisecret":apiSecretKey})
    response = bitvavo.balance({})
    abrevs =list()
    amount = list()
    totalAmount = 0
    for item in response:
        abrevs.append(item['symbol'])
        amount.append(item['available'])
    abrevs.pop(0)
    amount.pop(0)
    for index,symbol in enumerate(abrevs):
        totalAmount += float(get_current_value_from_currency(symbol))*float(amount[index])
    return (round(totalAmount,2))

def get_amount_of_currency_per_currency(apiKey,apiSecretKey): #{'ADA': '157.810902', 'NANO': '3.334171', 'RSR': '4621.39822719', 'VET': '1200.40159841', 'XRP': '63.900059'}
    bitvavo = Bitvavo({"apikey":apiKey,"apisecret":apiSecretKey})
    response = bitvavo.balance({})
    return {item["symbol"]:item["available"] for item in response if item["symbol"] != "EUR" }

def get_account_win_loss(apiKey,apiSecretKey):  #{'totalInvested': 700, 'balance': 710.75, 'winnings': 10.75}
    apiKey = api_key
    apiSecretKey = api_secret_key
    totalInvested = get_total_account_deposits_in_eur(apiKey,apiSecretKey)
    balance = get_total_account_balance(apiKey,apiSecretKey)
    return {"totalInvested":totalInvested,"balance":balance,"winnings":round((balance-totalInvested),2)}

def get_totalinvested_per_currency(apiKey,apiSecretKey): #{'ADA': 265, 'NANO': 30, 'RSR': 185, 'VET': 150, 'XRP': 70}
    bitvavo = Bitvavo({"apikey":apiKey,"apisecret":apiSecretKey})
    account_currencys = get_account_currencys(apiKey,apiSecretKey)
    currencys = {}
    for currency in account_currencys:
        if currency not in currencys:
            currencys[currency] = 0
        total_value = 0
        for item in bitvavo.trades(currency +'-EUR', {}):
            value = float(item["price"]) * float(item["amount"])
            total_value += value
        currencys[currency] = math.ceil(total_value)
    return currencys


def get_all_currency_with_current_value(apiKey,apiSecretKey): #{'ADA': 282.9707283762, 'NANO': 16.857568576, 'RSR': 176.09837944707496, 'VET': 167.9721956655113, 'XRP': 66.63498152519999}
    symbols = get_account_currencys(apiKey,apiSecretKey)
    currency_with_totalinvested = get_amount_of_currency_per_currency(apiKey,apiSecretKey)
    accountcurrencys = {}
    for symbol in symbols:
        for key,value in currency_with_totalinvested.items():
            if key == symbol:
                accountcurrencys[symbol] = float(get_current_value_from_currency(symbol))*float(value)
    return accountcurrencys

def get_trades(apiKey,apiSecretKey):
    bitvavo = Bitvavo({"apikey":apiKey,"apisecret":apiSecretKey})
    response = bitvavo.trades('ADA-EUR', {})
    accountcurrencys = get_account_currencys(apiKey,apiSecretKey)
    accounttrades = {"timestamp":"","market":"","price":0}
    for currency in accountcurrencys:
        for item in bitvavo.trades(currency +'-EUR', {}):
            if item["timestamp"] == accounttrades["timestamp"]:
                accounttrades["timestamp"] = ""
                accounttrades["market"] = ""
                accounttrades["price"] = 0
            else:
                timestamp = datetime.fromtimestamp(item["timestamp"]/1000.0).date()
                timestampStr = timestamp.strftime("%d-%b-%Y")
                accounttrades["timestamp"] = timestampStr
                accounttrades["market"] = item["market"]
                accounttrades["price"] = math.ceil(float(item["price"])*float(item["amount"]))
    return accounttrades
#1 Jan 1970 for timestamps
currencys = get_totalinvested_per_currency(api_key,api_secret_key)
currentvalues = get_all_currency_with_current_value(api_key,api_secret_key)
test = get_trades(api_key,api_secret_key)
time = datetime.fromtimestamp((1628984117053-3600000)/1000.0)
