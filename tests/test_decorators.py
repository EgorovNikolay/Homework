from src.decorators import my_function


def test_successful_execution(capsys):
    result = my_function(2, 2)
    assert result == 4

    captured = capsys.readouterr()
    assert (
        "Начало выполнения функции my_function с аргументами (2, 2) и {}"
        in captured.out
    )
    assert "my_function ok" in captured.out
    assert "Результат работы функции 4" in captured.out
    assert (
        "Конец выполнения функции my_function с аргументами (2, 2) и {}" in captured.out
    )


def test_invalid_argument(capsys):
    result = my_function("2", 2)
    assert result is None

    captured = capsys.readouterr()
    assert (
        "Начало выполнения функции my_function с аргументами ('2', 2) и {}"
        in captured.out
    )
    assert (
        "Функция: my_function Ошибка: Аргументы должны быть целым или вещественным числом. "
        "Введенные аргументы: ('2', 2), {}"
        in captured.out
    )


def test_empty_argument(capsys):
    result = my_function()
    assert result is None

    captured = capsys.readouterr()
    assert "Начало выполнения функции my_function с аргументами () и {}" in captured.out
    assert (
        "Функция: my_function Ошибка: my_function() missing 2 required positional arguments: 'x' and 'y'. "
        "Введенные аргументы: (), {}"
        in captured.out
    )
