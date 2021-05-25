from materialType import *
from Primitives.sphere import *
from Primitives.plane import *
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
p_cam = PerspectiveCamera(position=Vec3(0, 0, 0), view_direction=Vec3(0, 0, 1), width=256, height=256, fov=40)
o_cam = OrthogonalCamera(position=Vec3(0, 0, 0), view_direction=Vec3(0, 0, 1), width=512, height=512, pixel_size=(0.01, 0.01))

texture = Texture('sample_texture.png')
material_dull = Material(material_type=MaterialType.Dull)
material_reflective = Material(material_type=MaterialType.Reflective)
material_refractive = Material(material_type=MaterialType.Refractive, index_of_refraction=1.5)

primitives1 = [
    # Mesh('cube.obj', position=Vec3(0, 0, 12), color=[.5, .5, .5], material=material_dull),
    Plane(Vec3(0, 0, -1), 14, color=[1, 0, 0], material=material_dull),
    Plane(Vec3(0, 1, 0), 2.5, color=[0, 1, 0], material=material_dull),
    Plane(Vec3(0, -1, 0), 2.5, color=[0, 0, 1], material=material_dull),
    Plane(Vec3(1, 0, 0), 2.5, color=[1, 0, 1], material=material_dull),
    Plane(Vec3(-1, 0, 0), 2.5, color=[1, 1, 0], material=material_dull),
    Plane(Vec3(0, 0, 1), 0, color=[0, 1, 1], material=material_dull),
    Sphere(Vec3(1.5, 1.5, 10), .75, [0, 0, 1], material_reflective),
    Sphere(Vec3(-1.5, -1.5, 10), .75, [1, 1, 1], material_refractive)
]


# First element is ambient light: [intensity, [color]]
lights = [
    [.1, [1, 1, 1]],
    PointLightSource(position=Vec3(0, 0, 10), color=[1, 1, 1], intensity=10)
]

p_cam.render_scene(primitives1, lights, antialiasing=False)
# o_cam.render_scene(primitives3)

print('KONIEC')