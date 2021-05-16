from Primitives.primitive import *
from Primitives.ray import *
from Primitives.triangle import *
from obj_parser import *
import numpy as np


## Documentation for a class Mesh.
class Mesh(Primitive):

    ## Constructor.
    def __init__(self, obj_file, position=Vec3(), material=None):

        super().__init__(None, material)

        triangles_list = read_obj_file(obj_file)

        vertices = []
        self.triangles = []
        for t in triangles_list[0]:
            vertices.append(t)
        for f in triangles_list[1]:
            c = np.random.rand()
            self.triangles.append(Triangle(position + vertices[f.x], position + vertices[f.y], position + vertices[f.z], [c, c, c], material))

    ## Checks if ray intersects with mesh and returns list of hits
    def get_detailed_intersections(self, ray):
        hits = []
        for t in self.triangles:
            hit = t.get_detailed_intersection(ray)
            if hit.point is not None:
                hits.append(hit)
        return hits

    ## Checks if ray intersects with mesh and returns hit closest to ray origin.
    def get_detailed_intersection(self, ray):
        closest_hit = None
        for hit in self.get_detailed_intersections(ray):
            if closest_hit is None or hit.distance < closest_hit.distance:
                closest_hit = hit
        return closest_hit

    ## Function returning intersection point.
    def get_intersection(self, ray):
        return self.get_detailed_intersection(ray).point

    def get_normal(self, point):
        pass

