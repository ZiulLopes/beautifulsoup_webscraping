import requests
from bs4 import BeautifulSoup

result = requests.get("https://registroponto.com.br")

#print(result.status_code)
#print(result.headers)

soup = BeautifulSoup(result.content, 'lxml')

'''
links = soup.find_all("a")

for link in links:
    if (len(link.text) > 0):
        print(link.text)
'''

divs = soup.find_all("div", class_="inside")

for div in divs:
    if (div.h1 != None):
        print(div.h1.text)
        print(div.p.text.strip() + "\n")


imgs = soup.find_all("img")

for img in imgs:
    print(img)
    print(img.attrs["src"])