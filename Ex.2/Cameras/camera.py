from PIL import Image
from Primitives.ray import *
import numpy as np


## Class for othogonal camera
class Camera:

    ## Constructor
    def __init__(self, position=Vec3(0, 0, 0), view_direction=Vec3(0, 0, 1), width=512, height=256):
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

    def ortogonal_init(self, pixel_size=(0.01, 0.01)):
        x_offset = np.sin(self.x_angle) * pixel_size[0]
        y_offset = np.sin(self.y_angle) * pixel_size[1]
        z_offset = np.sin(self.z_angle) * pixel_size[0]
        center = Vec3(x_offset * self.w * .5, y_offset * self.h * .5, z_offset * self.w * .5)

        for i in range(self.w):
            for j in range(self.h):
                self.arRay[i][j] = Ray(self.position - center + Vec3(x_offset * i, y_offset * j, z_offset * i), self.view_direction)

    def perspectic_init(self, horizontal_fov=60, pixel_size=(0.01, 0.01)):
        single_angle = horizontal_fov / self.w

        x_sin = np.sin(self.x_angle)
        y_sin = np.sin(self.y_angle)
        z_sin = np.sin(self.z_angle)
        center = Vec3(horizontal_fov * .5 * x_sin * pixel_size[0],
                      horizontal_fov * .5 * y_sin * pixel_size[1] * self.hw_ratio,
                      horizontal_fov * .5 * z_sin * pixel_size[0])
        x_offset = x_sin * single_angle * pixel_size[0]
        y_offset = y_sin * single_angle * pixel_size[1]
        z_offset = z_sin * single_angle * pixel_size[0]

        for i in range(self.w):
            for j in range(self.h):
                direction = self.view_direction - center + Vec3(x_offset * i, y_offset * j, z_offset * i)
                self.arRay[i][j] = Ray(self.position, direction)
        pass

    def generate_image(self, primitives):
        image = MyImage(self.h, self.w)
        background_color = (153, 204, 255)  # RGB
        image.clear_color(background_color)

        depth = np.zeros((self.h, self.w))
        depth.fill(-1)

        for i in range(self.h):
            for j in range(self.w):
                for p in primitives:
                    # Get intersection point
                    point = p.get_intersection(self.arRay[j][i])
                    # If there is no intersection, continue
                    if point is None:
                        continue
                    # If there is intersection, calculate distance
                    distance = self.arRay[j][i].origin.distance(point)
                    # If there was no data for this pixel before or that data is from pixel that is futher from pixel
                    # ...assign color and depth
                    if depth[i][j] == -1 or depth[i][j] > distance:
                        MyImage.set_pixel(image, i, j, [255, 0, 0])
                        depth[i][j] = distance
                        continue

        MyImage.save_image(image)
