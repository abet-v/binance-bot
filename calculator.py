from scraper import nm_one, nm_two, nm_tree, nm_four, all_unique_coin
from itertools import islice

# OLD VERSION FOR TOP 5


def get_moneyToBuyInUSDT(balance):
    moneyToBuyInUSDT = {}
    for coin in all_unique_coin:
        moneyToBuyInUSDT[coin] = 0.00
    for coin in nm_one:
        moneyToBuyInUSDT[coin] += (3 * balance / 100)
    for coin in nm_two:
        moneyToBuyInUSDT[coin] += (11 * balance / 100)
    for coin in nm_tree:
        moneyToBuyInUSDT[coin] += (3 * balance / 100)
    for coin in nm_four:
        moneyToBuyInUSDT[coin] += (3 * balance / 100)
    return moneyToBuyInUSDT


# NEW VERSION FOR ANY TOP


def get_top_moneyToBuyInUSDT(balance, limit):
    moneyToBuyInUSDT = {}
    for coin in all_unique_coin:
        moneyToBuyInUSDT[coin] = 0.00
    for coin in islice(nm_one, limit):
        moneyToBuyInUSDT[coin] += ((15 / limit) * balance / 100)
    for coin in islice(nm_two, limit):
        moneyToBuyInUSDT[coin] += ((55 / limit) * balance / 100)
    for coin in islice(nm_tree, limit):
        moneyToBuyInUSDT[coin] += ((15 / limit) * balance / 100)
    for coin in islice(nm_four, limit):
        moneyToBuyInUSDT[coin] += ((15 / limit) * balance / 100)
    return moneyToBuyInUSDT


# ALL COIN EMPTY DICT
def get_empty_moneydict():
    moneydict = {}
    for coin in all_unique_coin:
        moneydict[coin] = 0.00
    return moneydict
