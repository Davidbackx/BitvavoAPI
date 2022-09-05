import sys
from urllib import response
sys.path.append('crypto_api_site/bitvavo_api')
from bitvavo_api import wallet
from bitvavo_api import dataset
from bitvavo_api.wallet import total_invested,current_value
from django.shortcuts import render
from bitvavo_api.bitvavovariables import bitvavo_api,bitvavo_secret_api
from .utils import get_plot
from .forms import RegisterForm
import numpy as np
import matplotlib.pyplot as plt
from django.http import HttpResponse

# Create your views here.
def home(response):
    return render(response,"main/home.html")
def overview(response):
    account_overview = wallet.account_overview
    params = {
    "coins":account_overview
    }
    return render(response,"main/overview.html",params)
def data(response):
    general_data = dataset.general_data
    timespan = dataset.timespan
    last = dataset.last_update
    params = {"coins":general_data, "timespan":timespan, "last_update":last}
    return render(response, "main/data.html",params)

def data_search(request):
    currency = request.GET.get("currency")
    timespan = dataset.timespan
    last = dataset.last_update
    general_data = dataset.overview_currency(currency)
    params = {"coins":general_data, "timespan":timespan, "last_update":last}
    return render(request, "main/data_currency.html",params)

def overviewpost(request):
    api_key = request.POST["api-key"]
    api_secret_key = request.POST["api-key-secret"]
    print(api_key)
    print(api_secret_key)
    account_overview = wallet.overview(api_key,api_secret_key)
    print(account_overview)
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