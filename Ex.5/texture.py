

## Documentation for a class Texture.
class Texture:
    
    def __init__(self, height, width) -> None:
        
        self.height = height

        self.width = width


    def rectangular_mapping() -> None:
        pass


    def spherical_mapping() -> None:
        pass
    
    def __str__(self) -> str:
        return 'Texture: height = ' + str(self.height) + ', width = ' + str(self.width)