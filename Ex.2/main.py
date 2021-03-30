from Primitives.sphere import *
from Primitives.plane import *
from Cameras.camera import *
from light_intensity import *
from image import *

# ============
#    ZAD 2
# ============
cam = Camera(position=Vec3(0, 0, 0), view_direction=Vec3(0, 0, 1))
cam.perspectic_init()
# cam.ortogonal_init()

primitives = [
    Sphere(Vec3(-1.1, 0, 10), 1),
    Sphere(Vec3(1.1, 0, 20), 1)
]

cam.generate_image(primitives)

background_color = (153, 204, 255)  # RGB
im = MyImage(500, 500)
im.clear_color(background_color)

background_color2 = (250, 0, 0)     # RGB
for i in range(10):
    for j in range(30):
        im.set_pixel(j, i, background_color2)
im.save_image()
