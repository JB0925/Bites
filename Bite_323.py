from functools import reduce
from typing import Iterable, Set, Any


def intersection(*args: Iterable) -> Set[Any]:
    try:
        return set((reduce(lambda i, j: i & j, (set(arg)\
             for arg in args if arg != None and len(arg) >= 1))))
    
    except TypeError:
        return set()





print(intersection([1,2,3,3,2,1]))