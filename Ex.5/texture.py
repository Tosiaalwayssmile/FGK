from PIL import Image, r
import math


## Documentation for a class Texture.
class Texture:
    
    def __init__(self, file_name) -> None:
        
        self.img = Image.open(file_name).convert('RGB')

        self.height = self.img.shape[0]

        self.width = self.img.shape[1]


    def rectangular_mapping(self, coords: Vec3): 
        u = (coords.z + 1)/2
        v = (coords.x - 1)/2

        x = (self.height - 1) * u
        y = (self.width - 1) * v

        r, g, b = self.img.getpixel((x, y))

        return [r, g, b]


    def spherical_mapping(self, coords: Vec3):
        phi = math.atan(coords.x/coords.z)
        theta = math.acos(coords.y)

        if phi < 0:
            phi += 2*math.pi

        u = phi/(2*math.pi)
        v = 1 - theta/math.pi
        
        x = (self.height - 1) * u
        y = (self.width - 1) * v

        r, g, b = self.img.getpixel((x, y))

        return [r, g, b]
    
    def __str__(self) -> str:
        return 'Texture: height = ' + str(self.height) + ', width = ' + str(self.width)