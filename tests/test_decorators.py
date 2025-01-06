from src.decorators import my_function


def test_console_logging_success(capsys):
    result = my_function(2, 2)
    captured = capsys.readouterr()
    assert result == 4
    assert "Начало выполнения функции my_function с аргументами (2, 2) и {}" in captured.out
    assert "Результат работы функции 4" in captured.out
    assert "Конец выполнения функции my_function с аргументами (2, 2) и {}" in captured.out
    assert "my_function ok" in captured.out


def test_console_invalid_value(capsys):
    result = my_function('2', 2)
    captured = capsys.readouterr()
    assert result is None
    assert "Начало выполнения функции my_function с аргументами ('2', 2) и {}" in captured.out
    assert ("Функция: my_function Ошибка: Аргументы должны быть целым или вещественным числом. "
            "Введенные аргументы: ('2', 2), {}") in captured.out


def test_console_empty_value(capsys):
    result = my_function()
    captured = capsys.readouterr()
    assert result is None
    assert "Начало выполнения функции my_function с аргументами () и {}" in captured.out
    assert ("Функция: my_function Ошибка: my_function() missing 2 required positional arguments: 'x' and 'y'. "
            "Введенные аргументы: (), {}") in captured.out


def test_console_success_kwargs(capsys):
    result = my_function(4, y=3)
    captured = capsys.readouterr()
    assert result == 7
    assert "Начало выполнения функции my_function с аргументами (4,) и {'y': 3}" in captured.out
    assert "Результат работы функции 7" in captured.out
    assert "Конец выполнения функции my_function с аргументами (4,) и {'y': 3}" in captured.out
    assert "my_function ok" in captured.out


def test_console_invalid_value_kwargs(capsys):
    result = my_function(4, y='3')
    captured = capsys.readouterr()
    assert result is None
    assert "Начало выполнения функции my_function с аргументами (4,) и {'y': '3'}" in captured.out
    assert ("Функция: my_function Ошибка: Аргументы должны быть целым или вещественным числом. "
            "Введенные аргументы: (4,), {'y': '3'}") in captured.out


def test_console_empty_kwargs(capsys):
    result = my_function(y='3')
    captured = capsys.readouterr()
    assert result is None
    assert "Начало выполнения функции my_function с аргументами () и {'y': '3'}" in captured.out
    assert ("Функция: my_function Ошибка: Аргументы должны быть целым или вещественным числом. "
            "Введенные аргументы: (), {'y': '3'}") in captured.out
