from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from dotenv import load_dotenv, find_dotenv, dotenv_values

env_path = find_dotenv(".env")
key = dotenv_values(env_path)
API_KEY = key['API_KEY']


# Create your views here.
def home(request):
    return render(request, "news/home.html")


def search(request):
    search_keyword = request.GET["q"]
    params = {
        "apiKey": API_KEY,
        "q": search_keyword,
        "sortBy": "popularity",
        "pagesize": 20,
        "language": "en",
    }
    API_ENDPOINT = "https://newsapi.org/v2/everything"

    try:
        data = requests.get(API_ENDPOINT, params=params)
        news_collection = data.json()["articles"]

        return render(
            request,
            "news/search.html",
            {"news_collection": news_collection, "search_keyword": search_keyword},
        )
    except ConnectionError:
        error_page(request)


def search_by_category(request, category):
    API_KEY = "28072e2ae4e1448b96bc16d1300e475e"
    API_ENDPOINT = "https://newsapi.org/v2/top-headlines"
    category = category
    params = {"apiKey": API_KEY, "category": category}

    try:
        data = requests.get(API_ENDPOINT, params=params)
        news = data.json()["articles"]
        return render(
            request,
            "news/category.html",
            {"news_collection": news, "category": category},
        )
    except ConnectionError:
        error_page(request)


def error_page(request):
    return render(request, "news/error.html")
