import argparse
from functools import reduce
import operator


def calculator(operation, numbers):
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals"""
    numbers = [float(n) for n in numbers]
    operators = {'add': operator.add,
                 'sub': operator.sub,
                 'mul': operator.mul}
    
    if operation == 'div':
        return round(reduce(lambda a,b: a/b, numbers), 2)

    op = operators.get(operation)
    answer = str(reduce(lambda a,b: op(a, b), numbers))
    if len(answer) > 4:
        if '-' in answer:
            return float(answer[0:5])
        else:
            return float(answer[0:4])
    
    return float(answer)
    
    
def create_parser():
    """TODO 2:
       Create an ArgumentParser object:
       - have one operation argument,
       - have one or more integers that can be operated on.
       Returns a argparse.ArgumentParser object.

       Note that type=float times out here so do the casting in the calculator
       function above!"""
    parser = argparse.ArgumentParser(prog='calculator', usage='calculator.py [-h]'
            '[-a ADD [ADD ...]] [-s SUB [SUB ...]] [-m MUL [MUL ...]] [-d DIV [DIV ...]]',\
             description='a simple calculator')
    parser.add_argument('-a', '--add', help='Sums numbers', nargs='+')
    parser.add_argument('-s', '--sub', help='Subtracts numbers', nargs='+')
    parser.add_argument('-m', '--mul', help='Multiplies numbers', nargs='+')
    parser.add_argument('-d', '--div', help='Divides numbers', nargs='+')
    
    return parser


def call_calculator(args=None, stdout=False):
    """Provided/done:
       Calls calculator with provided args object.
       If args are not provided get them via create_parser,
       if stdout is True print the result"""
    parser = create_parser()

    if args is None:
        args = parser.parse_args()

    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    for operation, numbers in vars(args).items():
        if numbers is None:
            continue

        try:
            res = calculator(operation, numbers)
        except ZeroDivisionError:
            res = 0

        if stdout:
            print(res)

        return res


if __name__ == '__main__':
    call_calculator(stdout=True)