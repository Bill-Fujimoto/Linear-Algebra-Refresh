


class Matrix(object):

    def __init__(self, matrix):
        try:
            if not (matrix and matrix[0]):
                raise ValueError
            self.rows = len(matrix)
            self.columns = len(matrix[0])
            self.matrix = matrix

        except ValueError:
            raise ValueError('The matrix must be nonempty')

        except TypeError:
            raise TypeError('The matrix must be an iterable')

    def __repr__(self):
        return 'Matrix(' + str(self.matrix) +')'


    def __str__(self):
        output = '[\n'
        for row in self.matrix:
            output += str(row) + ',\n'
        output += ']'
        return output


    def get_row(self, row):
        return self.matrix[row]


    def get_column(self, column_number):
        column = []
        for row in self.matrix:
            num = row[column_number]
            column.append(num)
        return column


    def matrix_addition(self, matrixB):
        '''
        Input: MatrixA (self), MatrixB objects
        Output: Matrix object of sum matrix
        (reivew: both matrices must have indentical dimensions)
        '''
        try:
            if not (self.rows == matrixB.rows and self.columns == matrixB.columns):
                raise ValueError
        except ValueError:
            raise ValueError('Both matrices must have the same m x n dimensions')

        matrixSum = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                plus = self.matrix[i][j] + matrixB.matrix[i][j]
                row.append(plus)
            matrixSum.append(row)
        return Matrix(matrixSum)


    def matrix_subtraction(self, matrixB):
        '''
        Input: MatrixA, MatrixB objects
        Order: matrixA.matrix_subtraction(matrixB)
        Output: Matrix object of subtract matrix
        (reivew: both matrices must have indentical dimensions)
        '''
        try:
            if not (self.rows == matrixB.rows and self.columns == matrixB.columns):
                raise ValueError
        except ValueError:
            raise ValueError('Both matrices must have the same m x n dimensions')

        matrixSub = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                sub = self.matrix[i][j] - matrixB.matrix[i][j]
                row.append(sub)
            matrixSub.append(row)
        return Matrix(matrixSub)


    def scalar_x_matrix(self, const):
        '''
        Input: Matrix object, scalar constant
        Order: self.scalar_x_matrix(const)
        Output: Matrix object of scaled matrix
        (review: scalar multiplies all elements of matrix)
        '''
        scaled = []
        for row in self.matrix:
            new_row = []
            for col in row:
                new_row.append(col*const)
            scaled.append(new_row)
        return Matrix(scaled)


    def matrix_multiplication(self, matrixB):
        '''
        Input: MatrixA (self), MatrixB objects
        Order: matrixA.matrix_multiplication(matrixB)
        Output: Matrix object of product
        Review: A is M x N, B is N x P; A columns must equal B rows;
        AB is NOT commutative, AB is size M x P
        '''
        try:
            if not (self.columns == matrixB.rows):
                raise ValueError
        except ValueError:
            raise ValueError('Matrix A columns does not equal Matrix B rows')
        
        ab = []
        trans_b = matrixB.transpose()

        for row in self.matrix:
            new_row = []
            ## each element in AB is dot product of A row x B col
            ## (after B is transposed, B col = rows in trans_B)
            for col in trans_b.matrix:
                dot_product = sum([x*y for x, y in zip(row, col)])
                new_row.append(dot_product)
            ab.append(new_row)
        return Matrix(ab)


    def transpose(self):
        '''
        Input: Matrix object
        Output: Matrix object of transposed matrix
        Review: this is swap of row and cols for simple dot product in matrix
        multiplication.
        '''
        matrix_transpose = [[row[i] for row in self.matrix] for i in range(self.columns)]
        return Matrix(matrix_transpose)

    @classmethod
    def identity_matrix(self, n):
        '''
        Input: integer dim of square matrix
        Output: Matrix object of indentity matrix (diagonal 1's)
        Review: identity matrix does not depend on any input object, only n.
        '''
        identity = []
        for i in range(n):
            new_row = []
            for j in range(n):
                if i == j:
                    new_row.append(1)
                else:
                    new_row.append(0)
            identity.append(new_row)
        return Matrix(identity)


    def inverse_matrix(self):
        '''
        Input: Matrix object, square
        Output: Matrix object for 1x1 or 2x2 matrix
        Due to complexity, this is limited to 2x2 matrix max.
        '''

        if self.rows != self.columns:
            raise ValueError('The matrix must be square')
        if self.rows > 2:
            raise ValueError('The matrix must be 2x2 max')
        if self.rows == 2:
            determinant = self.matrix[0][0]*self.matrix[1][1] - self.matrix[0][1]*self.matrix[1][0]
            if determinant == 0:
                raise ValueError('The matrix is not invertible')

            trace = self.matrix[0][0] + self.matrix[1][1]
            ident = self.identity_matrix(self.rows)
            trace_x_ident = ident.scalar_x_matrix(trace)
            diff = trace_x_ident.matrix_subtraction(self)
            inverse = diff.scalar_x_matrix(1/determinant)
            return inverse

        else:
            return Matrix([[1/self.matrix[0][0]]])
