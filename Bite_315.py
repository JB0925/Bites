import logging
from typing import List  # python 3.9 we can drop this


logger = logging.getLogger('app')


def sum_even_numbers(numbers: List[float]) -> float:
    """
    1. Of the numbers passed in sum the even ones
       and return the result.
    2. If all goes well log an INFO message:
       Input: {numbers} -> output: {ret}
    3. If bad inputs are passed in
       (e.g. one of the numbers is a str), catch
       the exception log it, then reraise it.
    """
    logging.basicConfig(level=logging.INFO)
    try:
        output = sum([n for n in numbers if n % 2 == 0])
        logger.info(f'Input: {numbers} -> output: {output}')
        return output
        
    except TypeError as t:
        logger.exception(f'Bad inputs: {numbers}')
        raise 
        
    
    
    

print(sum_even_numbers([1,2,3,'a',5,6]))

