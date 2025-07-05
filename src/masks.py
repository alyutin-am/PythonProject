def get_mask_card_number(card_number: str) -> str:
    """Функция скрытия номера карты (замены части номера карты на '*')"""
    if len(card_number) != 16 or card_number.isdigit() == False:
        return "Неверный номер карты"
    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(mask_account: str) -> str:
    """Функция скрытия номера счета (замены части номера счета на '*')"""
    if len(mask_account) != 20 or mask_account.isdigit() == False:
        return "Неверный номер счета"
    return f"**{mask_account[-4:]}"
