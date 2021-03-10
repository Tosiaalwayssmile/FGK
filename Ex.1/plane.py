from vector import *
from ray import *


class Plane:

    def __init__(self, normal_vector, d):
        if normal_vector == Vec(0, 0, 0):
            raise ValueError('Normal vector cannot be (0, 0, 0)')

        self.normal_vector = normal_vector
        self.a = normal_vector.x
        self.b = normal_vector.y
        self.c = normal_vector.z
        self.d = d

    def __str__(self):
        return str(self.a) + 'x + ' + str(self.b) + 'y + ' + str(self.c) + 'z + ' + str(self.d)

    def get_intersection(self, ray):
        # Can't calculate is ray has direction (0, 0, 0)
        if ray.direction == Vec(0, 0, 0):
            raise ValueError('Ray direction vector cannot be (0, 0, 0)')

        # Ray is paralell to plane
        if self.normal_vector * ray.direction == 0:
            return None

        # Calculate parameters
        t = (-self.d - (self.normal_vector * ray.origin)) / (self.normal_vector * ray.direction)

        # Check if intersection is before origin of ray
        if t < 0:
            return None

        x = ray.origin.x + (t * ray.direction.x)
        y = ray.origin.y + (t * ray.direction.y)
        z = ray.origin.z + (t * ray.direction.z)
        point = Vec(x, y, z)

        # Check if point is in range
        if ray.origin.distance(point) > ray.length:
            return None

        return point
