def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    conversions = {'cm': round(value * 2.54, 4),
                   'in': round(value * 0.393701, 4)}

    if type(value) != float and type(value) != int:
        raise TypeError
    
    if fmt.lower() != 'in' and fmt.lower() != 'cm':
        raise ValueError
    
    return conversions.get(fmt.lower(), None)


print(convert(60.5, 'CM'))