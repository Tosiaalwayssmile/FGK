from vector import *
from ray import *

## Documentation for a class Plane.
class Plane:

    ## The constructor.
    def __init__(self, normal_vector, d):
        if normal_vector == Vec3(0, 0, 0):
            raise ValueError('Normal vector cannot be (0, 0, 0)')

        ## A class variable. Normal vector.
        self.normal_vector = normal_vector
        ## A class variable. Coordinate x of the normal vector.
        self.a = normal_vector.x
        ## A class variable. Coordinate y of the normal vector.
        self.b = normal_vector.y
        ## A class variable. Coordinate z of the normal vector.
        self.c = normal_vector.z
        ## A class variable. A shift, along the plane normal, from the center of the coordinate system.
        self.d = d

    ## Function returning object values in string format.
    def __str__(self):
        return str(self.a) + 'x + ' + str(self.b) + 'y + ' + str(self.c) + 'z + ' + str(self.d)

    ## Function returning intersection of a ray and a plane.   
    def get_intersection(self, ray):
        # Ray is paralell to plane
        if self.normal_vector * ray.direction == 0:
            return None

        # Calculate parameters
        t = (-self.d - (self.normal_vector * ray.origin)) / (self.normal_vector * ray.direction)

        # Check if intersection is before origin of ray
        if t < 0:
            return None

        x = round(ray.origin.x + (t * ray.direction.x), 5)
        y = round(ray.origin.y + (t * ray.direction.y), 5)
        z = round(ray.origin.z + (t * ray.direction.z), 5)
        point = Vec3(x, y, z)

        # Check if point is in range
        if ray.origin.distance(point) > ray.length:
            return None

        return point
