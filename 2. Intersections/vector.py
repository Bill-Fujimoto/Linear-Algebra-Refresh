from math import sqrt, acos, pi
from decimal import Decimal

class Vector(object):
    
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(c) for c in coordinates])
            self.dimension = len(coordinates)
#            self.normalize = self.normalize()

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')
        
    def __repr__(self):
        coords = []
        for num in self.coordinates:
            coords.append(round(float(num), 3)) 
        return 'Vector(' + str(coords) +')'


    def __str__(self):     
        coords = []
        for num in self.coordinates:
            coords.append(round(float(num), 3))            
        return f'Vector: {tuple(coords)}'  #'Vector: {}'.format(tuple(coords))
     

    def __eq__(self, v):
        return self.coordinates == v.coordinates
    

    def plus(self, v):
        new_coordinates = tuple([x+y for x,y in zip(self.coordinates, v.coordinates)])
        return new_coordinates
    
    
    def minus(self, v):
        new_coordinates = tuple([x-y for x,y in zip(self.coordinates, v.coordinates)])
        return new_coordinates
    

    def scalar_mult(self, c):
        '''
        This computes the scaled vector for given a scalar constant
        '''
        new_coordinates = tuple([Decimal(c)*x for x in self.coordinates])
        return new_coordinates
    
    
    def magnitude(self):
        '''
        This computes the magnitude scalar value of a given vector
        '''
        coord_squared = [x**2 for x in self.coordinates]
        return Decimal(sqrt(sum(coord_squared)))
    
    
    def normalize(self):
        '''
        This computes the unit vector of a given vector
        '''
        try:
            mag = self.magnitude()
            return self.scalar_mult(Decimal(1.0)/mag)

        except ZeroDivisionError:           
            return Exception('Cannot normalize the zero vector')
        

    def dot_prod(self, v):
        '''
        This computes the dot product value of a given pair of vectors
        '''
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])
    
    
    def dot_prod_unit(self, v):
        '''
        This computes the dot product of a given pair of internally normalized
        (unit) vectors. Result is numerically equal to the cosine of the angle between.
        '''
        try:
            return sum([x*y for x,y in zip(self.normalize(), v.normalize())])
        except:
            return 'One or more zero vectors'
    
    
    def angle(self, v, degrees = False):
        '''
        This computes the incident angle between two non-zero vectors
        '''
        if (self.is_zero() or v.is_zero()):
            return 'One or more zero vectors'

        cosine = round(self.dot_prod_unit(v), 10)
        angle_rad = acos(cosine)
        
        if degrees:
            angle_deg = angle_rad*180/pi
            return angle_deg
        return angle_rad
    
    
    def parallel(self, v, tolerance = 10e-10):
        '''
        This computes the angle of two vectors, if less than tolerance or at least
        one of the vectors is a zero vector, the result is True.
        '''
        return (self.is_zero() or v.is_zero() or \
                abs(self.angle(v)) < tolerance or \
                abs(abs(self.angle(v)) - pi) < tolerance)
    
    
    def is_zero(self, tolerance=1e-10):
        '''
        Tests the vector magnitue if < tolerance
        '''
        return self.magnitude() < tolerance
    
    
    def orthogonal(self, v, tolerance = 10e-10):
        '''
        If dot product is less than tolerance, the vectors are orthogonal
        '''
        dot_prod = abs(self.dot_prod(v))
        return dot_prod < tolerance
    
    
    def proj_on_b(self, v):
        '''
        This computes the parallel component of a given vector v on to a reference
        vector b.  Self instance is the reference vector b.
        V dot reference unit vector is V parallel magnitude.
        '''
        unit_b = Vector(self.normalize())
        mag_vpar = v.dot_prod(unit_b) #scalar value
        return unit_b.scalar_mult(mag_vpar)
    
    
    def perp_to_b(self, v):
        '''
        This computes the perpendicular component of a given vector v relative
        to a reference vector b.  Self instance is the reference vector b.
        V minus Vparallel vector is Vpendicular vector.
        '''       
        v_para = Vector(self.proj_on_b(v))
        return v.minus(v_para)
    
    
    def para_plus_perp(self, b):
        '''
        This computes the sum of the parallel and perpendicular components of a
        given vector v relative to a reference vector b.  Self instance is the vector v.
        The sum of components will equal the original vector v (self).
        '''          
        v_para = Vector(b.proj_on_b(self))
        v_perp = Vector(b.perp_to_b(self))
        return v_para.plus(v_perp)
    
    
    def cross_prod(self, w):
        '''
        This computes the cross product vector (3D max) of a given pair of vectors
        '''
        Vx, Vy, Vz = self.coordinates
        Wx, Wy, Wz = w.coordinates
        return tuple([Vy*Wz - Wy*Vz, Wx*Vz - Vx*Wz, Vx*Wy - Wx*Vy])
    
    
    def area_parallogram (self, w):
        '''
        This computes the area of a parallelogram given pair of vectors, which
        is the magnitude of the cross product
        '''
        cross = Vector(self.cross_prod(w))
        return cross.magnitude()
    
    
    def area_of_triangle(self, w):
        '''
        This computes the area of a triangle given pair of vectors, which
        is the magnitude of the cross product divided by 2.
        '''
        cross = Vector(self.cross_prod(w))
        return cross.magnitude()/2
    
