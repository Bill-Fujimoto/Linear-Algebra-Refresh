from linearsys import LinearSystem
from vector import Vector
from plane import Plane

p0 = Plane(normal_vector=Vector([1,1,1]), constant_term = 1)
p1 = Plane(normal_vector=Vector([0,1,0]), constant_term = 2)
p2 = Plane(normal_vector=Vector([1,1,-1]), constant_term = 3)
p3 = Plane(normal_vector=Vector([1,0,-2]), constant_term = 2)

s = LinearSystem([p0,p1,p2,p3])
print(s)
print()
#print('First non-zero index of each eqn:', s.indices_of_first_nonzero_terms_in_each_row())
#print()
##print('{}\n{}\n{}\n{}'.format(s[0],s[1],s[2],s[3]))
#print('# Equations:', len(s))
#print()
s[0] = p1
print(s)

#~ print(MyDecimal('1e-9').is_near_zero())
#~ print(MyDecimal('1e-11').is_near_zero())
