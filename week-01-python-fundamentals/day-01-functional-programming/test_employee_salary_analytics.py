import unittest

from employee_salary_analytics import EMPLOYEES, analyze_salaries


class AnalyzeSalariesTests(unittest.TestCase):
    def test_builds_report_for_eligible_employees(self):
        report = analyze_salaries(EMPLOYEES)

        self.assertEqual(
            [employee["name"] for employee in report["employees"]],
            ["Amit", "Neha", "Kuhu"],
        )
        self.assertEqual(report["total_salary"], 270000)
        self.assertEqual(report["average_salary"], 90000)
        self.assertEqual(report["unique_salaries"], [78000, 96000])
        self.assertEqual(
            [employee["name"] for employee in report["highest_paid_employees"]],
            ["Neha", "Kuhu"],
        )

    def test_uses_custom_rating_threshold_and_increment(self):
        employees = [
            {"name": "Alex", "salary": 50000, "performance_rating": 3.5},
            {"name": "Blair", "salary": 60000, "performance_rating": 4.0},
        ]

        report = analyze_salaries(
            employees,
            min_rating=3.5,
            increment_rate=0.10,
        )

        self.assertEqual(
            [employee["salary"] for employee in report["employees"]],
            [55000, 66000],
        )

    def test_does_not_modify_input_employees(self):
        employees = [
            {"name": "Alex", "salary": 50000, "performance_rating": 4.0}
        ]
        original_employees = [employee.copy() for employee in employees]

        analyze_salaries(employees)

        self.assertEqual(employees, original_employees)

    def test_empty_input_returns_empty_report(self):
        report = analyze_salaries([])

        self.assertEqual(report["employees"], [])
        self.assertEqual(report["total_salary"], 0)
        self.assertEqual(report["average_salary"], 0)
        self.assertEqual(report["unique_salaries"], [])
        self.assertEqual(report["highest_paid_employees"], [])


if __name__ == "__main__":
    unittest.main()
