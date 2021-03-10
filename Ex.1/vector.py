import math


class Vec:

    # Methods
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'

    def length(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z))

    def distance(self, other):
        return math.sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2) + ((self.z - other.z) ** 2))

    def is_point_on_ray(self, ray):
        return ray.is_point_on_ray(self)
