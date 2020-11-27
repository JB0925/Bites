from typing import Tuple
from collections import Counter, namedtuple
from operator import attrgetter
from copy import copy

def max_letter_word(text: str) -> Tuple[str, str, int]:
    """
    Find the word in text with the most repeated letters. If more than one word
    has the highest number of repeated letters choose the first one. Return a
    tuple of the word, the (first) repeated letter and the count of that letter
    in the word.
    >>> max_letter_word('I have just returned from a visit...')
    ('returned', 'r', 2)
    >>> max_letter_word('$5000 !!')
    ('', '', 0)
    """
    if text != str(text):
        raise ValueError

    chars = [' ', '-', "'"]
    copytext = ''.join([t for t in text if t.isalpha() or t in chars]).split()
    words = []
    letters = namedtuple('letters', 'word letter count index')
    text = ''.join([t for t in text if t.isalpha() or t == ' ']).split()
    
    for word in text:
        count = Counter(word.casefold())
        l = letters(word=word, letter=count.most_common()[0][0], count=count.most_common()[0][1], index=text.index(word))
        words.append(l)
    
    words = sorted(words, key=lambda x: x.count, reverse=True)
    if words != []:
        maxcount = words[0].count
    
    words = [item for item in words if item.count == maxcount]
    words = sorted(words, key=lambda x: x.index)

    if words != []:
        idx = words[0].index
    return ('', '', 0) if words == [] else (copytext[idx], words[0].letter, words[0].count)





print(max_letter_word(1.0))