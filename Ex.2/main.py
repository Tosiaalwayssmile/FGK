from Primitives.sphere import *
from Primitives.plane import *
from Cameras.camera import *
from light_intensity import *
from image import *
import time


# ============
#    ZAD 2
# ============
time_0 = time.time()
cam = Camera(position=Vec3(0, 0, 0), view_direction=Vec3(0, 0, 1))
time_1 = time.time()
cam.perspective_init2()
# cam.ortogonal_init()
time_2 = time.time()

primitives = [
    Sphere(Vec3(-1.1, 0, 10), 1),
    Sphere(Vec3(1.1, 0, 20), 1)
]
time_3 = time.time()

cam.generate_image(primitives)
time_4 = time.time()

print("Czasy:")
print("Utworzenie obiektu kamery:           " + str(time_1 - time_0))
print("Czas utworzenia tablicy prmomieni:   " + str(time_2 - time_1))
print("Czas generowania obrazu:             " + str(time_4 - time_3))
