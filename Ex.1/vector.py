import math


class Vec:

    # Methods
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __ne__(self, other):
        return not self.__eq__(other)  # reuse __eq__

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'

    def length(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z))

    def distance(self, other):
        return math.sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2) + ((self.z - other.z) ** 2)) 
 
    #dot product
    def __mul__(self, other): 
        if type(other) == type(self): # for vector
             return self.x * other.x + self.y * other.y + self.z * other.z
        else: # for scalar
            return Vec(other * self.x, other * self.y, other * self.z)
    
    #k*a = (kax,kay, kaz) 
    def __rmul__(self, other): 
        return self.__mul__(other)
    
    #cross product
    def cross(self, other): 
        return Vec(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)         

    #-a = (-ax,-ay,-az)
    def __neg__(self):
        return Vec(-self.x, -self.y, -self.z)

    #+a = (ax,ay,az)   

    
