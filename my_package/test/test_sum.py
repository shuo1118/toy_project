import unittest
from my_package.sum import sum_numbers

class TestSum(unittest.TestCase):
    def test_sum_numbers(self):
        self.assertEqual(sum_numbers([1, 2, 3]), 6)
        self.assertEqual(sum_numbers([-1, 1]), 0)
        self.assertEqual(sum_numbers([2]*10), 20)

if __name__ == '__main__':
    unittest.main()
