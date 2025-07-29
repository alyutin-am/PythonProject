import json
import requests

headers = {
    "apikey" : "G1D01mi8bZDRstqfKCeK6thvUvTl37LU"
}

url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code_of_currency}&amount={dict_amount}"

def sum_transaction(operations: dict) -> float:
    dict_amount = operations["amount"]
    if operations["code"] != "RUB":
        code_of_currency = operations["code"]
        try:
            result = requests.request("convert", url, headers=headers, data=)
