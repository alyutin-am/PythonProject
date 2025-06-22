def filter_by_state(dictionaries: list, state: str = "EXECUTED") -> list:
    """
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ соответствует указанному значению, по умолчанию 'EXECUTED'
    """
    new_data = []
    for dictionary in dictionaries:
        if state in dictionary["state"]:
            new_data.append(dictionary)
    return new_data


def sort_by_date(unsort_date: list, sort: bool = True) -> list:
    """
    Функция должна возвращать новый список, отсортированный по дате,
    имеет возможность сортировки по возрастанию или убыванию
    """
    sort_date = sorted(unsort_date, key=lambda unsort_date: unsort_date["date"], reverse=sort)
    return sort_date
