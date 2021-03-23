from Primitives.ray import *
import numpy as np


## Class for othogonal camera
class CameraOrthogonal:

    ## Constructor
    def __init__(self, position=Vec3(0, 0, 0), view_direction=Vec3(1, 0, 0), width=512, height=256):
        ## Position of the camera
        self.position = position
        ## Direction camera is facing
        self.view_direction = view_direction
        ## Width in pixels
        self.w = width
        ## Height in pixels
        self.h = height

        ## Minimum X coordinate of the pixel
        self.x_min = 0
        ## Minimum Y coordinate of the pixel
        self.y_min = 0

        if width % 2 == 0:
            x_min = -width * 0.5 + 0.5
        else:
            x_min = -width * 0.5

        if height % 2 == 0:
            y_min = -height * 0.5 + 0.5
        else:
            y_min = -height * 0.5

        ## Array of rays
        self.arRay = np.zeros((width, height), Ray)
        x_offset = self.view_direction.x
        y_offset = self.view_direction.y
        z_offset = self.view_direction.z


    def generate_image(self, primitives):
        image = np.zeros((self.w, self.h), (float, float, float))
        depth = np.zeros((self.w, self.h), None)

        ray = Ray()

        for i in range(self.h):
            for j in range(self.w):
                for p in primitives:
                    pass



