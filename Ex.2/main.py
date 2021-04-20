from Primitives.sphere import *
from Cameras.perspective_camera import *
from Cameras.orthogonal_camera import *

# ============
#    ZAD 2
# ============
p_cam = PerspectiveCamera(position=Vec3(0, 0, 0), view_direction=Vec3(0, 0, 1), width=500, height=500, fov=60)
o_cam = OrthogonalCamera(position=Vec3(0, 0, 0), view_direction=Vec3(0, 0, 1), width=500, height=500, pixel_size=(0.01, 0.01))

primitives1 = [
    Sphere(Vec3(0, 0, 8), 2, [.2, .4, .75]),
    Sphere(Vec3(2, 0, 6), 1, [.9, .0, 0])
]

primitives2 = [
    Sphere(Vec3(0, 0, 8), 1, [.4, .4, .7]),
]

p_cam.render_scene(primitives1)
#o_cam.render_scene(primitives2)

print('KONIEC')
