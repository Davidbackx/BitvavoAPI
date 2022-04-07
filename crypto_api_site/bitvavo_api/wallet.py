from functools import total_ordering
from lib2to3.pygram import Symbols
from urllib import response
from matplotlib.pyplot import pink
from python_bitvavo_api.bitvavo import Bitvavo
#from bitvavovariables import bitvavo_api,bitvavo_secret_api

api_key = "30477b338507ae0f02edf1d363ad7b28cc2c6ec19934b393a0940fb9f9ff6151"
api_secret = '33ae1f6ad81423f557d8203a7305aa96d0da2a30c9d95765619ebfa5e41063dae4649eaa2ff811db19b407e7d85f12cc0546821677cebd316906e026abfba956'

def get_account_currencies(apiKey,apiSecretKey):
    bitvavo = Bitvavo({"apikey":apiKey,"apisecret":apiSecretKey})
    response = bitvavo.balance({})
    account_currencies = {}
    total = []
    account_coins = []
    for item in response:
        if item["symbol"] != "EUR":
            account_coins.append(item["symbol"]+"-EUR")
            account_currencies = {"symbol":item["symbol"]+"-EUR","total":round(float(item["available"]),3)}
            total.append(account_currencies)
    return total,account_coins
def get_total_value_per_currency(apiKey,apiSecretKey):
    total,_ = get_account_currencies(apiKey,apiSecretKey)
    total_value = []
    for item in total:
        total_value.append({"symbol":item["symbol"],"total_value":round(float(item["total"])*float(get_current_val_per_currency(item["symbol"])),3)})
    return total_value
def get_vwap_of_currency_for_account_currencies(apiKey,apiSecretKey):
    bitvavo = Bitvavo()
    response = bitvavo.ticker24h({})
    _,symbols = get_account_currencies(apiKey,apiSecretKey)
    typical_price :float = 0.0
    vwap :float = 0.0
    account_vwap = {}
    total = []
    for order in response:
        if order["market"] in symbols:
            typical_price = (float(order["high"])+float(order["low"])+float(order["last"]))/3
            vwap = (typical_price * float(order["volume"]))/float(order["volume"])
            account_vwap = {"market":order["market"],"VWAP":round(vwap,3)}
            total.append(account_vwap)
    return total
def get_current_val_per_currency(currency):
    bitvavo = Bitvavo()
    response = bitvavo.tickerPrice({})
    for market in response:
        if market["market"] == currency:
            return market["price"]
def get_current_value_for_account_currencies(apiKey,apiSecretKey):
    bitvavo = Bitvavo()
    response = bitvavo.tickerPrice({})
    _,symbols = get_account_currencies(apiKey,apiSecretKey)
    current_value = {}
    total = []
    for market in response:
        if market["market"] in symbols:
            current_value = {"market":market["market"],"current_price":round(float(market["price"]),3)}
            total.append(current_value)
    return total
def get_all_trades(apiKey,apiSecretKey):
    bitvavo = Bitvavo({"apikey":apiKey,"apisecret":apiSecretKey})
    _,symbols = get_account_currencies(apiKey,apiSecretKey)
    trades = []
    trade ={}
    for currency in symbols:
        for item in bitvavo.trades(currency, {}):
            trade = {
                "market":item["market"],
                "amount":item["amount"],
                "price":item["price"],
                "timestamp":item["timestamp"]
            }
            trades.append(trade)
    return trades
def get_deposits(apiKey,apiSecretKey):
    bitvavo = Bitvavo({"apikey":apiKey,"apisecret":apiSecretKey})
    response = bitvavo.depositHistory({})
    total_deposited = ([int(deposit["amount"]) for deposit in response])
    total_deposited_sum = sum(total_deposited)

def get_overview(apiKey,apiSecretKey):
    
    overview_account = []
    total,symbols = get_account_currencies(apiKey,apiSecretKey)

    for currency in symbols:
        overview = {
        "currency":currency,
        "current_price":float,
        "total_invested":float,
        "total_value":float,
        "VWAP":float,
        "is_profitable_purchase":bool
        }
        overview["current_price"] = get_current_val_per_currency(currency)
        for item in total:
            if item["symbol"] == currency:
                overview["currency"] = item["symbol"]
                overview["total_invested"] = item["total"]
        for item in get_vwap_of_currency_for_account_currencies(apiKey,apiSecretKey):
            if item["market"] == currency:
                overview["VWAP"] = item["VWAP"]
                overview["is_profitable_purchase"] = float(overview["VWAP"]) > float(overview["current_price"])
        for item in get_total_value_per_currency(apiKey,apiSecretKey):
            if item["symbol"] == currency:
                overview["total_value"] = item["total_value"]
        overview_account.append(overview)
    return overview_account
_,currencylist = get_account_currencies(api_key,api_secret)
account_overview = get_overview(api_key,api_secret)