from decimal import getcontext, Decimal

from vector import Vector

getcontext().prec = 30


class Plane(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 3

        if not normal_vector:
            normal_vector = Vector((0,)*self.dimension)
            
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = 0.0
            
        self.constant_term = constant_term

        self.basepoint = self.set_basepoint()
        
    def __eq__(self, p):
        
        if self.normal_vector.is_zero():
            if not p.normal_vector.is_zero():
                return False
            else:
                diff = self.constant_term - p.constant_term
                return MyDecimal(diff).is_near_zero()
        elif p.normal_vector.is_zero():
            return False
        
        if not self.parallel(p):
            return False
        
        x0 = Vector(self.basepoint)
        y0 = Vector(p.basepoint)
        basepoint_difference = Vector(x0.minus(y0))
        n = self.normal_vector
        return basepoint_difference.orthogonal(n)

            
    def __repr__(self):
        
        return 'Plane(normal_vector = Vector(' + str([value for value in  self.normal_vector.coordinates]) + '), constant_term = ' + str(self.constant_term) +')'
            

    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'
            if not is_initial_term:
                output += ' '
            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))
            return output

        n = self.normal_vector.coordinates
        var = {0:'x', 1:'y', 2:'z'}
        try:
            initial_index = Plane.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + var[i]
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output
    

    def parallel(self, p):
        
        n1 = self.normal_vector
        n2 = p.normal_vector
        return n1.parallel(n2)
    
    
    def plane_equal_with(self, p):
        return self == p
       
            
    def set_basepoint(self):
        try:
            n = self.normal_vector.coordinates
            c = self.constant_term
            basepoint_coords = [0]*self.dimension
            initial_index = Plane.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = c/initial_coefficient
            return basepoint_coords

        except Exception as e:
            if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                return None
            else:
                raise e

    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Plane.NO_NONZERO_ELTS_FOUND_MSG)


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps


