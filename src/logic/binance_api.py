import requests


from src.utils.config import BINANCE_URL


cryptos = ["BTC", "ETH", "DOGE", "BNB"]
state_currencies = ["USDT", "EUR", "RUB", "GBP"]

prices_crypto = {}


def getting_crypt_currency() -> dict:
    for crypto in cryptos:
        for currency in state_currencies:
            symbol_crypto = f"{crypto}{currency}"
            url = f"{BINANCE_URL}?symbol={symbol_crypto}"
            response = requests.get(url)
            data = response.json()
            prices_crypto[symbol_crypto] = data["price"]

    return prices_crypto


