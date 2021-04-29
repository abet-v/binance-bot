import requests
from bs4 import BeautifulSoup


def get_money_name_for_index(index):
    # url = 'http://anovamoeda.oinvestidordesucesso.com/IS/nmREPORT.asp?NM=2'
    cookies = {
        'ASPSESSIONIDCSTDQQCQ': 'FCKNJKGDGDHEFFFNFHDDKIJO',
    }
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://anovamoeda.oinvestidordesucesso.com/IS/nmREPORT.asp?NM=2',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    params = (
        ('NM', index),
    )
    response = requests.get('http://anovamoeda.oinvestidordesucesso.com/IS/nmREPORT.asp',
                            headers=headers, params=params, cookies=cookies, verify=False)

    soup = BeautifulSoup(response.text, 'lxml')
    tds = soup.findAll('td')
    moedas = [tds[8].text, tds[14].text,
              tds[20].text, tds[26].text, tds[32].text]
    return moedas


nm_one = get_money_name_for_index(1)
nm_two = get_money_name_for_index(2)
nm_tree = get_money_name_for_index(3)
nm_four = get_money_name_for_index(4)
all_unique_coin = list(set().union(nm_one, nm_two, nm_tree, nm_four))
