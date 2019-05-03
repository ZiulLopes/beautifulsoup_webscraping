from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.clickbus.com.br/onibus/curitiba-pr/sao-paulo-sp-todos?departureDate=2019-05-03&returnDate=2019-05-06")

soup = BeautifulSoup(html.content, 'lxml')

divs = soup.find_all("div", {"class": "search-item search-item-direct available-red reference-price promo"})

for div in divs:
    company = div.find("div", {"class": "company"})
    saida = div.find("div", {"class": "hour"})
    embarquedesembarque = div.find("div", {"class": "bus-stations"})
    duracao = div.find("div", {"class": "duration"})
    preco = div.find("div", {"class": "price"})
    
    #print(embarquedesembarque.span)

    print("Empresa: {} | Saida: {} | Embarque/Desembarque: {} | Durção: {} | Preço: {} ".format(company["data-name"], saida.time["data-time"], embarquedesembarque.span.text, duracao.time.text, preco["data-price"]))