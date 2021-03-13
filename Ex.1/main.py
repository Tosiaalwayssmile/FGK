from vector import *

v1 = Vec3(1, 2, 3)
v2 = Vec3(4, 5, 6)
v3 = v1 + v2

v4 = Vec3(1, 1, 1)
v5 = Vec3(-2, 5, 0)

print(Vec3.cross(v4, v5))
print(str(v2.length()))

