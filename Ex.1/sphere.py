from math import *
from vector import *
from ray import *

class Sphere:
    def __init__(self, centre = Vec(0, 0, 0), radius = math.inf):
        self.centre = centre
        self.radius = radius
        self.area = 0
        self.volume = 0

    def get_centre(self):
        return self.centre
        
    def get_radius(self):
        return self.radius

    def surface_area(self):
        self.area = 4 * 3.14 * (self.radius * self.radius)
        return (self.area)

    def get_volume(self):
        self.volume = (4/3) * 3.14 * (self.radius * self.radius * self.radius)
        return round(self.volume, 2)
        
    # Print #
    def __str__(self):
        return 'Sphere with radius (' + str(self.radius) + ')'

    