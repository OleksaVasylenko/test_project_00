import unittest
from parameterized import parameterized
from task_02 import handle_string


data = (
    ("Hello world! 123!", 'Letters - 10\nDigits - 3'),
    ("00123", 'Letters - 0\nDigits - 5'),
    ("'example'", 'Letters - 7\nDigits - 0'),
    ('', 'Letters - 0\nDigits - 0')
)


class TestHandleString(unittest.TestCase):
    @parameterized.expand(data)
    def test(self, string, expected):
        result = handle_string(string)
        self.assertEqual(result, expected)
