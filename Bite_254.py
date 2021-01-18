num_hundreds = -1


def sum_numbers(numbers: list) -> int:
    """Sums passed in numbers returning the total, also
       update the global variable num_hundreds with the amount
       of times 100 fits in total"""
    global num_hundreds

    result = str(sum(numbers))
    num_hundreds += int(result[0]) if len(result) == 3 else 10\
        * int(result[0]) + int(result[1]) if len(result) == 4 else 0
    return int(result)



print(sum_numbers([140, 50, 60]))
print(num_hundreds)
