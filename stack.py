class Stack:
    def __init__(self):
        self.stack = []
    
    def size(self):
        return len(self.stack)
    
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return self.stack == []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        return self.stack.pop()


