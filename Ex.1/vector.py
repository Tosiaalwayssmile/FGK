import math


class Vec:

    # Methods #
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Addition #
    def __add__(self, other):
        if type(other) == type(self): # For vector
            return Vec(self.x + other.x, self.y + other.y, self.z + other.z)
        else: # For scalar
            return Vec(self.x + other, self.y + other, self.z + other)

    # In-place Addition #
    def __iadd__(self, other):
        if type(other) == type(self): # For vector
            return Vec(self.x + other.x, self.y + other.y, self.z + other.z)
        else: # For scalar
            return Vec(self.x + other, self.y + other, self.z + other)

    # Subtraction #
    def __sub__(self, other):
        if type(other) == type(self): # For vector
            return Vec(self.x - other.x, self.y - other.y, self.z - other.z)
        else: # For scalar
            return Vec(self.x - other, self.y - other, self.z - other)

    # In-place Subtraction #
    def __isub__(self, other):
        if type(other) == type(self): # For vector
            return Vec(self.x - other.x, self.y - other.y, self.z - other.z)
        else: # For scalar
            return Vec(self.x - other, self.y - other, self.z - other)
    
    # Equal #
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    # Absolute #
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    # Not equal #
    def __ne__(self, other):
        return not self.__eq__(other)  

    # Negation #
    def __neg__(self):
        return Vec(-self.x, -self.y, -self.z)

    # Positive #
    def __pos__(self):
        return Vec(+self.x, +self.y, +self.z)

    # Print #
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'
    
    # Vector length #
    def length(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z))

    # The length of the displacement vector (Distance between two points) #
    def distance(self, other):
        return math.sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2) + ((self.z - other.z) ** 2)) 
 
    # Division #
    def __truediv__(self, other): 
        if type(other) == type(self): # For vector
             return Vec(self.x / other.x,self.y / other.y,self.z / other.z)
        else: # For scalar
            return Vec(self.x / other, self.y / other, self.z / other)

    # In-place Division #
    def __itruediv__(self, other): 
        if type(other) == type(self): # For vector
             return Vec(self.x / other.x,self.y / other.y,self.z / other.z)
        else: # For scalar
            return Vec(self.x / other, self.y / other, self.z / other)
    
    # Dot product and multiplication #
    def __mul__(self, other): 
        if type(other) == type(self): # For vector
             return self.x * other.x + self.y * other.y + self.z * other.z
        else: # For scalar
            return Vec(other * self.x, other * self.y, other * self.z)
            
    # In-place Dot product and multiplication #
    def __imul__(self, other): 
        if type(other) == type(self): # For vector
             return self.x * other.x + self.y * other.y + self.z * other.z
        else: # For scalar
            return Vec(other * self.x, other * self.y, other * self.z)
    
    # Reverse multiplication #
    def __rmul__(self, other): 
        return self.__mul__(other)
    
    # Cross product #
    def cross(self, other): 
        return Vec(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)         


    
