from unittest.mock import patch

import pandas as pd

from src.utils import load_csv, load_json, load_xlsx, read_json_file


@patch("builtins.open")
def test_read_json_file(mock_obj):
    mock_file = mock_obj.return_value.__enter__.return_value
    mock_file.read.return_value = '[{"key": "value"}]'
    assert read_json_file("test.txt") == [{"key": "value"}]
    mock_obj.assert_called_once_with("test.txt", "r")


@patch("builtins.open")
def test_read_json_file_invalid(mock_obj):
    mock_file = mock_obj.return_value.__enter__.return_value
    mock_file.read.return_value = ""
    assert read_json_file("test.txt") == []
    mock_obj.assert_called_once_with("test.txt", "r")


@patch("builtins.open")
def test_load_json(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = (
        '[{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]'
    )
    result = load_json("mock_data.json")
    expected = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
    assert result == expected
    mock_open.assert_called_once_with("mock_data.json", "r")


@patch("pandas.read_csv")
def test_load_csv(mock_read_csv):
    mock_data = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
    mock_read_csv.return_value = pd.DataFrame(mock_data)
    result = load_csv("mock_data.csv")
    expected = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
    assert result == expected
    mock_read_csv.assert_called_once_with("mock_data.csv")


@patch("pandas.read_excel")
def test_load_xlsx(mock_read_excel):
    mock_data = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
    mock_read_excel.return_value = pd.DataFrame(mock_data)
    result = load_xlsx("mock_data.xlsx")
    expected = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
    assert result == expected
    mock_read_excel.assert_called_once_with("mock_data.xlsx")
