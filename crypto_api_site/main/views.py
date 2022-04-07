import sys
sys.path.append('crypto_api_site/bitvavo_api')
from bitvavo_api import wallet
from django.shortcuts import render
from bitvavo_api.bitvavovariables import bitvavo_api,bitvavo_secret_api
from .utils import get_plot
from .forms import RegisterForm

# Create your views here.
def home(response):
    return render(response,"main/home.html")
# def wallet(request):    
#     currencys = wallet.currencys
#     coin = ([key for key,val in currencys.items()])
#     value = ([val for key,val in currencys.items()])
#     graph = get_plot(coin,value)
#     params = {
#         "graph": graph
#     }
#     return render(request,"main/home.html",params)
def overview(response):
    account_overview = wallet.account_overview
    params = {
        "coins":account_overview
    }
    return render(response,"main/overview.html",params)
def register(response):
    form = RegisterForm()
    return render(response,"main/register.html",{"form":form})