import json
from binance.client import Client
import config
import binance.exceptions
from datetime import date, timedelta

client = Client(config.apiKey, config.apiSecurity)
yesterday = date.today() - timedelta(days=1)
with open('./logs/'+yesterday.strftime("%Y-%m-%d")+'_data.json') as json_file:
    data = json.load(json_file)
    moneyToSellInCoin = data[0]
    moneyToSellInUSDT = data[1]
print("Going to sell (in coin)")
print(moneyToSellInCoin)
for coin, value in moneyToSellInCoin.items():
    try:
        print("Selling " + coin + " : " + str(value))
        order = client.order_market_sell(
            symbol=coin+'USDT',
            quantity=value)
    except binance.exceptions.BinanceAPIException as error:
        print(error.message)

balanceYesterday = 0
for coin, value in moneyToSellInUSDT.items():
    balanceYesterday += value
balance = client.get_asset_balance(asset='USDT')

print("Yesterday :" + str(balanceYesterday))
print("Today :" + str(balance['free']))
print("Variation :" +
      str((float(balance['free']) - float(balanceYesterday) / float(balanceYesterday)) * 100) + "%")
