from math import sqrt, acos, pi

class Vector(object):
    
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)
    
    
    def scalarmult(self, c):
        new_coordinates = tuple([c*x for x in self.coordinates])
        return new_coordinates
    
    
    def magnitude(self):
        coord_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coord_squared))
    
    
    def normalize(self):
        try:
            mag = self.magnitude()
            # Vector(...) is needed to enable attributes for some reason...
            return Vector(self.scalarmult(1.0/mag))

        except ZeroDivisionError:
            return 'Divide by zero error'
        

    def dotprod(self, v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])

    
    def angle(self, v):

## This section below is identical to instructor example using normalized unit
## vectors but it does not work, error indication is 'dot_prod' not
## valid attribute for list object as verified by dir(u1). Instructor is using v2.7, I'm using v3.6.2.
## Performing the normalize method on self or v removes the dot_prod and other methods.
## Work around is to create new instance of Vector object in the normalize method def above.
        
        u1 = self.normalize()
        u2 = v.normalize()     
        
        unit_dotprod = round((u1.dotprod(u2)), 8)
        
        print('Unit dot product:', unit_dotprod)
        
        angle = acos(unit_dotprod)
        return angle
    
    #### Test Code #####
    
v1 = Vector([-7.579, -7.88])
v2 = Vector([22.737, 23.64])

print('Magnitude v1:', v1.magnitude())
print('Normalized v1:', v1.normalize())
print()

print('Magnitude v2:', v2.magnitude())
print('Normalized v2:', v2.normalize())
print()
print('Dot product:', v1.dotprod(v2))
print('Angle_rad:', v1.angle(v2))
