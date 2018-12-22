from vector_alt import Vector
from plane import Plane

print('1st Pair....')
n1 = Vector((-0.412, 3.806, 0.728))
k1 = -3.46
n2 = Vector((1.03, -9.515, -1.82))
k2 = 8.65
p1 = Plane(n1, k1)
p2 = Plane(n2, k2)
print('Planes Parallel?', p1.parallel(p2))
print('Planes Equal?', p1.plane_equal_with(p2))
print()
print('2nd Pair....')
n1 = Vector((2.611, 5.528, 0.283))
k1 = 4.6
n2 = Vector((7.715, 8.306, 5.342))
k2 = 3.76
p1 = Plane(n1, k1)
p2 = Plane(n2, k2)
print('Planes Parallel?', p1.parallel(p2))
print('Planes Equal?', p1.plane_equal_with(p2))
print()
print('3rd Pair....')
n1 = Vector((-7.926, 8.625, -7.212))
k1 = -7.952
n2 = Vector((-2.642, 2.875, -2.404))
k2 = -2.443
p1 = Plane(n1, k1)
p2 = Plane(n2, k2)
print('Planes Parallel?', p1.parallel(p2))
print('Planes Equal?', p1.plane_equal_with(p2))