from PIL import Image
from Primitives.ray import *
from Primitives.primitive import *
from image import *
import numpy as np


## Class for othogonal camera
class Camera:

    ## Constructor
    def __init__(self, position = Vec3(0, 0, 0), view_direction = Vec3(0, 0, 1), width = 512, height = 512, near = .1, far = 1000):
        
        ## Position of the camera
        self.position = position
        ## Direction camera is facing
        self.view_direction = view_direction.normalize() # target
        ## Width in pixels
        self.width = width
        ## Height in pixels
        self.height = height
        ## Near clipping plane
        self.near = near
        ## Far clipping plane
        self.far = far
        ## Field of View
        self.fov = 65.0
        ##
        self.up = Vec3(0, 1, 0)

    @staticmethod
    def adaptive_antialiasing(ray, A, B, C, D, E, depth, max_depth, horizontal, vertical, background_color, primitives):

        ray.set_direction(A)
        a_color = ray.get_pixel_color(primitives)
        if a_color is None:
            a_color = background_color

        ray.set_direction(B)
        b_color = ray.get_pixel_color(primitives)
        if b_color is None:
            b_color = background_color

        ray.set_direction(C)
        c_color = ray.get_pixel_color(primitives)
        if c_color is None:
            c_color = background_color

        ray.set_direction(D)
        d_color = ray.get_pixel_color(primitives)
        if d_color is None:
            d_color = background_color

        ray.set_direction(E)
        e_color = ray.get_pixel_color(primitives)
        if e_color is None:
            e_color = background_color

        """
        A---B
        |	|
        | E |
        |	|
        D---C
        A, B, C, D, E
        FOR A, E box: A, E + ver, E, E-hor, E-hor/2 + ver/2
        FOR B, E box: E + ver, B, E + hor, E, E + hor/2 + ver/2
        FOR C, E box: E, E+hor, C, E-ver, E + hor/2 - ver/2
        FOR D, E box: E - hor, E, E - ver, D, E-hor/2 - ver/2
        """

        # Check if algorithm reached maximum Depth, if so return color of the middle of subpixel
        if depth >= max_depth:
            return e_color

        if not np.array_equal(a_color, e_color):
            b_prim = E + vertical
            d_prim = E - horizontal
            e_prim = E - horizontal / 2 + vertical / 2
            a_color = Camera.adaptive_antialiasing(ray, A, b_prim, E, d_prim, e_prim, depth + 1, max_depth, horizontal / 2, vertical / 2, background_color, primitives)

        if not np.array_equal(b_color, e_color):
            a_prim = E + vertical
            c_prim = E + horizontal
            e_prim = E + horizontal / 2 + vertical / 2
            b_color = Camera.adaptive_antialiasing(ray, a_prim, B, c_prim, E, e_prim, depth + 1, max_depth, horizontal / 2, vertical / 2, background_color, primitives)

        if not np.array_equal(c_color, e_color):
            b_prim = E + horizontal
            d_prim = E - vertical
            e_prim = E + horizontal / 2 - vertical / 2
            c_color = Camera.adaptive_antialiasing(ray, E, b_prim, C, d_prim, e_prim, depth + 1, max_depth, horizontal / 2, vertical / 2, background_color, primitives)

        if not np.array_equal(d_color, e_color):
            a_prim = E - horizontal
            c_prim = E - vertical
            e_prim = E - horizontal / 2 - vertical / 2
            d_color = Camera.adaptive_antialiasing(ray, a_prim, E, c_prim, D, e_prim, depth + 1, max_depth, horizontal / 2, vertical / 2, background_color, primitives)

        # get mean of the colors and return them
        return np.multiply(np.add(np.add(np.add(np.add(a_color, b_color), c_color), d_color), np.multiply(e_color, 4)), 0.25)
        # return ((a_color + e_color) * 0.5 + (b_color + e_color) * 0.5 + (c_color + e_color) * 0.5 + (d_color + e_color) * 0.5) * 0.25

    def render_scene(self, primitives):
        image = MyImage(self.height, self.width)
        image.fancy_background()
        ## Coordinates viewPlane
        w = Vec3(0, 0, 0)
        u = Vec3(0, 0, 0)
        v = Vec3(0, 0, 0)
        theta = self.fov * math.pi / 180
        half_height = math.tan(theta / 2.0)
        aspect = self.width / self.height
        half_width = aspect * half_height

        # near_plane is used to mark viewFrustrum
        near_plane = Vec3.length(self.view_direction - self.position)

        # W, U, V coordinates, V and U are swapped places and v is negated compared to original
        w = Vec3.normalize(self.position - self.view_direction)
        u = Vec3.normalize(-(Vec3.cross(self.up, w)))
        v = Vec3.normalize(Vec3.cross(w, u))
        
        u0 = self.position.x - half_width * near_plane
        v0 = self.position.y - half_height * near_plane

        # lower left corner of ViewPlane
        lower_left_corner = u * u0 + v * v0 - near_plane * w

        # lower right corner of ViewPlane
        horizontal = (2 * half_width * near_plane) * u

        # upper left corner of ViewPlane
        vertical = (2 * half_height * near_plane) * v

        # size of singular pixel in viewPlane
        pixel_horizontal = horizontal / self.width
        pixel_vertical = vertical / self.height

        for i in range(self.width):
            for j in range(self.height):
                # New Ray, direction will be changed in antialiasing
                ray = Ray(self.position, Vec3(0.0, 0.0, 1.0))
                
                # Calculate middle of pixel and  corners of the pixel, A, B, C, D, look at antialiasing for exact positions
                ray_target = lower_left_corner + pixel_vertical * j + pixel_horizontal * i + pixel_horizontal / 2 + pixel_vertical / 2
                a_corner = ray_target - pixel_horizontal / 2 + pixel_vertical / 2
                b_corner = ray_target + pixel_horizontal / 2 + pixel_vertical / 2
                c_corner = ray_target + pixel_horizontal / 2 - pixel_vertical / 2
                d_corner = ray_target - pixel_horizontal / 2 - pixel_vertical / 2

                # Get background color from buffer, used in antialiasing
                background_color = image.get_pixel_color(i, j)
                
                # antialiasing
                # final_color = background_color
                final_color = Camera.adaptive_antialiasing(ray, a_corner, b_corner, c_corner, d_corner, ray_target, 0, 5, pixel_horizontal / 2, pixel_vertical / 2, background_color, primitives)
                
                # set pixel color 
                image.set_pixel(i, j, final_color)
        
        MyImage.save_image(image)
