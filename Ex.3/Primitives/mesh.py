from Primitives.primitive import *
from Primitives.ray import *
from Primitives.triangle import *
from obj_parser import *
import numpy as np


class Mesh(Primitive):

    def __init__(self, obj_file, position=Vec3()):

        super().__init__(None)

        triangles_list = read_obj_file(obj_file)

        vertices = []
        self.triangles = []
        m=0
        for t in triangles_list[0]:
            vertices.append(t)
        for f in triangles_list[1]:
            c = np.random.rand()
            self.triangles.append(Triangle(position + vertices[f.x], position + vertices[f.y], position + vertices[f.z], [c, c, c]))

    def get_detailed_intersection(self, ray):
        point = None
        distance = None
        color = None
        for t in self.triangles:
            hit = t.get_detailed_intersection(ray)
            if hit[0] is not None:
                if distance is None or hit[1] < distance:
                    color = t.color
                    point = hit[0]
                    distance = hit[1]
        return point, distance, color

    def get_intersection(self, ray):
        return get_detailed_intersection(ray)[0]
