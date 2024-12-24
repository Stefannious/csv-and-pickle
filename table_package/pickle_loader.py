import pickle  # Импортируем модуль для работы с сериализацией объектов

def load_table(file_path):
    """Загружает таблицу из Pickle файла."""
    with open(file_path, 'rb') as file:
        # Открываем файл с данными в бинарном режиме для чтения
        return pickle.load(file)  # Загружаем и возвращаем сохраненную таблицу

def save_table(table, file_path):
    """Сохраняет таблицу в Pickle файл."""
    with open(file_path, 'wb') as file:
        # Открываем файл для записи в бинарном режиме
        pickle.dump(table, file)  # Сериализуем и сохраняем таблицу в файл
