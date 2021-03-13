from math import *
from vector import *
from ray import *


class Sphere:
    def __init__(self, centre = Vec3(0, 0, 0), radius = math.inf):
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
        return self.area

    def get_volume(self):
        self.volume = (4/3) * 3.14 * (self.radius * self.radius * self.radius)
        return round(self.volume, 2)
        
    # Print #
    def __str__(self):
        return 'Sphere: Centre: ' + self.centre + ', Radius: ' + str(self.radius)
        
    def get_sphere_intersection(self, ray):
        
        x1 = ray.origin.x
        y1 = ray.origin.y
        z1 = ray.origin.z

        x2 = ray.direction.x
        y2 = ray.direction.y
        z2 = ray.direction.z

        xc = self.centre.x        
        yc = self.centre.y       
        zc = self.centre.z

        a = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) + (z2 - z1) * (z2 - z1) 
        b =  2 * ((x2 - x1) * (xc - x1) + (y2 - y1) * (yc - y1) + (zc - z1) * (z2 - z1))
        c = (xc - x1)* (xc - x1) + (yc - y1) * (yc - y1) + (zc - z1) * (zc - z1) - self.radius * self.radius
      
        point = []
        t = []

        delta = b * b - 4 * a * c 
        if delta < 0:
            return None

        if delta == 0:
            t.append(-b / 2 * a)
            
        if delta > 0:
            t.append(-b - math.sqrt(delta) / (2 * a)) 
            t.append(-b + math.sqrt(delta) / (2 * a)) 
            
        t_length = len(t)
        for i in range (t_length):
            x = round(x1 + (x2 - x1) * t[i], 2)
            y = round(y1 + (y2 - y1) * t[i], 2)
            z = round(z1 + (z2 - z1) * t[i], 2)
            point.append(Vec3(x, y, z))

        return point
   
