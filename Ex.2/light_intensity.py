import math
from vector import *

## Documentation for a class LightIntensity.
class LightIntensity(Vec3):

    ## Function mapping (0, 255) values to (0,1).
    def map_0_1(light):

        x1 = light.x 
        y1 = light.y 
        z1 = light.z 

        if x1 < 0:
            x1 = 0
        if y1 < 0:
            y1 = 0
        if z1 < 0:
            z1 = 0

        if x1 > 1:
            x1 = 1
        if y1 > 1:
            y1 = 1
        if z1 > 1:
            z1 = 1

        return Vec3(x1, y1, z1)

    ## Function mapping (0,1) values to (0, 255).
    def map_0_255(light):
        LightIntensity.map_0_1(light)
        x1 = int(light.x * 256)
        y1 = int(light.y * 256)
        z1 = int(light.z * 256)

        if x1 < 0:
            x1 = 0
        if y1 < 0:
            y1 = 0
        if z1 < 0:
            z1 = 0

        if x1 > 255:
            x1 = 255
        if y1 > 255:
            y1 = 255
        if z1 > 255:
            z1 = 255

        return Vec3(x1, y1, z1)
