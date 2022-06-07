import requests
from bs4 import BeautifulSoup
import csv

with open("index.html", encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

all_products_hrefs = soup.find_all(class_="catalog_item_content_body")
# print(all_products_hrefs)

for item in all_products_hrefs:
    item_text = item.find("p").text
    price = item.find("span", class_="new_price").text
    item_href = "https://ekb.manaraga.ru" + item.find("p").find("a").get("href")

#     print(item_text, "===", price, "===", item_href)
    with open("catalog.csv", "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                item_text,
                price,
                item_href
            ]

        )