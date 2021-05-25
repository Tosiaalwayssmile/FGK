from Math.hit import *
from Math.ray import *
from Primitives.primitive import *


## Documentation for a class Sphere.
class Sphere(Primitive):

    ## Constructor.
    def __init__(self, centre=Vec3(0, 0, 0), radius=1, color=[1, 0, 1], material=None):

        super().__init__(color, material)

        ## Centre of the sphere
        self.centre = centre
        self.change_radius(radius)
        self.color = color

    ## Sets radius and recalculates area and volume
    def change_radius(self, new_radius):
        ## Radius of the sphere.
        self.radius = new_radius
        ## Area of the sphere.
        self.area = round(4 * 3.14 * (self.radius * self.radius), 5)
        ## Volume of the sphere.
        self.volume = round((4/3) * 3.14 * (self.radius * self.radius * self.radius), 5)

    ## Function returning object values in string format.
    def __str__(self):
        return 'Sphere: Centre: ' + self.centre + ', Radius: ' + str(self.radius)
        
    ## Checks if ray intersects with sphere and returns list of hits
    def get_detailed_intersections(self, ray):
        # Calculate variables
        oc = ray.origin - self.centre
        a = round(ray.direction * ray.direction, 5)
        b = round(2 * (ray.direction * oc), 5)
        c = round(oc * oc - (self.radius * self.radius), 5)

        # Calculate delta
        delta = round(b * b - 4 * a * c, 5)

        # If delta is negative, there is no intersection
        if delta < -0.001:
            return [None]

        # If delta equals zero, there is one possible intersection
        if 0.001 >= delta >= -0.001:
            t = -b / (2 * a)
            # If t is negative, intersetion occurs before origin point of ray
            if t < 0:
                return [None]
            # Otherwise, return intersection point as one-element array (since 2 intersections are possible if delta is positive)
            p = ray.origin + t * ray.direction
            p.x = round(p.x, 5)
            p.y = round(p.y, 5)
            p.z = round(p.z, 5)
            dist = ray.origin.distance(p)
            return [Hit(p, dist, self.color, self)]

        p1 = None
        p2 = None
        dist1 = None
        dist2 = None

        t1 = (-b + math.sqrt(delta)) / (2 * a)
        if t1 >= 0:
            p1 = ray.origin + t1 * ray.direction
            p1.x = round(p1.x, 5)
            p1.y = round(p1.y, 5)
            p1.z = round(p1.z, 5)
            dist1 = ray.origin.distance(p1)

        t2 = (-b - math.sqrt(delta)) / (2 * a)
        if t2 >= 0:
            p2 = ray.origin + t2 * ray.direction
            p2.x = round(p2.x, 5)
            p2.y = round(p2.y, 5)
            p2.z = round(p2.z, 5)
            dist2 = ray.origin.distance(p2)

        if p1 is None and p2 is None:
            return [None]
        if p1 is None:
            return [Hit(p2, dist2, self.color, self)]
        if p2 is None:
            return [Hit(p1, dist1, self.color, self)]
        return [Hit(p1, dist1, self.color, self), Hit(p2, dist2, self.color, self)]

    ## Function returning hit.
    def get_detailed_intersection(self, ray):
        hits = self.get_detailed_intersections(ray)
        if len(hits) == 1 or hits[0].distance < hits[1].distance:
            return hits[0]
        return hits[1]

    ## Checks if ray intersects with sphere and returns point closest to ray origin.
    def get_intersection(self, ray):
        hit = self.get_detailed_intersection(ray)
        if hit is None:
            return None
        return hit.point

    ## Gets normal for given point
    def get_normal(self, point):
        return (point - self.centre).normalized()

    ## Gets pixel color from material texture. If texture or material is None than return privmitive color
    def get_texture_color(self, coords):
        if self.material is None or self.material.texture is None :
            return self.color
        else:
            return self.material.texture.spherical_mapping((coords - self.centre).normalized(), self.radius)
