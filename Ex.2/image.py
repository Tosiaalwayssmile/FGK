import numpy as np
from PIL import Image
import math

# Documentation for a class MyImage.
class MyImage:

    # The constructor.
    def __init__(self, width = 500, height = 500):
        
        # A class variable. Width of an image.
        self.width = width
        # A class variable. Height of an image.
        self.height = height
        # A class variable. 
        self.image_matrix = np.zeros((width, height, 3), dtype = np.uint8)
    
    def len(self):
        return self.height * self.width

    def clear_color(self, rgb_color):
        for j in range(self.height):
            for i in range(self.width):
                self.image_matrix[i, j] = rgb_color
        return self.image_matrix

    def set_pixel(self, i, j, value):
        self.image_matrix[i, j] = value 
        return self.image_matrix

    def save_image(self):
        img = Image.fromarray(self.image_matrix, 'RGB')
        img.save('MyImage.png')
        # img.show()

    def __str__(self):
        s = "\n" + "\n".join([str(i) for i in [rows for rows in self.rows] ]) + "\n"
        return s
