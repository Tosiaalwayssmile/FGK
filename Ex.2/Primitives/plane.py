from Primitives.ray import *
from Primitives.primitive import *


## Documentation for a class Plane.
class Plane(Primitive):

    ## Constructor.
    def __init__(self, normal_vector, d, color=[255, 0, 255]):

        super().__init__(color)

        if normal_vector == Vec3(0, 0, 0):
            raise ValueError('Normal vector cannot be (0, 0, 0)')

        ## VEctor perpendicular to plane.
        self.normal_vector = normal_vector
        ## Represents A in 'Ax + By + Cz D = 0' equation.
        self.a = normal_vector.x
        ## Represents B in 'Ax + By + Cz D = 0' equation.
        self.b = normal_vector.y
        ## Represents C in 'Ax + By + Cz D = 0' equation.
        self.c = normal_vector.z
        ## Represents D in 'Ax + By + Cz D = 0' equation.
        self.d = d

    ## Function returning object values in string format.
    def __str__(self):
        return str(self.a) + 'x + ' + str(self.b) + 'y + ' + str(self.c) + 'z + ' + str(self.d)

    ## Returns tuple with multiple data: point (None if no intersection), distance to point
    def get_detailed_intersection(self, ray):
        # Ray is paralell to plane
        if self.normal_vector * ray.direction == 0:
            return None, 0

        # Calculate parameters
        t = (-self.d - (self.normal_vector * ray.origin)) / (self.normal_vector * ray.direction)

        # Check if intersection is before origin of ray
        if t < 0:
            return None, 0

        x = round(ray.origin.x + (t * ray.direction.x), 5)
        y = round(ray.origin.y + (t * ray.direction.y), 5)
        z = round(ray.origin.z + (t * ray.direction.z), 5)
        point = Vec3(x, y, z)

        # Check if point is in range
        distance = ray.origin.distance(point)
        if distance > ray.length:
            return None, 0

        return point, distance

    ## Checks if plane and ray intersect witch each other and returns intersection point if they do, otherwise None.
    def get_intersection(self, ray):
        return self.get_detailed_intersection(ray)[0]
