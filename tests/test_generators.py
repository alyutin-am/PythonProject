import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 5, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004"]),
        (
            9999999999999995,
            10000000000000000,
            [
                "9999 9999 9999 9995",
                "9999 9999 9999 9996",
                "9999 9999 9999 9997",
                "9999 9999 9999 9998",
                "9999 9999 9999 9999",
            ],
        ),
    ],
)
def test_card_number_generator(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected


def test_filter_by_currency():
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]

    result = list(filter_by_currency(transactions, "USD"))
    expected = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]

    assert result == expected


@pytest.mark.parametrize(
    "expected",
    [
        [
            "Перевод организации",
            "Перевод с карты на счет",
            "Перевод с карты на счет",
            "Перевод с карты на карту",
            "Перевод организации",
        ]
    ],
)
def test_transaction_descriptions(expected):
    transactions = [
        {
            "id": 970157810,
            "date": "2018-06-08T10:3:58.027767",
            "operationAmount": {"amount": "150", "currency": {"code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет - 63475662387234505765",
            "to": "Счет 8175128657841941437",
        },
        {
            "id": 129309161,
            "date": "2018-09-26T00:6:36.256087",
            "operationAmount": {"amount": "17250", "currency": {"code": "RUB"}},
            "description": "Перевод с карты на счет",
            "from": "Visa Classic 1313132313442324",
            "to": "Счет 1743370781324891402",
        },
        {
            "id": 129309161,
            "date": "2018-09-26T00:46:36.256087",
            "operationAmount": {"amount": "17250", "currency": {"code": "RUB"}},
            "description": "Перевод с карты на счет",
            "from": "Visa Classic 1313132313442324",
            "to": "Счет 1743370781324891402",
        },
        {
            "id": 129309161,
            "date": "2018-09-26T00:46:36.256087",
            "operationAmount": {"amount": "17250", "currency": {"code": "RUB"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 1313132313442324",
            "to": "Счет 1743370781324891402",
        },
        {
            "id": 129309161,
            "date": "2018-09-26T00:46:36.256087",
            "operationAmount": {"amount": "17250", "currency": {"code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Classic 1313132313442324",
            "to": "Счет 1743370781324891402",
        },
    ]
    result = list(transaction_descriptions(transactions))
    assert result == expected
