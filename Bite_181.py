from bisect import insort


class OrderedList:

    def __init__(self):
        self._numbers = []

    def add(self, num):
        insort(self._numbers, num)

    def __str__(self):
        return ', '.join(str(num) for num in self._numbers)
