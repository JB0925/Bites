from string import digits

def positive_divide(numerator, denominator):
    try:
        retval = numerator / denominator
    
    except(ZeroDivisionError, TypeError):
        if denominator == 0:
            return 0
        if all(d not in digits for d in str(numerator)) or\
            all(d not in digits for d in str(denominator)):
            raise
    else:
        if retval < 0:
            raise ValueError
        return retval


print(positive_divide(1, ))