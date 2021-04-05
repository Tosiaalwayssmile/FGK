import math
from vector import *


## Documentation for a class Ray.
class Ray:

    ## Constructor.
    def __init__(self, origin = Vec3(0, 0, 0), direction = Vec3(1, 1, 1), length = math.inf):

        ## Origin vector of a given ray.
        ## Default = (0, 0, 0)
        self.origin = origin
        ## Direction vector of a given ray.
        ## Cannot be (0, 0, 0).
        ## Default = (1, 1, 1)
        self.direction = direction / direction.length()
        ## Length of a given ray.
        ## Default = Infinity
        self.length = length

    ## Function returning object values in string format.
    def __str__(self):
        return 'Origin: ' + str(self.origin) + ', Vector: ' + str(self.direction)

    ## Check if point is on ray, returns true if yes, false otherwise.
    def is_point_on_ray(self, point):

        # Variables to indicate if there is need to calculate parametric values
        skip_x = False
        skip_y = False
        skip_z = False

        # Check if direction value is not zero (to prevent divide by zero error) and if value is indeed zero,
        # compare values of point and origin (if they are different, then point is not on line)
        if self.direction.x == 0:
            if point.x != self.origin.x:
                return False
            skip_x = True
        if self.direction.y == 0:
            if point.y != self.origin.y:
                return False
            skip_y = True
        if self.direction.z == 0:
            if point.z != self.origin.z:
                return False
            skip_z = True

        # Get parametric values for X and Y coordinate
        if not skip_x:
            x_var = round((point.x - self.origin.x) / self.direction.x, 5)
        if not skip_y:
            y_var = round((point.y - self.origin.y) / self.direction.y, 5)
        if not skip_z:
            z_var = round((point.z - self.origin.z) / self.direction.z, 5)

        # Check if point is on the line
        if not ((skip_x or skip_y or x_var == y_var) and (skip_y or skip_z or y_var == z_var) and (skip_x or skip_z or x_var == z_var)):
            return False

        # Check if point is before or after origin point
        if (not skip_x and x_var < 0) or (not skip_y and y_var < 0) or (not skip_z and z_var < 0):
            return False

        # Check if point is in range
        if self.origin.distance(point) > self.length:
            return False

        # If all conditions are met, return true
        return True

    ## Sets new direction vector and converts it to normalized vector.
    def set_direction(self, new_direction):
        if new_direction == Vec3(0, 0, 0):
            raise ValueError('Direction vector cannot be (0, 0, 0)')
        self.direction = self.direction.normalize()

    ## Plane.get_intersection(ray) wrapper.
    def get_plane_intersection(self, plane):
        return plane.get_intersection(self)

    ## Sphere.get_intersection(ray) wrapper.
    def get_sphere_intersection(self, sphere):
        return sphere.get_intersection(self)

    ## Sphere.get_ray_intersections(ray) wrapper.
    def get_sphere_intersections(self, sphere):
        return sphere.get_ray_intersections(self)

    ## Iterates through list of primitives and returns color of the pixel
    def get_pixel_color(self, primitives):
        d = None
        c = None
        for p in primitives:
            hit = p.get_detailed_intersection(self)
            if hit[0] is None:
                continue
            if d is None or hit[1] < d:
                c = p.color
        return c
