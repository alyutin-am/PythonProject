def filter_by_currency(transaction_dictionaries: list, currency: str ="USD") -> iter:
    """
    Функция принимает на вход список словарей и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует currency
    """
    for dictionaries in transaction_dictionaries:
        if dictionaries["operationAmount"]["currency"]["code"] == currency:
            yield dictionaries


