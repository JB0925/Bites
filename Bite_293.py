from typing import List, TypeVar
T = TypeVar('T', int, float)


test = [1,2,3]
test2 = [0,1,2,3]
test3 = [8,9,10]
test4 = [5.2, 1600, 520, 3600, 13, 55, 4000]

def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    if n < 1:
        raise ValueError ('Sorry, n needs to be a positive integer')
    
    numbers = [str(x) for x in numbers]
    period = '.'
    new_numbers = []
    negative_numbers = [x[:2] for x in numbers if '-' in x]

    for num in numbers:
        num = num.replace(period, '').replace('-', '')

        if len(num) == n:
            new_numbers.append(int(num))
        
        if len(num) < n:
            amount = n - len(num)
            num = num.ljust(n, '0')
            new_numbers.append(int(num))
        
        if len(num) > n:
            
            difference = len(num) - 2
            if '-' + str(num)[0] in negative_numbers:
                num = num[:difference+1]
            else:
                num = num[:n]
            
            new_numbers.append(int(num))
    
    return [-x if '-' + str(x)[0] in negative_numbers else x for x in new_numbers]
    






print(n_digit_numbers([-1.1, 2.22, -3.333, 4444, 55555], 4))