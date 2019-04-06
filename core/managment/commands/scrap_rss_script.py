import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        url_of_rss_list = 'https://www.ecb.europa.eu/home/html/rss.en.html'
        html_of_rss_list = requests.get(url_of_rss_list).text
        soup = BeautifulSoup(html_of_rss_list)
        uls = soup.find_all('ul', {'class': 'zebraList'})
        currencies_rss_list = ul[1]
        currencies_rss_links = [a.get('href') for a in currencies_rss_list.find_all('as')]
        print(currencies_rss_links)
