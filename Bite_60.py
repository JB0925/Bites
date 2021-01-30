from collections import namedtuple

SUITS = 'Red Green Yellow Blue'.split()

UnoCard = namedtuple('UnoCard', 'suit name')


def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    digits = [0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,'Draw Two', 'Draw Two',\
        'Skip', 'Skip', 'Reverse', 'Reverse']
    wilds = ['Wild', 'Wild Draw Four']
    
    cards = [UnoCard(suit=suit, name=str(name)) for suit in SUITS for name in digits]
    cards.extend([UnoCard(suit=None, name=name) for name in wilds for _ in range(4)])
    return cards


print(create_uno_deck())