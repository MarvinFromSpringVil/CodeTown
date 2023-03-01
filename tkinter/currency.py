import requests
import json

_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
_supported_currency = ['USD', 'EUR', 'JPY']

def get_curreny_ratio(currency):
    if not currency.upper() in _supported_currency:
        raise ValueError('Only support following currencies: {}'.format(' '.join(_supported_currency)))
    url = 'https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRW{}'.format(currency.upper())
    exchange =requests.get(url, headers=_headers).json()
    return exchange[0]['basePrice']

def upbit_get_last_trades(name):
    url = "https://crix-api-endpoint.upbit.com/v1/crix/trades/days?code=CRIX.UPBIT.KRW-{CoinName}&count=1".format(CoinName=name)
    try:
        trades = requests.get(url, headers=_headers).json()
    except:
        print("exception occured at upbit_get_last_trades.")
        return
    else:
        return trades[0]['tradePrice']

if __name__ == '__main__':
    print(get_curreny_ratio('USD'))
    print(get_curreny_ratio('EUR'))
    print(get_curreny_ratio('JPY'))
    print(upbit_get_last_trades('BTC'))