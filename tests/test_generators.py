from generators import (card_number_generator, filter_by_currency,
                        transaction_descriptions)


def test_filter_by_currency(data_transactions):
    expected = [
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
    ]

    result = list(filter_by_currency(data_transactions, "USD"))

    assert result == expected


def test_filter_by_currency_no_transactions_for_currency(data_transactions):
    result = list(filter_by_currency(data_transactions, "RUB"))

    assert result == []


def test_filter_by_currency_empty_list():
    result = list(filter_by_currency([], "USD"))

    assert result == []


def test_transaction_descriptions(data_transactions):
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]

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


def test_card_number_generator():
    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]

    card_numbers = list(card_number_generator(1, 5))

    assert card_numbers == expected


def test_card_number_generator_empty_range():
    card_numbers = list(card_number_generator(12, 5))

    assert card_numbers == []


def test_card_number_generator_maximum():
    expected = ["9999 9999 9999 9999"]

    card_numbers = list(card_number_generator(9999999999999999, 9999999999999999))

    # Сравниваем результат с ожидаемым
    assert card_numbers == expected
