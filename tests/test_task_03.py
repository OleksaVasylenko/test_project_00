import unittest
from parameterized import parameterized
from task_03 import handle_list_of_tuples

data = (
    (
        [
            ("Tom", "19", "167", "54"),
            ("Jony", "24", "180", "69"),
            ("Json", "21", "185", "75"),
            ("John", "27", "190", "87"),
            ("Jony", "24", "191", "98"),
        ],
        [
            ("John", "27", "190", "87"),
            ("Jony", "24", "191", "98"),
            ("Jony", "24", "180", "69"),
            ("Json", "21", "185", "75"),
            ("Tom", "19", "167", "54"),
        ]
    ),
    (
        [
            ("Tom", "19", "167", "54"),
            ("Jony", "34", "191", "69"),
            ("Json", "21", "185", "75"),
            ("John", "27", "190", "87"),
            ("Jony", "24", "191", "98"),
        ],
        [
            ("John", "27", "190", "87"),
            ("Jony", "34", "191", "69"),
            ("Jony", "24", "191", "98"),
            ("Json", "21", "185", "75"),
            ("Tom", "19", "167", "54"),
        ]
    ),
)


class TestHadleListOfTuples(unittest.TestCase):
    @parameterized.expand(data)
    def test(self, list_of_tuples, expected):
        result = handle_list_of_tuples(list_of_tuples)
        self.assertEqual(result, expected)
