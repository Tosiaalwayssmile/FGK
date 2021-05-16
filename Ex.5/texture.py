from PIL import Image
import math
import numpy as np


## Documentation for a class Texture.
class Texture:
    
    ## Constructor
    def __init__(self, file_name) -> None:

        self.file_name = file_name
        
        self.img = Image.open(file_name).convert('RGB')

        self.height = self.img.size[0]

        self.width = self.img.size[1]


    ## Returns pixel color for primitive and ray intersection represented by coords for rectangulars
    def rectangular_mapping(self, coords): 
        u = (coords.z + 1)/2
        v = (coords.x - 1)/2

        x = (self.height - 1) * u
        y = (self.width - 1) * v

        r, g, b = self.img.getpixel((x, y))/255.
        r, g, b = r/255., g/255., b/255.

        return [r, g, b]


    ## Returns pixel color for primitive and ray intersection represented by coords for spheres. Needs a spehere radius to scale properly 
    def spherical_mapping(self, coords, r):

        u = 0.5 + np.arctan2(coords.x, coords.z)/(2*np.pi)
        v = 0.5 - np.arcsin(coords.y/r)/np.pi

        x = (self.height - 1) * u
        y = (self.width - 1) * v

        r, g, b = self.img.getpixel((x, y))
        r, g, b = r/255., g/255., b/255.

        return [r, g, b]
    
    def __str__(self) -> str:
        return 'Texture: height = ' + str(self.height) + ', width = ' + str(self.width) + ', file name: ' + self.file_name