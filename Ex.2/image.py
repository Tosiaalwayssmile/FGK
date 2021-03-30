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

    ## Function setting background color.
    def fancy_background(self):
        partX = self.width / 6
        partY = self.height / 6
        for x in range(self.width):
            for y in range(self.height):
                intensity = int(y / partY) / 6.0
                newValue = int(intensity * 255)
                column = int(x / partX)
                if (column == 0):
                    MyImage.set_pixel(self, y, x,  [(newValue + 20), 0, 0])
                elif (column == 1):
                    MyImage.set_pixel(self, y, x,  [0, (newValue + 20), 0])
                elif (column == 2):
                    MyImage.set_pixel(self, y, x,  [0, 0, (newValue + 20)])
                elif (column == 3):               
                    MyImage.set_pixel(self, y, x,  [255, (newValue * 0.30), newValue])
                elif (column == 4):
                    MyImage.set_pixel(self, y, x,  [(newValue * 0.30), 255, newValue])
                elif (column == 5):
                    MyImage.set_pixel(self, y, x, [255, 255, (newValue + 43)])
                else:
                    MyImage.set_pixel(self, y, x, [255, 255, newValue])

        return self.image_matrix
 

    ## Function changing pixel color.
    def set_pixel(self, i, j, value):
        if (value[0] < 0):
            value[0] = 0
        elif (value[1] < 0):
            value[1] = 0
        elif (value[2] < 0):
            value[2] = 0        
        elif (value[0] > 255):
            value[0] = 255
        elif (value[1] > 255):
            value[1] = 255
        elif (value[2] > 255):
            value[2] = 255

        self.image_matrix[i, j] = value 

    ## Function saving image to png format.
    def save_image(self):
        img = Image.fromarray(self.image_matrix, 'RGB')
        img.save('MyImage.png')
        # img.show()
