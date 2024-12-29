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
