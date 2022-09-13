import sys
from urllib import response
sys.path.append('crypto_api_site/bitvavo_api')
from bitvavo_api import wallet
from bitvavo_api import charts
from bitvavo_api import dataset
from django.shortcuts import render
from bitvavo_api.bitvavovariables import bitvavo_api,bitvavo_secret_api
from .utils import get_plot
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
    account_overview = wallet.overview(api_key,api_secret_key)
    params = {
    "coins":account_overview
    }
    return render(request,"main/overview.html",params)

def charts_view(response):
    # save barchart
    charts.val_and_current_val_per_coin()
    return render(response,'main/charts.html')