from python_bitvavo_api.bitvavo import Bitvavo
import math
from datetime import datetime
#from bitvavovariables import bitvavo_api,bitvavo_secret_api
api_key = '30477b338507ae0f02edf1d363ad7b28cc2c6ec19934b393a0940fb9f9ff6151'
api_secret_key ='33ae1f6ad81423f557d8203a7305aa96d0da2a30c9d95765619ebfa5e41063dae4649eaa2ff811db19b407e7d85f12cc0546821677cebd316906e026abfba956'

def init_account(apiKey,apiSecretKey):
    return Bitvavo({"apikey":apiKey,"apisecret":apiSecretKey})

bitvavo = Bitvavo()
response = bitvavo.tickerPrice({})
assets = bitvavo.assets({})
bitvavoWithKey = init_account(api_key,api_secret_key)
pricesLatest24h = bitvavo.ticker24h({})
balance = bitvavoWithKey.balance({})
depositHistory = bitvavoWithKey.depositHistory({})



def get_current_value_from_currency(currency):
    if "-EUR" not in currency:
        currency = currency+"-EUR"
    for order in pricesLatest24h:
        if order['market'] == currency:
            return order['last']
        
def get_account_currencys(apiKey,apiSecretKey): #['ADA', 'NANO', 'RSR', 'VET', 'XRP']
    bitvavo = Bitvavo({"apikey":apiKey,"apisecret":apiSecretKey})
    response = balance
    abrevs =list()
    for item in response:
        abrevs.append(item["symbol"])
    abrevs.pop(0)
    return [item for item in abrevs]
def get_total_account_balance(apiKey,apiSecretKey): #710.7
    bitvavo = Bitvavo({"apikey":apiKey,"apisecret":apiSecretKey})
    response = balance
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
    response = balance
    return {item["symbol"]:item["available"] for item in response if item["symbol"] != "EUR" }

    
def get_total_account_deposits_in_eur(apiKey,apiSecretKey): #700
    response = depositHistory
    totalAmount = 0
    for item in response:
        totalAmount += int(item['amount'])
    return (totalAmount) 



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

#1 Jan 1970 for timestamps
def get_all_orders(apiKey,apiSecretKey):
    bitvavo = Bitvavo({"apikey":apiKey,"apisecret":apiSecretKey})
    orders = []   
    for currency in get_account_currencys(apiKey,apiSecretKey):
        currency = currency+"-EUR"
        response = bitvavo.getOrders(currency, {})
        for item in response:
            order = {
                "market":"",
                "amount":0,
                "price":0,
                "timestamp":0
            } 
            order["market"]=(item["market"])
            order["amount"]=(item["filledAmount"])
            order["price"]=(item["fills"][0]["price"])
            order["timestamp"] = unixtimestamp_to_date(item["fills"][0]["timestamp"])
            orders.append(order)
    return orders
def get_orders_currency(apiKey,apiSecretKey,currency):
    all_orders = get_all_orders(apiKey,apiSecretKey)
    orders = []
    for item in all_orders:
        order = {
            "market":"",
            "amount":0,
            "price":0,
            "timestamp":0
        }
        if item["market"] == currency:
            order["market"] = currency
            order["amount"] = item["amount"]
            order["price"] = item["price"]
            order["timestamp"] = item["timestamp"]
            orders.append(order)
    return orders
def unixtimestamp_to_date(timestamp):
    return str(datetime.fromtimestamp(timestamp/1000.0).date())

def average_price_per_currency(apiKey,apiSecretKey,currency):
    if "-EUR" not in currency:
        currency = currency+"-EUR"
    all_orders = get_all_orders(apiKey,apiSecretKey)
    average_price : float = 0
    total_orders_of_that_currency = 0
    for order in all_orders:
        if order["market"] == currency:
            total_orders_of_that_currency += 1
            average_price += float(order["price"])
    return average_price/total_orders_of_that_currency
def is_profitable_purchase(apiKey,apiSecretKey,currency):
    if "-EUR" not in currency:
        currency = currency+"-EUR"
    current_price = get_current_value_from_currency(currency)
    average_price = average_price_per_currency(apiKey,apiSecretKey,currency)
    if float(current_price) < float(average_price):
        return True
    else:
        return False
def get_vwap_of_currency(currency):
    if "-EUR" not in currency:
        currency = currency+"-EUR"
    typical_price :float = 0
    vwap :float = 0
    for order in pricesLatest24h:
        if order["market"] == currency:
            typical_price = (float(order["high"])+float(order["low"])+float(order["last"]))/3
            vwap = (typical_price * float(order["volume"]))/float(order["volume"])
    return round(vwap,3)
def is_profitable_purchase_vwap(currency):
    current_price = get_current_value_from_currency(currency)
    vwap = get_vwap_of_currency(currency)
    if float(current_price) < float(vwap):
        return True
    else:
        return False
def overview(apiKey,apiSecretKey,currency):
    if "-EUR" not in currency:
        currency = currency+"-EUR"
    current_price = get_current_value_from_currency(currency)
    average_price = average_price_per_currency(apiKey,apiSecretKey,currency)
    vwap = get_vwap_of_currency(currency)
    total_invested = get_totalinvested_per_currency(apiKey,apiSecretKey)
    profitable_average : bool = is_profitable_purchase(apiKey,apiSecretKey,currency)
    profitable_vwap : bool = is_profitable_purchase_vwap(currency)   
    current_value = get_all_currency_with_current_value(apiKey,apiSecretKey)
    total_invested_in_currency = 0
    current_value_in_currency = 0
    for item in total_invested.items():
        currency_in_item = item[0]+"-EUR"
        if currency_in_item == currency:
            total_invested_in_currency = item[1]
    for item in current_value.items():    
        currency_in_item = item[0]+"-EUR"
        if currency_in_item == currency:
            current_value_in_currency = item[1]
    return {"currency":currency,"current_price":current_price,"total_invested":total_invested_in_currency,"current_value":round(current_value_in_currency,3),"average_price":round(average_price,3),"vwap":round(vwap,3),"profitable_average":profitable_average,"profitable_vwap":profitable_vwap}
def get_overview_all_coins(apiKey,apiSecretKey):
    all_coins = get_account_currencys(apiKey,apiSecretKey)
    overview_all_coins = []
    for coin in all_coins:
        coin = coin+"-EUR"
        overview_all_coins.append(overview(apiKey,apiSecretKey,coin))
    return overview_all_coins
currencys = get_totalinvested_per_currency(api_key,api_secret_key)
# currencylist = get_account_currencys(api_key,api_secret_key)
# account_overview = get_overview_all_coins(api_key,api_secret_key)
print(currencys)