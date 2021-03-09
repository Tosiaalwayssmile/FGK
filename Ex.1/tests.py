from vector import *
from ray import *
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.v1 = Vec(1, 2, 3)
        self.v2 = Vec(4, 5, 6)
        self.v3 = Vec(0, 0, 0)
        self.v4 = Vec(1, 1, 1)
        self.v5 = Vec(-2, 5, 0)

        self.r1 = Ray()
        self.r2 = Ray(self.v1, self.v2)
        self.r3 = Ray(self.v2, self.v1)
        self.r4 = Ray(self.v4, self.v5, 10)

    # Vector tests #
    def test_add(self):
        self.assertEqual(self.v1 + self.v2, Vec(5, 7, 9))
        self.assertNotEqual(self.v1 + self.v2, Vec(5, 5, 9))

    def test_length(self):
        self.assertEqual(self.v1.length(), 3.7416573867739413)
        self.assertEqual(self.v2.length(), 8.774964387392123)

    def test_mul(self):
        self.assertEqual(self.v1 * 3, Vec(3, 6, 9))
        self.assertEqual(-3 * self.v2, Vec(-12, -15, -18))
       # self.assertEqual(self.v4 * self.v5, Vec(-2, 5, 0))

    def test_cross(self):
        #self.assertEqual(Vec.cross(self.v4, self.v5), (-5, -2, 7))
        #self.assertEqual(self.v4.cross(self.v5), (-5, -2, 7)) 

    # Ray tests #
    def test_point_on_line(self):
        self.assertEqual(self.r1.is_point_on_line(self.v1), False)
        self.assertEqual(self.r1.is_point_on_line(self.v2), False)
        self.assertEqual(self.r1.is_point_on_line(self.v3), True)

        self.assertEqual(self.r2.is_point_on_line(self.v1), True)
        self.assertEqual(self.r2.is_point_on_line(self.v2), False)
        self.assertEqual(self.r2.is_point_on_line(Vec(15, 19.5, 24)), True)
        self.assertEqual(self.r2.is_point_on_line(Vec(-3, -3, -3)), True)
        self.assertEqual(self.r2.is_point_on_line(Vec(-3, -3, -2)), False)

        self.assertEqual(self.r3.is_point_on_line(Vec(6, 9, 12)), True)
        self.assertEqual(self.r3.is_point_on_line(Vec(1, -1, -3)), True)
        self.assertEqual(self.r3.is_point_on_line(Vec(6, 9, 11)), False)
        self.assertEqual(self.r3.is_point_on_line(Vec(1, -1, -4)), False)

        self.assertEqual(self.r4.is_point_on_line(self.v1), False)
        self.assertEqual(self.r4.is_point_on_line(Vec(-2, 8.5, 1)), True)
        self.assertEqual(self.r4.is_point_on_line(Vec(-2, 8.5, 25)), False)     # Point is on line, but not in range of ray
        self.assertEqual(self.r4.is_point_on_line(Vec(3, -4, 1)), False)        # Point is on line and in range, but on the opposite side
        self.r4.length = math.inf                                               # By setting range to infinity, side is ignored
        self.assertEqual(self.r4.is_point_on_line(Vec(3, -4, 1)), True)



# print(v3.__dict__)

if __name__ == "__main__":
    unittest.main()
