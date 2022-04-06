from sqlite3 import paramstyle
from django.shortcuts import render
import sys

sys.path.append('crypto_api_site/bitvavo_api')
from bitvavo_api import bitvavowallet
from bitvavo_api.bitvavovariables import bitvavo_api,bitvavo_secret_api
from .utils import get_plot

# Create your views here.
def home(response):
    currencylist = bitvavowallet.currencylist
    params = {
        "title":"Home",
        "subtitle":"My crypto wallet visualized",
        "list": currencylist
    }
    return render(response,"main/home.html",params)
def wallet(request):    
    currencys = bitvavowallet.currencys
    coin = ([key for key,val in currencys.items()])
    value = ([val for key,val in currencys.items()])
    graph = get_plot(coin,value)
    params = {
        "graph": graph
    }
    return render(request,"main/home.html",params)
def overview(response):
    account_overview = bitvavowallet.account_overview
    params = {
        "coins":account_overview
    }
    return render(response,"main/overview.html",params)