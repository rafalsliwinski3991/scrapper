from api.views import CurrencyListAPIView, CurrencyRetrieveAPIView, ExchangeRateListAPIView, ExchangeRateRetrieveAPIView
from django.urls import path

urlpatterns = [
    path('core/currency/', CurrencyListAPIView.as_view(), name='currency_list'),
    path('core/currency/<int:pk>/', CurrencyRetrieveAPIView.as_view(), name='currency_detail'),
    path('core/exchangerate/', ExchangeRateListAPIView.as_view(), name='exchangerate_list'),
    path('core/exchangerate/<int:pk>/', ExchangeRateRetrieveAPIView.as_view(), name='exchangerate_detail'),
]
