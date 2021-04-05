import numpy as np
from PIL import Image
import math
from light_intensity import *

## Documentation for a class MyImage.
class MyImage:

    ## The constructor.
    def __init__(self, width = 500, height = 500):
        
        # A class variable. Width of an image.
        self.width = width
        # A class variable. Height of an image.
        self.height = height
        # A class variable. 
        self.image_matrix = np.zeros((width, height, 3), dtype = np.uint8)

    ## Function returning image length.
    def len(self):
        return self.height * self.width

    ## Function setting background color.
    def clear_color(self, rgb_color):
        for j in range(self.height):
            for i in range(self.width):
                 MyImage.set_pixel(self, i, j, rgb_color)
        return self.image_matrix

    ## Function setting background color.
    def fancy_background(self):
        part_x = self.width / 6
        part_y = self.height / 6
        for x in range(self.width):
            for y in range(self.height):
                intensity = int(y / part_y) / 6.0
                column = int(x / part_x)
                if column == 0:
                    MyImage.set_pixel(self, y, x,  [(intensity + 0.1), 0, 0])
                elif column == 1:
                    MyImage.set_pixel(self, y, x,  [0, (intensity + 0.1), 0])
                elif column == 2:
                    MyImage.set_pixel(self, y, x,  [0, 0, (intensity + 0.1)])
                elif column == 3:
                    MyImage.set_pixel(self, y, x,  [1, (intensity * 0.3), intensity])
                elif column == 4:
                    MyImage.set_pixel(self, y, x,  [(intensity * 0.3), 1, intensity])
                elif column == 5:
                    MyImage.set_pixel(self, y, x, [1, 1, (intensity + 0.15)])
                else:
                    MyImage.set_pixel(self, y, x, [1, 1, intensity])

        return self.image_matrix

    ## Function changing pixel color.
    def set_pixel(self, i, j, value):
        value = LightIntensity.clamp_0_255(value)
        clamped_value = [value.x, value.y, value.z]
        self.image_matrix[i, j] = clamped_value 

    ## Function saving image to png format.
    def save_image(self):
        img = Image.fromarray(self.image_matrix, 'RGB')
        img.save('MyImage.png')
        # img.show()
