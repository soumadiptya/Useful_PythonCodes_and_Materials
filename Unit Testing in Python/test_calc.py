import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        # Generally multiple test cases are added
        self.assertEqual(calc.add(-1, 5), 4)
        self.assertEqual(calc.add(-22, -32), -54)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 5), -6)
        self.assertEqual(calc.subtract(-22, -32), 10)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 5), -5)
        self.assertEqual(calc.multiply(-22, -1), 22)
        self.assertEqual(round(calc.multiply(2.2, 3.2), 2), 7.04)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-5, 5), -1)
        self.assertEqual(calc.divide(-22, -1), 22)
        self.assertEqual(round(calc.divide(2.2, 1), 2), 2.2)

        # Testing division by 0- testing using an exception
        self.assertRaises(ZeroDivisionError, calc.divide, 1, 0)

        # With a context manager
        with self.assertRaises(ZeroDivisionError):
            calc.divide(1, 0)


# Unittests can be run in two ways:
# 1) From Console- python -m unittest test_calc.py
# 2) From editor- unittest.main()

if __name__ == "__main__":
    unittest.main()
