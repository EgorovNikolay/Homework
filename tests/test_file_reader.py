from unittest.mock import patch

from src.file_reader import read_csv_transactions, read_excel_transactions


@patch("pandas.read_csv")
def test_read_transactions_from_csv(mock_read_csv, csv_test_data):
    mock_read_csv.return_value = csv_test_data

    result = read_csv_transactions("mock_path.csv")
    expected = [
        {"id": 1, "amount": 100, "date": "2025-01-01"},
        {"id": 2, "amount": 200, "date": "2025-01-02"},
    ]

    assert result == expected
    mock_read_csv.assert_called_once_with("mock_path.csv")


@patch("pandas.read_excel")
def test_read_transactions_from_excel(mock_read_excel, excel_test_data):
    mock_read_excel.return_value = excel_test_data

    result = read_excel_transactions("mock_path.xlsx")
    expected = [
        {"id": 1, "amount": 100, "date": "2025-01-01"},
        {"id": 2, "amount": 200, "date": "2025-01-02"},
    ]

    assert result == expected
    mock_read_excel.assert_called_once_with("mock_path.xlsx")


@patch("pandas.read_csv")
def test_read_transactions_from_csv_error(mock_read_csv):
    mock_read_csv.side_effect = Exception("Test error")
    result = read_csv_transactions("wrong_path.csv")
    assert result == []


@patch("pandas.read_excel")
def test_read_transactions_from_excel_error(mock_read_excel):
    mock_read_excel.side_effect = Exception("Test error")
    result = read_excel_transactions("wrong_path.xlsx")
    assert result == []
