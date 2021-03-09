from vector import *

v1 = Vec(1, 2, 3)
v2 = Vec(4, 5, 6)
v3 = v1 + v2

v4 = Vec(3, -5, 4)
v5 = Vec(2, 6, 5)
#rint(v1*v2)
print(v1*3) 
print(3*v1) 

v6 = Vec(1, 1, 1)
v7 = Vec(-2, 5, 0)
print(Vec.cross(v6,v7))

print(str(v2.length()))
