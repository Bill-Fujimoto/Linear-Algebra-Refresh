from linearsys import LinearSystem
from plane import Plane
from vector import Vector


p0 = Plane(normal_vector=Vector([1,1,1]), constant_term=1)
p1 = Plane(normal_vector=Vector([0,1,0]), constant_term=2)
p2 = Plane(normal_vector=Vector([1,1,-1]), constant_term=3)
p3 = Plane(normal_vector=Vector([1,0,-2]), constant_term=2)

s = LinearSystem([p0,p1,p2,p3])
s.swap_rows(0,1)
if (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print('test case 1 passed')
else:
    print('test case 1 failed')

s.swap_rows(1,3)
if (s[0] == p1 and s[1] == p3 and s[2] == p2 and s[3] == p0):
    print('test case 2 passed')
else:
    print('test case 2 failed')

s.swap_rows(3,1)
if (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print('test case 3 passed')
else:
    print('test case 3 failed')

s.multiply_coefficient_and_row(1,0)
if (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print('test case 4 passed')
else:
    print('test case 4 failed')

s.multiply_coefficient_and_row(-1,2)
if (s[0] == p1 and
        s[1] == p0 and
        s[2] == Plane(normal_vector=Vector([-1,-1,1]), constant_term=-3) and
        s[3] == p3):
    print('test case 5 passed')
else:
    print('test case 5 failed')

s.multiply_coefficient_and_row(10,1)
if (s[0] == p1 and
        s[1] == Plane(normal_vector=Vector([10,10,10]), constant_term=10) and
        s[2] == Plane(normal_vector=Vector([-1,-1,1]), constant_term=-3) and
        s[3] == p3):
    print('test case 6 passed')
else:
    print('test case 6 failed')
    
s.add_multiple_times_row_to_row(0,0,1)
if (s[0] == p1 and
        s[1] == Plane(normal_vector=Vector([10,10,10]), constant_term=10) and
        s[2] == Plane(normal_vector=Vector([-1,-1,1]), constant_term=-3) and
        s[3] == p3):
    print('test case 7 passed')
else:
    print('test case 7 failed')

s.add_multiple_times_row_to_row(1,0,1)
if (s[0] == p1 and
        s[1] == Plane(normal_vector=Vector([10,11,10]), constant_term=12) and
        s[2] == Plane(normal_vector=Vector([-1,-1,1]), constant_term=-3) and
        s[3] == p3):
    print('test case 8 passed')
else:
    print('test case 8 failed')

s.add_multiple_times_row_to_row(-1,1,0)
print(s[0], Plane(normal_vector=Vector([-10,-10,-10]), constant_term=-10))
print(s[1], Plane(normal_vector=Vector([10,11,10]), constant_term=12))
print(s[2], Plane(normal_vector=Vector([-1,-1,1]), constant_term=-3))
print(s[3], p3)
if (s[0] == Plane(normal_vector=Vector([-10,-10,-10]), constant_term=-10) and
        s[1] == Plane(normal_vector=Vector([10,11,10]), constant_term=12) and
        s[2] == Plane(normal_vector=Vector([-1,-1,1]), constant_term=-3) and
        s[3] == p3):
    print('test case 9 passed')
else:
    print('test case 9 failed')