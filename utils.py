import calculator
import config
from binance.client import Client

def print_bitcoin_addr(client):
    address = client.get_deposit_address(asset='BTC')
    print(address)


def print_balance(client):
    info = client.get_account()
    bal = info['balances']
    print("BALANCE AVALIABLE :")
    for b in bal:
        if float(b['free']) > 0:
            print(b)
    print("---------------------------\n")

def print_btcusdt(client):
    avg_price = client.get_avg_price(symbol='BTCUSDT')
    print(avg_price)


def print_top_for_100(limit):
    moneyToBuyInUSDT = calculator.get_top_moneyToBuyInUSDT(260, limit)
    print(moneyToBuyInUSDT)

def print_historical_trade(client):
    trades = client.get_historical_trades(symbol='BNBBTC')
    print(trades)


# from pathlib import Path

# print(filename)
# entries = Path(filename)
# for entry in entries.iterdir():
#     print(entry.name)
#  client = Client(config.apiKey, config.apiSecurity)
# print_historical_trade(client)