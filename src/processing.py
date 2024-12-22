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


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
            },
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2018-10-14T08:21:33.419441",
            },
        ],
        False,
    )
)
