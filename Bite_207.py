from random import random
from time import sleep
from functools import wraps


def cached_property(func):
    """decorator used to cache expensive object attribute lookup"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        mass_dict = {}
        name = args[0]
        value = func(*args, **kwargs)
        for k in mass_dict.keys():
            if name == k:
                raise AttributeError
        mass_dict[name] = value
        return mass_dict[name]

    return wrapper
        


class Planet:
    """the nicest little orb this side of Orion's Belt"""

    GRAVITY_CONSTANT = 42
    TEMPORAL_SHIFT = 0.12345
    SOLAR_MASS_UNITS = 'M\N{SUN}'

    def __init__(self, color):
        self.color = color
        self._mass = None

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.color)})'

    #@property
    @cached_property
    def mass(self):
        scale_factor = random()
        sleep(self.TEMPORAL_SHIFT)
        self._mass = (f'{round(scale_factor * self.GRAVITY_CONSTANT, 4)} '
                      f'{self.SOLAR_MASS_UNITS}')
        return self._mass

    # @mass.setter
    # def mass(self, value):
    #     self._mass = value

planet = Planet('blue')
planet._mass = 5
print(planet.mass)
