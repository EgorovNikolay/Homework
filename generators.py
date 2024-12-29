def filter_by_currency(transactions: list, currency: str):
    """Функция фильтрует транзакции по указанной валюте"""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> str:
    """Функция выводит описание транзакции"""
    for transaction in transactions:
        result = transaction.get("description")

        if result is None:
            raise ValueError("Отсутствует ключ description")

        yield result


