from typing import Dict, List


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Возвращает список словарей по значению. По умолчанию 'EXECUTED'"""
    if not isinstance(data, list):
        raise ValueError("Входные данные должны быть списком словарей.")
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Каждый элемент входного списка должен быть словарем.")
    if not isinstance(state, str):
        raise ValueError("Аргумент 'state' должен быть строкой.")
    result = []
    for i in data:
        if i.get("state") == state:
            result.append(i)
    return result


def sort_by_date(data: List[Dict], sort: bool = True) -> List[Dict]:
    """Функия, сортирующая список по дате"""
    if not isinstance(data, list):
        raise ValueError("Входные данные должны быть списком словарей")
    if not isinstance(sort, bool):
        raise ValueError("Агрумент 'sort' должен быть булевым значением")
    sorted_list = sorted(data, key=lambda x: x["date"], reverse=sort)
    return sorted_list
