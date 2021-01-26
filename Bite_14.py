import random

names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
aliases = 'Pythonista Nerd Coder'.split() * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = ' | '


def generate_table(*args):
    result = []
    table = list(zip(*args))
    for item in table:
        result.append(SEPARATOR.join(list(str(x) for x in item)))
    return result


print(generate_table(names, aliases))
    