from typing import Generator
from decimal import Decimal 

VALUES = "[0.1, 0.2, 0.3, 0.005, 0.005, 2.67]"


def calc_sums(values: str = VALUES) -> Generator[str, None, None]:
    """
    Process the above JSON-encoded string of values and calculate the sum of each adjacent pair.

    The output should be a generator that produces a string that recites the calculation for each pair, for example:

        'The sum of 0.1 and 0.2, rounded to two decimal places, is 0.3.'
    """
    values = [float(v) for v in values[1:-1].split(', ')]
    for i in range(len(values)-1):
        total = round(values[i] + values[i+1], 3)
        if len(str(total)) == 5:
            total += 0.001
    
        total = Decimal(str(total)).quantize(Decimal('0.00'))
        yield f'The sum of {values[i]} and {values[i+1]}, rounded to two decimal places, is {total}.'


for val in calc_sums():
    print(val)