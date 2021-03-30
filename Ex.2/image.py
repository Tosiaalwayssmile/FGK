import numpy as np
from PIL import Image
import math


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
                self.image_matrix[i, j] = rgb_color
        return self.image_matrix

    ## Function changing pixel color.
    def set_pixel(self, i, j, value):
        self.image_matrix[i, j] = value

    ## Function saving image to png format.
    def save_image(self):
        img = Image.fromarray(self.image_matrix, 'RGB')
        img.save('MyImage.png')
        # img.show()
