import requests
import json

API_KEY = "28072e2ae4e1448b96bc16d1300e475e"
API_ENDPOINT = "https://newsapi.org/v2/everything"

search_keyword = "Sony"
params = {
    "apiKey": API_KEY,
    "q": search_keyword,
    "sortBy": "popularity",
    "pagesize": 20,
}

data =  requests.get(API_ENDPOINT, params=params)
news = data.json()['articles']
for item in news:
    print(item['urlToImage'])
    print(item['title'])
    print(item['source']['name'])
    print(item['description'])
    print(item['author'])
    print(item['date'])
