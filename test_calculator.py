import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

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
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
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