from definitions import *
import unittest


class Test(unittest.TestCase):
    # Vector addition test #
    def setUp(self):
        self.v1 = Vec(1, 2, 3)
        self.v2 = Vec(4, 5, 6)

    def test_add(self):
        self.assertEqual(self.v1 + self.v2, Vec(5, 7, 9))
        self.assertNotEqual(self.v1 + self.v2, Vec(5, 5, 9))

    def test_length(self):
        self.assertEqual(self.v1.length(), 3.7416573867739413)
        self.assertEqual(self.v2.length(), 8.774964387392123)


# print(v3.__dict__)

if __name__ == "__main__":
    unittest.main()
