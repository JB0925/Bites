from random import choice

def round_to_next(number: int, multiple: int):
    total = 0
    match = 0
    i = 0

    while True:
        total = multiple * i
        if number < 0 and multiple < 0:
            if total <= number:
                return total
        
        else:
            if abs(number) == abs(multiple) and number < multiple:
                total = -multiple * i
                if total <= number:
                    return total
            else:
                if total >= number:
                    return total
        i += 1
        



print(round_to_next(-6,-10))