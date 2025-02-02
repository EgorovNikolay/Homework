import pytest
from src.masks import get_mask_account, get_mask_card_number

@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_length():
    result = get_mask_card_number("12345")
    assert result == ''


def test_get_mask_card_number_is_digit():
    result = get_mask_card_number("AFs5-6ak1-9fha-1")
    assert result == ''


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("70007922896063611256", "**1256"),
        ("15968870519983477635", "**7635"),
        ("77347267569721588641", "**8641"),
    ],
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected


def test_get_mask_account_length():
    result = get_mask_account("123456789")
    assert result == ''


def test_get_mask_account_isdigit():
    result = get_mask_account("77aj472-AKj88-41Gh91")
    assert result == ''

