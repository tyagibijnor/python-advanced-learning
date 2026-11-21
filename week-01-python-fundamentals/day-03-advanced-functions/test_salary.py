"""Unit tests for salary reporting."""

import unittest

from salary import salary_report


class SalaryTests(unittest.TestCase):
    def test_valid_salary(self):
        result = salary_report(45000, 65000, 80000, 55000)

        self.assertEqual(result["total_salary"], 245000)
        self.assertEqual(result["average_salary"], 61250)
        self.assertEqual(result["highest_salary"], 80000)

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            salary_report()

    def test_negative_salary(self):
        with self.assertRaises(ValueError):
            salary_report(-50000)

    def test_string_salary(self):
        with self.assertRaises(TypeError):
            salary_report("50000")

    def test_boolean_salary(self):
        with self.assertRaises(TypeError):
            salary_report(True)

    def test_zero_salary_is_valid(self):
        result = salary_report(0)

        self.assertEqual(result["total_salary"], 0)
        self.assertEqual(result["average_salary"], 0)
        self.assertEqual(result["highest_salary"], 0)


if __name__ == "__main__":
    unittest.main()
