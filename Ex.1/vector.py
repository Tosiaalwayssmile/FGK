import math


class Vec3:

    # Methods #
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Addition #
    def __add__(self, other):
        if type(other) == type(self):  # For Vector
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        else:  # For scalar
            return Vec3(self.x + other, self.y + other, self.z + other)

    # In-place Addition #
    def __iadd__(self, other):
        if type(other) == type(self):  # For Vector
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        else:  # For scalar
            return Vec3(self.x + other, self.y + other, self.z + other)

    # Subtraction #
    def __sub__(self, other):
        if type(other) == type(self):  # For Vec3tor
            return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        else:  # For scalar
            return Vec3(self.x - other, self.y - other, self.z - other)

    # In-place Subtraction #
    def __isub__(self, other):
        if type(other) == type(self):  # For Vector
            return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        else:  # For scalar
            return Vec3(self.x - other, self.y - other, self.z - other)
    
    # Equal #
    def __eq__(self, other):
        if other is None:
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    # Absolute #
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    # Not equal #
    def __ne__(self, other):
        return not self.__eq__(other)  

    # Negation #
    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    # Positive #
    def __pos__(self):
        return Vec3(+self.x, +self.y, +self.z)

    # Print #
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'
    
    # Vector length #
    def length(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z))

    # The length of the displacement Vector (Distance between two points) #
    def distance(self, other):
        return math.sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2) + ((self.z - other.z) ** 2))

    # Is point on ray wrapper
    def is_point_on_ray(self, ray):
        return ray.is_point_on_ray(self)

    # Division #
    def __truediv__(self, other): 
        if type(other) == type(self):  # For Vector
            return Vec3(self.x / other.x, self.y / other.y, self.z / other.z)
        else: # For scalar
            return Vec3(self.x / other, self.y / other, self.z / other)

    # In-place Division #
    def __itruediv__(self, other): 
        if type(other) == type(self):  # For Vector
            return Vec3(self.x / other.x, self.y / other.y, self.z / other.z)
        else:  # For scalar
            return Vec3(self.x / other, self.y / other, self.z / other)
    
    # Dot product and multiplication #
    def __mul__(self, other): 
        if type(other) == type(self):  # For Vector
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:  # For scalar
            return Vec3(other * self.x, other * self.y, other * self.z)
            
    # In-place Dot product and multiplication #
    def __imul__(self, other): 
        if type(other) == type(self):  # For Vector
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:  # For scalar
            return Vec3(other * self.x, other * self.y, other * self.z)
    
    # Reverse multiplication #
    def __rmul__(self, other): 
        return self.__mul__(other)
    
    # Cross product #
    def cross(self, other): 
        return Vec3(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)


class Vec2:

    # Methods #
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Addition #
    def __add__(self, other):
        if type(other) == type(self):  # For Vector
            return Vec2(self.x + other.x, self.y + other.y)
        else:  # For scalar
            return Vec2(self.x + other, self.y + other)

    # In-place Addition #
    def __iadd__(self, other):
        if type(other) == type(self):  # For Vector
            return Vec2(self.x + other.x, self.y + other.y)
        else:  # For scalar
            return Vec2(self.x + other, self.y + other)

    # Subtraction #
    def __sub__(self, other):
        if type(other) == type(self):  # For Vector
            return Vec2(self.x - other.x, self.y - other.y)
        else:  # For scalar
            return Vec2(self.x - other, self.y - other)

    # In-place Subtraction #
    def __isub__(self, other):
        if type(other) == type(self):  # For Vector
            return Vec2(self.x - other.x, self.y - other.y)
        else:  # For scalar
            return Vec2(self.x - other, self.y - other)
    
    # Equal #
    def __eq__(self, other):
        if other is None:
            return False
        return self.x == other.x and self.y == other.y 
    
    # Absolute #
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    # Not equal #
    def __ne__(self, other):
        return not self.__eq__(other)  

    # Negation #
    def __neg__(self):
        return Vec2(-self.x, -self.y)

    # Positive #
    def __pos__(self):
        return Vec2(+self.x, +self.y)

    # Print #
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    
    # Vector length #
    def length(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y))

    # The length of the displacement Vector (Distance between two points) #
    def distance(self, other):
        return abs(self - other)

    # Division #
    def __truediv__(self, other): 
        if type(other) == type(self):  # For Vector
            return Vec2(self.x / other.x, self.y / other.y)
        else: # For scalar
            return Vec2(self.x / other, self.y / other)

    # In-place Division #
    def __itruediv__(self, other): 
        if type(other) == type(self):  # For Vector
            return Vec2(self.x / other.x, self.y / other.y)
        else:  # For scalar
            return Vec2(self.x / other, self.y / other)
    
    # Dot product and multiplication #
    def __mul__(self, other): 
        if type(other) == type(self):  # For Vector
            return self.x * other.x + self.y * other.y 
        else:  # For scalar
            return Vec2(other * self.x, other * self.y)
            
    # In-place Dot product and multiplication #
    def __imul__(self, other): 
        if type(other) == type(self):  # For Vector
            return self.x * other.x + self.y * other.y 
        else:  # For scalar
            return Vec2(other * self.x, other * self.y)
    
    # Reverse multiplication #
    def __rmul__(self, other): 
        return self.__mul__(other)
    