from abc import *


class Primitive(ABC):
    @abstractmethod
    def get_intersection(self, ray):
        pass
