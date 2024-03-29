from enum import Enum
from copy import copy


class Equality(Enum):
    SAME_REFERENCE = 4
    SAME_ORDERED = 3
    SAME_UNORDERED = 2
    SAME_UNORDERED_DEDUPED = 1
    NO_EQUALITY = 0


def check_equality(list1, list2):
    """Check if list1 and list2 are equal returning the kind of equality.
       Use the values in the Equality Enum:
       - return SAME_REFERENCE if both lists reference the same object
       - return SAME_ORDERED if they have the same content and order
       - return SAME_UNORDERED if they have the same content unordered
       - return SAME_UNORDERED_DEDUPED if they have the same unordered content
         and reduced to unique items
       - return NO_EQUALITY if none of the previous cases match"""
    if set(list1) != set(list2):
        return Equality.NO_EQUALITY
    
    elif list1 is list2:
        return Equality.SAME_REFERENCE
    
    elif list1 == list2:
        return Equality.SAME_ORDERED
    
    elif len(set(list1) ^ set(list2)) == 0 and len(list1) == len(list2):
        return Equality.SAME_UNORDERED
    
    else:
        return Equality.SAME_UNORDERED_DEDUPED
    
    
    




a = [1, 2, 3]
b = [4, 5, 7]

print(check_equality(a, b))