from datetime import datetime
import requests
import json
import csv
import pandas as pd
from pandas import DataFrame
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

url = "https://open-api.bybt.com/api/pro/v1/futures/funding_rates"
payload = {}
headers = {
	'bybtSecret': '2b789c432da5437f8b97a3484d53d196'
}

# Tickers
tickers = {
    "btc": {"symbol": "btc"},
    "eth": {"symbol": "eth"},
    "ltc": {"symbol": "ltc"},
    "trx": {"symbol": "trx"},
    "bch": {"symbol": "bch"},
    "eos": {"symbol": "eos"},
    "etc": {"symbol": "etc"},
    "xrp": {"symbol": "xrp"},
    "link": {"symbol": "link"},
    "xlm": {"symbol": "xlm"},
    "ada": {"symbol": "ada"},
    "zec": {"symbol": "zec"},
    "dash": {"symbol": "dash"},
    "xtz": {"symbol": "xtz"},
    "bnb": {"symbol": "bnb"},
    "atom": {"symbol": "atom"},
    "neo": {"symbol": "neo"},
    "theta": {"symbol": "theta"},
    "algo": {"symbol": "algo"},
    "knc": {"symbol": "knc"},
    "omg": {"symbol": "omg"},
    "bal": {"symbol": "bal"},    
    "comp": {"symbol": "comp"},
    "dot": {"symbol": "dot"},
    "aave": {"symbol": "aave"},
    "snx": {"symbol": "snx"},
    "doge": {"symbol": "doge"},
    "waves": {"symbol": "waves"},
    "yfi": {"symbol": "yfi"},
    "sushi": {"symbol": "sushi"},
    "uni": {"symbol": "uni"},
    "band": {"symbol": "band"},
    "crv": {"symbol": "crv"},
    "rune": {"symbol": "rune"},
    "fil": {"symbol": "fil"},
}

exchanges = [
    "Huobi",
    "Binance",
    "Okex",
    "Gate",
    "FTX",
    "Bybit",
    "Deribit",
    "Bitmex",
]

def check_for_coin(df, exchange, element, value):
    try:
        return df[exchange][element][value]
    except KeyError:
        return None


def funding_refresh(ticker):
    response = requests.get(url, headers=headers, data=payload, params=ticker)
    if response.status_code != 200:
        print("oh no... failed to get 200", response.status_code)
        return

    json_dataset = response.json()
    df = DataFrame(json_dataset["data"])

    total_funding = 0
    number_of_exchanges = 0

    for exchange in exchanges:
        funding = check_for_coin(df, exchange, 0, "rate")
        if funding is not None:
            total_funding += funding
            number_of_exchanges += 1

    if number_of_exchanges > 0:
    	average_funding = total_funding / number_of_exchanges
    else: average_funding = None
    return average_funding

now = datetime.now()
dt_string = now.strftime("%m/%d   %H:%M")
print("date and time =", dt_string)

csv_headers = ["Date/time"]
values = [dt_string]
#ticker_list = []

for symbol, param in tickers.items():
    ticker_id = param["symbol"].upper()
    #csv_headers.append(ticker_id)
    average_funding = funding_refresh(param)
    values.append(average_funding)
    #ticker_list.append(ticker_id)
    print(ticker_id, "    ", average_funding)

with open("february_funding_data.csv", "a", newline="") as f:
    csv_writer = csv.writer(f, delimiter=",")
    #csv_writer.writerow(csv_headers)
    csv_writer.writerow(values)

