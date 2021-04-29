from binance.client import Client
import config
import calculator
import json
import datetime

today = datetime.date.today()
client = Client(config.apiKey, config.apiSecurity)


balance = client.get_asset_balance(asset='USDT')
print("Balance dispinible : " + str(balance['free']))
moneyToBuyInUSDT = calculator.get_top_moneyToBuyInUSDT(
    float(balance['free']), config.strategyTop)
moneyBuyInCoin = calculator.get_empty_moneydict()
for coin, value in moneyToBuyInUSDT.items():
    print("Achat de " + coin + " : " + str(value))
    order = client.order_market_buy(
        symbol=coin+'USDT', quoteOrderQty=value)
    moneyBuyInCoin[coin] = order['origQty']

logs = [moneyBuyInCoin, moneyToBuyInUSDT]
with open('./logs/'+today.strftime("%Y-%m-%d")+'_data.json', 'w') as outfile:
    json.dump(logs, outfile)
