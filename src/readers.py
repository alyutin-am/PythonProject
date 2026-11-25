import logging
from pathlib import Path
from typing import Any, Dict, List, cast

import pandas as pd

LOG_DIR = Path(__file__).resolve().parent.parent / "Logs"
LOG_DIR.mkdir(exist_ok=True)

logger = logging.getLogger('readers')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    LOG_DIR / "readers.log", mode="w", encoding="utf-8"
)
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.propagate = False


def read_csv_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые транзакции из CSV-файла.
    """
    logger.info(f"Попытка чтения CSV файла: {file_path}")
    try:
        df = pd.read_csv(file_path)
        transactions: List[Dict[str, Any]] = cast(List[Dict[str, Any]], df.to_dict(orient='records'))
        if not transactions:
            logger.warning(f"CSV файл пуст: {file_path}")
            return []
        logger.info(f"Успешно прочитано {len(transactions)} транзакций из CSV")
        return transactions

    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []
    except pd.errors.EmptyDataError:
        logger.error(f"Файл пуст или не содержит данных: {file_path}")
        return []
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV файла {file_path}: {e}")
        return []


def read_excel_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые транзакции из Excel-файла (XLSX).
    """
    logger.info(f"Попытка чтения Excel файла: {file_path}")
    try:
        df = pd.read_excel(file_path)
        transactions: List[Dict[str, Any]] = cast(List[Dict[str, Any]], df.to_dict(orient='records'))
        if not transactions:
            logger.warning(f"Excel файл пуст: {file_path}")
            return []
        logger.info(f"Успешно прочитано {len(transactions)} транзакций из Excel")
        return transactions
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []
    except Exception as e:
        logger.error(f"Ошибка при чтении Excel файла {file_path}: {e}")
        return []
