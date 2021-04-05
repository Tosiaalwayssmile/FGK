from PIL import Image
from Primitives.ray import *
from Primitives.primitive import *
from image import *
import numpy as np


## Class for othogonal camera
class Camera:

    ## Constructor
    def __init__(self, position = Vec3(0, 0, 0), view_direction = Vec3(0, 0, 1), width = 512, height = 512, near = .3, far = 1000):
        ## Position of the camera
        self.position = position
        ## Direction camera is facing
        self.view_direction = view_direction.normalize()
        ## Width in pixels
        self.w = width
        ## Height in pixels
        self.h = height
        ## Width-height raio
        self.wh_ratio = width / height
        ## Height-width ratio
        self.hw_ratio = height / width
        ## Array of rays
        self.arRay = np.zeros((width, height), Ray)
        ## Angle between view direction vector and X axis
        self.x_angle = np.arccos(self.view_direction * Vec3(1, 0, 0))
        ## Angle between view direction vector and Y axis
        self.y_angle = np.arccos(self.view_direction * Vec3(0, 1, 0))
        ## Angle between view direction vector and Z axis
        self.z_angle = np.arccos(self.view_direction * Vec3(0, 0, 1))
        ## Near clipping plane
        self.near = near
        ## Far clipping plane
        self.far = far

    def ortogonal_init(self, pixel_size=(0.01, 0.01)):
        x_offset = np.sin(self.x_angle) * pixel_size[0]
        y_offset = np.sin(self.y_angle) * pixel_size[1]
        z_offset = np.sin(self.z_angle) * pixel_size[0]
        center = Vec3(x_offset * self.w * .5 - .5, y_offset * self.h * .5 - .5, z_offset * self.w * .5 - .5)

        for i in range(self.w):
            for j in range(self.h):
                self.arRay[i][j] = Ray(self.position - center + Vec3(x_offset * i, y_offset * j, z_offset * i), self.view_direction)

    def perspective_init2(self, horizontal_fov=60, vertical_fov=0, pixel_size=(0.01, 0.01)):
        single_angle_hor = horizontal_fov / self.w
        if vertical_fov == 0:
            vertical_fov = horizontal_fov * self.hw_ratio
        single_angle_ver = vertical_fov / self.h

        x_sin = np.sin(self.x_angle)
        y_sin = np.sin(self.y_angle)
        z_sin = np.sin(self.z_angle)
        center = Vec3(horizontal_fov * .5 * x_sin * pixel_size[0],
                      vertical_fov * .5 * y_sin * pixel_size[1],
                      horizontal_fov * .5 * z_sin * pixel_size[0])
        x_offset = x_sin * single_angle_hor * pixel_size[0]
        y_offset = y_sin * single_angle_ver * pixel_size[1]
        z_offset = z_sin * single_angle_hor * pixel_size[0]

        for i in range(self.w):
            for j in range(self.h):
                direction = self.view_direction - center + Vec3(x_offset * i, y_offset * j, z_offset * i)
                self.arRay[i][j] = Ray(self.position, direction)

    def perspective_init(self, hor_fov=60, vert_fov=0, s=1):

        if vert_fov == 0:
            vert_fov = hor_fov * self.hw_ratio

        up = self.view_direction.cross(Vec3(0, 1, 0)).cross(self.view_direction).normalize()
        w = -1 * self.view_direction.normalize()
        up_cross_w = up.cross(w)
        u = -1 * up_cross_w / up_cross_w.length()
        v = -up

        pass

    def generate_image(self, primitives):
        image = MyImage(self.h, self.w)
        #background_color = (0.6, 0.8, 1.0)  # RGB
        #image.clear_color(background_color)
        image.fancy_background()

        depth = np.zeros((self.h, self.w))
        depth.fill(-1)

        hit_obj = np.zeros((self.h, self.w), dtype=Primitive)
        hit_obj.fill(None)

        for i in range(self.h):
            for j in range(self.w):
                for p in primitives:
                    # Get intersection point
                    hit = p.get_detailed_intersection(self.arRay[j][i])
                    # If there is no intersection, continue
                    if hit[0] is None:
                        continue
                    # TODO - add clipping planes
                    # If there was no data for this pixel before or that data is from pixel that is futher from pixel
                    # ...assign color and depth
                    if depth[i][j] == -1 or depth[i][j] > hit[1]:
                        MyImage.set_pixel(image, i, j, p.color * 255)
                        depth[i][j] = hit[1]
                        hit_obj[i][j] = p
                        continue

        # TODO - antialiasing

        MyImage.save_image(image)

