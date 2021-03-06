import requests


def get_coin_data():
    coins = ["BTC", "ETH", "XRP", "LTC", "BCH",
             "ADA", "DOT", "LINK", "BNB", "XLM"]

    # connect to the CryptoCompare API
    crypto_data = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD".format(",".join(coins))).json()["RAW"]

    # get coins data and store in a python dictionary
    data = {}
    for i in crypto_data:
        data[i] = {
            "coin": i,
            "price": crypto_data[i]["USD"]["PRICE"],
            "change_day": crypto_data[i]["USD"]["CHANGEPCT24HOUR"],
            "change_hour": crypto_data[i]["USD"]["CHANGEPCTHOUR"]
        }

    return data


if __name__ == "__main__":
    print(get_prices())
