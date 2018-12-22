from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane

getcontext().prec = 30


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solution exists'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)
        
        self.planes = planes
        self.dimension = d


    def __repr__(self):
        return 'LinearSystem(' + str([plane for plane in self.planes]) + ')'
    
    
    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret
    

    def __len__(self):
        return len(self.planes)


    def __getitem__(self, i):
        return self.planes[i]


    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)
        
        
    def swap_rows(self, row1, row2):
        temp = self[row1]
        self[row1] = self[row2]
        self[row2] = temp
        return


    def multiply_coefficient_and_row(self, coefficient, row):
        c = coefficient
        constant_term = self[row].constant_term * c
        self[row] = Plane(Vector(self[row].normal_vector.scalar_mult(c)), constant_term)
        return


    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_add_to):
        c = coefficient
        rta = row_to_add
        rtat = row_to_add_to
        temp_constant = self[rta].constant_term * c
        temp_vector = Vector(self[rta].normal_vector.scalar_mult(c))        
        self[rtat] = Plane(Vector(temp_vector.plus(self[rtat].normal_vector)),\
                                  self[rtat].constant_term + temp_constant)
        return

    def compute_triangular_form(self):
        '''
        Input: System of equations
        Output: System of equations in triangular form
        This method arranges the system so that each variable is a leading variable, ie.
        starting from row 1, the leading variable will not have the same variable in the
        rows below it.  It will stop if 0=k is found (inconsistent).
        '''
        system = deepcopy(self)
        num_equations = len(system.planes)
        num_variables = system.dimension       
        j = 0
        # i, j are row, col indices; row is equation, col is variable
        for i in range(num_equations):
            while j < num_variables:
                # This tests the first variable of current row for 0 coeff.  If true, then the following rows
                # are tested for non-zero coeff for the same variable.  If found, the rows will swap.
                # If no non-zero coeff are found on any row, this means that variable is not in the system.
                # The while loop then tests the next variable of the current row.
                c = MyDecimal(system[i].normal_vector.coordinates[j])
                if c.is_near_zero():
                    swap_succeeded = system.swap_with_row_below_for_nonzero_coefficient_if_able(i ,j)
                    if not swap_succeeded:
                        j += 1
                        continue
                # The next step happens once a row swap has occurred.  Once the coeff are cleared
                # in all rows below, the while loop breaks and the for loop moves to the next equation.
                system.clear_coefficients_below(i, j)
                j += 1
                break
        return system
    
    def swap_with_row_below_for_nonzero_coefficient_if_able(self, row, col):
        '''
        This tests the following rows for non-zero coeff and will swap rows when the
        first non-zero coeff is found, then return True.
        '''
        num_equations = len(self)
        
        for k in range(row+1, num_equations):
            coefficient = MyDecimal(self[k].normal_vector.coordinates[col])
            if not coefficient.is_near_zero():
                self.swap_rows(row, k)
                return True
        return False
    
    
    def clear_coefficients_below(self, row, col):
        '''
        This function will scale the current [row, col] equation and add to the rows below.
        Even if the coeff for the variable in the row below is already 0, this will simply scale
        the current row by 0 and add 0=0 to the row below.  This will loop for all rows below.
        This applies only to the variable in question [col].
        '''
        num_equations = len(self)
        beta = self[row].normal_vector.coordinates[col]       
        delta = MyDecimal(beta)
        
        if not delta.is_near_zero():
            for k in range(row+1, num_equations):
                gamma = self[k].normal_vector.coordinates[col]
                alpha = -gamma/beta
                self.add_multiple_times_row_to_row(alpha, row, k)         
        return
                                                 

    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension
        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector.coordinates)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e
        return indices

    def compute_rref(self):
        '''
        Input: System of equations
        Output: System of equations in reduce row echelon form (RREF)
        This method arranges the system so that each pivot variable is in its own column, ie.
        starting from triangular form bottom row, the leading variable will not have the same
        variable in the rows above it.  It will stop if 0=k is found (inconsistent).
        '''
        tf = self.compute_triangular_form()
        
        num_equations = len(tf)
        pivot_indices = tf.indices_of_first_nonzero_terms_in_each_row()
        for i in range(num_equations)[::-1]:
             j = pivot_indices[i]
             if j < 0:
                 continue
             tf.scale_row_to_make_coeffcient_equal_one(i, j)
             tf.clear_coefficients_above(i, j)     
        return tf
    
    
    def scale_row_to_make_coeffcient_equal_one(self, row, col):
        '''
        This function normalizes the first coefficient of each row.
        '''
        n = self[row].normal_vector.coordinates
        beta = 1.0/n[col]
        self.multiply_coefficient_and_row(beta, row)
        return
    
        
    def clear_coefficients_above(self, row, col):
        '''
        This function will scale the current [row, col] equation and add to the rows above.
        Even if the coeff for the variable in the row above is already 0, this will simply scale
        the current row by 0 and add 0=0 to the row above.  This will loop for all rows above.
        This applies only to the variable in question [col].
        '''
        for k in range(row)[::-1]:
            n = self[k].normal_vector.coordinates
            alpha = -(n[col])
            self.add_multiple_times_row_to_row(alpha, row, k)
        return
    
    def compute_ge_solution(self):
        '''
        '''
        try:
            return self.do_gaussian_elimination_and_extract_solution()
        
        except Exception as e:
            if (str(e) == self.NO_SOLUTIONS_MSG or str(e) == self.INF_SOLUTIONS_MSG):
                return str(e)
            else:
                raise e
            
    def do_gaussian_elimination_and_extract_solution(self):
        rref = self.compute_rref()
        
        rref.raise_exception_if_contradictory_equation()
        rref.raise_exception_too_few_pivots()
        
        num_variables = rref.dimension
        solution_coordinates = [rref[i].constant_term for i in range(num_variables)]
        return Vector(solution_coordinates)
    
    def raise_exception_if_contradictory_equation(self):
        for p in self.planes:
            try:
                p.first_nonzero_index(p.normal_vector.coordinates)
                
            except Exception as e:
                if str(e) == 'No nonzero elements found':
                    # This checks for 0 = k condition, if constant k is non-zero, an inconsistency
                    # has occured and no solution exists
                    constant_term = MyDecimal(p.constant_term)
                    if not constant_term.is_near_zero():
                        raise Exception(self.NO_SOLUTIONS_MSG)
                    return
