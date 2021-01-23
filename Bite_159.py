import operator
from string import digits

def simple_calculator(calculation):
    """Receives 'calculation' and returns the calculated result,

       Examples - input -> output:
       '2 * 3' -> 6
       '2 + 6' -> 8

       Support +, -, * and /, use "true" division (so 2/3 is .66
       rather than 0)

       Make sure you convert both numbers to ints.
       If bad data is passed in, raise a ValueError.
    """
    digits_ = digits + '-'
    operators = {'+': operator.add, '-': operator.sub, \
        '*': operator.mul, '/': operator.truediv}
        
    number1, op, number2 = calculation.split()
    
    if any(d not in digits_ for d in number1) or any(d not in digits_ for d in number2):
        raise ValueError ('digits must come before and after the operand')
    if op == '/' and number2 == '0':
        raise ValueError ('cannot divide by zero')
    if op not in operators:
        raise ValueError ('not a valid operand for this calculator')
    
    return operators.get(op)(int(number1), int(number2))
    
    
