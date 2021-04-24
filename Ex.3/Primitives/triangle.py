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
        self.normal_vector = ((v2 - v1).cross(v3 - v1)).normalize()

    ## Function returning object values in string format.
    def __str__(self):
        return 'Triangle: A' + str(self.v1) + ', B' + str(self.v2) + ', C' + str(self.v3) + ', Normal' + str(self.normal_vector)

    ## Checks if ray intersects with triangle and returns intersection points in form one- or two-element array.
    def get_ray_intersections(self, ray):

        # Calculate variables
        e1 = Vec3(self.v2.x - self.v1.x, self.v2.y - self.v1.y, self.v2.z - self.v1.z)
        e2 = Vec3(self.v3.x - self.v1.x, self.v3.y - self.v1.y, self.v3.z - self.v1.z)

        h = Vec3.cross(ray.direction, e2)
        a = e1 * h

        if (a > -0.00001 and a < 0.00001):
            return None, 0

        f = 1 / a
        s = Vec3(ray.origin.x - self.v1.x, ray.origin.y - self.v1.y, ray.origin.z - self.v1.z)

        u = f * s * h

        if (u < 0.0 or u > 1.0):
            return None, 0

        q = s.cross(e1)
        v = f * ray.direction * q
        
        if (v < 0.0 or u + v > 1.0):
            return None, 0

        distance = f * e2 * q

        # Ray Intersection
        if (distance <= 0.00001):
            return None, 0
        
        point = ray.origin + distance * ray.direction
        return [(point, distance)]

    ## Checks if ray intersects with sphere and returns point closest to ray origin.
    def get_intersection(self, ray):
        intersections = self.get_ray_intersections(ray)
        if intersections is None:
            return None
        if len(intersections) == 1:
            return intersections[0][0]
        if intersections[0][1] < intersections[1][1]:
            return intersections[0][0]
        return intersections[1][0]

    ## Function returning intersection point and distance
    def get_detailed_intersection(self, ray):
        intersections = self.get_ray_intersections(ray)
        if intersections[0] is None:
            return None, 0
        if len(intersections) == 1 or intersections[0][1] < intersections[1][1]:
            return intersections[0]
        return intersections[1]
    
    

   