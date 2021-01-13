from functools import lru_cache


def num_ops(n,memo={1: None}):
    """
    Input: an integer number, the target number
    Output: the minimum number of operations required to reach to n from 1.

    Two operations rules:
    1.  multiply by 2
    2.  int. divide by 3

    The base number is 1. Meaning the operation will always start with 1
    These rules can be run in any order, and can be run independently.

    [Hint] the data structure is the key to solve it efficiently.
    """
    ops_num = 0
    start =[1]

    while True:
        new_added = []
        for x in start:
            if 2*x not in memo:
                memo[2*x] = [x, 2]
                new_added.append(2*x)
            if x//3 not in memo:
                memo[x//3] = [x,3]
                new_added.append(x//3)
        ops_num += 1
        if n in memo:
            break
        
        start[:] = new_added
    
    return ops_num


    



print(num_ops(2020,{}))






