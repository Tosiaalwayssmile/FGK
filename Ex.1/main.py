from vector import *
from ray import *
from sphere import *

# Zdefiniować sferę S o środku w punkcie (0,0,0) i promieniu 10. #
v1 = Vec3(0, 0, 0)
s1 = Sphere(v1, 10)

# Zdefiniować promień R1 o początku w punkcie (0,0,-20) i skierowany w środek kuli.#
v2 = Vec3(0, 0, -20)
v3 = Vec3(0, 0, 0)
r1 = Ray(v2, v3)

# Zdefiniować promień R2 o początku w tym samym punkcie, co R1, skierowany równolegle do osi Y.
v4 = Vec3(0, 1, 0)
r2 = Ray(v2, v4)

# Sprawdzić, czy istnieje przecięcie sfery S z promieniami R1 oraz R2. Wynik w postaci współrzędnych punktu przecięcia należy wyświetlić.
print("Miejsce przecięcia sfery s1 i promienia r1: ")
Sphere.show_sphere_intersection(Sphere.get_sphere_intersection(s1, r1))   

print("Miejsce przecięcia sfery s1 i promienia r2: ")  
Sphere.show_sphere_intersection(Sphere.get_sphere_intersection(s1, r2))     

# Zdefiniować dowolny promień R3, tak aby przecinał on sferę S w dokładnie jednym punkcie. Podać współrzędne punktu przecięcia.
r3 = Ray(Vec3(0, 10, 0), Vec3(10, 10, 0))
print("Miejsce przecięcia sfery s1 i promienia r3: ")  
Sphere.show_sphere_intersection(Sphere.get_sphere_intersection(s1, r3))     

# Zdefiniować płaszczyznę P przechodzącą przez punkt (0,0,0), której wektor normalny tworzy kąt 45 stopni z osiami Y i Z.

# Znaleźć punkt przecięcia płaszczyzny P z promieniem R2.