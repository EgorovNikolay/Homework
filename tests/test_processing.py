import pytest

from src.processing import filter_by_state, sort_by_date
from tests.conftest import input_data


def test_filter_by_state_default(input_data):
    expected = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    assert filter_by_state(input_data) == expected


def test_filter_by_state_custom(input_data):
    expected = [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    assert filter_by_state(input_data, "CANCELED") == expected


def test_filter_by_state_no_matches(input_data):
    assert filter_by_state(input_data, "ANOTHER_VALUE") == []


def test_filter_by_state_invalid_data_type():
    with pytest.raises(ValueError):
        filter_by_state("string")


def test_filter_by_state_invalid_element_type():
    data = [{"id": 41428829, "state": "EXECUTED"}, "no_dict"]
    with pytest.raises(ValueError):
        filter_by_state(data)


def test_filter_by_state_invalid_state_type(input_data):
    with pytest.raises(ValueError):
        filter_by_state(input_data, 123)


def test_sort_by_date_reverse_true(input_data):
    expected = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]
    assert sort_by_date(input_data) == expected


def test_by_date_reverse_false(input_data):
    expected = [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    assert sort_by_date(input_data, False) == expected


def test_sort_by_date_empty_list():
    assert sort_by_date([]) == []


def test_sort_by_date_invalid_data_type():
    with pytest.raises(ValueError):
        sort_by_date("no_dict")


def test_sort_by_date_invalid_sort_type():
    with pytest.raises(ValueError):
        sort_by_date(input_data, 123)


def test_sort_by_date_mixed_types():
    input_data = [
        {"id": 41428829, "state": "EXECUTED", "date": 123},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]
    with pytest.raises(TypeError):
        sort_by_date(input_data)
