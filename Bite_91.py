import re
import string

VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    consonants = ''.join([l for l in string.ascii_lowercase if l not in VOWELS])
    
    search = re.search(rf'[aeiou]+', input_str, re.IGNORECASE).span()
    high = search[1] 
    low = search[0]

    if high - low == len(input_str):
        return True
    return False
        


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    search = re.findall(r'[python]+', input_str, re.IGNORECASE)
    return len(search) >= 1


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    search = re.findall(r'[\d]+', input_str)
    return len(search) >= 1


#print(contains_only_vowels('aaAiIee'))
#print(contains_any_py_chars('123'))
#print(contains_digits('hello2'))