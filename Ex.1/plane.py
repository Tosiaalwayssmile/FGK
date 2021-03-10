class Plane:

    def __init__(self, vector_abc, d):

        if vectorABC is Vec(0, 0, 0):
            raise ValueError('Vector ABC cannot be (0, 0, 0)')

        self.vector_abc = vector_abc
        self.a = vectorABC.x
        self.b = vectorABC.y
        self.c = vectorABC.z
        self.d = d

    # def does_ray_intersects(self, ray):
