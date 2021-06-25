import requests
from bs4 import BeautifulSoup
import json


def search_animes(name):
    response_html = requests.get(f'https://gogoanime2.org/search/{name}').text
    soup = BeautifulSoup(response_html, 'lxml')
    items = soup.find('ul', {'class': 'items'}).find_all('li')
    results = []
    for i in items:
        result = {
            'title': i.a['title'],
            'anime-id': i.a['href'][7:],
            'image': 'https://gogoanime2.org/'+i.img['src']
        }
        results.append(result)
        # returns a json string
    return json.dumps(results)
