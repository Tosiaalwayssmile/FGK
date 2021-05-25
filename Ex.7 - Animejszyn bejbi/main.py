import imageio
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


p_cam = PerspectiveCamera(position=Vec3(0, 0, 0), view_direction=Vec3(0, 0, 1), width=256, height=256, fov=40)

material_dull = Material(material_type=MaterialType.Dull)
material_reflective = Material(material_type=MaterialType.Reflective)
material_refractive = Material(material_type=MaterialType.Refractive, index_of_refraction=1.5)

primitives1 = [
    Sphere(Vec3(0, 0, 10), .75, [0, 0, 1], material_reflective),
    Sphere(Vec3(0, 0, 10), .75, [1, 1, 1], material_refractive),

    Plane(Vec3(0, 0, -1), 14, color=[1, 0, 0], material=material_dull),
    Plane(Vec3(0, 1, 0), 2.5, color=[0, 1, 0], material=material_dull),
    Plane(Vec3(0, -1, 0), 2.5, color=[0, 0, 1], material=material_dull),
    Plane(Vec3(1, 0, 0), 2.5, color=[1, 0, 1], material=material_dull),
    Plane(Vec3(-1, 0, 0), 2.5, color=[1, 1, 0], material=material_dull),
    Plane(Vec3(0, 0, 1), 0, color=[0, 1, 1], material=material_dull),
]


# First element is ambient light: [intensity, [color]]
lights = [
    [.1, [1, 1, 1]],
    PointLightSource(position=Vec3(0, 0, 10), color=[1, 1, 1], intensity=10)
]

images = []
for i in range(360):
    print('GENERATING IMAGE: ' + str(i + 1))
    filename = 'Images/Image_' + str(i) + '.png'
    angle = np.deg2rad(i)
    sin = np.sin(angle)
    cos = np.cos(angle)
    lights[1].position.z = 10 + 1.5 * sin
    primitives1[0].position.y = sin
    primitives1[0].position.x = cos
    primitives1[1].position.y = -sin
    primitives1[0].position.x = -cos

    p_cam.render_scene(primitives1, lights, antialiasing=False, filename=filename)
    images.append(imageio.imread(filename))

gif_name = 'gif.gif'
if os.path.exists(gif_name):
    os.remove(gif_name)
imageio.mimsave(gif_name, images, fps=60)

print('KONIEC')
