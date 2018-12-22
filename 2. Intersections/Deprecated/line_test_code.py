from vector import Vector
from line import Line


print('1st Pair....')
n1 = Vector((4.046, 2.836))
k1 = 1.21
n2 = Vector((10.115, 7.09))
k2 = 3.025
ell1 = Line(n1, k1)
ell2 = Line(n2, k2)
print('Calculate Intersection:', ell1.intersection_with(ell2))
print()
print('2nd Pair....')
n1 = Vector((7.204, 3.182))
k1 = 8.68
n2 = Vector((8.172, 4.114))
k2 = 9.883
ell1 = Line(n1, k1)
ell2 = Line(n2, k2)
print('Calculate Intersection:', ell1.intersection_with(ell2))
print()
print('3rd Pair....')
n1 = Vector((1.182, 5.562))
k1 = 6.744
n2 = Vector((1.773, 8.343))
k2 = 9.525
ell1 = Line(n1, k1)
ell2 = Line(n2, k2)
print('Calculate Intersection:', ell1.intersection_with(ell2))