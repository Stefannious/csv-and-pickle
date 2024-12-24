class Table:
    def __init__(self, data):
        """Конструктор, принимает данные в формате словаря для инициализации таблицы."""
        if not isinstance(data, dict):
            raise ValueError("Данные должны быть представлены в виде словаря.")  # Проверяем, что данные - это словарь
        self.data = data  # Сохраняем данные как атрибут
        self.types = {key: str for key in data.keys()}  # По умолчанию типы значений - строки для всех столбцов

    def get_rows_by_number(self, start, stop=None, copy_table=False):
        """Получение строк по их номеру."""
        if not isinstance(start, int) or (stop is not None and not isinstance(stop, int)):
            raise ValueError("Номера строк должны быть целыми числами.")  # Проверяем корректность типов

        rows = self.data.values()  # Получаем значения таблицы
        selected_rows = list(rows)[start:stop]  # Выбираем нужные строки в заданном диапазоне

        if copy_table:
            # Если требуется копия, создаем новую таблицу из выбранных строк
            return Table({key: [row[i] for row in selected_rows] for i, key in enumerate(self.data.keys())})
        return Table(self.data)  # Возвращаем оригинальную таблицу без изменений

    def get_rows_by_index(self, *vals, copy_table=False):
        """Получение строк по значению в первом столбце."""
        # Проверяем, что все переданные значения имеют допустимые типы (int, str, float)
        if not all(isinstance(val, (int, float, str)) for val in vals):
            raise ValueError("Значения должны быть int, str или float.")

        # Фильтруем строки по условиям
        selected_rows = [row for row in zip(*self.data.values()) if row[0] in vals]

        if copy_table:
            # Если требуется копия, создаем новую таблицу из выбранных строк
            return Table({key: [row[i] for row in selected_rows] for i, key in enumerate(self.data.keys())})
        return Table(self.data)  # Возвращаем оригинальную таблицу без изменений

    def get_column_types(self, by_number=True):
        """Получение типов значений в столбцах."""
        types_dict = self.types  # Получаем словарь типов значений
        if by_number:
            # Если требуется индексация, возвращаем типы по номеру столбца
            return {i: t for i, t in enumerate(types_dict.values())}
        return types_dict  # Возвращаем названия столбцов и их типы

    def set_column_types(self, types_dict, by_number=True):
        """Установка типов для столбцов."""
        if not isinstance(types_dict, dict):
            raise ValueError(
                "Типы столбцов должны быть переданы в виде словаря.")  # Проверяем, что входные данные - словарь

        if by_number:
            # Устанавливаем типы по указанным индексам
            for key, value in types_dict.items():
                if isinstance(key, int) and key < len(self.types):
                    self.types[list(self.data.keys())[key]] = value  # Присваиваем новый тип соответствующему столбцу
                else:
                    raise ValueError("Некорректный индекс столбца.")  # Ошибка для недопустимых индексов
        else:
            # Устанавливаем типы по названию столбца
            for key, value in types_dict.items():
                if key in self.types:
                    self.types[key] = value  # Присваиваем новый тип для существующего столбца
                else:
                    raise KeyError(f"Столбец '{key}' не существует.")  # Ошибка, если столбца нет

    def get_values(self, column=0):
        """Получение значений из столбца."""
        if isinstance(column, int):
            key = list(self.data.keys())[column]  # Определяем имя столбца по индексу
        else:
            key = column  # Используем переданное имя столбца

        if key not in self.data:
            raise KeyError(f"Столбец '{key}' не существует.")  # Ошибка, если столбца нет

        # Возвращаем значения, преобразованные к указанному типу
        return [self.cast_value(value, self.types[key]) for value in self.data[key]]

    def get_value(self, column=0):
        """Получение одного значения из столбца для представления с одной строкой."""
        values = self.get_values(column)  # Получаем значения из столбца
        if values:
            return values[0]  # Возвращаем первое значение
        raise ValueError(f"Столбец '{column}' пуст.")  # Ошибка, если столбец пуст

    def set_values(self, values, column=0):
        """Установка значений в столбце."""
        if not isinstance(values, list):
            raise ValueError("Значения должны быть списком.")  # Проверяем, что входные данные - список

        if isinstance(column, int):
            key = list(self.data.keys())[column]  # Определяем имя столбца по индексу
        else:
            key = column  # Используем переданное имя столбца

        if key not in self.data:
            raise KeyError(f"Столбец '{key}' не существует.")  # Ошибка, если столбца нет

        if len(values) != len(self.data[key]):
            raise ValueError("Количество значений должно соответствовать числу строк.")  # Проверка на количество

        # Присваиваем новые значения, преобразованные к указанному типу
        self.data[key] = [self.cast_value(value, self.types[key]) for value in values]

    def set_value(self, value, column=0):
        """Установка одного значения в столбце."""
        if isinstance(column, int):
            key = list(self.data.keys())[column]  # Определяем имя столбца по индексу
        else:
            key = column  # Используем переданное имя столбца

        if key not in self.data:
            raise KeyError(f"Столбец '{key}' не существует.")  # Ошибка, если столбца нет

        self.data[key][0] = self.cast_value(value, self.types[key])  # Устанавливаем значение в первую строку

    def print_table(self):
        """Вывод таблицы на консоль."""
        headers = self.data.keys()  # Получаем имена столбцов
        print('\t'.join(headers))  # Выводим заголовки разделенные табуляцией
        rows = zip(*self.data.values())  # Объединяем строки для вывода
        for row in rows:
            # Выводим каждую строку, преобразованную в строки
            print('\t'.join(map(str, row)))

    def cast_value(self, value, typ):
        """Приведение значения к указанному типу."""
        if typ == int:
            return int(value) if value is not None else None  # Преобразование в int
        elif typ == float:
            return float(value) if value is not None else None  # Преобразование в float
        elif typ == bool:
            return bool(value) if value is not None else None  # Преобразование в bool
        return str(value)  # По умолчанию возвращаем строку
