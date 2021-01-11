from typing import List


def pascal(N: int) -> List[int]:
    """
    Return the Nth row of Pascal triangle
    """
    if N <= 0:
        return []

    triangle = []
    i = 1

    while i <= N:
        temp = []
        if i == 1:
            temp.append(1)
            triangle.append(temp)
        else:
            temp.append(1)
            for j in range(len(triangle[-1])-1):
                next_number = triangle[-1][j] + triangle[-1][j+1]
                temp.append(next_number)
            temp.append(1)
            triangle.append(temp)
        i += 1
    
    return triangle[-1]

print(pascal(5))

