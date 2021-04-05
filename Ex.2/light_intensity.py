import math
from vector import *

## Documentation for a class LightIntensity.
class LightIntensity(Vec3):

    ## Function clamping values to 0 - 1 range.
    def clamp_0_1(light):

        x1 = light[0] 
        y1 = light[1]  
        z1 = light[2] 

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

    ## Function clamping values to 0 - 255 range.
    def clamp_0_255(light):
        LightIntensity.clamp_0_1(light)
        x1 = int(light[0] * 255)
        y1 = int(light[1] * 255)
        z1 = int(light[2] * 255)

        if x1 > 255:
            x1 = 255
        if y1 > 255:
            y1 = 255
        if z1 > 255:
            z1 = 255

        return Vec3(x1, y1, z1)
