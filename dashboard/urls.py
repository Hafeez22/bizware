from . import views
from django.urls import path

urlpatterns = [
    path('', views.mainDashboard, name = "Dashboard"),
    path('products', views.product, name = 'products')
]