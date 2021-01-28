from collections import namedtuple
from string import ascii_uppercase
import random
from itertools import cycle

ACTIONS = ['draw_card', 'play_again',
           'interchange_cards', 'change_turn_direction']
NUMBERS = range(1, 5)

PawCard = namedtuple('PawCard', 'card action')

def create_paw_deck(n=8):
    if n > 26:
        raise ValueError

    letters = [ascii_uppercase[i] for i in range(n)]
    numbers = list(NUMBERS)
    c = cycle(ACTIONS)
    actions = [next(c) for i in range(n)]
    result = []

    for letter in letters:
        temp = []
        options = [None, None, None, random.choice(actions)]
        for number in numbers:
            p = PawCard(card=f'{letter}{number}', action=random.choice(options))
            idx = options.index(p.action)
            del options[idx]
            temp.append(p)

            if p.action in actions:
                actions.remove(p.action)
        result.extend(temp)

    return result




print(create_paw_deck(4))