
def scalar_x_matrix(matrix, const):
    m = []
    for row in matrix:
        new_row = []
        for col in row:
            new_row.append(col*const)
        m.append(new_row)
    return m


def matrix_addition(matrixA, matrixB):
    matrixSum = []

    for i in range(len(matrixA)):
        row = []
        for j in range(len(matrixA[0])):
            plus = matrixA[i][j] + matrixB[i][j]
            row.append(plus)
        matrixSum.append(row)
    return matrixSum


def matrix_subtraction(matrixA, matrixB):
    matrixSub = []
    
    for i in range(len(matrixA)):
        row = []
        for j in range(len(matrixA[0])):
            sub = matrixA[i][j] - matrixB[i][j]
            row.append(sub)
        matrixSub.append(row)   
    return matrixSub


def get_row(matrix, row):
    return matrix[row]


def get_column(matrix, column_number):
    column = []
    for row in matrix:
        num = row[column_number]
        column.append(num)
    return column


def dot_product(vector_one, vector_two):
    return sum([x*y for x, y in zip(vector_one, vector_two)])


def matrix_multiplication(matrixA, matrixB):
    ab = []
    trans_b = transpose(matrixB)
    
    for row in matrixA:
        new_row = []
        ## col refers to the original matrixB column prior to transpose,
        ## even though they are now rows in trans_b matrix.
        for col in trans_b:
            dp = dot_product(row, col)
            new_row.append(dp)
        ab.append(new_row)
    return ab


def transpose(matrix):
    matrix_transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]    
    return matrix_transpose


def identity_matrix(n):    
    identity = []
    for i in range(n):
        new_row = []
        for j in range(n):
            if i == j:
                new_row.append(1)
            else:
                new_row.append(0)
        identity.append(new_row)
    return identity

def inverse_matrix(matrix):    
    dim = len(matrix) 
    
    if dim != len(matrix[0]):
        raise ValueError('The matrix must be square')
    
    if dim > 2:
        raise ValueError('The matrix must be 2x2 max')
        
    if dim == 1:
        return [[1/matrix[0][0]]]
       
    determinant = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    
    if determinant == 0:
        raise ValueError('The matrix is not invertible')
       
    trace = matrix[0][0] + matrix[1][1]
    ident = identity_matrix(dim)
    trace_x_ident = scalar_x_matrix(ident, trace)
    diff = matrix_subtraction(trace_x_ident, matrix)
    inverse = scalar_x_matrix(diff, 1/determinant)
    return inverse
    
