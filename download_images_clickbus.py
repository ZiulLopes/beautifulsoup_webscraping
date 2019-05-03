from bs4 import BeautifulSoup
import requests
import os
import shutil

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

html = requests.get("https://www.clickbus.com.br/onibus/curitiba-pr/sao-paulo-sp-todos?departureDate=2019-05-03&returnDate=2019-05-06")

soup = BeautifulSoup(html.content, 'lxml')

divs = soup.find_all("div", {"class": "search-result-item valign-wrapper"})

for div in divs:
    for info in div.find_all("div"):
        if info.img != None:
            print(info.img["src"])
            response = requests.get(info.img["src"])
            if (response.status_code == 200):
                path = "{0}".format(os.path.join(THIS_FOLDER, info.img["src"].split('/')[-1]))
                print(path)
                with open(path, 'wb') as f:
                    f.write(response.content)