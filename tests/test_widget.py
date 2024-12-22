import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "data, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
    ],
)
def test_mask_account_card(data, expected):
    assert mask_account_card(data) == expected


def test_mask_account_card_invalid():
    with pytest.raises(ValueError):
        mask_account_card("")

    with pytest.raises(ValueError):
        mask_account_card("646864736788")

    with pytest.raises(ValueError):
        mask_account_card("Номер 64686473678894779589")


def test_invalid_card_format():
    with pytest.raises(ValueError):
        mask_account_card("Visa")

    with pytest.raises(ValueError):
        mask_account_card("7000792289606361")

    with pytest.raises(ValueError):
        mask_account_card("Visa 12345678901234")


@pytest.mark.parametrize(
    "data, expected",
    [
        ("2024-03-11", "11.03.2024"),
        ("2024-05-09", "09.05.2024"),
        ("2024-09-17", "17.09.2024"),
    ],
)
def test_get_date(data, expected):
    assert get_date(data) == expected


def test_get_date_invalid():
    with pytest.raises(ValueError):
        get_date("")

    with pytest.raises(ValueError):
        get_date("2024-04-5")

    with pytest.raises(ValueError):
        get_date("2024-04-день")

    with pytest.raises(ValueError):
        get_date("2024-04-32")

    with pytest.raises(ValueError):
        get_date("2024-44-22")

    with pytest.raises(ValueError):
        get_date("2024-02-31")

    with pytest.raises(ValueError):
        get_date("2024-09-31")
