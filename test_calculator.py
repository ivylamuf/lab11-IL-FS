# https://github.com/ivylamuf/lab11-IL-FS.git
# Partner 1: Ivy
# Partner 2: FInn
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(2, 2), 4)
        self.assertEqual(add(1, 5), 6)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(2, 8), 6)
        self.assertEqual(subtract(1, 10), 9)
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(-2, 4), -8)

    def test_divide(self):
        self.assertEqual(divide(2, 8), 4)
        self.assertEqual(divide(1, 10), 10)
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        self.assertEqual(divide(0, 0), 0)
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(3, 81), 4)
        self.assertEqual(logarithm(2, 32), 5)
        with self.assertRaises(ZeroDivisionError):
            logarithm(0, 5)

    def test_log_invalid_base(self): # 1 assertion
        self.assertEqual(logarithm(2, 8), 3)
        with self.assertRaises(ValueError):
            logarithm(-3, 8)
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5.0)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-1)

        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(0), 0)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()