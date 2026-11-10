# https://github.com/ivylamuf/lab11-IL-FS.git
# Partner 1: Ivy
# Partner 2: Finn

import math
import unittest

from calculator import (
    add,
    subtract,
    mul,
    div,
    logarithm,
    exp,
    square_root,
    hypotenuse
)


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-2, 5), 3)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(3, 8), -5)

    def test_multiply(self):
        self.assertEqual(mul(6, 7), 42)
        self.assertEqual(mul(-3, 4), -12)

    def test_divide(self):
        self.assertEqual(div(2, 10), 5)
        self.assertAlmostEqual(div(4, 7), 1.75)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, 0)

        with self.assertRaises(ValueError):
            logarithm(2, -5)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)

        with self.assertRaises(ValueError):
            logarithm(0, 10)

        with self.assertRaises(ValueError):
            logarithm(-2, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(-5, 12), 13)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(25), 5)
        self.assertAlmostEqual(square_root(2), math.sqrt(2))

        with self.assertRaises(ValueError):
            square_root(-1)


if __name__ == "__main__":
    unittest.main()
