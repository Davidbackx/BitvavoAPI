from django.urls import path
from main import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("",views.home,name="home"),
    path("charts/",views.charts_view,name="charts_view"),
    path("overview/", views.overview, name="overview"),
    path("data/",views.data, name="data"),
    path('data/search/',views.data_search),
    path('charts/line/', views.line_search),
    path("overview/user/", views.overviewpost, name="overviewpost")
]

urlpatterns += staticfiles_urlpatterns()