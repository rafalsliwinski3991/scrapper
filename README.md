# Requiments
- beautifulsoup4==4.7.1
- certifi==2019.3.9
- Django==2.2
- djangorestframework==3.9.2
- lxml==4.3.3
- requests==2.21.0

# Creating enviroment
Please run command below:

```ssh
pipenv install
```

# Development
To scrap exchange rates from ECB run:
```ssh
pipen run python manage.py scrapper_script
```
**URLS**:
- api/core/currency/
- api/core/currency/<int:pk>/
- api/core/exchangerate/
- api/core/exchangerate/<int:pk>/
