def calc_median_from_dict(d: dict) -> float:
    """
    :param d: dict of numbers and their occurrences
    :return: float: median
    Example:
    {1: 2, 3: 1, 4: 2} -> [1, 1, 3, 4, 4] --> 3 is median
    """

    # TODO: Your code
    # nums_list = []
    # for k,v in d.items():
    #     if type(v) != int:
    #         raise TypeError
    #     nums_list.extend([k] * v)
    
    # median = sum(nums_list) / len(nums_list)
    # return median
    keys = 0
    values = 0
    for k, v in d.items():
        if type(v) != int:
            raise TypeError
        keys += k * v
        values += v
    
    return int(keys / values)


x = {1:1_000_000_000_000_000, 2:1, 3:1_000_000_000_000_000}

y = {
                0: 800_000_000,
                1: 200_000_000,
                2: 200_000_000,
                3: 200_000_000,
                4: 200_000_000,
                5: 1_000_000_000,
                6: 20_000_000_000,
                7: 4_000_000_000,
                8: 8_000_000_000,
                9: 16_000_000_000,
            }
print(calc_median_from_dict(y))