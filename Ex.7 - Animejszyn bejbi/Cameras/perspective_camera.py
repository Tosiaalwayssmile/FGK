from Math.ray import *
from image import *
import numpy as np
from threading import Thread
import multiprocessing
from multiprocessing import shared_memory
import sys
from Scene import *


## Mothod compares two colors and returns true if they are equal
def are_colors_equal(arr1, arr2, max_diff=3):
    if np.abs(arr1[0] - arr2[0]) < max_diff and np.abs(arr1[1] - arr2[1]) < max_diff and np.abs(
            arr1[2] - arr2[1]) < max_diff:
        return True
    return False


## Class for othogonal camera
class PerspectiveCamera:

    ## Constructor
    def __init__(self, position=Vec3(0, 0, 0), view_direction=Vec3(0, 0, 1), width=512, height=512, near=.1, far=1000,
                 fov=60):

        ## Position of the camera
        self.position = position
        ## Direction camera is facing
        self.view_direction = view_direction.normalized()  # target
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
    def adaptive_antialiasing(ray, A, B, C, D, E, depth, max_depth, horizontal, vertical, background_color, scene, shutter_exposure_timeframe):

        if type(E) is Vec3:
            ray.set_target(E)
            e_color = ray.get_pixel_color(scene=scene, shutter_exposure_timeframe=shutter_exposure_timeframe)
            if e_color is None:
                e_color = background_color
        else:
            e_color = E

        # Check if algorithm reached maximum Depth, if so return color of the middle of subpixel
        if depth >= max_depth:
            return e_color

        if type(A) is Vec3:
            ray.set_target(A)
            a_color = ray.get_pixel_color(scene=scene, shutter_exposure_timeframe=shutter_exposure_timeframe)
            if a_color is None:
                a_color = background_color
        else:
            a_color = A

        if type(B) is Vec3:
            ray.set_target(B)
            b_color = ray.get_pixel_color(scene=scene, shutter_exposure_timeframe=shutter_exposure_timeframe)
            if b_color is None:
                b_color = background_color
        else:
            b_color = B

        if type(C) is Vec3:
            ray.set_target(C)
            c_color = ray.get_pixel_color(scene=scene, shutter_exposure_timeframe=shutter_exposure_timeframe)
            if c_color is None:
                c_color = background_color
        else:
            c_color = C

        if type(D) is Vec3:
            ray.set_target(D)
            d_color = ray.get_pixel_color(scene=scene, shutter_exposure_timeframe=shutter_exposure_timeframe)
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
            a_color = PerspectiveCamera.adaptive_antialiasing(ray, a_color, b_prim, e_color, d_prim, e_prim, depth + 1,
                                                              max_depth, horizontal / 2, vertical / 2, background_color,
                                                              scene, shutter_exposure_timeframe=shutter_exposure_timeframe)

        if not are_colors_equal(b_color, e_color):
            a_prim = E + vertical
            c_prim = E + horizontal
            e_prim = E + horizontal / 2 + vertical / 2
            b_color = PerspectiveCamera.adaptive_antialiasing(ray, a_prim, b_color, c_prim, e_color, e_prim, depth + 1,
                                                              max_depth, horizontal / 2, vertical / 2, background_color,
                                                              scene, shutter_exposure_timeframe=shutter_exposure_timeframe)

        if not are_colors_equal(c_color, e_color):
            b_prim = E + horizontal
            d_prim = E - vertical
            e_prim = E + horizontal / 2 - vertical / 2
            c_color = PerspectiveCamera.adaptive_antialiasing(ray, e_color, b_prim, c_color, d_prim, e_prim, depth + 1,
                                                              max_depth, horizontal / 2, vertical / 2, background_color,
                                                              scene, shutter_exposure_timeframe=shutter_exposure_timeframe)

        if not are_colors_equal(d_color, e_color):
            a_prim = E - horizontal
            c_prim = E - vertical
            e_prim = E - horizontal / 2 - vertical / 2
            d_color = PerspectiveCamera.adaptive_antialiasing(ray, a_prim, e_color, c_prim, d_color, e_prim, depth + 1,
                                                              max_depth, horizontal / 2, vertical / 2, background_color,
                                                              scene, shutter_exposure_timeframe=shutter_exposure_timeframe)

        # get mean of the colors and return them
        ae = np.multiply(np.add(a_color, e_color), .5)
        be = np.multiply(np.add(b_color, e_color), .5)
        ce = np.multiply(np.add(c_color, e_color), .5)
        de = np.multiply(np.add(d_color, e_color), .5)
        summ = np.add(ae, be)
        summ = np.add(summ, ce)
        summ = np.add(summ, de)

        return np.multiply(summ, .25)

    def render_part_of_scene(self, scene, shutter_exposure_timeframe, blur_ratio, antialiasing, start_row, start_col, rows, cols,
                             lower_left_corner, pixel_horizontal, pixel_vertical, returned_img, process_nr):

        image = MyImage(self.width, self.height)

        for i in range(start_row, start_row + rows):
            if i >= self.height:
                break
            for j in range(start_col, start_col + cols):
                if j >= self.width:
                    break

                curr_percent = int(np.round(self.current_px * 100 / self.number_of_pixels))
                if curr_percent % 1 == 0 and self.last_percent != curr_percent:
                    self.last_percent = curr_percent
                    print('|', end='')
                self.current_px += 1

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
                    final_color = PerspectiveCamera.adaptive_antialiasing(ray, a_corner, b_corner, c_corner, d_corner,
                                                                          ray_target, 0, 3, pixel_horizontal / 2,
                                                                          pixel_vertical / 2, final_color, scene, shutter_exposure_timeframe)
                else:
                    # NO ANTIALIASING
                    ray = Ray(self.position, target=-ray_target)
                    color = ray.get_avg_pixel_color(scene=scene, shutter_exposure_timeframe=shutter_exposure_timeframe, amount_of_samples=blur_ratio)
                    if color is not None:
                        final_color = color

                # set pixel color
                image.set_pixel(i, j, final_color)
        returned_img[process_nr] = process_nr, image.image_matrix[start_row:start_row + rows]

    ## Function rendering the scene
    def render_scene(self, shutter_exposure_timeframe, blur_ratio=1, antialiasing=True, amount_of_processes=1):

        # Prepare color buffer and fill it with background color
        image = MyImage(self.width, self.height)
        image.clear_color([0, 0, 0])

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

        self.number_of_pixels = self.width * self.height
        self.current_px = 1
        self.last_percent = 0

        scene = Scene()

        print(
            '|0%       |10%      |20%      |30%      |40%      |50%      |60%      |70%      |80%      |90%      |100%')
        print('|', end='')

        manager = multiprocessing.Manager()
        returned_img = manager.dict()
        columns_per_process = int(np.ceil(self.width / amount_of_processes))
        rows_per_process = int(np.ceil(self.height / amount_of_processes))
        processes = []
        for i in range(amount_of_processes):
            p = multiprocessing.Process(target=self.render_part_of_scene, args=(
                scene, shutter_exposure_timeframe, blur_ratio, antialiasing, i * rows_per_process, 0, rows_per_process, self.width,
                lower_left_corner, pixel_horizontal, pixel_vertical, returned_img, i))
            processes.append(p)

        for p in processes:
            p.start()

        for p in processes:
            p.join()

        whole_image = returned_img.values()

        tmp = []
        for p in whole_image:
            tmp.append(p)

        tmp.sort(key=lambda x: x[0])

        tmp2 = []
        for p in tmp:
            for r in p[1]:
                tmp2.append(r)

        image.image_matrix = np.array(tmp2)

        print()

        return image
