def countdown():
    """Write a generator that counts from 100 to 1"""
    i = 100
    while i > 0:
        yield i
        i -= 1




c = countdown()
print(next(c))
print(next(c))