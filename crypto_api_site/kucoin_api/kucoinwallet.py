from kucoin.client import Client
from kucoinvariables import kucoin_api,kucoin_secret_api,kucoin_passhprase
api_key = kucoin_api
api_secret = kucoin_secret_api
api_passhrase = kucoin_passhprase

client  = Client(api_key,api_secret,passphrase=api_passhrase)
account_id = client.get_accounts()[0]['id']

def getCoinsSymbols() :
    return client.get_account(account_id)['currency']+"-USDT"
def getCoins(): 
    balance = client.get_account(account_id)
    return {balance['currency']:balance['balance']}
def getBalanceFromCoin(coin):
    return client.get_ticker(coin)['price']
def getAccountBalance():
    account = {}
    coin_price = getBalanceFromCoin(getCoinsSymbols())
    coin_symbol = getCoinsSymbols()
    coin_symbol = coin_symbol.split('-')[0]
    coins = getCoins()
    coin_amount = coins[coin_symbol]
    coin_balance = float(coin_amount)*float(coin_price)
    account[coin_symbol] = coin_balance
    return account
account_balance = getAccountBalance()

