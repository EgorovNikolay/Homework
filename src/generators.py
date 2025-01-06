def filter_by_currency(transactions, currency):
    """Функция фильтрует транзакции по указанной валюте"""
    for transaction in transactions:
        if (
            transaction.get("operationAmount", {}).get("currency", {}).get("code")
            == currency
        ):
            yield transaction


def transaction_descriptions(transactions):
    """Функция выводит описание транзакции"""
    for transaction in transactions:
        result = transaction.get("description")

        if result is None:
            raise ValueError("Отсутствует ключ description")

        yield result


def card_number_generator(start, end):
    """Генератор номеров банковских карт"""
    for number in range(start, end + 1):
        number_str = str(number)
        while len(number_str) < 16:
            number_str = "0" + number_str
        formatted_number = (
            number_str[:4]
            + " "
            + number_str[4:8]
            + " "
            + number_str[8:12]
            + " "
            + number_str[12:]
        )
        yield formatted_number
