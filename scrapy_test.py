from bs4 import BeautifulSoup
import requests
import csv



filename = "dataset-frases.csv"

f = open(filename, "w", encoding='utf-8')

headers = "autor|frase\n"
f.write(headers)    


for i in range(10):
    source = requests.get('https://www.pensador.com/frases_inteligentes/{}'.format(i)).text

    soup = BeautifulSoup(source, 'lxml')

    for content in soup.find_all('div', class_='thought-card'):
        #print('{}|{}'.format(content.p.text, content.span.text))
        line = '{0}|{1}\n'.format(content.p.text.strip(), content.span.text.strip())
        print(line)
        f.write(line)



f.close()

#print(soup.prettify())