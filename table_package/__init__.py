table = {
    'column1': ['value1_1', 'value1_2', 'value1_3'],
    'column2': ['value2_1', 'value2_2', 'value2_3'],
}
if not isinstance(table, dict):
    raise ValueError("Таблица должна быть представлена в виде словаря.")
