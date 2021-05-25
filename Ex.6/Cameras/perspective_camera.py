from Math.ray import *
from image import *
import numpy as np


## Mothod compares two colors and returns true if they are equal
def are_colors_equal(arr1, arr2, max_diff=3):
    if np.abs(arr1[0] - arr2[0]) < max_diff and np.abs(arr1[1] - arr2[1]) < max_diff and np.abs(arr1[2] - arr2[1]) < max_diff:
        return True
    return False


## Class for othogonal camera
class PerspectiveCamera:

    ## Constructor
    def __init__(self, position = Vec3(0, 0, 0), view_direction = Vec3(0, 0, 1), width = 512, height = 512, near = .1, far = 1000, fov=60):
        
        ## Position of the camera
        self.position = position
        ## Direction camera is facing
        self.view_direction = view_direction.normalized() # target
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
        ## Vector direction aligned with the "up" direction of camera
        self.up = Vec3(0, 1, 0)

    ## Function calculating color of pixel using adaptive antialiasing
    @staticmethod
    def adaptive_antialiasing(ray, A, B, C, D, E, depth, max_depth, horizontal, vertical, background_color, primitives, lights):

        if type(E) is Vec3:
            ray.set_target(E)
            e_color = ray.get_pixel_color(primitives, lights)
            if e_color is None:
                e_color = background_color
        else:
            e_color = E

        # Check if algorithm reached maximum Depth, if so return color of the middle of subpixel
        if depth >= max_depth:
            return e_color

        if type(A) is Vec3:
            ray.set_target(A)
            a_color = ray.get_pixel_color(primitives, lights)
            if a_color is None:
                a_color = background_color
        else:
            a_color = A

        if type(B) is Vec3:
            ray.set_target(B)
            b_color = ray.get_pixel_color(primitives, lights)
            if b_color is None:
                b_color = background_color
        else:
            b_color = B

        if type(C) is Vec3:
            ray.set_target(C)
            c_color = ray.get_pixel_color(primitives, lights)
            if c_color is None:
                c_color = background_color
        else:
            c_color = C

        if type(D) is Vec3:
            ray.set_target(D)
            d_color = ray.get_pixel_color(primitives, lights)
            if d_color is None:
                d_color = background_color
        else:
            d_color = D

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
            a_color = PerspectiveCamera.adaptive_antialiasing(ray, a_color, b_prim, e_color, d_prim, e_prim, depth + 1, max_depth, horizontal / 2, vertical / 2, background_color, primitives, lights)

        if not are_colors_equal(b_color, e_color):
            a_prim = E + vertical
            c_prim = E + horizontal
            e_prim = E + horizontal / 2 + vertical / 2
            b_color = PerspectiveCamera.adaptive_antialiasing(ray, a_prim, b_color, c_prim, e_color, e_prim, depth + 1, max_depth, horizontal / 2, vertical / 2, background_color, primitives, lights)

        if not are_colors_equal(c_color, e_color):
            b_prim = E + horizontal
            d_prim = E - vertical
            e_prim = E + horizontal / 2 - vertical / 2
            c_color = PerspectiveCamera.adaptive_antialiasing(ray, e_color, b_prim, c_color, d_prim, e_prim, depth + 1, max_depth, horizontal / 2, vertical / 2, background_color, primitives, lights)

        if not are_colors_equal(d_color, e_color):
            a_prim = E - horizontal
            c_prim = E - vertical
            e_prim = E - horizontal / 2 - vertical / 2
            d_color = PerspectiveCamera.adaptive_antialiasing(ray, a_prim, e_color, c_prim, d_color, e_prim, depth + 1, max_depth, horizontal / 2, vertical / 2, background_color, primitives, lights)

        # get mean of the colors and return them
        ae = np.multiply(np.add(a_color, e_color), .5)
        be = np.multiply(np.add(b_color, e_color), .5)
        ce = np.multiply(np.add(c_color, e_color), .5)
        de = np.multiply(np.add(d_color, e_color), .5)
        summ = np.add(ae, be)
        summ = np.add(summ, ce)
        summ = np.add(summ, de)

        return np.multiply(summ, .25)

    ## Function rendering the scene
    def render_scene(self, primitives, light_sources, antialiasing=True):
        # Prepare color buffer and fill it with background color
        image = MyImage(self.width, self.height)
        # image.fancy_background()
        image.clear_color([0.9, 0.9, 0.8])

        ## Coordinates viewPlane
        theta = self.fov * math.pi / 180
        half_height = math.tan(theta / 2.0)
        aspect = self.width / self.height
        half_width = aspect * half_height

        # near_plane is used to mark viewFrustrum
        near_plane = Vec3.length(self.view_direction - self.position)

        # W, U, V coordinates, V and U are swapped places and v is negated compared to original
        w = Vec3.normalized(-self.position - self.view_direction)
        u = Vec3.normalized(-(Vec3.cross(self.up, w)))
        v = Vec3.normalized(Vec3.cross(w, u))
        
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

                # Set background color as default, if something is hit, it will be changed to primitive's color
                final_color = image.get_pixel_color(i, j) / 255
                ray_target = lower_left_corner + pixel_vertical * i + pixel_horizontal * j + pixel_horizontal / 2 + pixel_vertical / 2

                if antialiasing:
                    # ANTIALIASING
                    # Calculate middle of pixel and  corners of the pixel, A, B, C, D, look at antialiasing for exact positions
                    a_corner = ray_target - pixel_horizontal / 2 + pixel_vertical / 2
                    b_corner = ray_target + pixel_horizontal / 2 + pixel_vertical / 2
                    c_corner = ray_target + pixel_horizontal / 2 - pixel_vertical / 2
                    d_corner = ray_target - pixel_horizontal / 2 - pixel_vertical / 2

                    ray = Ray(self.position, target=ray_target)
                    final_color = PerspectiveCamera.adaptive_antialiasing(ray, a_corner, b_corner, c_corner, d_corner, ray_target, 0, 3, pixel_horizontal / 2, pixel_vertical / 2, final_color, primitives, light_sources)
                else:
                    # NO ANTIALIASING
                    ray = Ray(self.position, target=-ray_target)
                    color = ray.get_pixel_color(primitives, light_sources)
                    if color is not None:
                        final_color = color

                # set pixel color
                image.set_pixel(i, j, final_color)
        
        print('Progress: 100%   ')

        MyImage.save_image(image)
