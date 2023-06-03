import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

file = open("Football Greatest moments.csv", "w", newline="\n")
csv_obj = csv.writer(file)
pages = 1

while pages <= 10:
    url = ("https://www.fourfourtwo.com/features/ranked-the-100-best-football-players-of-all-time/"+str(pages))
    h = {"Accept-Language": "en-US"}
    response = requests.get(url, headers=h)
    content = response.text
    soup = BeautifulSoup(content, "html.parser")
    info = soup.find("div", class_="text-copy")
    all_info = info.find_all("h2")
    for i in all_info:
        rank_and_name = i.text
        csv_obj.writerow([rank_and_name ])
    pages+=1
    sleep(randint(1, 5))
print(response)