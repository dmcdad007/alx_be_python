import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # ----- Addition Tests -----
    def test_addition(self):
        """Test the add method with various inputs."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -7), -12)
        self.assertEqual(self.calc.add(0, 10), 10)
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6)

    # ----- Subtraction Tests -----
    def test_subtraction(self):
        """Test the subtract method with various inputs."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(0, 10), -10)
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3, places=1)

    # ----- Multiplication Tests -----
    def test_multiplication(self):
        """Test the multiply method with various inputs."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertAlmostEqual(self.calc.multiply(2.5, 4.0), 10.0)

    # ----- Division Tests -----
    def test_division(self):
        """Test the divide method with various inputs."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertIsNone(self.calc.divide(10, 0))  # Division by zero should return None

    # ----- Edge Case Tests -----
    def test_edge_cases(self):
        """Additional edge cases for robustness."""
        self.assertEqual(self.calc.add(1e10, 1e10), 2e10)
        self.assertEqual(self.calc.subtract(1e-5, 1e-5), 0)
        self.assertAlmostEqual(self.calc.multiply(1.5, 0), 0)
        self.assertIsNone(self.calc.divide(0, 0))  # 0 divided by 0 should return None

if __name__ == "__main__":
    unittest.main()
