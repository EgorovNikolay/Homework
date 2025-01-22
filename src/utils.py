import json
from typing import Dict, List


def read_json_file(path_to_file: str) -> List[Dict]:
    """Функция читает json файл по указанному пути и возвращает список словарей """
    try:
        with open(path_to_file, 'r') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
