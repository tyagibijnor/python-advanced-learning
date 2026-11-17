import unittest

from salary import salary_report


class SalaryTests(unittest.TestCase):

    def test_valid_salary(self):
        result = salary_report(45000, 65000, 80000, 55000)

        # Check total salary is 245000
        self.assertEqual(result["total_salary"], 245000)
        # Check average salary is 61250
        self.assertEqual(result["average_salary"], 61250)
        # Check highest salary is 80000
        self.assertEqual(result["highest_salary"], 80000)

    def test_empty_input(self):
        # Check that ValueError is raised
        with self.assertRaises(ValueError):
            salary_report()

    def test_negative_salary(self):
        # Check that ValueError is raised
        with self.assertRaises(ValueError):
            salary_report(-50000)


if __name__ == "__main__":
    unittest.main()