from masks import get_mask_card_number
from masks import get_mask_account


def mask_account_card(card_inform: str) -> str:
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


def get_date():
    pass


card_inform = "Maestro 1596837868705199"
result = mask_account_card(card_inform)
print(result)