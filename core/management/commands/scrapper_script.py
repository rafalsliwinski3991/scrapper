import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from core.models import Currency, ExchangeRate


class Command(BaseCommand):

    def handle(self, *args, **options):
        ecb_domain = 'https://www.ecb.europa.eu'
        url_of_rss_list = '{}/home/html/rss.en.html'.format(ecb_domain)
        html_of_rss_list = requests.get(url_of_rss_list).text

        soup = BeautifulSoup(html_of_rss_list, features='html.parser')
        uls = soup.find_all('ul', {'class': 'zebraList'})
        currencies_rss_list = uls[1]
        currencies_rss_links = [a.get('href') for a in currencies_rss_list.find_all('a')]

        for link in currencies_rss_links:
            url = '{}{}'.format(ecb_domain, link)


            break
