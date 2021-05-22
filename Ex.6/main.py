from materialType import *
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
material1 = Material(material_type=MaterialType.Dull)
material2 = Material(material_type=MaterialType.Reflective)

primitives1 = [
    Sphere(Vec3(-1.5, 0, 8), 2, [1, 0, 0], material1),
    Sphere(Vec3(2, 0, 8), 1, [0, 0, 1], material2)
    # Sphere(Vec3(-1.5, 2, 8), 1, [.2, .4, .75], material1)
]

# primitives2 = [
#     Triangle(Vec3(-3, 0, 8), Vec3(0, 3, 8), Vec3(3, 0, 8), [0, 0, 0], material)
# ]
# primitives3 = [
#     Mesh('cube.obj', position=Vec3(0, 2.3, 8), material=material),
#     Mesh('pyramid.obj', position=Vec3(0, -2, 8), material=material),
#     Sphere(Vec3(0, 2.3, 8), 1.1, [.2, .4, .75], material)
# ]

# First element is ambient light: [intensity, [color]]
lights = [
    [0.3, [1, 1, 1]],
    PointLightSource(position=Vec3(3, 0, 3), color=[1, 1, 1], intensity=10)
]

p_cam.render_scene(primitives1, lights, antialiasing=False)
# o_cam.render_scene(primitives3)

print('KONIEC')