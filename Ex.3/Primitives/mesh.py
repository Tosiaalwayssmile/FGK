from Primitives.primitive import *
from Primitives.ray import *
from Primitives.triangle import *
from obj_parser import *


class Mesh(Primitive):

    def __init__(self, obj_file, position=Vec3(), color=[1, 0, 1]):

        super().__init__(color)

        triangles_list = read_obj_file(obj_file)

        vertices = []
        self.triangles = []

        for t in triangles_list[0]:
            vertices.append(t)
        for f in triangles_list[1]:
            self.triangles.append(Triangle(position + vertices[f.x], position + vertices[f.y], position + vertices[f.z], color))

    def get_detailed_intersection(self, ray):
        p = None
        d = None
        for t in self.triangles:
            hit = t.get_detailed_intersection(ray)
            if hit[0] is not None:
                if d is None or hit[1] < d:
                    p = hit[0]
                    d = hit[1]
        return p, d

    def get_intersection(self, ray):
        return get_detailed_intersection(ray)[0]
