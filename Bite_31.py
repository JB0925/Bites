class Matrix(object):

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'
    
    def __matmul__(self, other):
        self.values_list = []
        left_list = []
        right_list = []
        left = self.values


        if isinstance(other, Matrix):
            right = other.values
        else:
            right = other
        
        
        for i in range(len(left)):
            for j in range(len(left[i])):
                if left[i][j] == left[0][0]:
                    left_list.append((left[i][j] * right[i][j]) + (left[i][j+1] * right[i+1][j]))
                    left_list.append((left[i][j] * right[i][j+1]) + (left[i][j+1] * right[i+1][j+1]))
                    right_list.append((left[i+1][j] * right[i][j]) + (left[i+1][j+1] * right[i+1][j]))
                    right_list.append((left[i+1][j] * right[i][j+1]) + (left[i+1][j+1] * right[i+1][j+1]))
            break

        self.values_list = [left_list, right_list]
        return Matrix(self.values_list)
    

    def __rmatmul__(self, other):
        m = Matrix(self.values)
        m = m @ other
        return m
    

    def __imatmul__(self, other):
        m = Matrix(self.values)
        m = m @ other
        return m
    






x = [[1,2],[3,4]]
y = [[11,12],[13,14]]

m = Matrix(y)
m2 = Matrix(x)
print(m @ m2)
print(m2 @ m)
tot = y @ m2
print(tot)
type(tot)
m2 @= m
print(type(m2))
print(m2)

m3 = m @ m2
print(m3)
print(type(m3))
