import datetime

import functools


def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            time_start = None
            time_finish = None
            try:
                time_start = datetime.datetime.now()
                result = func(*args, **kwargs)
                time_finish = datetime.datetime.now()
                log_message = (
                    f"{func.__name__} ok. Inputs: {args}, {kwargs}. Start time: {time_start},"
                    f" End time: {time_finish}"
                )
            except Exception as error:
                log_message = (
                    f"{func.__name__} error: {error}. Inputs: {args}, {kwargs}. Start time: {time_start}, "
                    f"End time: {time_finish}"
                )
            if not filename is None:
                with open(filename, "a") as f:
                    f.write(log_message + "\n")
            else:
                print(log_message)
            return result

        return wrapper

    return decorator



def function_for_test(a, b):
    result = a / b
    print(result)
    return result

function_for_test = log(function_for_test(3,3))