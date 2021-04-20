from Primitives.sphere import *
from Cameras.perspective_camera import *
from Cameras.orthogonal_camera import *

# ============
#    ZAD 2
# ============
<<<<<<< HEAD
time_0 = time.time()
cam = Camera(position=Vec3(0, 0, 0), view_direction=Vec3(0, 0, 1))
time_1 = time.time() 
cam.perspective_init2()
# cam.ortogonal_init()
time_2 = time.time()

primitives = [
    Sphere(Vec3(0, 0, 8), 1, [.5, .5, 1]),
    Sphere(Vec3(2.5, 0, 16), 1, [.2, .2, .5])
=======
p_cam = PerspectiveCamera(position=Vec3(0, 0, 0), view_direction=Vec3(0, 0, 1), width=500, height=500, fov=60)
o_cam = OrthogonalCamera(position=Vec3(0, 0, 0), view_direction=Vec3(0, 0, 1), width=500, height=500, pixel_size=(0.01, 0.01))

primitives1 = [
    Sphere(Vec3(0, 0, 8), 1, [.5, .5, .5]),
    Sphere(Vec3(3, 0, 8), 1, [.8, .4, 0])
]

primitives2 = [
    Sphere(Vec3(0, 0, 8), 1, [.2, .2, .75]),
>>>>>>> antyaliasing
]

# p_cam.render_scene(primitives1)
o_cam.render_scene(primitives2)

<<<<<<< HEAD
print("Czasy:")
print("Utworzenie obiektu kamery:           " + str(time_1 - time_0))
print("Czas utworzenia tablicy promieni:    " + str(time_2 - time_1))
print("Czas generowania obrazu:             " + str(time_4 - time_3))
=======
print('KONIEC')
>>>>>>> antyaliasing
