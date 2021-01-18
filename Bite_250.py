from math import floor
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits
from typing import Dict
from copy import deepcopy

CODEX: str = digits + ascii_lowercase + ascii_uppercase
BASE: int = len(CODEX)
# makeshift database record
LINKS: Dict[int, str] = {
    1: "https://pybit.es",
    45: "https://pybit.es/pages/articles.html",
    255: "http://pbreadinglist.herokuapp.com",
    600: "https://pybit.es/pages/challenges.html",
    874: "https://stackoverflow.com",
}
SITE: str = "https://pybit.es"

# error messages
INVALID = "Not a valid PyBites shortened url"
NO_RECORD = "Not a valid shortened url"


def encode(record: int) -> str:
    """Encodes an integer into Base62"""
    if record < 62:
        return CODEX[record]
    return encode(record // 62) + encode(record % 62)


def decode(short_url: str) -> int:
    """Decodes the Base62 string into a Base10 integer"""
    number = 0
    
    for i, n in enumerate(short_url[::-1]):
        number += CODEX.index(n) * 62 ** i
    return int(number)


def redirect(url: str) -> str:
    """Retrieves URL from shortened DB (LINKS)

    1. Check for valid domain
    2. Check if record exists
    3. Return URL stored in LINKS or proper message
    """
    
    end = decode(url.split('/')[-1])
    
    if SITE not in url:
        return INVALID
    if not LINKS.get(end):
        return NO_RECORD
    
    return LINKS[end]
    
    
def shorten_url(url: str, next_record: int) -> str:
    """Shortens URL and updates the LINKS DB

    1. Encode next_record
    2. Adds url to LINKS
    3. Return shortened URL
    """
    new_record = encode(next_record)
    LINKS[next_record] = url
    return f'{SITE}/{new_record}'


#print(encode(5120))
print(decode('e6'))
print(shorten_url("https://youtube.com", 6000))
print(redirect("https://pybit.es/1yM"))
print(LINKS)
