from Primitives.sphere import *
from Primitives.plane import *
from Cameras.camera_orthogonal import *
from light_intensity import *

# Zdefiniować sferę S o środku w punkcie (0,0,0) i promieniu 10. #
s1 = Sphere(Vec3(0, 0, 0), 10)

# Zdefiniować promień R1 o początku w punkcie (0,0,-20) i skierowany w środek kuli.#
v2 = Vec3(0, 0, -20)
v3 = Vec3(0, 0, 20)
r1 = Ray(v2, v3)

# Zdefiniować promień R2 o początku w tym samym punkcie, co R1, skierowany równolegle do osi Y.
v4 = Vec3(0, 1, 0)
r2 = Ray(v2, v4)

# Sprawdzić, czy istnieje przecięcie sfery S z promieniami R1 oraz R2. Wynik w postaci współrzędnych punktu przecięcia należy wyświetlić.
print("Miejsce przecięcia sfery s1 i promienia r1: ")
intersections = s1.get_ray_intersections(r1)
print(str(intersections[0]) + ", " + str(intersections[1]))

print("Miejsce przecięcia sfery s1 i promienia r2: ")  
intersections = s1.get_ray_intersections(r2)
print(str(intersections))

# Zdefiniować dowolny promień R3, tak aby przecinał on sferę S w dokładnie jednym punkcie. Podać współrzędne punktu przecięcia.
r3 = Ray(Vec3(10, 10, 10), Vec3(-10, 0, -10))
print("Miejsce przecięcia sfery s1 i promienia r3: ")
print(str(s1.get_ray_intersections(r3)[0]))

# Zdefiniować płaszczyznę P przechodzącą przez punkt (0,0,0), której wektor normalny tworzy kąt 45 stopni z osiami Y i Z.
p1 = Plane(Vec3(0, 1, 1), 0)

# Znaleźć punkt przecięcia płaszczyzny P z promieniem R2.
print('Miejsce przecięcia płaszczyzny p1 z promieniem r2: ')
print(p1.get_intersection(r2))

# ============
#    ZAD 2
# ============
cam = CameraOrthogonal()

print('Test klasy LightIntensity: ')
lightyLight = LightIntensity(0.3, -0.5, 1)
print(lightyLight + lightyLight.r)
r = lightyLight + lightyLight.r
print(LightIntensity.map_0_1(r))
print(LightIntensity.map_0_255(r))
