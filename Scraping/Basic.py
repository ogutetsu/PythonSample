import requests
from bs4 import BeautifulSoup
import csv
import re

# wikipediaから今日は何の日を取得する

url = "https://ja.wikipedia.org"
response = requests.get(url)
sp = BeautifulSoup(response.content, "html.parser")
today = sp.find("div", attrs={"id": "on_this_day"}).text

today_list = []
entries = sp.find_all('li')
for i, entry in enumerate(entries):
    today_text = entry.get_text().replace("（","(").replace("）",")")
    match = re.search("\((.*?)年\)", today_text)
    if match:
        today_list.append([i + 1, entry.get_text(), match.group(1)])
    else:
        today_list.append([i+1, entry.get_text()])

with open("IOFiles/wiki_today.csv", "w", encoding="UTF8") as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerows(today_list)

