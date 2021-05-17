from Lights.light_source import *


## Documentation for a class PointLightSource. Light emitted from a Point.
class PointLightSource(LightSource):

    def __init__(self, position=[0, 0, 0], color=[1, 1, 1], intensity=1):
        super().__init__(position, color, intensity)

