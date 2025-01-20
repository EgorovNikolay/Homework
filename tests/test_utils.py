from unittest.mock import patch

from src.utils import read_json_file


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
