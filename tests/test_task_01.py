import unittest
from parameterized import parameterized
from task_01 import handle_numbers

data = (
    (1, 10, 2, '5, because 2, 4, 6, 8, 10 are divisible by 2'),
    (10, 1, 2, '5, because 2, 4, 6, 8, 10 are divisible by 2'),
    (10, 1, 2, '5, because 2, 4, 6, 8, 10 are divisible by 2'),
    (2, 2, 2, '1, because 2 is divisible by 2'),
    (-10, 2, 2, '7, because -10, -8, -6, -4, -2, 0, 2 are divisible by 2'),
    (1, 10, 0, '0, because no numbers are divisible by 0'),
    (-3, 10, 3, '5, because -3, 0, 3, 6, 9 are divisible by 3'),
    (1, 15, 100, '0, because none in given range is divisible by 100')
)


class TestHandleNumbers(unittest.TestCase):
    @parameterized.expand(data)
    def test(self, start, end, div, expected):
        result = handle_numbers(start, end, div)
        self.assertEqual(result, expected)
