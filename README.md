# Homework 10.2

## Описание проекта

Проект создан в учебных целях, чтобы отработать навыки работы с Git.  
Это программа для обработки банковских операций.

В проекте представлены две функции:

* filter_by_state: возвращает список словарей по указанному значению состояния.
* sort_by_date: сортирует список словарей по дате в порядке убывания и возвращает результат.

## Структура проекта

* src/processing.py: модуль, в котором реализованы функции:
* filter_by_state: фильтрует список словарей по заданному состоянию state.
* sort_by_date: сортирует и возвращает список по дате.
* main.py: модуль, который демонстрирует использование функций filter_by_state и sort_by_date.

## Примеры работы функций

Примеры использования функций и их результаты можно найти в файле `main.py`.

## Установка

Так как проект является учебным заданием, его установка не требуется.  
Вы можете склонировать его с моего [GitHub](https://github.com/EgorovNikolay/Homework10.1).

## Тестирование

Тесты можно запустить с помощью фреймворка `pytest`
Для этого необходимо установить `pytest` с помощью команды `poetry add --dev pytest`

### Основные функции и их назначение

* **get_mask_card_number:** фунцкия маскировки карты 
* **get_mask_account:** фунцкия маскировки счета
* **mask_account_card:** функия обработки и маскировки карты или счета
* **get_date:** функия для обработки и вызова даты
* **filter_by_state:** фильтрует входные данные (список словарей)
* **sort_by_date:** функия фильтрует список словарей по дате

### Покрытие тестами 

Для проверки функциональности программы были написаны юнит-тесты с использованием библиотеки `pytest`.

Для просмотра покрытия тестами проекта необходимо открыть в дирректории `htmlcov` файл `class_index.html`, например с помощью браузера.
Там будет показано покрытие тестами проекта в процентном соотношении.

## Домашнее задание 11.1

В этом домашнем задании реализованы функции генераторов и фильтрации транзакций.
Добавлен модуль `generators` и модуль `test_generators` в пакете `tests`

### Модуль `generators`

Модуль содержит функции для работы с транзакциями и генерацией номеров банковских карт.

### Основные функции в модуле `generators` и их назначение

* **filter_by_currency:** Функция фильтрует транзакции по указанной валюте
* **transaction_descriptions:** Функция выводит описание транзакции
* **card_number_generator:** Генератор номеров банковских карт

Для просмотра покрытия тестами проекта необходимо открыть в дирректории `htmlcov` файл `class_index.html`, например с помощью браузера.
Там будет показано покрытие тестами проекта в процентном соотношении.


## Домашнее задание 11.2

В этом домашнем задании реализован декоратор `log`, который логирует начало и конец выполнения функции, а также результаты выполнения или возникшие ошибки.
Декоратор `log` принимает необязательный аргумент `filename`, который указывает на файл, в который будет записываться информация о выполнении функции.

### Модуль `decorators` 

Модуль `decorators` предоставляет функциональность для декорирования функций. Включает декоратор `log`, 
который автоматически логирует начало и конец выполнения функции, а также результат или возникающие ошибки.

- Если аргумент `filename` задан, логи записываются в указанный файл.
- Если аргумент `filename` не задан, логи выводятся в консоль.
- Логи включают:
  - Имя функции.
  - Входные аргументы.
  - Результат выполнения или описание ошибки.

### Пример использования

Пример использования для функции `my_function` в модуле `decorators`

Для просмотра покрытия тестами проекта необходимо открыть в дирректории `htmlcov` файл `class_index.html`, например с помощью браузера.
Там будет показано покрытие тестами проекта в процентном соотношении.

## Домашнее задание 13.1

В этом домашнем задании реализованы функции чтения CSV и EXCEL файлов. 

### Модуль `file_reader` 

В модуле `file_reader` Реализована функция read_transactions_from_csv, которая принимает путь к файлу CSV и возвращает список словарей с транзакциями.
Также реализована функция read_transactions_from_excel, которая принимает путь к файлу Excel и возвращает список словарей с транзакциями.

### Пример использования

Пример использования функций показан в модуле `file_reader`

Для просмотра покрытия тестами проекта необходимо открыть в дирректории `htmlcov` файл `class_index.html`, например с помощью браузера.
Там будет показано покрытие тестами проекта в процентном соотношении.

## Домашнее задание 13.2

В этом домашнем задании реализованы функции для фильтрации транзаций и подсчета категорий.

### Модуль `transactions`

В модуле `transactions` Реализована функция `search_transactions`, которая принимает список транзакций и строку для фильтрации и возвращает список транзакций, в описании которых встречается заданная строка.
Также функция `count_transactions`, которая принимает список транзакций и категории для операции и возвращает сколько раз встречается каждая категория в операциях.
Также реализован основной модуль `main`, который связывает функциональность и демонстрирует работу функций.

### Покрытие тестами
Для просмотра покрытия тестами проекта необходимо открыть в дирректории htmlcov файл class_index.html, например с помощью браузера. 
