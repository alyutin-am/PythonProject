import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Load API_KEY from the environment
API_KEY = os.getenv("API_KEY")
API_URL = "https://api.apilayer.com/exchangerates_data/latest?symbols=USD%2C%20EUR&base=RUB"
payload: dict[str, Any] = {}
headers = {"apikey": os.getenv("API_KEY")}


def convert_currency_to_rub(transaction: Dict[str, Any]) -> float:
    """
    A function that converts the transaction amount from USD or EUR to rubles.
    """

    # Check for the presence of the 'operationAmount' key and nested data
    if "operationAmount" not in transaction or "amount" not in transaction["operationAmount"]:
        print(f"Error: Transaction {transaction} does not contain the necessary information for conversion.")
        return 0.0  # Return 0.0 and continue execution

    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount  # If it is already in RUB, we simply return the amount

    # We make a request to the API to get the current exchange rate
    response = requests.request("GET", API_URL, headers=headers, data=payload)

    if response.status_code == 200:
        rates = response.json().get("rates", {})

        # Check if there is a rate for this currency
        if currency in rates:
            conversion_rate = float(rates[currency])
            converted_amount = amount * (1 / conversion_rate)

            return converted_amount  # Return the converted amount in rubles
        else:
            print(f"Rate for currency 'float({currency})' not found.")
    else:
        print(f"Error while accessing API: {response.status_code}")

    return 0.0  # In case of error, return 0