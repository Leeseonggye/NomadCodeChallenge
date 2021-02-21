import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = requests.get("https://www.iban.com/currency-codes")
indeed_soup =BeautifulSoup(url.text,"html.parser")

table_raw = list(indeed_soup.find_all('td'))


table_all = []
for value in table_raw:
  value = str(value)
  value = value[4:-5]
  table_all.append(value)

table_country =[]
table_currency =[]

for i in range(int(len(table_all)/4)):
    table_country.append(table_all[4*i])
    table_currency.append(table_all[4*i+1])

NoCurrencyIndex = []

for currency in table_currency:
    if currency == "No universal currency":
        NoCurrencyIndex.append(table_currency.index(currency))
        table_currency.remove(currency)

for value in NoCurrencyIndex:
  table_country.remove(table_country[value])

print("Hello! please choose select a country by number:")

for i, j in enumerate(table_country):
  print(f"# {i}", j)

while True:
  try:
    number = int(input("#: "))
    try:
      print(f"You choose {table_country[number]}")
      print(f"The currency code is {table_currency[number]}")
      break
    
    except:
      print("Choose a number from the list")         

  except ValueError:
    print("That wasn't a number.")