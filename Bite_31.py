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
        # left = None
        # right = None

        # if len(left) >= len(right):
        #     left = left
        #     right = right
        # else:
        #     left = right
        #     right = left
        
        
        for i in range(len(left)):
            for j in range(len(left[i])):
                if left[i][j] == left[0][0]:
                    total += (left[i][j] * right[i][j]) + (left[i][j] * right[i][j+1])
                    total += (left[i+1][j] * right[i][j]) + (left[i+1][j] * right[i][j+1])
                    total += (left[i][j+1] * right[i+1][j]) + (left[i][j+1] * right[i+1][j+1])
                    total += (left[i+1][j+1] * right[i+1][j]) + (left[i+1][j+1] * right[i+1][j+1])
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

