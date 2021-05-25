from Primitives.triangle import *
from obj_parser import *


## Documentation for a class Mesh.
class Mesh(Primitive):

    ## Constructor.
    def __init__(self, obj_file, position=Vec3(), color=[1, 1, 1], material=None):

        super().__init__(None, material)

        triangles_list = read_obj_file(obj_file)

        vertices = []
        self.triangles = []
        for t in triangles_list[0]:
            vertices.append(t)
        for f in triangles_list[1]:
            self.triangles.append(Triangle(position + vertices[f.x], position + vertices[f.y], position + vertices[f.z], color, material))

    ## Checks if ray intersects with mesh and returns list of hits
    def get_detailed_intersections(self, ray):
        hits = []
        for t in self.triangles:
            hit = t.get_detailed_intersection(ray)
            if hit is not None:
                hits.append(hit)

        if len(hits) == 0:
            hits.append(None)
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

    def get_texture_color(self, coords):
        if self.material is None or self.material.texture is None:
            return self.color
        else:
            return self.material.texture.rectangular_mapping(coords)

