import logging
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parent.parent / "Logs"
LOG_DIR.mkdir(exist_ok=True)

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    LOG_DIR / "masks.log", mode="w", encoding="utf-8"
)
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.propagate = False


def get_mask_card_number(card_number: str) -> str:
    """Функция скрытия номера карты (замены части номера карты на '*')"""
    logger.info('Запуск функции скрытия номера карты')
    if isinstance(card_number, str):
        if len(card_number) != 16 or not card_number.isdigit():
            logger.error('Номер карты неверен')
            return "Номер карты неверен"
        logger.info('Номер карты верен, скрытие номера произведено')
        return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}"
    else:
        logger.error('Неверный тип данных функции скрытия номера карты')
        return "Неверный тип данных"


def get_mask_account(mask_account: str) -> str:
    """Функция скрытия номера счета (замены части номера счета на '*')"""
    logger.info('Запуск функции скрытия номера счета')
    if isinstance(mask_account, str):
        if len(mask_account) != 20 or not mask_account.isdigit():
            logger.error('Неверный номер счета')
            return "Неверный номер счета"
        logger.info('Номер счета верен. Скрытие произведено')
        return f"**{mask_account[-4:]}"
    else:
        logger.error('Неверный тип данных при работе функции скрытия номера счета')
        return "Неверный тип данных"
