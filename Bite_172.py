from functools import partial

# create 2 partials:
# - 'rounder_int' rounds to int (0 places)
# - 'rounder_detailed' rounds to 4 places
rounder_int =  0
rounder_detailed =  0


def round_to_int(num, places):
    return round(num, places)


rounder_int = partial(round_to_int, places=0)
rounder_detailed = partial(round_to_int, places=4)
print(rounder_detailed(10.4232567))

