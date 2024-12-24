from table_operations import Table  # Импортируем класс Table


def main():
    # Пример исходных данных в формате словаря
    data = {
        'Name': ['Vadim', 'Anri', 'Roma'],
        'Age': [18, 19, 18],
        'Country': ['Russia', 'Georgia', 'Belarus']
    }

    # Создаем экземпляр таблицы на основе данных
    table = Table(data)

    # Выводим исходную таблицу в консоль
    print("Исходная таблица:")
    table.print_table()

    # Получаем строки по номеру
    print("\nПолучение строк по номеру:")
    rows = table.get_rows_by_number(1, 3, copy_table=True)  # Получаем строки с 1 по 2
    rows.print_table()  # Печатаем эти строки

    # Получаем значения из конкретного столбца
    print("\nПолучение значений из столбца 'Age':")
    age_values = table.get_values('Age')
    print(age_values)  # Печатаем значения из столбца Age

    # Устанавливаем новые значения в столбец
    print("\nУстановка новых значений в столбец 'Country':")
    table.set_values(['Russia', 'Georgia', 'Belarus'], 'Country')
    table.print_table()  # Печатаем измененную таблицу


if __name__ == '__main__':
    main()  # Запускаем основную функцию

