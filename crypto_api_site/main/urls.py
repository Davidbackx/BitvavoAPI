import imp
from unicodedata import name
from django.urls import path
from main import views
urlpatterns = [
    path("",views.home,name="home"),
    path("overview/", views.overview, name="overview"),
    path("wallet/",views.wallet,name="wallet")
]