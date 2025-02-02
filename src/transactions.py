import re
from collections import Counter
from typing import Dict, List


def search_transactions(transactions: List[Dict], search_str: str) -> List[Dict]:
    """Функция фильтрует транзакции по указанному слову"""
    pattern = re.compile(search_str, re.IGNORECASE)

    found_transactions = []

    for transaction in transactions:
        if "description" in transaction and pattern.search(transaction["description"]):
            found_transactions.append(transaction)
    return found_transactions


def count_transactions(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """Функция считает колличество операций в каждой категорий"""
    count_category = Counter()

    for transaction in transactions:
        descriptions = transaction.get('description', '').lower()
        for category in categories:
            if category.lower() in descriptions:
                count_category[category] += 1

    if not count_category:
        return {category: 0 for category in categories}

    return dict(count_category)
