import csv  # Импортируем модуль для работы с CSV файлами

def load_table(file_path):
    """Загружает таблицу из CSV файла."""
    table = {}  # Создаем пустой словарь для хранения данных
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        # Открываем CSV файл для чтения
        reader = csv.DictReader(csvfile)  # Инициализируем reader для чтения как словарь
        for row in reader:  # Проходим по каждой строке в файле
            for key, value in row.items():  # Для каждого ключа и значения в строке
                if key not in table:  # Проверяем, если ключ уже есть в таблице
                    table[key] = []  # Если нет, создаем новый список для этого ключа
                table[key].append(value)  # Добавляем значение в список по этому ключу
    return table  # Возвращаем заполненный словарь

def save_table(table, file_path):
    """Сохраняет таблицу в CSV файл."""
    with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
        # Открываем CSV файл для записи
        writer = csv.DictWriter(csvfile, fieldnames=table.keys())  # Инициализируем writer и передаем заголовки
        writer.writeheader()  # Пишем заголовки в файл
        rows = zip(*table.values())  # Получаем строки из значений словаря
        for row in rows:  # Проходим по каждой строке
            writer.writerow(dict(zip(table.keys(), row)))  # Записываем строку в файл
