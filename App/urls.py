
from django.contrib import admin
from django.urls import path
from .views import InvoiceAPI,InvoiceDetailAPI

urlpatterns = [
    path('invoice/',InvoiceAPI.as_view() ),
    path('invoice_detail/',InvoiceDetailAPI.as_view()),
    
]
