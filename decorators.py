import datetime
import functools
from typing import Any, Callable, Optional, TypeVar

T = TypeVar("T")


def log(filename: Optional[str] = None) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """Декоратор автоматически регистрирует детали выполнения функций: время вызова, имя функции,
    передаваемые аргументы, результат выполнения и информация об ошибках"""

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            result: Optional[T] = None
            time_start: Optional[datetime.datetime] = None
            time_finish: Optional[datetime.datetime] = None

            try:
                time_start = datetime.datetime.now()
                result = func(*args, **kwargs)
                time_finish = datetime.datetime.now()
                log_message = (
                    f"{func.__name__} ok. Inputs: {args}, {kwargs}. Start time: {time_start},"
                    f" End time: {time_finish}"
                )
            except Exception as error:
                time_finish = datetime.datetime.now()
                log_message = (
                    f"{func.__name__} error: {error}. Inputs: {args}, {kwargs}. Start time: {time_start}, "
                    f"End time: {time_finish}"
                )
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)
                raise

            if filename:
                with open(filename, "a") as f:
                    f.write(log_message + "\n")
            else:
                print(log_message)
            return result

        return wrapper

    return decorator
