from linearsys import LinearSystem, MyDecimal
from vector_alt import Vector
from hyperplane import Hyperplane

p0 = Hyperplane(normal_vector=Vector([1,1,1]), constant_term = 1)
p1 = Hyperplane(normal_vector=Vector([0,1,0]), constant_term = 2)
p2 = Hyperplane(normal_vector=Vector([1,1,-1]), constant_term = 3)
p3 = Hyperplane(normal_vector=Vector([1,0,-2]), constant_term = 2)

s = LinearSystem([p0,p1,p2,p3])
print(s)
print()
#print('First non-zero index of each eqn:', s.indices_of_first_nonzero_terms_in_each_row())
#print()
##print('{}\n{}\n{}\n{}'.format(s[0],s[1],s[2],s[3]))
print('# Equations:', len(s))
print()
s[0] = p1
print(s)
print()
print(MyDecimal('1e-9').is_near_zero())
print(MyDecimal('1e-11').is_near_zero())
