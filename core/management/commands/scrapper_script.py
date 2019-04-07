import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from core.models import Currency, ExchangeRate


class Command(BaseCommand):

    def handle(self, *args, **options):
        ecb_domain = 'https://www.ecb.europa.eu'
        url_of_rss_list = '{}/home/html/rss.en.html'.format(ecb_domain)
        html_of_rss_list = requests.get(url_of_rss_list).text

        soup = BeautifulSoup(html_of_rss_list, features='lxml')
        uls = soup.find_all('ul', {'class': 'zebraList'})
        currencies_rss_list = uls[1]
        currencies_rss_links = [a.get('href') for a in currencies_rss_list.find_all('a')]

        for link in currencies_rss_links:
            url = '{}{}'.format(ecb_domain, link)
            currency_content = requests.get(url).text
            currency_soup = BeautifulSoup(currency_content, features='html.parser')
            main_title = currency_soup.find('title').string
            main_title_list = main_title.split(' (')
            target_currency_name = main_title_list[0].split(' | ')[1]
            base_currency_name = main_title_list[1].split('- ')[1].split(' foreign')[0]

            items = currency_soup.find_all('item')
            for item in items:
                rate_date = item.find('dc:date').string

                exchange_rate = item.find('cb:statistics').find('cb:exchangerate')
                rate_value = exchange_rate.find('cb:value').string
                target_currency_symbol = exchange_rate.find('cb:targetcurrency').string
                base_currency_symbol = exchange_rate.find('cb:basecurrency').string

                base_currency, base_currency_created = Currency.objects.get_or_create(
                    symbol=base_currency_symbol,
                    name=base_currency_name
                )
                target_currency, target_currency_created = Currency.objects.get_or_create(
                    symbol=target_currency_symbol,
                    name=target_currency_name
                )
                exchange_rate, exchange_rate_created = ExchangeRate.objects.get_or_create(
                    rate=rate_value,
                    base_currency=base_currency,
                    target_currency=target_currency,
                    date=rate_date,
                )
