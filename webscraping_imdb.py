import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.imdb.com/chart/top?ref_=nv_mv_250")

soup = BeautifulSoup(result.content, 'lxml')

trs = soup.findAll('table')[0].findAll('tr')

filename = "dataset-filmes.csv"
f = open(filename, "w", encoding='utf-8')
headers = "RANK|NOME_FILME|NOTA|IMAGEM\n"
f.write(headers)  

rank = 1
for tr in trs:
    if (len(tr.findAll('td')) > 3):
        #print(tr.findAll('td')[0].img['src'])
        #print(tr.findAll('td')[1].a.text)
        #print(tr.findAll('td')[2].strong.text)
        f.write("{}|{}|{}|{}\n".format(rank, tr.findAll('td')[1].a.text, tr.findAll('td')[2].strong.text, tr.findAll('td')[0].img['src']))
        rank += 1

f.close()