class Matrix(object):

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'
    
    def __matmul__(self, other):
        self.values_list = []
        left_list = []
        right_list = []

        if isinstance(other, Matrix):
            right = other.values
        else:
            right = other
        
        total = 0
        left = self.values
        
        for i in range(len(left)):
            for j in range(len(left[i])):
                if left[i][j] == left[0][0]:
                    total += (left[i][j] * right[i][j]) + (left[i][j] * right[i][j+1])
                    left_list.append((left[i][j] * right[i][j]) + (left[i][j+1] * right[i+1][j]))
                    left_list.append((left[i][j] * right[i][j+1]) + (left[i][j+1] * right[i+1][j+1]))
                    total += (left[i+1][j] * right[i][j]) + (left[i+1][j] * right[i][j+1])
                    total += (left[i][j+1] * right[i+1][j]) + (left[i][j+1] * right[i+1][j+1])
                    right_list.append((left[i+1][j] * right[i][j]) + (left[i+1][j+1] * right[i+1][j]))
                    right_list.append((left[i+1][j] * right[i][j+1]) + (left[i+1][j+1] * right[i+1][j+1]))
                    total += (left[i+1][j+1] * right[i+1][j]) + (left[i+1][j+1] * right[i+1][j+1])
            break
        self.values_list = [left_list, right_list]
        return self.values_list
    

    def __rmatmul__(self, other):
        m = Matrix(self.values)
        return m @ other
    

    def __imatmul__(self, other):
        m = Matrix(self.values)
        m = m @ other
        return m
    






x = [[1,2],[3,4]]
y = [[11,12],[13,14]]

m = Matrix(x)
m2 = Matrix(y)
print(m @ m2)

