from abc import ABC, abstractmethod
from vector import *

## Documentation for a class LightSource.
class LightSource(ABC):

    ## The constructor. Creates a LightSource with a specified Colour at a given Location.
    @abstractmethod
    def __init__(self, position=Vec3(0, 0, 0), color=[1, 1, 1], intensity=1):
        ## Colour of light source.
        self.color = color

        ## Position of light source.
        self.position = position

        ## Intensity of light
        self.intensity = intensity

    ## Function returning object values in string format.
    def __str__(self):
        return 'LightSource: color' + str(self.color) + ', position' + str(self.position)
