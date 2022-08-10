import sys
from urllib import response
sys.path.append('crypto_api_site/bitvavo_api')
from bitvavo_api import wallet
from bitvavo_api.wallet import total_invested,current_value
from django.shortcuts import render
from bitvavo_api.bitvavovariables import bitvavo_api,bitvavo_secret_api
from .utils import get_plot
from .forms import RegisterForm
import numpy as np
import matplotlib.pyplot as plt

# Create your views here.
def home(response):
    return render(response,"main/home.html")
def overview(response):
    account_overview = wallet.account_overview
    params = {
    "coins":account_overview
    }
    return render(response,"main/overview.html",params)
def overviewpost(request):
    api_key = request.POST["api-key"]
    api_secret_key = request.POST["api-key-secret"]
    account_overview = wallet.get_account_currencies(api_key,api_secret_key)
    params = {
    "coins":account_overview
    }
    return render(request,"main/overview.html",params)
def register(response):
    form = RegisterForm()
    return render(response,"main/register.html",{"form":form})
def barchart(response):
    coin = ([item["symbol"] for item in total_invested])
    value = ([item["total"] for item in total_invested])
    currentval = ([item["total_value"] for item in current_value])
    color = [] 
    for i in range(len(coin)):
        if value[i] > currentval[i]:
            color.append("RED")
        elif value[i] == currentval[i]:
            color.append = "ORANGE"
        else:
            color.append("GREEN")
    X = np.arange(len(coin))
    width = 0.35
    fig,ax = plt.subplots()
    rects1 = ax.bar(X-width/2,value,width)
    rects2 = ax.bar(X+width/2,currentval,width,color=color)
    ax.set_xlabel("coins")
    ax.set_ylabel("value")
    ax.set_title("total invested and currentval per coin")
    ax.set_xticks(X,coin)
    ax.legend()
    ax.bar_label(rects1,padding=0.35)
    ax.bar_label(rects2,padding=0.35)
    fig.tight_layout()
    plt.savefig('main/static/main/barchart.png')
    return render(response,'main/charts.html')