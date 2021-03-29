from PIL import Image
from Primitives.ray import *
import numpy as np
from image import *

## Class for othogonal camera
class CameraOrthogonal:

    ## Constructor
    def __init__(self, position=Vec3(0, 0, 0), view_direction=Vec3(0, 0, 1), width=512, height=256, pixel_size=(0.01, 0.01)):
        ## Position of the camera
        self.position = position
        ## Direction camera is facing
        self.view_direction = view_direction
        ## Width in pixels
        self.w = width
        ## Height in pixels
        self.h = height

        view_n = view_direction / view_direction.length()

        # Angles in radians
        x_angle = np.arccos(view_n * Vec3(1, 0, 0))
        y_angle = np.arccos(view_n * Vec3(0, 1, 0))
        z_angle = np.arccos(view_n * Vec3(0, 0, 1))

        x_offset = np.sin(x_angle) * pixel_size[0]
        y_offset = np.sin(y_angle) * pixel_size[1]
        z_offset = np.sin(z_angle) * pixel_size[0]
        center = Vec3(x_offset * width * .5, y_offset * height * .5, z_offset * width * .5)

        ## Array of rays
        self.arRay = np.zeros((width, height), Ray)
        for i in range(width):
            for j in range(height):
                self.arRay[i][j] = Ray(position - center + Vec3(x_offset * i, y_offset * j, z_offset * i), view_direction)

    def generate_image(self, primitives):
        image = MyImage(self.h, self.w)
        background_color = (153, 204, 255)  # RGB
        image.clear_color(background_color)
        
        
        #image = np.zeros((self.h, self.w, 3), dtype=np.uint8)
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
                        #image[i][j] = [255, 0, 0]
                        depth[i][j] = distance
                        continue

        MyImage.save_image(image)
        #img = Image.fromarray(image, 'RGB')
        #img.save('MyImage.png')
