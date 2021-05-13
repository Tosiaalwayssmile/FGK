from Primitives.ray import *
from Primitives.primitive import *


## Documentation for a class Triangle.
class Triangle(Primitive):

    ## Constructor.

    def __init__(self, v1=Vec3(0, 0, 0), v2=Vec3(0, 0, 0), v3=Vec3(0, 0, 0), color=[1, 0, 1]):

        super().__init__(color)

        ## Triangle vertex
        self.v1 = v1
        ## Triangle vertex
        self.v2 = v2
        ## Triangle vertex
        self.v3 = v3
        ## Color of triangle
        self.color = color
        ## Vector perpendicular to plane.
        self.normal_vector = ((v2 - v1).cross(v3 - v1)).normalized()

    ## Function returning object values in string format.
    def __str__(self):
        return 'Triangle: A' + str(self.v1) + ', B' + str(self.v2) + ', C' + str(self.v3) + ', Normal' + str(self.normal_vector)

    ## Checks if ray intersects with triangle and returns hit in form of a list.
    def get_detailed_intersections(self, ray):
        return [self.get_detailed_intersections(ray)]

    ## Checks if ray intercescts with triangle and returns hit.
    def get_detailed_intersection(self, ray):
        # Calculate variables
        e1 = Vec3(self.v2.x - self.v1.x, self.v2.y - self.v1.y, self.v2.z - self.v1.z)
        e2 = Vec3(self.v3.x - self.v1.x, self.v3.y - self.v1.y, self.v3.z - self.v1.z)

        h = Vec3.cross(ray.direction, e2)
        a = e1 * h

        if -0.00001 < a < 0.00001:
            return None

        f = 1 / a
        s = Vec3(ray.origin.x - self.v1.x, ray.origin.y - self.v1.y, ray.origin.z - self.v1.z)

        u = f * s * h

        if u < 0.0 or u > 1.0:
            return None

        q = s.cross(e1)
        v = f * ray.direction * q

        if v < 0.0 or u + v > 1.0:
            return None

        distance = f * e2 * q

        # Ray Intersection
        if distance <= 0.00001:
            return None

        point = ray.origin + distance * ray.direction
        return Hit(point, distance, self.color, self)

    ## Checks if ray intersects with triangle and return intersection point
    def get_intersection(self, ray):
        intersection = self.get_ray_intersection(ray)
        if intersection is None:
            return None
        return intersection.point

    def get_normal(self, point):
        v1 = self.v1 - self.v2
        v2 = self.v1 - self.v3
        return v1.cross(v2)
