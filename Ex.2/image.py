import numpy as np
from PIL import Image
import math

# Documentation for a class MyImage.
class MyImage:

    # The constructor.
    def __init__(self, width = 500, height = 500, rgba_color = (255, 255, 255, 255)):
        
        # A class variable. Width of an image.
        self.width = width
        # A class variable. Height of an image.
        self.height = height
        # A class variable. Color of an image.
        self.rgba_color = rgba_color
        # A class variable. 
        self.image_matrix = np.zeros((width, height, 4), dtype = np.uint8)
    
    def len(self):
        return self.height * self.width

    def clear_color(self, rgba_color):

         for j in range(self.height):
             for i in range(self.width):
                 self.image_matrix[i, j] = rgba_color
         return self.image_matrix
        # def clear_color(self, fill_list):
        # index = 0
        # for i in range(len(self.rows)):
        #     try:
        #         for j in range(len(self.rows[i])):
        #             self.rows[i][j] = fill_list[index]
        #             index += 1
        #     except IndexError:
        #         print (f"Matrix not filled \nMatrix fill stopped at: row {i}, Column {j}")
        #         break        
        # return fill_list[index:]

    def save_image(self):

        img = Image.fromarray(self.image_matrix, 'RGBA')
        img.save('MyImage.png')
        #img.show()

    def __str__(self):
        s = "\n" + "\n".join([str(i) for i in [rows for rows in self.rows] ]) + "\n"
        return s
