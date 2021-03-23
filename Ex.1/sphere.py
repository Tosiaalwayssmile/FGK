from math import *
from vector import *
from ray import *

## Documentation for a class Sphere.
class Sphere:

    ## The constructor.
    def __init__(self, centre = Vec3(0, 0, 0), radius = math.inf):
        
        ## A class variable. Centre of a sphere.
        self.centre = centre
        ## A class variable. Radius of a sphere.
        self.radius = radius
        ## A class variable. Area of a sphere.
        self.area = 0
        ## A class variable. Volume of a sphere.
        self.volume = 0

    ## Function returning centre of the sphere.
    def get_centre(self):
        return self.centre

    ## Function returning radius of the sphere.   
    def get_radius(self):
        return self.radius

    ## Function returning area of the sphere.  
    def surface_area(self):
        self.area = 4 * 3.14 * (self.radius * self.radius)
        return self.area

    ## Function returning volume of the sphere.  
    def get_volume(self):
        self.volume = (4/3) * 3.14 * (self.radius * self.radius * self.radius)
        return round(self.volume, 2)
        
    ## Function returning object values in string format.
    def __str__(self):
        return 'Sphere: Centre: ' + self.centre + ', Radius: ' + str(self.radius)
        
    ## Function returning intersection of a ray and a sphere.     
    def get_ray_intersections(self, ray):

        # Calculate variables
        oc = ray.origin - self.centre
        a = round(ray.direction * ray.direction, 5)
        b = round(2 * (ray.direction * oc), 5)
        c = round(oc * oc - (self.radius * self.radius), 5)

        # Calculate delta
        delta = round(b * b - 4 * a * c, 5)

        # If delta is negative, there is no intersection
        if delta < -0.001:
            return None

        # If delta equals zero, there is one possible intersection
        if 0.001 >= delta >= -0.001:
            t = -b / (2 * a)
            # If t is negative, intersetion occurs before origin point of ray
            if t < 0:
                return None
            # Otherwise, return intersection point as one-element array (since 2 intersections are possible if delta is positive)
            p = ray.origin + t * ray.direction
            p.x = round(p.x, 5)
            p.y = round(p.y, 5)
            p.z = round(p.z, 5)
            return [p]

        p1 = None
        p2 = None

        t1 = (-b + math.sqrt(delta)) / (2 * a)
        if t1 >= 0:
            p1 = ray.origin + t1 * ray.direction
            p1.x = round(p1.x, 5)
            p1.y = round(p1.y, 5)
            p1.z = round(p1.z, 5)

        t2 = (-b - math.sqrt(delta)) / (2 * a)
        if t2 >= 0:
            p2 = ray.origin + t2 * ray.direction
            p2.x = round(p2.x, 5)
            p2.y = round(p2.y, 5)
            p2.z = round(p2.z, 5)

        if p1 is None and p2 is None:
            return None
        if p1 is None:
            return [p2]
        if p2 is None:
            return [p1]
        return [p1, p2]
