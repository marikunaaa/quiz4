import requests
import sqlite3
from bs4 import BeautifulSoup
import csv

numb = 1
url = f"https://veli.store/category/teqnika/mobilurebi-aqsesuarebi/mobiluri-telefonebi/60/?page={numb}"
database= "C:\\Users\\lukee\\OneDrive\\Desktop\\Python masalebi\\Databases\\Samplee.sqlite"

result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')
telefonebi = soup.find('div', class_='styled__ProductView-sc-183mmht-28 inZYkn')
yvela_telefoni = telefonebi.find_all("div", class_="styled__CardWrapper-sc-1gjp82p-0 eknzBd")

informacia = []

for telefoni in yvela_telefoni:
    fasi = telefoni.find('div', class_="info").span.text
    saxeli = telefoni.find('div', class_="info").find("span", class_="title").text
    # print(f"ტელეფონის ფასია - {fasi}  ||  "
    #       f"ტელეფონის მოდელია - {saxeli} ")

    informacia.append((saxeli, fasi))


with open("Phones.csv", "w", encoding="utf-8") as file:
    f = csv.writer(file)
    for i in informacia:
        f.writerow([i[0], i[1]])

    file.close()














