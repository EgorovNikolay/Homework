import json
import logging
import os
from typing import Dict, List

import pandas as pd

base_path = os.path.dirname(__file__)
full_path = os.path.join(base_path, "..", "logs", "utils.log")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(full_path, "w")
file_formater = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def read_json_file(path_to_file: str) -> List[Dict]:
    """Функция читает json файл по указанному пути и возвращает список словарей"""
    logger.info(f"Чтение файла по указанному пути {path_to_file}")
    try:
        with open(path_to_file, "r") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info("Файл возвращен в виде списка")
                return data
            logger.warning("Файл не является списком")
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error(f"Путь {path_to_file} не найден")
        return []


test_data_invalid = read_json_file("wrong_path")
file_path = os.path.join("..", "data", "operations.json")
test_data_correct = read_json_file(file_path)


def load_json(filename: str) -> List[Dict]:
    """Функция читает json файл по указанному пути и возвращает список словарей"""
    with open(filename, "r") as file:
        return json.load(file)


def load_csv(filename: str) -> List[Dict]:
    """Функция читает csv файл по указанному пути и возвращает список словарей"""
    df = pd.read_csv(filename)
    return df.to_dict(orient="records")


def load_xlsx(filename: str) -> List[Dict]:
    """Функция читает excel файл по указанному пути и возвращает список словарей"""
    df = pd.read_excel(filename)
    return df.to_dict(orient="records")
