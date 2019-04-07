from django.db import models


class Currency(models.Model):
    symbol = models.CharField(max_length=3)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.symbol

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'


class ExchangeRate(models.Model):
    rate = models.DecimalField(max_digits=12, decimal_places=6)
    base_currency = models.ForeignKey(Currency, related_name='base_currencies', on_delete=models.CASCADE)
    target_currency = models.ForeignKey(Currency, related_name='target_currencies', on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return '{0} {1} - {2}, {3}'.format(
            self.base_currency,
            self.target_currency,
            self.date,
            self.rate
        )


    class Meta:
        unique_together = ('base_currency', 'target_currency', 'date')
        verbose_name = 'ExchangeRate'
        verbose_name_plural = 'ExchangeRates'
