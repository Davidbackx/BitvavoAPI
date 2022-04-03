import imp
from django.urls import path
from main import views
import sys
sys.path.append('crypto_api_site/bitvavo_api/')
urlpatterns = [
    path("",views.home,name="home"),
    path("wallet/",views.wallet,name="wallet")
]