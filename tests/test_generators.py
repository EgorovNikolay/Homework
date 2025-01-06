import pytest

from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)


@pytest.mark.parametrize(
    "currency, expected",
    [
        (
            "USD",
            [
                {
                    "id": 1,
                    "operationAmount": {
                        "amount": "100.00",
                        "currency": {"name": "USD", "code": "USD"},
                    },
                    "description": "Перевод организации",
                },
                {
                    "id": 3,
                    "operationAmount": {
                        "amount": "150.00",
                        "currency": {"name": "USD", "code": "USD"},
                    },
                    "description": "Перевод с карты на карту",
                },
                {
                    "id": 4,
                    "operationAmount": {
                        "amount": "300.00",
                        "currency": {"name": "USD", "code": "USD"},
                    },
                    "description": "Перевод организации",
                },
            ],
        ),
    ],
)
def test_filter_by_currency(data_transactions, currency, expected):
    result = list(filter_by_currency(data_transactions, currency))
    assert result == expected


def test_filter_by_currency_no_transactions_for_currency(data_transactions):
    result = list(filter_by_currency(data_transactions, "RUB"))

    assert result == []


def test_filter_by_currency_empty_list():
    result = list(filter_by_currency([], "USD"))

    assert result == []


@pytest.mark.parametrize(
    "data_transactions, expected",
    [
        (
            [
                {
                    "id": 1,
                    "operationAmount": {
                        "amount": "100.00",
                        "currency": {"name": "USD", "code": "USD"},
                    },
                    "description": "Перевод организации",
                },
                {
                    "id": 2,
                    "operationAmount": {
                        "amount": "200.00",
                        "currency": {"name": "USD", "code": "USD"},
                    },
                    "description": "Перевод со счета на счет",
                },
                {
                    "id": 3,
                    "operationAmount": {
                        "amount": "150.00",
                        "currency": {"name": "USD", "code": "USD"},
                    },
                    "description": "Перевод с карты на карту",
                },
                {
                    "id": 4,
                    "operationAmount": {
                        "amount": "300.00",
                        "currency": {"name": "USD", "code": "USD"},
                    },
                    "description": "Перевод организации",
                },
            ],
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
                "Перевод организации",
            ],
        ),
    ],
)
def test_transaction_descriptions(data_transactions, expected):
    result = list(transaction_descriptions(data_transactions))

    assert result == expected


def test_transaction_descriptions_empty_list():
    descriptions = list(transaction_descriptions([]))

    assert descriptions == []


def test_transaction_descriptions_single_item():
    transactions = [
        {
            "id": 1,
            "operationAmount": {
                "amount": "100.00",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
        }
    ]

    descriptions = list(transaction_descriptions(transactions))

    assert descriptions == ["Перевод организации"]


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
    ],
)
def test_card_number_generator(start, end, expected):
    card_numbers = list(card_number_generator(start, end))
    assert card_numbers == expected


def test_card_number_generator_empty_range():
    card_numbers = list(card_number_generator(12, 5))

    assert card_numbers == []


def test_card_number_generator_maximum():
    expected = ["9999 9999 9999 9999"]

    card_numbers = list(card_number_generator(9999999999999999, 9999999999999999))

    assert card_numbers == expected
