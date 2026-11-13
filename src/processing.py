from typing import Union


def filter_by_state(dictionaries: list, state: str = "EXECUTED") -> Union[list, str]:
    """
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ соответствует указанному значению, по умолчанию 'EXECUTED'
    """
    if isinstance(dictionaries, list) and isinstance(state, str):
        if len(dictionaries) != 0:
            new_data = []
            for dictionary in dictionaries:
                if state in dictionary["state"]:
                    new_data.append(dictionary)
            return new_data
        else:
            return "Введены не верные данные, пожалуйста, устраните ошибку и попробуйте снова"
    else:
        return "Введены не верные данные, пожалуйста, устраните ошибку и попробуйте снова"


def sort_by_date(dictionaries: list, sort: bool = True) -> Union[list, str]:
    """
    Функция должна возвращать новый список, отсортированный по дате,
    имеет возможность сортировки по возрастанию или убыванию
    """
    if isinstance(dictionaries, list) and isinstance(sort, bool):
        if len(dictionaries) != 0:
            sort_dictionaries = sorted(dictionaries, key=lambda unsort_date: unsort_date["date"], reverse=sort)
            return sort_dictionaries
        else:
            return "Введены не верные данные, пожалуйста, устраните ошибку и попробуйте снова"
    else:
        return "Введены не верные данные, пожалуйста, устраните ошибку и попробуйте снова"
