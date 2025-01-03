from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Функция, обрабатывает и маскирует номер карты или счета"""
    if not data:
        raise ValueError("Строка не должна быть пустой")
    if "Счет" in data:
        if not data.startswith("Счет"):
            raise ValueError("Перед номером счета должно быть указано слово 'Счет'")
        account_number = data.split(" ")[-1]
        if len(account_number) != 20:
            raise ValueError("Счет должен содержать 20 цифр")
        return f"Счет {get_mask_account(account_number)}"
    else:
        parts = data.split(" ")
        if len(parts) < 2:
            raise ValueError("Строка должна содержать и название карты, и номер карты")
        name_of_the_card, card_number = data.split(" ")[0:-1], data.split(" ")[-1]
        if len(card_number) != 16:
            raise ValueError("Номер карты должен содержать 16 цифр")
        return f"{' '.join(name_of_the_card)} {get_mask_card_number(card_number)}"


def get_date(date: str) -> str:
    """Функция для обработки и вывода даты"""
    if len(date) != 10:
        raise ValueError("Дата должна быть в формате: '2024-03-11' ")
    day = date[8:10]
    month = date[5:7]
    year = date[:4]
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        raise ValueError("Число, месяц и год должны состоять из цифр")
    if int(day) < 1 or int(day) > 31:
        raise ValueError("Число месяца не может быть меньше 1 и больше 31")
    if int(month) < 1 or int(month) > 12:
        raise ValueError("Месяц не может быть меньше 1 и больше 12")
    if int(month) == 2:
        if int(day) > 28:
            raise ValueError("В Феврале только 28 дней")
    if int(month) in [4, 6, 9, 11] and int(day) > 30:
        raise ValueError("В этом месяце только 30 дней")
    return f"{day}.{month}.{year}"
