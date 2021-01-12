from collections import Counter

def major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """
    tally = Counter(numbers)
    major = tally.most_common(1)[0][0]
    minor = tally.most_common()[:len(tally)-2:-1][0][0]

    return major, minor


print(major_n_minor([1, 2, 3, 2, 2, 2, 3]))