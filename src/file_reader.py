import os
from typing import Dict, List

import pandas as pd


def read_csv_transactions(file_path: str) -> List[Dict]:
    """Чтение данных из CSV- файла"""
    try:
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        print(f"Ошибка при чтении CSV-файла: {e}")
        return []


def read_excel_transactions(file_path: str) -> List[Dict]:
    """Чтение данных из excel - файла"""
    try:
        df = pd.read_excel(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        print(f"Ошибка при чтении Excel-файла: {e}")
        return []


# Примеры работы функций:

csv_path = os.path.join("..", "data", "transactions.csv")
result = read_csv_transactions(csv_path)
print(result)

excel_path = os.path.join("..", "data", "transactions_excel.xlsx")
result = read_excel_transactions(excel_path)
print(result)
