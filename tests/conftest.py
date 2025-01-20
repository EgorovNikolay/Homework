import pytest


@pytest.fixture
def input_data():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def data_transactions():
    return [
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
                "currency": {"name": "EUR", "code": "EUR"},
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
    ]


@pytest.fixture
def transaction_rub():
    return {"operationAmount": {"amount": "100.0", "currency": {"code": "RUB"}}}


@pytest.fixture
def invalid_transaction():
    return {"operationAmount": {"amount": None, "currency": {"code": None}}}
