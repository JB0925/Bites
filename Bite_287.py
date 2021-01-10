from typing import List


def sum_indices(items: List[str]) -> int:
    duplicates = {}
    total = 0
    for i in range(len(items)):
        if items[i] in duplicates:
            duplicates[items[i]] += i
        else:
            duplicates[items[i]] = i
        
        total += max(items.index(items[i]), duplicates[items[i]])
    
    return total



print(sum_indices(['a', 'b', 'z', 'c', 'd', 'x', 'b', 'x', 'e']))