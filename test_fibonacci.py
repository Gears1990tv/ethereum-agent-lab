
import unittest

from fibonacci import fibonacci


class TestFibonacci(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(fibonacci(0), 0)

    def test_one(self):
        self.assertEqual(fibonacci(1), 1)

    def test_sequence(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        for n, result in enumerate(expected):
            with self.subTest(n=n):
                self.assertEqual(fibonacci(n), result)

    def test_negative(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_non_integer(self):
        with self.assertRaises(ValueError):
            fibonacci("10")

    def test_float(self):
        with self.assertRaises(ValueError):
            fibonacci(3.5)


if __name__ == "__main__":
    unittest.main()
