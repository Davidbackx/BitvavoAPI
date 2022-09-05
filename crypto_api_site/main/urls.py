from unicodedata import name
from django.urls import path
from main import views
urlpatterns = [
    path("",views.home,name="home"),
    path("charts/",views.barchart,name="barchart"),
    path("register/", views.register, name="register"),
    path("overview/", views.overview, name="overview"),
    path("data/",views.data, name="data"),
    path('data/search/',views.data_search),
    path("overview/user/", views.overviewpost, name="overviewpost")
]