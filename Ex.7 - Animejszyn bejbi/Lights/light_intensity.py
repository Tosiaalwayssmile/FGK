import numpy as np


## Documentation for a class LightIntensity.
class LightIntensity:

    ## Clamps value between 0 and 1
    @staticmethod
    def clamp01(value):
        if value <= 0:
            return 0
        if value >= 1:
            return 1
        return value

    ## Clamps value between 0 and 255
    @staticmethod
    def clamp_0_255(value):
        if isinstance(value, list) or isinstance(value, np.ndarray):
            return [LightIntensity.clamp_0_255(value[0]),
                    LightIntensity.clamp_0_255(value[1]),
                    LightIntensity.clamp_0_255(value[2])]

        if value <= 0:
            return 0
        if value >= 255:
            return 255
        return value

    ## Remapsvalue from 0-1 to 0-255
    @staticmethod
    def remap_0_255(value):
        if isinstance(value, list) or isinstance(value, np.ndarray):
            return [value[0] * 255,
                    value[1] * 255,
                    value[2] * 255]

        return value * 255

    ## Clamps color to 0-1
    @staticmethod
    def clamp_color(color):
        return [LightIntensity.clamp01(color[0]),
                LightIntensity.clamp01(color[1]),
                LightIntensity.clamp01(color[2])]

    def __init__(self, color=[0, 0, 0]):
        self.color = LightIntensity.clamp_color(color)

    def __add__(self, other):
        if isinstance(other, list):
            self.color = LightIntensity.clam_color([self.color[i] + other[i] for i in range(3)])
        if isinstance(other, LightIntensity):
            self.color = LightIntensity.clam_color([self.color[i] + other.color[i] for i in range(3)])

    def __truediv__(self, other):
        if isinstance(other, list):
            self.color = LightIntensity.clam_color([self.color[i] / other[i] for i in range(3)])
        if isinstance(other, LightIntensity):
            self.color = LightIntensity.clam_color([self.color[i] / other.color[i] for i in range(3)])
