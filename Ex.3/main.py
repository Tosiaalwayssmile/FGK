from Primitives.sphere import *
from Primitives.triangle import *
from Primitives.mesh import *
from Cameras.perspective_camera import *
from Cameras.orthogonal_camera import *
from obj_parser import *


p_cam = PerspectiveCamera(position=Vec3(0, 0, 0), view_direction=Vec3(0, 0, 1), width=512, height=512, fov=40)
o_cam = OrthogonalCamera(position=Vec3(0, 0, 0), view_direction=Vec3(0, 0, 1), width=512, height=512, pixel_size=(0.01, 0.01))

primitives1 = [
    Sphere(Vec3(0, 0, 8), 2, [.2, .4, .75]),
    Sphere(Vec3(2, 0, 7), 1, [.9, .0, 0])

]
primitives2 = [
    Triangle(Vec3(-1, 0, 8), Vec3(0, 1, 8), Vec3(1, 0, 8), [0, 0, 0])
]
primitives3 = [
    Mesh('cube.obj', position=Vec3(0, 2.3, 8)),
    Mesh('pyramid.obj', position=Vec3(0, -2, 8)),
    Sphere(Vec3(0, 2.3, 8), 1.1, [.2, .4, .75])
]

p_cam.render_scene(primitives3, antialiasing=False)
#o_cam.render_scene(primitives3)

print('KONIEC')
