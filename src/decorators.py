def log(filename=None):
    def wrapper(func):
        def inner(*args, **kwargs):
            try:
                log_message = f"Начало выполнения функции {func.__name__} с аргументами {args} и {kwargs}\n"
                if filename is None:
                    print(log_message)
                for arg in args:
                    if not isinstance(arg, (int, float)):
                        raise ValueError("Аргументы должны быть целым или вещественным числом")
                for key, value in kwargs.items():
                    if not isinstance(value, (int, float)):
                        raise ValueError("Аргументы должны быть целым или вещественным числом")
                result = func(*args, **kwargs)
                result_message = f"Результат работы функции {result}\n"
                end_message = f"Конец выполнения функции {func.__name__} с аргументами {args} и {kwargs}\n"
                success_message = f"{func.__name__} ok\n"

                if filename is None:
                    print(result_message)
                    print(end_message)
                    print(success_message)
                else:
                    with open(filename, "a") as f:
                        f.write(log_message)
                        f.write(result_message)
                        f.write(end_message)
                        f.write(success_message)
                return result
            except Exception as e:
                error_message = f"Функция: {func.__name__} Ошибка: {str(e)}. Введенные аргументы: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a") as file:
                        file.write(error_message)
                else:
                    print(error_message)
        return inner
    return wrapper


@log()
def my_function(x, y):
    """Функция складывает два числа"""
    return x + y


my_function('2', 2)
