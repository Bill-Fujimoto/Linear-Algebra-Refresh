from decimal import Decimal, getcontext

from vector import Vector

getcontext().prec = 30


class Line(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
##            all_zeros = [0]*self.dimension
            normal_vector = (0,)*self.dimension
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = constant_term
        
        self.basepoint = self.set_basepoint()
        
    def __eq__(self, ell):
        
        if self.normal_vector.is_zero():
            if not ell.normal_vector.is_zero():
                return False
            else:
                diff = self.constant_term - ell.constant_term
                return MyDecimal(diff).is_near_zero()
        elif ell.normal_vector.is_zero():
            return False
        
        if not self.parallel(ell):
            return False
        
        x0 = Vector(self.basepoint)
        y0 = Vector(ell.basepoint)
        basepoint_difference = Vector(x0.minus(y0))
        n = self.normal_vector
        return basepoint_difference.orthogonal(n)
    

    def parallel(self, ell):
        
        n1 = self.normal_vector
        n2 = ell.normal_vector
##        print('Is Par?:', n1.parallel(n2))
        return n1.parallel(n2)
    
    def intersection_with(self, ell):
        try:
            A, B = self.normal_vector.coordinates
            C, D = ell.normal_vector.coordinates
            k1 = self.constant_term
            k2 = ell.constant_term
            
            x_numerator = D*k1 - B*k2
            y_numerator = -C*k1 + A*k2
            one_over_denom = 1.0/round((A*D - B*C), 10)
##            print(A*D - B*C)
            return Vector([x_numerator, y_numerator]).scalar_mult(one_over_denom)
        
        except ZeroDivisionError:
            if self == ell:
##                print('self:', self)
##                print('ell:', ell)
##                print(self == ell)
                return self
            else:
                return None
            
    def set_basepoint(self):
        try:
            n = self.normal_vector.coordinates
            c = self.constant_term
            basepoint_coords = [0]*self.dimension

            initial_index = Line.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = c/initial_coefficient
            return basepoint_coords
##            self.basepoint = basepoint_coords

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
                return None
            else:
                raise e
            

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

        try:
            initial_index = Line.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
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


    @staticmethod
    def first_nonzero_index(iterable):
        print(iterable)
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps



n1 = Vector((4.046, 2.836))
k1 = 1.21
n2 = Vector((10.115, 7.09))
k2 = 3.025
l1 = Line(n1, k1)
l2 = Line(n2, k2)
print()
print(l1)
print()
print(l2)
print('Class.__dict__:', Line.__dict__)
print()
print('Instance.__dict__:', l1.__dict__)
print()
print('Instance normal vector var:', l1.normal_vector)
print()
print('Instance basepoint var:', l1.basepoint)
print()
print('Instance method:', l1.set_basepoint())
print()
print('Dir(l1):', dir(l1))
print()
print('Dir(line):', dir(Line))

