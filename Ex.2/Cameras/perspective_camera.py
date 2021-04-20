from PIL import Image
from Primitives.ray import *
from Primitives.primitive import *
from image import *
import numpy as np


## Mothod compares two colors and returns true if they are equal
def are_colors_equal(arr1, arr2):
    if arr1[0] == arr2[0] and arr1[1] == arr2[1] and arr1[2] == arr2[2]:
        return True
    return False


## Class for othogonal camera
class PerspectiveCamera:

    ## Constructor
    def __init__(self, position = Vec3(0, 0, 0), view_direction = Vec3(0, 0, 1), width = 512, height = 512, near = .1, far = 1000, fov=60):
        
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
        self.fov = fov
        ##
        self.up = Vec3(0, 1, 0)

    @staticmethod
    def adaptive_antialiasing(ray, A, B, C, D, E, depth, max_depth, horizontal, vertical, background_color, primitives):

        ray.set_target(E)
        e_color = ray.get_pixel_color(primitives)
        if e_color is None:
            e_color = background_color

        # Check if algorithm reached maximum Depth, if so return color of the middle of subpixel
        if depth >= max_depth:
            return e_color

        ray.set_target(A)
        a_color = ray.get_pixel_color(primitives)
        if a_color is None:
            a_color = background_color

        ray.set_target(B)
        b_color = ray.get_pixel_color(primitives)
        if b_color is None:
            b_color = background_color

        ray.set_target(C)
        c_color = ray.get_pixel_color(primitives)
        if c_color is None:
            c_color = background_color

        ray.set_target(D)
        d_color = ray.get_pixel_color(primitives)
        if d_color is None:
            d_color = background_color

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

        if not are_colors_equal(a_color, e_color):
            b_prim = E + vertical
            d_prim = E - horizontal
            e_prim = E - horizontal / 2 + vertical / 2
            a_color = PerspectiveCamera.adaptive_antialiasing(ray, A, b_prim, E, d_prim, e_prim, depth + 1, max_depth, horizontal / 2, vertical / 2, background_color, primitives)

        if not are_colors_equal(b_color, e_color):
            a_prim = E + vertical
            c_prim = E + horizontal
            e_prim = E + horizontal / 2 + vertical / 2
            b_color = PerspectiveCamera.adaptive_antialiasing(ray, a_prim, B, c_prim, E, e_prim, depth + 1, max_depth, horizontal / 2, vertical / 2, background_color, primitives)

        if not are_colors_equal(c_color, e_color):
            b_prim = E + horizontal
            d_prim = E - vertical
            e_prim = E + horizontal / 2 - vertical / 2
            c_color = PerspectiveCamera.adaptive_antialiasing(ray, E, b_prim, C, d_prim, e_prim, depth + 1, max_depth, horizontal / 2, vertical / 2, background_color, primitives)

        if not are_colors_equal(d_color, e_color):
            a_prim = E - horizontal
            c_prim = E - vertical
            e_prim = E - horizontal / 2 - vertical / 2
            d_color = PerspectiveCamera.adaptive_antialiasing(ray, a_prim, E, c_prim, D, e_prim, depth + 1, max_depth, horizontal / 2, vertical / 2, background_color, primitives)

        # get mean of the colors and return them
        ae = np.multiply(np.add(a_color, e_color), .5)
        be = np.multiply(np.add(b_color, e_color), .5)
        ce = np.multiply(np.add(c_color, e_color), .5)
        de = np.multiply(np.add(d_color, e_color), .5)
        summ = np.add(ae, be)
        summ = np.add(summ, ce)
        summ = np.add(summ, de)

        return np.multiply(summ, .25)
        # return np.multiply(np.add(np.add(np.add(np.add(a_color, b_color), c_color), d_color), np.multiply(e_color, 4)), 0.25)
        # return ((a_color + e_color) * 0.5 + (b_color + e_color) * 0.5 + (c_color + e_color) * 0.5 + (d_color + e_color) * 0.5) * 0.25

    def render_scene(self, primitives):
        # Prepare color buffer and fill it with background color
        image = MyImage(self.width, self.height)
        image.fancy_background()

        ## Coordinates viewPlane
        theta = self.fov * math.pi / 180
        half_height = math.tan(theta / 2.0)
        aspect = self.width / self.height
        half_width = aspect * half_height

        # near_plane is used to mark viewFrustrum
        near_plane = Vec3.length(self.view_direction - self.position)

        # W, U, V coordinates, V and U are swapped places and v is negated compared to original
        w = Vec3.normalize(-self.position - self.view_direction)
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

        number_of_pixels = self.width * self.height
        current_px = 1

        for i in range(self.height):
            for j in range(self.width):

                if current_px % 1000 == 0:
                    print('Progress: ' + str(round(current_px * 100 / number_of_pixels, 2)) + '%')
                current_px += 1

                # New ray
                ray_target = lower_left_corner + pixel_vertical * i + pixel_horizontal * j + pixel_horizontal / 2 + pixel_vertical / 2
                ray = Ray(self.position, target=ray_target)

                # Set background color as default, if something is hit, it will be changed to primitive's color
                final_color = image.get_pixel_color(i, j) / 255

                # ANTIALIASING
                # Calculate middle of pixel and  corners of the pixel, A, B, C, D, look at antialiasing for exact positions
                a_corner = ray_target - pixel_horizontal / 2 + pixel_vertical / 2
                b_corner = ray_target + pixel_horizontal / 2 + pixel_vertical / 2
                c_corner = ray_target + pixel_horizontal / 2 - pixel_vertical / 2
                d_corner = ray_target - pixel_horizontal / 2 - pixel_vertical / 2
                final_color = PerspectiveCamera.adaptive_antialiasing(ray, a_corner, b_corner, c_corner, d_corner, ray_target, 0, 5, pixel_horizontal / 2, pixel_vertical / 2, final_color, primitives)

                # NO ANTIALIASING
                color = ray.get_pixel_color(primitives)
                if color is not None:
                    #final_color = color
                    pass

                # set pixel color
                image.set_pixel(i, j, final_color)

        MyImage.save_image(image)
