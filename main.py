from bs4 import BeautifulSoup
import requests

url = 'https://ekb.manaraga.ru/search?text=%D0%BA%D1%80%D0%BE%D0%BD%D0%B8%D0%B4%D0%BE%D0%B2'

req = requests.get(url)
src = req.text

with open ("index.html", "w", encoding='utf-8') as file:
    file.write(src)
