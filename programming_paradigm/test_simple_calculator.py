class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return None
        return a / b

import unittest
from simple_calculator import SimpleCalculator  # Correct import

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    # Addition tests
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -7), -12)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6)

    # Subtraction tests
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(-5, 5), -10)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)

    # Multiplication tests
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-3, -3), 9)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0)

    # Division tests
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertEqual(self.calc.divide(-8, -2), 4)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)

    # Division by zero tests
    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(-5, 0))

if __name__ == "__main__":
    unittest.main()
