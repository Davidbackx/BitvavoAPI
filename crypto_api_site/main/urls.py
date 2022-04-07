from unicodedata import name
from django.urls import path
from main import views
urlpatterns = [
    path("",views.home,name="home"),
    path("register/", views.register, name="register"),
    path("overview/", views.overview, name="overview")
]