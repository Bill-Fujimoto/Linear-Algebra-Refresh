from matrix import Matrix 

m1 = Matrix([[1, 2, 3]])
m2 = Matrix([[4, 5, 6]])
assert m1.matrix_addition(m2).matrix == [[5, 7, 9]]

m3 = Matrix([[4]])
m4 = Matrix([[5]])
assert m3.matrix_addition(m4).matrix == [[9]]

m5 = Matrix([[1, 2, 3], [4, 5, 6]])
m6 = Matrix([[7, 8, 9], [10, 11, 12]])
assert m5.matrix_addition(m6).matrix == [[8, 10, 12], [14, 16, 18]]

m7 = Matrix([[5], [2]])
m8 = Matrix([[5, 1]])
m9 = Matrix([[5, 1]])
m10 = Matrix([[5], [2]])
m11 = Matrix([[4]])
m12 = Matrix([[3]])
m13 = Matrix([[2, 1, 8, 2, 1], [5, 6, 4, 2, 1]])
m14 = Matrix([[1, 7, 2], [2, 6, 3], [3, 1, 1], [1, 20, 1], [7, 4, 16]])
assert m7.matrix_multiplication(m8).matrix == [[25, 5], [10, 2]]
assert m9.matrix_multiplication(m10).matrix == [[27]]
assert m11.matrix_multiplication(m12).matrix == [[12]]
assert m13.matrix_multiplication(m14).matrix == [[37, 72, 33], [38, 119, 50]]

m15 = Matrix([[5, 4, 1, 7], [2, 1, 3, 5]])
m16 = Matrix([[5]])
m17 = Matrix([[5, 3, 2], [7, 1, 4], [1, 1, 2], [8, 9, 1]])
assert m15.transpose().matrix == [[5, 2], [4, 1], [1, 3], [7, 5]]
assert m16.transpose().matrix == [[5]]
assert m17.transpose().matrix == [[5, 7, 1, 8], [3, 1, 1, 9], [2, 4, 2, 1]]

m18 = Matrix([[5, 3, 1], [6, 2, 7]])
m19 = Matrix([[4, 2], [8, 1], [7, 4]])
m20 = Matrix([[5]])
m21 = Matrix([[4]])
m22 = Matrix([[2, 8, 1, 2, 9], [7, 9, 1, 10, 5], [8, 4, 11, 98, 2], [5, 5, 4, 4, 1]])
m23 = Matrix([[4], [2], [17], [80], [2]])
m24 = Matrix([[2, 8, 1, 2, 9], [7, 9, 1, 10, 5], [8, 4, 11, 98, 2], [5, 5, 4, 4, 1]])
m25 = Matrix([[4, 1, 2], [2, 3, 1], [17, 8, 1], [1, 3, 0], [2, 1, 4]])
assert m18.matrix_multiplication(m19).matrix == [[51, 17], [89, 42]]
assert m20.matrix_multiplication(m21).matrix == [[20]]
assert m22.matrix_multiplication(m23).matrix == [[219], [873], [8071], [420]]
assert m24.matrix_multiplication(m25).matrix == [[61, 49, 49], [83, 77, 44], [329, 404, 39], [104, 65, 23]]

assert Matrix.identity_matrix(1).matrix == [[1]]
assert Matrix.identity_matrix(2).matrix == [[1, 0], [0, 1]]
assert Matrix.identity_matrix(3).matrix == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
assert Matrix.identity_matrix(4).matrix == [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]


m25 = Matrix([[5, 9, 2, 4], [3, 8, 5, 6], [1, 0, 0, 15]])
assert m25.matrix_multiplication(Matrix.identity_matrix(4)).matrix == m25.matrix
assert Matrix.identity_matrix(3).matrix_multiplication(m25).matrix == m25.matrix

m26 = Matrix([[100]])
m27 = Matrix([[4, 5], [7, 1]])
assert m26.inverse_matrix().matrix == [[0.01]]
assert m27.inverse_matrix().matrix == [[-0.03225806451612903, 0.16129032258064516], [0.22580645161290322, -0.12903225806451613]]

print('Completed, All pass!')
print()

#Test for mismatch in A columns and B rows, will throw ValueError:
#assert m24.matrix_multiplication(m22).matrix == [[]]


