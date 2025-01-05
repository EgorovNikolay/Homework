def log(filename=None):
    def wrapper(func):
        def inner(*args, **kwargs):
            try:
                print(f"Начало выполнения функции {func.__name__} с аргументами {args} и {kwargs}")
                for arg in args:
                    if not isinstance(arg, (int, float)):
                        raise ValueError("Аргументы должны быть целым или вещественным числом")
                for key, value in kwargs.items():
                    if not isinstance(value, (int, float)):
                        raise ValueError("Аргументы должны быть целым или вещественным числом")
                result = func(*args, **kwargs)
                print(f"{func.__name__} ok")
                print(f"Результат работы функции {result}")
                print(f"Конец выполнения функции {func.__name__} с аргументами {args} и {kwargs}")
                if filename:
                    with open(filename, "a") as f:
                        f.write(f"{func.__name__} ok\n")
                return result
            except Exception as e:
                error_message = f"Функция: {func.__name__} Ошибка: {str(e)}. Введенные аргументы: {args}, {kwargs}\n"
                print(error_message)
                if filename:
                    with open(filename, "a") as file:
                        file.write(error_message + "\n")

        return inner

    return wrapper


@log(filename="mylog.txt")
def my_function(x, y):
    """Функция складывает два числа"""
    return x + y


my_function('2', 2)
