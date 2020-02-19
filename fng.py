import requests, bs4
import csv
import datetime

date_x = datetime.datetime.now()
date = (date_x.strftime("%x"))

res = requests.get('https://alternative.me/crypto/fear-and-greed-index/#fng-history')
res.raise_for_status()

fngSoup = bs4.BeautifulSoup(res.text, features = "lxml")

csv_file = open('fng_data.csv', 'a')

csv_writer = csv.writer(csv_file)


fngSearch = fngSoup.findAll('div', {"class": "fng-circle"})

line = fngSearch[0]
fng = line.getText()

print(fng)

print()

csv_writer.writerow([date, fng])
