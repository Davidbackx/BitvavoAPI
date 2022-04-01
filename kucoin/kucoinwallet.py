from kucoin.client import Client
import sys
sys.path.append('../bitvavoapi')
from bitvavoapi.variables import kucoin_api,kucoin_secret_api,kucoin_passhprase
#from variables import kucoin_api,kucoin_secret_api,kucoin_passhprase
api_key = ""
api_secret = ""
api_passhrase = ""

client = Client(api_key,api_secret,passphrase=api_passhrase)
account_id = client.get_accounts()[0]['id']
def getCoinsSymbols():
    return client.get_account(account_id)['currency']+"-USDT"
def getCoins(): 
    balance = client.get_account(account_id)
    return {balance['currency']:balance['balance']}
def getBalanceFromCoin(coin):
    return client.get_ticker(coin)['price']
def getAccountBalance():
    coin_price = getBalanceFromCoin(getCoinsSymbols())
    coin_symbol = getCoinsSymbols()
    coin_symbol = coin_symbol.split('-')[0]
    coins = getCoins()
    coin_amount = coins[coin_symbol]
    return round(float(coin_amount)*float(coin_price),3)

print(getAccountBalance())