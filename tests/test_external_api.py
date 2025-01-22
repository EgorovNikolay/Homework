import os
from unittest.mock import patch

import pytest

from src.external_api import conversion_function

API_KEY = os.getenv("API_KEY")


def test_conversion_rub(transaction_rub):
    result = conversion_function(transaction_rub)
    assert result == 100.0


def test_conversion_invalid_data(invalid_transaction):
    with pytest.raises(ValueError):
        conversion_function(invalid_transaction)


@patch("requests.get")
def test_conversion_function(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 830412.91879}
    assert (
        conversion_function(
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {"name": "USD", "code": "USD"},
                },
            }
        )
        == 830412.91879
    )

    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37",
        headers={"apikey": API_KEY},
    )
