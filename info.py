from binance.client import Client
import binance.exceptions
import config
import calculator
import json
import datetime
from datetime import date, timedelta


today = datetime.date.today()
yesterday = date.today() - timedelta(days=1)
client = Client(config.apiKey, config.apiSecurity)

with open('./logs/'+yesterday.strftime("%Y-%m-%d")+'_data.json') as json_file:
    data = json.load(json_file)
    moneyToSellInCoin = data[0]
    moneyToSellInUSDT = data[1]
print("Info for coins :")
print(moneyToSellInCoin)
totalBefore = 0
totalAfter = 0
for coin, value in moneyToSellInUSDT.items():
    if value > 0:
        try:
            balance = client.get_asset_balance(asset=coin)
            avg_price = client.get_avg_price(symbol=coin+'USDT')
            owned = float(balance['free']) * float(avg_price['price'])
            totalBefore += value
            totalAfter += owned
            std = ((owned - value) / value) * 100
            print(coin + ' Buyed ' + str(round(value, 2)) + ' USDT is now ' +
                  str(round(owned, 2)) + ' USDT var : ' + str(round(std, 2)) + '%')
        except binance.exceptions.BinanceAPIException as error:
            print(error.message)
totalStd = ((totalAfter - totalBefore) / totalBefore) * 100
print("############################")
print('TOTAL Buyed ' + str(round(totalBefore, 2)) + ' USDT is now ' +
      str(round(totalAfter, 2)) + ' USDT var : ' + str(round(totalStd, 2)) + '%')
print("############################")
