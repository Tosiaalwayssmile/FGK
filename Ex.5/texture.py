from PIL import Image


## Documentation for a class Texture.
class Texture:
    
    def __init__(self, height, width, file_name) -> None:
        
        self.img = Image.open(file_name).convert('RGB')

        self.height = self.img.shape[0]

        self.width = self.img.shape[1]


    def rectangular_mapping(coordinates: Vec3): 
        u = (coordinates[2] + 1)/2
        v = (coordinates[0] - 1)/2

        x = (self.height - 1) * u
        y = (self.width - 1) * v

        r, g, b = rgb_im.getpixel((x, y))

        return [r, g, b]


    def spherical_mapping() -> None:
        pass
    
    def __str__(self) -> str:
        return 'Texture: height = ' + str(self.height) + ', width = ' + str(self.width)