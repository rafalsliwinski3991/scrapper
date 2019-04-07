from core.models import Currency, ExchangeRate
from rest_framework import serializers


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = (
            'id', 'name', 'symbol',
        )


class ExchangeRateSerializer(serializers.ModelSerializer):
    base_currency = CurrencySerializer(required=True)
    target_currency = CurrencySerializer(required=True)

    class Meta:
        model = ExchangeRate

        fields = (
            'id',  'rate', 'base_currency', 'target_currency', 'date',
        )
