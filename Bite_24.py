from abc import ABC, abstractmethod
import random


class Challenge(ABC):
    def __init__(self, number, title):
        super().__init__()
        self.number = number
        self.title = title
    
    @abstractmethod
    def verify(self):
        pass
    
    @abstractmethod
    def pretty_title(self):
        pass

class BlogChallenge(Challenge):
    def __init__(self, merged_prs, number, title):
        super().__init__(number, title)
        self.merged_prs = merged_prs
        self.number = number
        self.title = title
    

    def verify(self, other):
        super().verify()
        return other in self.merged_prs
    
    @property
    def pretty_title(self):
        super().pretty_title()
        return f'PCC1 - {self.title}'
        

class BiteChallenge(Challenge):
    def __init__(self, result, number, title):
        super().__init__(number, title)
        self.result = result
        self.number = number
        self.title = title
    
    def verify(self, statement):
        return self.result == statement
    
    @property
    def pretty_title(self):
        return f'Bite {self.number}. {self.title}'
    
merged_prs = [41,42,44]
num = random.choice(merged_prs)
blog = BlogChallenge(merged_prs, 1, 'Wordvalues')
print(blog.verify(39))
print(blog.pretty_title)

bite = BiteChallenge('my result', 24, 'ABC and class inheritance')
print(bite.verify('other result'))