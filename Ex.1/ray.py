import math
from vector import *

## Documentation for a class Ray.
class Ray:

    ## The constructor.
    def __init__(self, origin=Vec3(0, 0, 0), direction=Vec3(1, 1, 1), length=math.inf):

        ## A class variable. Origin vector of a given ray.
        self.origin = origin
        ## A class variable. Direction vector of a given ray.
        self.direction = direction / direction.length()
        ## A class variable. Length of a given ray.
        self.length = length

    ## Function printing ray attributes. 
    def __str__(self):
        return 'Origin: ' + str(self.origin) + ', Vector: ' + str(self.direction)

    ## Function returning true if point is on ray and false otherwise. 
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

    ## Function setting new direction vector.
    def set_direction(self, new_direction):
        if new_direction == Vec3(0, 0, 0):
            raise ValueError('Direction vector cannot be (0, 0, 0)')
        self.direction = new_direction / new_direction.length()

    ## Function calling plane.get_intersection() method.
    def get_plane_intersection(self, plane):
        return plane.get_intersection(self)

    ## Function calling sphere.get_ray_intersections() method.
    def get_sphere_intersections(self, sphere):
        return sphere.get_ray_intersections(self)
