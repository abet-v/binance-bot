import calculator


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


def print_top3_for_100():
    moneyToBuyInUSDT = calculator.get_top_moneyToBuyInUSDT(100, 5)
    print(moneyToBuyInUSDT)


print_top3_for_100()
