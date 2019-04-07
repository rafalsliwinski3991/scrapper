from api.serializers import CurrencySerializer, ExchangeRateSerializer
from django.shortcuts import render
from core.models import Currency, ExchangeRate
from rest_framework.generics import ListAPIView, RetrieveAPIView

# queryset = User.objects.all()
# serializer_class = UserSerializer


class CurrencyListAPIView(ListAPIView):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()


class CurrencyRetrieveAPIView(RetrieveAPIView):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()


class ExchangeRateListAPIView(ListAPIView):
    serializer_class = ExchangeRateSerializer
    queryset = ExchangeRate.objects.all()


class ExchangeRateRetrieveAPIView(RetrieveAPIView):
    serializer_class = ExchangeRateSerializer
    queryset = ExchangeRate.objects.all()
