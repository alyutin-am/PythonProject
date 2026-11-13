import json
import logging
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parent.parent / "Logs"
LOG_DIR.mkdir(exist_ok=True)

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    LOG_DIR / "utils.log", mode="w", encoding="utf-8"
)
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.propagate = False


def get_transactions(operations: str | Path) -> list:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        try:
            with open(operations, encoding="utf-8") as json_file:
                result = json.load(json_file)
                if type(result) is list:
                    logger.info("Загружено транзакций: %d из %s", len(result), operations)
                    return result
                else:
                    logger.error("JSON не является списком (%s): %s", type(result).__name__, operations)
                    return []
        except json.JSONDecodeError:
            logger.error("Некорректный JSON или пустой файл: %s", operations)
            return []
    except FileNotFoundError:
        logger.error("Файл не найден: %s", operations)
        return []
