def convert(number: int, base: int = 2) -> str:
    """Converts an integer into any base between 2 and 36 inclusive

    Args:
        number (int): Integer to convert
        base (int, optional): The base to convert the integer to. Defaults to 2.

    Raises:
        Exception (ValueError): If base is less than 2 or greater than 36

    Returns:
        str: The returned value as a string
    """
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    if base < 2 or base > 36:
        raise ValueError ('Sorry, the base needs to be between 2 and 36')
    
    if number <= base:
        if digits[number] == 'Q':
            num = '10' + str(number)[-1]
            return num[:2]
        else:
            return digits[number]
    else:
        return convert(number // base, base) + convert(number % base, base) 



print(convert(126,2))