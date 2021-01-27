from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:
    def __init__(self, limit: int):
        self.limit = limit
        self.count = 0
    
    
    def __iter__(self):
        return self
    
    
    def __next__(self):
        self.count += 1 
        if self.count > self.limit:
            raise StopIteration
        
        return f'{choice(COLORS)} egg'


for egg in EggCreator(5):
    print(egg)