from src.transactions import count_transactions, search_transactions
from src.utils import load_csv, load_json, load_xlsx


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    file_choice = input("Введите номер пункта: ").strip()

    if file_choice == "1":
        filename = input("Введите путь к JSON-файлу: ").strip()
        transactions = load_json(filename)
        print("Для обработки выбран JSON-файл.")
    elif file_choice == "2":
        filename = input("Введите путь к CSV-файлу: ").strip()
        transactions = load_csv(filename)
        print("Для обработки выбран CSV-файл.")
    elif file_choice == "3":
        filename = input("Введите путь к XLSX-файлу: ").strip()
        transactions = load_xlsx(filename)
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Некорректный выбор. Завершение программы.")

    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}

    while True:
        status = (
            input(
                "Введите статус, по которому необходимо выполнить фильтрацию (EXECUTED, CANCELED, PENDING): "
            )
            .strip()
            .upper()
        )
        if status in valid_statuses:
            break
        print(f'Статус операции "{status}" недоступен.')

    filtered_transactions = [
        transaction
        for transaction in transactions
        if transaction.get("status", "").upper() == status
    ]
    print(f'Операции отфильтрованы по статусу "{status}"')

    sort_by_date = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_by_date == "да":
        order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        reverse = order == "по убыванию"
        filtered_transactions.sort(key=lambda x: x.get("date", ""), reverse=reverse)

    only_rub = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if only_rub == "да":
        filtered_transactions = [
            t for t in filtered_transactions if t.get("currency", "").lower() == "rub"
        ]

    search_in_description = (
        input("Отфильтровать список транзакций по слову в описании? Да/Нет: ")
        .strip()
        .lower()
    )
    if search_in_description == "да":
        search_str = input("Введите слово для поиска в описаниях: ").strip()
        filtered_transactions = search_transactions(filtered_transactions, search_str)

    if filtered_transactions:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            date = transaction.get("date", "Неизвестная дата")
            description = transaction.get("description", "Без описания")
            amount = transaction.get("amount", "Неизвестная сумма")
            currency = transaction.get("currency", "Неизвестная валюта")
            print(f"{date} {description} Сумма: {amount} {currency}")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")

    count_categories = (
        input("Хотите подсчитать транзакции по категориям? Да/Нет: ").strip().lower()
    )
    if count_categories == "да":
        categories = input("Введите категории через запятую: ").strip().split(",")
        categories = [category.strip() for category in categories]
        category_counts = count_transactions(filtered_transactions, categories)
        print("Подсчет транзакций по категориям:")
        for category, count in category_counts.items():
            print(f"{category}: {count} операций")


if __name__ == "__main__":
    main()
