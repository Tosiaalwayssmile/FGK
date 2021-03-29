from Primitives.sphere import *
from Primitives.plane import *
from Cameras.camera_orthogonal import *

# ============
#    ZAD 2
# ============
cam = CameraOrthogonal(position=Vec3(1, 0, 0), view_direction=Vec3(0, .1, 1))
primitives = []

primitives.append(Sphere(Vec3(0, 0, 2), 1))
primitives.append(Sphere(Vec3(1, .5, 2), .5))

cam.generate_image(primitives)
