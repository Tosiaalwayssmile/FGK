from abc import *


class Primitive(ABC):
    @abstractmethod
    def __init__(self, color):
        print('dziala')
        self.color = color

    @abstractmethod
    def get_intersection(self, ray):
        pass

    @abstractmethod
    def get_detailed_intersection(self, ray):
        pass
