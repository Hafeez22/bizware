from . import views
from django.urls import path

urlpatterns = [
    path('', views.customerDashboard, name = "customer"),
    path('suppliers', views.supplier, name='suppliers')
]