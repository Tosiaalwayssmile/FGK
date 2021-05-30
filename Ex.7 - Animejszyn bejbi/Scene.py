from Primitives.sphere import *
from Primitives.plane import *
from Primitives.mesh import *
from Primitives.triangle import *
from material import *
from Lights.point_light_source import *


class Scene:

    def __init__(self):
        material_dull = Material(material_type=MaterialType.Dull)
        material_reflective = Material(material_type=MaterialType.Reflective)
        material_refractive = Material(material_type=MaterialType.Refractive, index_of_refraction=2)

        self.primitives = [
            Sphere(Vec3(1.5, 0, 7), .75, [0, 0, 1], material_reflective),
            Sphere(Vec3(-1.5, 0, 7), .75, [1, 1, 1], material_refractive),

            Plane(Vec3(1, 0, 0), 2.5, color=[1, 0, 1], material=material_dull),
            Plane(Vec3(-1, 0, 0), 2.5, color=[1, 1, 0], material=material_dull),
            Plane(Vec3(0, 1, 0), 2.5, color=[0, 1, 0], material=material_dull),
            Plane(Vec3(0, -1, 0), 2.5, color=[0, 0, 1], material=material_dull),
            Plane(Vec3(0, 0, 1), 0, color=[0, 1, 1], material=material_dull),
            Plane(Vec3(0, 0, -1), 10, color=[1, 0, 0], material=material_dull),
        ]

        # First element is ambient light: [intensity, [color]]
        self.lights = [
            [.2, [1, 1, 1]],
            PointLightSource(position=Vec3(0, 0, 7), color=[1, 1, 1], intensity=10)
        ]

    def get_scene_for_time(self, i):
        angle = np.deg2rad(i * 360)
        sin = np.sin(angle) * 1.5
        cos = np.cos(angle) * 1.5
        self.lights[1].position.z = 7 + sin
        self.primitives[0].position.y = sin
        self.primitives[0].position.x = cos
        self.primitives[1].position.y = -sin
        self.primitives[1].position.x = -cos

        return self.primitives, self.lights

