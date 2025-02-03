from src.transactions import count_transactions, search_transactions


def test_search_transactions_with_matching_description():
    transactions = [
        {"description": "Grocery shopping at the market", "amount": 100},
        {"description": "Coffee at cafe", "amount": 5},
        {"description": "Grocery shopping", "amount": 50},
    ]
    search_str = "grocery"

    result = search_transactions(transactions, search_str)
    expected = [
        {"description": "Grocery shopping at the market", "amount": 100},
        {"description": "Grocery shopping", "amount": 50},
    ]

    assert result == expected


def test_search_transactions_with_no_matching_description():
    transactions = [
        {"description": "Grocery shopping at the market", "amount": 100},
        {"description": "Coffee at cafe", "amount": 5},
        {"description": "Grocery shopping", "amount": 50},
    ]
    search_str = "electronics"

    result = search_transactions(transactions, search_str)
    expected = []

    assert result == expected


def test_search_transactions_with_case_insensitive_matching():
    transactions = [
        {"description": "Grocery shopping at the market", "amount": 100},
        {"description": "Coffee at cafe", "amount": 5},
        {"description": "Grocery shopping", "amount": 50},
    ]
    search_str = "GROCERY"

    result = search_transactions(transactions, search_str)
    expected = [
        {"description": "Grocery shopping at the market", "amount": 100},
        {"description": "Grocery shopping", "amount": 50},
    ]

    assert result == expected


def test_search_transactions_with_missing_description():
    transactions = [
        {"description": "Grocery shopping at the market", "amount": 100},
        {"amount": 5},  # Транзакция без описания
        {"description": "Coffee at cafe", "amount": 5},
    ]
    search_str = "coffee"

    result = search_transactions(transactions, search_str)
    expected = [{"description": "Coffee at cafe", "amount": 5}]

    assert result == expected


def test_search_transactions_with_empty_transactions():
    transactions = []
    search_str = "coffee"

    result = search_transactions(transactions, search_str)
    expected = []

    assert result == expected


def test_count_transactions_with_matching_descriptions():
    transactions = [
        {"description": "Grocery shopping"},
        {"description": "Coffee at cafe"},
        {"description": "Grocery shopping"},
    ]
    categories = ["grocery", "coffee"]

    result = count_transactions(transactions, categories)
    expected = {"grocery": 2, "coffee": 1}

    assert result == expected


def test_count_transactions_with_empty_transactions():
    transactions = []
    categories = ["grocery", "coffee"]

    result = count_transactions(transactions, categories)
    expected = {"grocery": 0, "coffee": 0}

    assert result == expected


def test_count_transactions_with_no_matching_categories():
    transactions = [
        {"description": "Grocery shopping"},
        {"description": "Coffee at cafe"},
        {"description": "Grocery shopping"},
    ]
    categories = ["electronics", "clothing"]

    result = count_transactions(transactions, categories)
    expected = {"electronics": 0, "clothing": 0}

    assert result == expected


def test_count_transactions_with_case_insensitive_matching():
    transactions = [
        {"description": "grocery shopping"},
        {"description": "COFFEE at cafe"},
        {"description": "Grocery shopping"},
    ]
    categories = ["Grocery", "coffee"]

    result = count_transactions(transactions, categories)
    expected = {"Grocery": 2, "coffee": 1}

    assert result == expected
