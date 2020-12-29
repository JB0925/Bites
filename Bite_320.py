from dataclasses import dataclass
import enum
from typing import List  # TODO: can remove >= 3.9
from collections import namedtuple


# 1. make a BiteLevel enum class
# keys = INTRO BEGINNER INTERMEDIATE ADVANCED
# values = 1 2 3 4
# make sure they can be sorted by int value
bitedata = namedtuple('bitedata', 'number title level')

class BiteLevel(enum.IntEnum):
    __order__ = 'INTRO BEGINNER INTERMEDIATE ADVANCED'
    INTRO = 1 
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4


# 2. make a dataclass that can be ordered
# attributes: number (int), title (str), level (BiteLevel)
@dataclass
class Bite:
    number: int
    title: str
    level: BiteLevel
    
    def __lt__(self,other):
        return self.number < other.number


# 3. complete the function below

def create_bites(numbers: List[int], titles: List[str],
                 levels: List[BiteLevel]):
    """Generate a generator of Bite dataclass objects"""
    for i in range(len(numbers)):
        bite = bitedata(number=numbers[i], title=titles[i], level=list(levels)[i])
        yield Bite(bite.number, bite.title, bite.level)
    

NUMBERS = [101, 1, 97, 2]
TITLES = 'f-string,sum numbers,scrape holidays,regex fun'.split(',')
b = BiteLevel.__members__.values()

for item in create_bites(NUMBERS,TITLES,b):
    print(item)

# x = Bite(number=7, title='why', level=BiteLevel.INTRO)
# print(x)

# x = [NUMBERS, TITLES, b]
# print(x)