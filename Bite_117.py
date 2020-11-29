from copy import copy

def round_even(number):
    """Takes a number and returns it rounded even"""
    num = copy(number)
    number = str(number)
    evens = '0 2 4 6 8'.split()

    if number[2] <= '5' and number[0] in evens:
        return int(number[0])
    
    return round(num) 
        


print(round_even(2.5))