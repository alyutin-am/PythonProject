def get_mask_card_number(card_number: str) -> str:
    """Функция скрытия номера карты (замены части номера карты на '*')"""
    if isinstance(card_number, str):
        if len(card_number) != 16 or not card_number.isdigit():
            return "Неверный номер карты"
        return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}"
    else:
        return "Неверный тип данных"


def get_mask_account(mask_account: str) -> str:
    """Функция скрытия номера счета (замены части номера счета на '*')"""
    if isinstance(mask_account, str):
        if len(mask_account) != 20 or not mask_account.isdigit():
            return "Неверный номер счета"
        return f"**{mask_account[-4:]}"
    else:
        return "Неверный тип данных"
