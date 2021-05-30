from materialType import *
import math
import numpy as np
from vector import *
from Primitives.plane import *
import copy
import Scene


## Documentation for a class Ray.
class Ray:

    ## Constructor.
    def __init__(self, origin = Vec3(0, 0, 0), direction=None, target=None, length = math.inf, medium=None):

        ## Origin vector of a given ray.
        ## Default = (0, 0, 0)
        self.origin = origin

        if direction is None and target is None:
            raise Exception('Ray has to have either direction or target')

        if direction is not None:
            if target is not None:
                raise Exception('Ray can have either direction or target, not both (second one is calculated based on given one)')

            if direction == Vec3(0, 0, 0):
                raise Exception('Ray\'s direction vector cannot be (0, 0, 0)')
            ## Direction vector of a given ray.
            ## Cannot be (0, 0, 0).
            self.direction = direction / direction.length()

            ## Target point of a given ray.
            ## Cannot be the same as origin.
            self.target = self.origin + self.direction

        if target is not None:
            if target == self.origin:
                raise Exception('Ray cannot have equal origin and target')
            self.target = target
            self.direction = self.origin - target
            self.direction /= self.direction.length()

        ## Length of a given ray.
        ## Default = Infinity
        self.length = length

        ## The medium in which the ray propagates
        self.medium = medium

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
        self.direction = new_direction.normalized()
        self.target = self.origin + new_direction

    ## Sets new target and updates direction vector.
    def set_target(self, new_target):
        if new_target == self.origin:
            raise Exception('Target cannot be equal to origin of ray')
        self.target = new_target
        self.direction = (self.target - self.origin).normalized()

    ## Plane.get_intersection(ray) wrapper.
    def get_plane_intersection(self, plane):
        return plane.get_intersection(self)

    ## Sphere.get_intersection(ray) wrapper.
    def get_sphere_intersection(self, sphere):
        return sphere.get_intersection(self)

    ## Sphere.get_ray_intersections(ray) wrapper.
    def get_sphere_intersections(self, sphere):
        return sphere.get_ray_intersections(self)

    ## Returns medium index of refraction
    def get_medium_refraction_index(self):
        if self.medium is None:
            return 1
        return self.medium.material.index_of_refraction

    ## Iterates through list of primitives and returns the closest hit, raytracing step 2
    def get_pixel_hit(self, primitives):
        closest_hit = None
        for pr in primitives:
            hits = pr.get_detailed_intersections(self)
            if hits[0] is None:
                continue
            for hit in hits:
                # if (closest_hit is None or hit.distance < closest_hit.distance) and (hit.distance > .05 ):
                if (closest_hit is None or hit.distance < closest_hit.distance) and (hit.distance > .05 ):
                    closest_hit = hit
                # elif hit.distance < closest_hit.distance and hit.primitive != closest_hit.primitive:
                #     closest_hit = hit

        return closest_hit

    ## Iterates through list of primitives and lights and calculates pixel color
    def get_pixel_color(self, scene=None, shutter_exposure_time=None, primitives=None, lights=None, recursion_number=0):
        recursion_limit = 6

        if scene is not None and shutter_exposire_time is not None and primitives is None and lights is None:
            primitives, lights = scene.get_scene_for_time(np.random.uniform(shutter_exposure_time[0], shutter_exposure_time[1]))

        hit = self.get_pixel_hit(primitives)

        if hit is None:
            return None

        # Set ambient light
        r = lights[0][0] * lights[0][1][0]
        g = lights[0][0] * lights[0][1][1]
        b = lights[0][0] * lights[0][1][2]

        # Iterate through lights
        for light in lights[1:]:

            distance = hit.point.distance(light.position)
            ray = Ray(origin=hit.point, target=light.position, length=distance + 0.001)
            if ray.check_light_intersection(primitives):
                # If something blocks the light, go to next light
                continue

            normal = hit.primitive.get_normal(hit.point).normalized()
            direction = ray.direction.normalized()
            falloff = np.abs(normal * direction / (normal.length() * direction.length()))

            # If nothing blocks the light
            i = light.intensity * falloff / distance ** 2
            i = min(i, 1)
            i = max(i, 0)

            # Phong model
            if hit.primitive.material is not None:
                reflection = -ray.direction - 2 * (-ray.direction * normal) * normal
                # For diffusing material
                intensity = -i * (hit.primitive.material.mirror_reflection_coefficient * (direction * normal) + hit.primitive.material.diffuse_reflection_coefficient * (reflection * -self.direction) ** hit.primitive.material.specularExponent)
                intensity = min(intensity, 1)
                intensity = max(intensity, 0)
            else:
                intensity = i

            r += light.color[0] * intensity
            g += light.color[1] * intensity
            b += light.color[2] * intensity
        
        # Recursive raytracing, reflective material
        if hit.primitive.material.material_type is MaterialType.Reflective and recursion_number < recursion_limit:
            normal = hit.primitive.get_normal(hit.point).normalized()
            reflection = self.direction - 2 * (self.direction * normal) * normal
            recursive_ray = Ray(origin=hit.point, direction=reflection)

            recursion_number += 1
            recursive_color = recursive_ray.get_pixel_color(primitives=primitives, lights=lights, recursion_number=recursion_number)

            if recursive_color is not None:
                # It's no matter how much recursive material is lit, it only matters how lit is point that it reflects
                # return [recursive_color[i] * [r, g, b][i] for i in range(3)]
                return recursive_color
        
        # Refractive material
        elif hit.primitive.material.material_type is MaterialType.Refractive and recursion_number < recursion_limit:
            normal = hit.primitive.get_normal(hit.point).normalized()
            n1 = self.get_medium_refraction_index()
            n2 = hit.primitive.material.index_of_refraction
            new_medium = hit.primitive

            n12 = n1 / n2
            direction = self.direction.normalized()
            nor_cross_dir = normal.cross(direction)

            refracted_vec = np.sqrt((1 - n12 ** 2) * (1 - (nor_cross_dir * nor_cross_dir))) * -normal + (n12 * (direction - nor_cross_dir * normal))

            recursive_ray = Ray(origin=hit.point, direction=refracted_vec, medium=new_medium)

            recursion_number += 1
            recursive_color = recursive_ray.get_pixel_color(primitives=primitives, lights=lights, recursion_number=recursion_number)

            if recursive_color is not None:
                # It's no matter how much recursive material is lit, it only matters how lit is point that is behind it
                # return [recursive_color[i] * [r, g, b][i] for i in range(3)]
                return recursive_color

        return [hit.primitive.get_texture_color(hit.point)[i] * [r, g, b][i] for i in range(3)]

    def get_avg_pixel_color(self, scene=None, shutter_exposure_timeframe=None, amount_of_samples=3):
        px_color = np.array([.0, .0, .0])
        step = (shutter_exposure_timeframe[1] - shutter_exposure_timeframe[0]) / amount_of_samples
        for i in range(amount_of_samples):
            primitives, lights = scene.get_scene_for_time(shutter_exposure_timeframe[0] + (step * i))
            px_color += self.get_pixel_color(primitives=primitives, lights=lights)
        return [c / amount_of_samples for c in px_color]

    ## Checks if ray intersects with any given primitive
    def check_intersection(self, primitives):
        for p in primitives:
            hits = p.get_detailed_intersections(self)
            if hits[0] is None:
                continue
            for hit in hits:
                min_dist = 0.0001
                if isinstance(p, Plane):
                    min_dist = 0
                if min_dist <= hit.distance <= self.length:
                    return False
        return True

    ## Checks if ray intersects with any given primitive, ignores primitives with refractive material
    def check_light_intersection(self, primitives):

        import Primitives.sphere

        for p in primitives:
            if isinstance(p, Primitives.sphere.Sphere):
                hits = p.get_detailed_intersections(self, invert_dir=True)
            else:
                hits = p.get_detailed_intersections(self)
            if hits[0] is None:
                continue
            for hit in hits:
                if isinstance(p, Plane) and hit.primitive is p:
                    continue
                if 0.001 <= hit.distance <= self.length and p.material.material_type != MaterialType.Refractive:
                    # If somethong blocks the light
                    return True
        return False


