from binance.client import Client
import binance.exceptions
import config
import calculator
import json
import datetime
import os

dirname = os.path.dirname(__file__)
logdir = os.path.join(dirname, 'logs')

today = datetime.date.today()
client = Client(config.apiKey, config.apiSecurity)


balance = client.get_asset_balance(asset='USDT')
print("Balance dispinible : " + str(balance['free']) + "USDT")
moneyToBuyInUSDT = calculator.get_top_moneyToBuyInUSDT(
    float(balance['free']), config.strategyTop)
moneyBuyInCoin = calculator.get_empty_moneydict()
for coin, value in moneyToBuyInUSDT.items():
    try:
        info = client.get_symbol_info(coin+'USDT')
        valueWithPrecision = round(value, info['quoteAssetPrecision'])
        print("Buying " + coin + " : " +
              str(valueWithPrecision) + " USDT")
        order = client.order_market_buy(
            symbol=coin+'USDT', quoteOrderQty=valueWithPrecision)
        moneyBuyInCoin[coin] = order['origQty']
    except binance.exceptions.BinanceAPIException as error:
        print(error.message)

logs = [moneyBuyInCoin, moneyToBuyInUSDT]
with open(logdir+today.strftime("%Y-%m-%d")+'_data.json', 'w') as outfile:
    json.dump(logs, outfile)
