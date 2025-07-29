import json


def get_transactions(operations: json) -> list:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        try:
            with open(operations, encoding="utf-8") as json_file:
                result = json.load(json_file)
                if type(result) is list:
                    return result
                else:
                    return []
        except json.JSONDecodeError:
            return []
    except FileNotFoundError:
        return []
