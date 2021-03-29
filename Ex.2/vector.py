import math


## Documentation for a class Vec3.
class Vec3:

    ## The constructor.
    def __init__(self, x = 0, y = 0, z = 0):

        ## A class variable. Coordinate x of a given vector.
        self.x = x
        ## A class variable. Coordinate y of a given vector.
        self.y = y
        ## A class variable. Coordinate z of a given vector.
        self.z = z

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, inp):
        self._x = inp
    @x.deleter
    def x(self):
        del self._x
    ## Alias    
    r = x

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, inp):
        self._y = inp
    @y.deleter
    def y(self):
        del self._y
    ## Alias 
    g = y

    @property
    def z(self):
        return self._z
    @z.setter
    def z(self, inp):
        self._z = inp
    @z.deleter
    def z(self):
        del self._z
    ## Alias 
    b = z

    ## Function returning sum of two vectors or sum of a vector and a scalar.
    def __add__(self, other):
        if type(other) == type(self):  # For Vector
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        else:  # For scalar
            return Vec3(self.x + other, self.y + other, self.z + other)

    ## Function returning sum (In-place addition) of two vectors or sum of a vector and a scalar.
    def __iadd__(self, other):
        if type(other) == type(self):  # For Vector
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        else:  # For scalar
            return Vec3(self.x + other, self.y + other, self.z + other)

    ## Function returning difference of two vectors or difference of a vector and a scalar.
    def __sub__(self, other):
        if type(other) == type(self):  # For Vec3tor
            return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        else:  # For scalar
            return Vec3(self.x - other, self.y - other, self.z - other)

    ## Function returning difference (In-place Subtraction) of two vectors or difference of a vector and a scalar.
    def __isub__(self, other):
        if type(other) == type(self):  # For Vector
            return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        else:  # For scalar
            return Vec3(self.x - other, self.y - other, self.z - other)
    
    ## Function "equal".
    def __eq__(self, other):
        if other is None:
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    ## Function returning absolute value of a given vector.
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    ## Function "not equal".
    def __ne__(self, other):
        return not self.__eq__(other)  

    ## Function negating vector coordinates.
    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    ## Function for positive vector coordinates.
    def __pos__(self):
        return Vec3(+self.x, +self.y, +self.z)

    ## Function returning object values in string format.
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'
    
    ## Function returning vector length.
    def length(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z))

    ## Function returning the length of the displacement vector (distance between two points).
    def distance(self, other):
        return math.sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2) + ((self.z - other.z) ** 2))

    ## Is point on ray wrapper
    def is_point_on_ray(self, ray):
        return ray.is_point_on_ray(self)


    ## Function returning quotient of two vectors or quotient of a vector and a scalar. 
    def __truediv__(self, other): 
        if type(other) == type(self):  # For Vector
            return Vec3(self.x / other.x, self.y / other.y, self.z / other.z)
        else: # For scalar
            return Vec3(self.x / other, self.y / other, self.z / other)

    ## Function returning quotient (In-place Division) of two vectors or quotient of a vector and a scalar. 
    def __itruediv__(self, other): 
        if type(other) == type(self):  # For Vector
            return Vec3(self.x / other.x, self.y / other.y, self.z / other.z)
        else:  # For scalar
            return Vec3(self.x / other, self.y / other, self.z / other)
    
    ## Function returning dot product of two vectors or dot product of a vector and a scalar. 
    def __mul__(self, other): 
        if type(other) == type(self):  # For Vector
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:  # For scalar
            return Vec3(other * self.x, other * self.y, other * self.z)
            
    ## Function returning dot product (In-place multiplication) of two vectors or dot product of a vector and a scalar. 
    def __imul__(self, other): 
        if type(other) == type(self):  # For Vector
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:  # For scalar
            return Vec3(other * self.x, other * self.y, other * self.z)
    
    ## Function returning dot product (Reverse multiplication). 
    def __rmul__(self, other): 
        return self.__mul__(other)
    
    ## Function returning cross product of two vectors.
    def cross(self, other): 
        return Vec3(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)

## Documentation for a class Vec2.
class Vec2:

    ## The constructor.
    def __init__(self, x, y):

        ## A class variable. Coordinate x of a given vector.
        self.x = x
        ## A class variable. Coordinate y of a given vector.
        self.y = y

    ## Function returning sum of two vectors or sum of a vector and a scalar.
    def __add__(self, other):
        if type(other) == type(self):  # For Vector
            return Vec2(self.x + other.x, self.y + other.y)
        else:  # For scalar
            return Vec2(self.x + other, self.y + other)

    ## Function returning sum (In-place addition) of two vectors or sum of a vector and a scalar.
    def __iadd__(self, other):
        if type(other) == type(self):  # For Vector
            return Vec2(self.x + other.x, self.y + other.y)
        else:  # For scalar
            return Vec2(self.x + other, self.y + other)

    ## Function returning difference of two vectors or difference of a vector and a scalar.
    def __sub__(self, other):
        if type(other) == type(self):  # For Vector
            return Vec2(self.x - other.x, self.y - other.y)
        else:  # For scalar
            return Vec2(self.x - other, self.y - other)

    ## Function returning difference (In-place Subtraction) of two vectors or difference of a vector and a scalar.
    def __isub__(self, other):
        if type(other) == type(self):  # For Vector
            return Vec2(self.x - other.x, self.y - other.y)
        else:  # For scalar
            return Vec2(self.x - other, self.y - other)
    
    ## Function "equal".
    def __eq__(self, other):
        if other is None:
            return False
        return self.x == other.x and self.y == other.y 
    
    ## Function returning absolute value of a given vector.
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    ## Function "not equal".
    def __ne__(self, other):
        return not self.__eq__(other)  

    ## Function negating vector coordinates.
    def __neg__(self):
        return Vec2(-self.x, -self.y)

    ## Function for positive vector coordinates.
    def __pos__(self):
        return Vec2(+self.x, +self.y)

    ## Function returning object values in string format.
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    
    ## Function returning vector length.
    def length(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y))

    ## Function returning the length of the displacement vector (distance between two points).
    def distance(self, other):
        return abs(self - other)

    ## Function returning quotient of two vectors or quotient of a vector and a scalar. 
    def __truediv__(self, other): 
        if type(other) == type(self):  # For Vector
            return Vec2(self.x / other.x, self.y / other.y)
        else: # For scalar
            return Vec2(self.x / other, self.y / other)

    ## Function returning quotient (In-place Division) of two vectors or quotient of a vector and a scalar.
    def __itruediv__(self, other): 
        if type(other) == type(self):  # For Vector
            return Vec2(self.x / other.x, self.y / other.y)
        else:  # For scalar
            return Vec2(self.x / other, self.y / other)
    
    ## Function returning dot product of two vectors or dot product of a vector and a scalar. 
    def __mul__(self, other): 
        if type(other) == type(self):  # For Vector
            return self.x * other.x + self.y * other.y 
        else:  # For scalar
            return Vec2(other * self.x, other * self.y)
            
    ## Function returning dot product (In-place multiplication) of two vectors or dot product of a vector and a scalar. 
    def __imul__(self, other): 
        if type(other) == type(self):  # For Vector
            return self.x * other.x + self.y * other.y 
        else:  # For scalar
            return Vec2(other * self.x, other * self.y)
    
    ## Function returning cross product of two vectors.
    def __rmul__(self, other): 
        return self.__mul__(other)
    