def filter_by_state(dictionaries: list, state='EXECUTED') -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ соответствует указанному значению, по умолчанию 'EXECUTED'"""
    new_data = []
    for dictionary in dictionaries:
        if state in dictionary["state"]:
            new_data.append(dictionary)
    return new_data


def sort_by_date(sort_list: list, reverse=True) -> list:
    """Функция должна возвращать новый список, отсортированный по дате, имеет возможность 'реверса'"""
    pass

