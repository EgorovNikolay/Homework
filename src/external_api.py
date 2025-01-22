import os

import requests
from dotenv import load_dotenv

env_path = os.path.join("..", ".env")
load_dotenv(env_path)
API_KEY = os.getenv("API_KEY")


def conversion_function(transaction: dict) -> float:
    """Функция принимает транзакцию и возвращает сумму транзакции в рублях"""
    try:
        amount = float(transaction.get("operationAmount", {}).get("amount", 0))
        currency_code = (
            transaction.get("operationAmount", {}).get("currency", {}).get("code")
        )
    except (KeyError, TypeError):
        raise ValueError("Должна быть передана сумма и валюта")

    if currency_code == "RUB":
        return amount
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
    headers = {"apikey": API_KEY}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get("result")
    except requests.RequestException:
        print("Не удалось конвертировать данные")
        return 0.0
