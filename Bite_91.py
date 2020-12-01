import re
import string

VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    consonants = ''.join([l for l in string.ascii_lowercase if l not in VOWELS])
    
    search = re.search(rf'[aeiou]+', input_str.lower()).span()
    high = search[1] 
    low = search[0]

    if high - low == len(input_str):
        return True
    return False
        


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    pass


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    pass


print(contains_only_vowels('aaAiIee'))