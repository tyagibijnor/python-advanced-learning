"""Unit tests for generator functions."""

import unittest

from generators import employee_generator, even_number, gen_number


class GeneratorTests(unittest.TestCase):
    def test_gen_number(self):
        self.assertEqual(list(gen_number()), list(range(1, 11)))

    def test_even_number(self):
        result = list(even_number())

        self.assertEqual(result, list(range(2, 51, 2)))

    def test_employee_generator_filters_and_yields_tuples(self):
        employees = [
            {"id": 101, "name": "Amit"},
            {"id": 102, "name": "Rahul"},
            {"id": 103, "name": "Neha"},
        ]

        self.assertEqual(
            list(employee_generator(employees)),
            [(102, "Rahul"), (103, "Neha")],
        )

    def test_employee_generator_empty_input(self):
        self.assertEqual(list(employee_generator([])), [])


if __name__ == "__main__":
    unittest.main()
