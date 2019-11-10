import requests, bs4
res = requests.get('https://alternative.me/crypto/fear-and-greed-index/#fng-history')
res.raise_for_status()
fngSoup = bs4.BeautifulSoup(res.text, features = "lxml")
fngSearch = fngSoup.findAll('div', {"class": "fng-circle"})
line = fngSearch[0]
fng = line.getText()
print(fng)