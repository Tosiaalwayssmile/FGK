import math
from vector import *


class Ray:

    def __init__(self, origin = Vec3(0, 0, 0), direction = Vec3(0, 0, 0), length = math.inf):
        self.origin = origin
        self.direction = direction
        self.length = length

    def __str__(self):
        return 'Origin: ' + str(self.origin) + ', Vector: ' + str(self.direction)

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
            x_var = (point.x - self.origin.x) / self.direction.x
        if not skip_y:
            y_var = (point.y - self.origin.y) / self.direction.y
        if not skip_z:
            z_var = (point.z - self.origin.z) / self.direction.z

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

    def get_intersection(self, plane):
        return plane.get_intersection(self)
