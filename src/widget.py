from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_inform: str) -> str:
    """Функция маскировки номера карты/счета с выводом карты/счета"""
    list_card_inform = card_inform.split()
    card_name = ""
    card_account = ""
    mask_number = ""
    for i in list_card_inform:
        if i.isalpha():
            card_name += i + " "
        if i.isdigit():
            card_account += i
    if "Счет" in card_inform:
        mask_number = get_mask_account(card_account)
    else:
        mask_number = get_mask_card_number(card_account)
    return f"{card_name}{mask_number}"


def get_date(date_time: str) -> str:
    """Функция вывода даты"""
    date = date_time[8:10] + "." + date_time[5:7] + "." + date_time[:4]
    return date
