from typing import List
from random import sample


def minimum_number(digits: List[int]) -> int:
    if digits == []:
        return 0

    digits = list(set(digits))
    smallest_number = []

    while digits:
        least = min(digits)
        smallest_number.append(str(least))
        del digits[digits.index(least)]
    
    return int(''.join(smallest_number))



print(minimum_number(sample(range(0, 6), 6)))