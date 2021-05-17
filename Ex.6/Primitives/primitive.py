from abc import *


class Primitive(ABC):
    @abstractmethod
    def __init__(self, color, material=None):
        self.color = color
        self.material = material

    @abstractmethod
    def get_intersection(self, ray):
        pass

    @abstractmethod
    def get_detailed_intersection(self, ray):
        pass

    @abstractmethod
    def get_detailed_intersections(self, ray):
        pass

    @abstractmethod
    def get_normal(self, point):
        pass

    @abstractmethod
    def get_texture_color(self):
        pass
