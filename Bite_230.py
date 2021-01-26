THUMBS_UP, THUMBS_DOWN = '👍', '👎'


class Thumbs:
    def __init__(self) -> None:
        self.up = THUMBS_UP
        self.down = THUMBS_DOWN


    def __mul__(self, other):
        if other == 0:
            raise ValueError
        
        elif other < 0:
            if other in [-3,-2,-1]:
                return THUMBS_DOWN * abs(other)
            else:
                return f'{THUMBS_DOWN} ({other}x)'
        else:
            if other in [1,2,3]:
                return THUMBS_UP * other
            else:
                return f'{THUMBS_UP} ({other}x)'
    

    def __rmul__(self, other):
        self, other = other, self
        return other * self


t = Thumbs()
print(0 * t)