from PIL import Image
from Primitives.ray import *
from Primitives.primitive import *
from image import *
import numpy as np


## Class for othogonal camera
class OrthogonalCamera:

    ## Constructor
    def __init__(self, position = Vec3(0, 0, 0), view_direction = Vec3(0, 0, 1), width = 512, height = 512, pixel_size=(0.01, 0.01)):
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

        x_offset = np.sin(self.x_angle) * pixel_size[0]
        y_offset = np.sin(self.y_angle) * pixel_size[1]
        z_offset = np.sin(self.z_angle) * pixel_size[0]
        top_right_corner_offset = Vec3(x_offset * self.w * .5, y_offset * self.h * .5, z_offset * self.w * .5)

        for i in range(self.w):
            for j in range(self.h):
                self.arRay[i][j] = Ray(self.position - top_right_corner_offset + Vec3(x_offset * i, y_offset * j, z_offset * i),
                                       self.view_direction)

    ## Function rendering the scene
    def render_scene(self, primitives):
        image = MyImage(self.h, self.w)
        #image.fancy_background()
        image.clear_color([0.9, 0.9, 0.8])
        
        depth = np.zeros((self.h, self.w))
        depth.fill(-1)

        hit_obj = np.zeros((self.h, self.w), dtype=Primitive)
        hit_obj.fill(None)

        number_of_pixels = self.w * self.h
        current_px = 1

        for i in range(self.h):
            for j in range(self.w):

                if current_px % 1000 == 0:
                    print('Progress: ' + str(round(current_px * 100 / number_of_pixels, 2)) + '%')
                current_px += 1

                color = self.arRay[j][i].get_pixel_color(primitives)
                if color is not None:
                    final_color = color
                    image.set_pixel(i, j, color)

        MyImage.save_image(image)

