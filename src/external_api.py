import os
from dotenv import load_dotenv
import requests
import json


EXCHANGE_RATES_API_KEY = os.getenv("API_KEY")


def convert_to_rub(transaction: dict) -> float:
    """Функция конвертации валюты (принимает на вход транзакцию и возвращает сумму транзакций
    (amount) в рублях, тип данных "float". Если транзакция была а "USD" или "EUR" происходит
    обращение к внешнему API)
    """
    amount = transaction["operationAmount"]["amount"]
    currency_code = transaction["operationAmount"]["currency"]["code"]
    if currency_code == "RUB":
        return float(amount)
    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {"to": "RUB", "from": currency_code, "amount": amount}
    headers = {"apikey": EXCHANGE_RATES_API_KEY}
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    data = response.json()
    return float(data["result"])
