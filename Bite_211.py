from functools import wraps
import random

MAX_RETRIES = 3


class MaxRetriesException(Exception):
    pass


def retry(func):
    """Complete this decorator, make sure
       you print the exception thrown"""
    # ... retry MAX_RETRIES times
    # ...
    # make sure you include this for testing:
    # except Exception as exc:
    #     print(exc)
    # ...
    # and use wraps to preserve docstring
    #
    @wraps(func)
    def wrapper(*args, **kwargs):
        count = 0
        while count != MAX_RETRIES - 1:
            try:
                return func(*args, **kwargs)
            except Exception as exc:
                print(exc)
            count += 1
        raise MaxRetriesException
    return wrapper


@retry
def get_two_numbers(numbers):
    for num in numbers:
        x = 2 / num
    return x


print(get_two_numbers([2, 'b']))