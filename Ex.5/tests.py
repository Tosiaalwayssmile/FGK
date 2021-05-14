import unittest

from Lights.light_intensity import *
from Primitives.plane import *
from Primitives.sphere import *


## Documentation for a class Test. Unit tests.
class Test(unittest.TestCase):
    def setUp(self):
        self.v1 = Vec3(1, 2, 3)
        self.v2 = Vec3(4, 5, 6)
        self.v3 = Vec3(0, 0, 0)
        self.v4 = Vec3(1, 1, 1)
        self.v5 = Vec3(-2, 5, 0)

        self.v6 = Vec2(1, 1)
        self.v7 = Vec2(-2, 5)

        self.r1 = Ray()
        self.r2 = Ray(self.v1, self.v2)
        self.r3 = Ray(self.v2, self.v1)
        self.r4 = Ray(self.v4, self.v5, 10)

        self.p1 = Plane(self.v1, 3)
        self.p2 = Plane(self.v5, -5)

        self.s1 = Sphere(self.v1, 12)
        self.s2 = Sphere(self.v2, 20.5)

        self.li1 = LightIntensity(0.3, 0.5, 1)
        self.li2 = LightIntensity(0.1, 1, 1)
    
    ## Vector tests 
    def test_add(self):
        self.assertEqual(self.v1 + self.v2, Vec3(5, 7, 9))       # Add two vectors
        self.assertEqual(self.v1 + 3, Vec3(4, 5, 6))             # Add vector and scalar
        self.assertNotEqual(self.v1 + self.v2, Vec3(5, 5, 9))
        self.v2 += 2
        self.assertEqual(self.v2,  Vec3(6, 7, 8))                # Subtract scalar from vector  (in-place)
        # Vec2 #
        self.assertEqual(self.v6 + self.v7, Vec2(-1, 6)) 
        self.assertEqual(self.v6 + 2, Vec2(3, 3)) 

    ## Vector tests 
    def test_sub(self):
        self.assertEqual(self.v1 - self.v2, Vec3(-3, -3, -3))    # Subtracts two vectors
        self.assertEqual(self.v2 - 3.5, Vec3(0.5, 1.5, 2.5))     # Subtract scalar from vector
        self.v2 -= 3.5
        self.assertEqual(self.v2, Vec3(0.5, 1.5, 2.5))           # Subtract scalar from vector (in-place)
        # Vec2 #
        self.assertEqual(self.v6 - self.v7, Vec2(3, -4))         

    ## Vector tests 
    def test_pos(self):
        self.assertEqual(+self.v5, Vec3(-2, 5, 0))

    ## Vector tests 
    def test_neg(self):
        self.assertEqual(-self.v5, Vec3(2, -5, 0))

    ## Vector tests 
    def test_length(self):
        self.assertEqual(self.v1.length(), 3.7416573867739413)
        self.assertEqual(self.v2.length(), 8.774964387392123)

    ## Vector tests 
    def test___truediv__(self):
        self.assertEqual(self.v1 / self.v2, Vec3(1/4, 2/5, 3/6))     # Divide vector by vector
        self.assertEqual(self.v2 / -2, Vec3(-2, -5/2, -3))           # Divide vector by scalar
        self.v2 /= -2      
        self.assertEqual(self.v2, Vec3(-2, -5/2, -3))                # Divide vector by scalar (in-place)

    ## Vector tests 
    def test_mul(self):
        self.assertEqual(self.v1 * self.v2, 32)                     # Multiply vector by vector
        self.assertEqual(self.v2 * 3, Vec3(12, 15, 18))              # Multiply vector by scalar
        self.assertEqual(-3 * self.v2, Vec3(-12, -15, -18))          # Multiply scalar by vector
        self.v2 *= -3  
        self.assertEqual(self.v2, Vec3(-12, -15, -18))               # Multiply scalar by vector (in-place)

    ## Vector tests 
    def test_cross(self):
        self.assertEqual(Vec3.cross(self.v5, self.v2), Vec3(30, 12, -30))
        self.assertEqual(Vec3.cross(self.v4, self.v5), Vec3(-5, -2, 7))

    ## Ray tests 
    def test_point_on_line(self):
        self.assertEqual(self.r1.is_point_on_ray(self.v1), False)
        self.assertEqual(self.r1.is_point_on_ray(self.v2), False)
        self.assertEqual(self.r1.is_point_on_ray(self.v3), True)

        self.assertEqual(self.r2.is_point_on_ray(self.v1), True)
        self.assertEqual(self.r2.is_point_on_ray(self.v2), False)
        self.assertEqual(self.r2.is_point_on_ray(Vec3(15, 19.5, 24)), True)
        self.assertEqual(self.r2.is_point_on_ray(Vec3(-3, -3, -3)), False)       # Point is on line, but before origin point

        self.assertEqual(self.r3.is_point_on_ray(Vec3(6, 9, 12)), True)
        self.assertEqual(self.r3.is_point_on_ray(Vec3(1, -1, -3)), False)
        self.assertEqual(self.r3.is_point_on_ray(Vec3(6, 9, 11)), False)

        self.assertEqual(self.r4.is_point_on_ray(self.v1), False)
        self.assertEqual(self.r4.is_point_on_ray(Vec3(-2, 8.5, 1)), True)
        self.assertEqual(self.r4.is_point_on_ray(Vec3(-2, 8.5, 25)), False)     # Point is on line, but not in range of ray
        self.assertEqual(self.r4.is_point_on_ray(Vec3(3, -4, 1)), False)        # Point is on line, but before origin point

    ## Plane tests
    def test_plane_intersection(self):
        self.assertEqual(self.p1.get_intersection(self.r2), None)               # Point on line, bot before origin
        self.assertEqual(self.p1.get_intersection(self.r3), None)
        self.assertNotEqual(self.p1.get_intersection(self.r2), Vec3(-1.126, -0.65625, -0.1875))
        self.assertEqual(self.p1.get_intersection(Ray(self.v1, Vec3(0, 3, -2))), None)

        self.assertEqual(self.p2.get_intersection(self.r2), None)
        self.assertEqual(self.p2.get_intersection(self.r4), Vec3(0.86207, 1.34483, 1))
        self.assertNotEqual(self.p2.get_intersection(self.r4), Vec3(1, 1, 1))
    
    ## Sphere tests 
    def test_get_centre(self):
        self.assertEqual(self.s1.centre, Vec3(1, 2, 3))

    ## Sphere tests 
    def test_get_radius(self):
        self.assertEqual(self.s2.radius, 20.5)

    ## Sphere tests 
    def test_surface_area(self):
        self.assertEqual(self.s1.area, 1808.64)
    
    ## Sphere tests 
    def test_get_volume(self):
        self.assertEqual(self.s1.volume, 7234.56)
    
    ## Sphere tests 
    def test_get_sphere_intersection(self):
        self.assertEqual(self.s1.get_ray_intersections(self.r2)[0][0], Vec3(6.47011, 8.83763, 11.20516))
        self.assertEqual(self.s2.get_ray_intersections(self.r3)[0][0], Vec3(9.47886, 15.95771, 22.43657))

    ## Light intensity tests 
    def test_clamp_0_255(self):
        self.assertEqual(LightIntensity.clamp_0_255(self.li1), Vec3(76, 128, 255))
        self.li3 = self.li1 + self.li2
        self.assertEqual(LightIntensity.clamp_0_1(self.li3), Vec3(0.4, 1, 1))


if __name__ == "__main__":
    unittest.main()
