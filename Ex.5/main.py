from Primitives.sphere import *
from Primitives.triangle import *
from Primitives.mesh import *
from Cameras.perspective_camera import *
from Cameras.orthogonal_camera import *
from Lights.point_light_source import *
from obj_parser import *
from material import *
from texture import *

# m1=Material()
# print(m1)
p_cam = PerspectiveCamera(position=Vec3(0, 0, 0), view_direction=Vec3(0, 0, 1), width=512, height=512, fov=40)
o_cam = OrthogonalCamera(position=Vec3(0, 0, 0), view_direction=Vec3(0, 0, 1), width=512, height=512, pixel_size=(0.01, 0.01))

texture = Texture('sample_texture.png')
material = Material(texture=texture)

primitives1 = [
    Sphere(Vec3(0, 0, 8), 2, [.2, .4, .75], material),
    #Sphere(Vec3(2, 0, 7), 1, [.9, .0, 0])
]

primitives2 = [
    Triangle(Vec3(-1, 0, 8), Vec3(0, 1, 8), Vec3(1, 0, 8), [0, 0, 0])
]
primitives3 = [
    Mesh('cube.obj', position=Vec3(0, 2.3, 8)),
    Mesh('pyramid.obj', position=Vec3(0, -2, 8)),
    Sphere(Vec3(0, 2.3, 8), 1.1, [.2, .4, .75])
]

# First element is ambient light: [intensity, [color]]
lights = [
    [0.2, [1, 1, 1]],
    PointLightSource(position=Vec3(3, 0, 3), color=[1, 1, 1], intensity=10)
]

p_cam.render_scene(primitives1, lights, antialiasing=True)
# o_cam.render_scene(primitives3)

print('KONIEC')