#                    else:
#                        raise e  #This was the bug!!!
                   
                    
    def raise_exception_too_few_pivots(self):
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        num_pivots = sum([1 if index >= 0 else 0 for index in pivot_indices])
        num_variables = self.dimension
        
        if num_pivots < num_variables:
            raise Exception(self.INF_SOLUTIONS_MSG)


    def compute_param_solution(self):
        '''
        '''
        try:
            return self.do_gaussian_elimination_and_parametrize_solution()
        
        except Exception as e:
            if str(e) == self.NO_SOLUTIONS_MSG:
                return str(e)
            else:
                raise e

    def do_gaussian_elimination_and_parametrize_solution(self):
        rref = self.compute_rref()
        rref.raise_exception_if_contradictory_equation()
        
        direction_vectors = rref.extract_direction_vectors_for_parametrization()
        basepoint = rref.extract_basepoint_for_parametrization()
    
        return Parametrization(basepoint, direction_vectors)
    
    
    def extract_direction_vectors_for_parametrization(self):
        num_variables = self.dimension
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        free_variable_indices = set(range(num_variables)) - set(pivot_indices)
        
        direction_vectors = []
        
        for free_var in free_variable_indices:
            vector_coords = [0] * num_variables
            vector_coords[free_var] = 1
            for i, p in enumerate(self.planes):
                pivot_var = pivot_indices[i]
                if pivot_var < 0:
                    break
                vector_coords[pivot_var] = -p.normal_vector.coordinates[free_var]
            direction_vectors.append(Vector(vector_coords))
             
        return direction_vectors
    
    
    def extract_basepoint_for_parametrization(self):
        num_variables = self.dimension
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        
        basepoint_coords = [0] * num_variables
        
        for i, p in enumerate(self.planes):
            pivot_var = pivot_indices[i]
            if pivot_var < 0:
                break
            basepoint_coords[pivot_var] = p.constant_term
                
        return Vector(basepoint_coords)


class Parametrization(object):
    
    BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM_MSG = \
        'The basepoint and direction vectors should all live in the same dimension'

    def __init__(self, basepoint, direction_vectors):
        self.basepoint = basepoint
        self.direction_vectors = direction_vectors
        self.dimension = self.basepoint.dimension
        
        try:
            for v in direction_vectors:
                assert v.dimension == self.dimension
        
        except AssertionError:
            raise Exception(BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM_MSG)
        
    def __repr__(self):

        return 'Basepoint: ' + str(self.basepoint) + '; Direction vectors: ' + str([vector for vector in self.direction_vectors])

        
    def __str__(self):
        '''
        This __str__ has my slightly modified version plus the original from the instructor.
        My version below uses x, y, z for the 3D variables which is easier to read, but is not
        scalable to higher dimensions, so in that case, just comment out and use the other version
        below it.
        '''
        var = {0:'x', 1:'y', 2:'z'}
        output = ''
        for coord in range(self.dimension):
            output += '{} = {} '.format(var[coord],
                                          round(self.basepoint.coordinates[coord], 3))
            for free_var, vector in enumerate(self.direction_vectors):
                output += '+ {}*t{}'.format(round(vector.coordinates[coord], 3),
                                             free_var + 1)
            output += '\n'
        return output
    
#        output = ''
#        for coord in range(self.dimension):
#            output += 'x{} = {} '.format(coord + 1,
#                                          round(self.basepoint[coord], 3))
#            for free_var, vector in enumerate(self.direction_vectors):
#                output += '+ {} t{}'.format(round(vector[coord], 3),
#                                             free_var + 1)
#            output += '\n'
#        return output   

    
class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps
