#module to get price of a BTC of the last 5 years every 4 hours


import requests
import json

def get_data():
    url = "https://api.coindesk.com/v1/bpi/historical/close.json?start=2013-09-01&end=2018-09-01&currency=USD"
    response = requests.get(url)
    data = response.json()
    return data
