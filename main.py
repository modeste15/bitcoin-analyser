import requests
import json
from config import API_KEY

url = "https://rest.coinapi.io/v1/exchangerate/BTC/USD"

payload={}
headers = {'X-CoinAPI-Key': API_KEY}

response = requests.request("GET", url, headers=headers)

data = json.loads(response.text)

print(data)
