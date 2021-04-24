from abc import *


class Primitive(ABC):
    @abstractmethod
    def get_intersection(self, ray):
        pass

    @abstractmethod
    def get_detailed_intersection(self, ray):
        pass
