import unittest
from demo.calc import Calculator

class TestOperations(unittest.TestCase):
    def test_sum(self):
        calculator = Calculator(8, 2)
        self.assertEqual(calculator.get_sum(), 10, "The answer was not 10.")

    def test_diff(self):
        calculator = Calculator(10, 20)
        self.assertEqual(calculator.get_diff(), -10, "The answer was not -10.")

if __name__ == "__main__":
    unittest.main()