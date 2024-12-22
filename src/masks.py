def get_mask_card_number(number_card: str) -> str:
    """Функция маскирует номер карты"""
    if len(number_card) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")
    if not number_card.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")
    return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция маскирует номер счета"""
    if len(account_number) != 20:
        raise ValueError("Номер счета должен содержать 20 цифр")
    if not account_number.isdigit():
        raise ValueError("Номер счета должен содержать только цифры")
    return f"**{account_number[-4:]}"
