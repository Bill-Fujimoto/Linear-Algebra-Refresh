from math import sqrt, acos, pi

class Vector(object):
    
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates) #[x for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

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
        new_coordinates = tuple([c*x for x in self.coordinates])
        return new_coordinates
    
    def magnitude(self):
        '''
        This computes the magnitude scalar value of a given vector
        '''
        coord_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coord_squared))
    
    def normalize(self):
        '''
        This computes the unit vector of a given vector
        '''
        try:
            mag = self.magnitude()
            return self.scalar_mult(1.0/mag)

        except ZeroDivisionError:
            return 'Divide by zero error'

    def dot_prod(self, v):
        '''
        This computes the dot product scalar value of a given pair of vectors
        '''
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])
    
    def angle(self, v, degrees = False):
        '''
        This computes the incident angle between two non-zero vectors
        '''
        if (self.is_zero() or v.is_zero()):
            return 'One or more zero vectors'

        u1 = Vector(self.normalize())
        u2 = Vector(v.normalize())
        cosine = round(u1.dot_prod(u2), 10)
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
    
    
##print('First pair...')
##v1 = Vector([-7.579, -7.88])
##v2 = Vector([22.737, 23.64])
##print('Normalized v:', v1.normalize())
##print('Is Orthogonal: ', v1.orthogonal(v2))
##print('Is parallel: ', v1.parallel(v2))
##print('Angle: ', v1.angle(v2))
##print()
##print('Second pair...')
##v1 = Vector([-2.029, 9.97, 4.172])
##v2 = Vector([-9.231, -6.639, -7.245])
##print('Normalized v:', v1.normalize())
##print('Is Orthogonal: ', v1.orthogonal(v2))
##print('Is parallel: ', v1.parallel(v2))
##print('Angle: ', v1.angle(v2))
##print()
##print('Third pair...')
##v1 = Vector([-2.328, -7.284, -1.214])
##v2 = Vector([-1.821, 1.072, -2.94])
##print('Normalized v:', v1.normalize())
##print('Is Orthogonal: ', v1.orthogonal(v2))
##print('Is parallel: ', v1.parallel(v2))
##print('Angle: ', v1.angle(v2))
##print()
##print('Fourth pair...')
##v1 = Vector([2.118, 4.827])
##v2 = Vector([0, 0])
##print('Normalized v:', v1.normalize())
##print('Is Orthogonal: ', v1.orthogonal(v2))
##print('Is parallel: ', v1.parallel(v2))
##print('Angle: ', v1.angle(v2))
##print()
##print('Project V onto b....')
##v = Vector([3.039, 1.879])
##b = Vector([0.825, 2.036])
##print('V parallel:', b.proj_on_b(v))
##print()
##print('V perpendicular to b....')
##v = Vector([-9.88, -3.264, -8.159])
##b = Vector([-2.155, -9.353, -9.473])
##print('V perp:', b.perp_to_b(v))
##print()
##print('Sum of V para and V perp....')
##v = Vector([3.009, -6.172, 3.692, -2.51])
##b = Vector([6.404, -9.144, 2.759, 8.718])
##print('V parallel:', b.proj_on_b(v))
##print('V perp:', b.perp_to_b(v))
##print('Sum of components:', v.para_plus_perp(b))
##print()
##print('VxW ...')
##v = Vector([8.462, 7.893, -8.187])
##w = Vector([6.984, -5.975, 4.778])
##VxW = Vector(v.cross_prod(w))
##print('VxW:', v.cross_prod(w))
##print()
##print('Area of Parallelogram ...')
##v = Vector([-8.987, -9.838, 5.031])
##w = Vector([-4.268, -1.861, -8.866])
##print('Area of Para gram:', v.area_parallogram (w))
##print()
##print('Area of Triangle ...')
##v = Vector([1.5, 9.547, 3.691])
##w = Vector([-6.007, 0.124, 5.772])
##print('Area of Triangle:', v.area_of_triangle(w))
##print()  

##
##print('Sum:', v.plus(b))
##print('Minus:', v.minus(b))
##print('Scalar mult:', b.scalar_mult(5))
##print('Normalized:', b.normalize())
##print('Magnitude:', v.magnitude())
##print('Angle:', v.angle(b))
##print(v1.parallel(v2))
##print('Normalized v:', v.normalize())
##print(my_Vector)
##print(v.coordinates)
##print(my_Vector.dimension)
##print(my_Vector==my_Vector2)

