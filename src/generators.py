from typing import Any, Generator, Iterator


def filter_by_currency(transaction_dictionaries: list, currency: str = "USD") -> Iterator[None]:
    """
    Функция принимает на вход список словарей и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует currency
    """
    for dictionaries in transaction_dictionaries:
        if dictionaries["operationAmount"]["currency"]["code"] == currency:
            yield dictionaries


def transaction_descriptions(transaction_descr: list) -> Generator[dict, Any, None]:
    """Генератор принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transaction_descr:
        result_transaction_descr = transaction.get("description")
        yield result_transaction_descr


def card_number_generator(start: int = 1, stop: int = 9999999999999999) -> Generator[str, Any, None]:
    """
    Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    """
    for gen_num in range(start, stop):
        len_numbers = 16 - len(str(gen_num))
        if gen_num >= 0:
            card_number_gen = ("0" * len_numbers) + str(gen_num)
            card_number_gen = (
                card_number_gen[:4]
                + " "
                + card_number_gen[4:8]
                + " "
                + card_number_gen[8:12]
                + " "
                + card_number_gen[-4:]
            )
            yield card_number_gen
