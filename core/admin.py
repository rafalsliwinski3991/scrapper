from django.contrib import admin
from core.models import Currency, ExchangeRate


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass


@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    pass
