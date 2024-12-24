def save_table(table, file_path):
    """Сохраняет таблицу в текстовом файле."""
    with open(file_path, 'w', encoding='utf-8') as textfile:
        # Открываем файл для записи в текстовом режиме
        headers = table.keys()  # Получаем ключи (заголовки) из таблицы
        textfile.write('\t'.join(headers) + '\n')  # Записываем заголовки, разделенные табуляцией

        rows = zip(*table.values())  # Создаем строки из значений в таблице
        for row in rows:  # Проходим по каждой строке
            textfile.write('\t'.join(row) + '\n')  # Записываем строку в файл, разделяя значения табуляцией
