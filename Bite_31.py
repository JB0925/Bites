class Matrix(object):

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'
    
    def __matmul__(self, other):
        if isinstance(other, Matrix):
            right = other.values
        else:
            right = other
        
        total = 0
        left = self.values
        larger = None
        smaller = None

        if len(left) >= len(right):
            larger = left
            smaller = right
        else:
            larger = right
            smaller = left
        
        
        for i in range(len(larger)):
            for j in range(len(larger[i])):
                if larger[i][j] == larger[0][0]:
                    total += (larger[i][j] * smaller[i][j]) + (larger[i][j] * smaller[i][j+1])
                    total += (larger[i+1][j] * smaller[i][j]) + (larger[i+1][j] * smaller[i][j+1])
                    total += (larger[i][j+1] * smaller[i+1][j]) + (larger[i][j+1] * smaller[i+1][j+1])
                    total += (larger[i+1][j+1] * smaller[i+1][j]) + (larger[i+1][j+1] * smaller[i+1][j+1])
            break
                
        return total
    

    def __rmatmul__(self, other):
        m = Matrix(self.values)
        return m @ other
    






x = [[1,2],[3,4]]
y = [[11,12],[13,14]]

m = Matrix(x)
m2 = Matrix(y)
print(m @ m2)
print(m.values)
print(m2.values)
