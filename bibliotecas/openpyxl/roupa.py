import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url='https://misshesse.store/collections/eterna-elegancia'
response=requests.get(url)

titulo_lista=[]
preco_lista=[]

print(response)

if response.status_code==200:

    site=BeautifulSoup(response.text, 'html.parser')
    produtos=site.find_all('li', attrs={'class':'grid__item'})

    for produto in produtos:
        titulos = produto.find('h3',attrs={'class':'card__heading'}).find('a',attrs={'class':'full-unstyled-link'})
        titulo_lista.append(titulos.get_text(strip=True))
        print(titulos.get_text(strip=True))

        precos = produto.find_all('span',attrs={'class':'price-item--regular'})
        for preco in precos:
            preco_lista.append(preco.get_text(strip=True))
            print(preco.get_text(strip=True))

else:
    print('erro')


workbook=Workbook()
sheet=workbook.active

sheet.append(['titulo','preco'])

for titulo,preco in zip(titulo_lista,preco_lista):
    sheet.append([titulo,preco])

workbook.save('produtos_precos.xlsx')