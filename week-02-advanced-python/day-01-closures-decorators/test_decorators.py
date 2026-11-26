import unittest

from decorators import (
    calculate_bonus,
    employee_salary,
    logging_decorator,
)


class TestLoggingDecorator(unittest.TestCase):

    def test_calculate_bonus(self):
        """Test decorated function with positional and keyword arguments."""
        with self.assertLogs("decorators", level="INFO") as logs:
            result = calculate_bonus(50000, percentage=15)

        self.assertEqual(result, 7500.0)
        self.assertIn("Starting function: calculate_bonus", logs.output[0])
        self.assertIn("Function completed successfully", logs.output[1])

    def test_zero_salary(self):
        """Test decorator with zero as input."""
        with self.assertLogs("decorators", level="INFO"):
            result = calculate_bonus(0)

        self.assertEqual(result, 0)

    def test_exception_logging(self):
        """Test whether decorator logs and re-raises exceptions."""

        @logging_decorator
        def failing_function():
            raise ValueError("Something went wrong")

        with self.assertLogs("decorators", level="INFO") as logs:
            with self.assertRaises(ValueError):
                failing_function()

        self.assertIn("Function failed: failing_function", logs.output[-1])
        self.assertIn("Something went wrong", logs.output[-1])

    def test_function_metadata(self):
        """Test whether functools.wraps preserves metadata."""

        @logging_decorator
        def sample_function():
            """Sample function documentation."""
            return "Success"

        self.assertEqual(sample_function.__name__, "sample_function")
        self.assertEqual(
            sample_function.__doc__,
            "Sample function documentation.",
        )

    def test_employee_salary(self):
        """Test decorated employee salary calculation."""
        from decorators import employee_salary

        with self.assertLogs("decorators", level="INFO"):
            result = employee_salary(50000, bonus=10000)

        self.assertEqual(result, 60000)

    def test_exception_is_not_suppressed(self):
        """Ensure original exception is propagated."""

        @logging_decorator
        def failing_function():
            raise ValueError("Invalid salary")

        with self.assertLogs("decorators", level="INFO"):
            with self.assertRaisesRegex(ValueError, "Invalid salary"):
                failing_function()

    def test_negative_salary(self):
        with self.assertLogs("decorators", level="INFO"):
            with self.assertRaisesRegex(ValueError, "Salary cannot be negative"):
                calculate_bonus(-5000)

    def test_invalid_salary_type(self):
        for salary in ("50000", None, True):
            with self.subTest(salary=salary):
                with self.assertLogs("decorators", level="INFO"):
                    with self.assertRaises(TypeError):
                        calculate_bonus(salary)

    def test_invalid_percentage(self):
        for percentage in (-10, 101):
            with self.subTest(percentage=percentage):
                with self.assertLogs("decorators", level="INFO"):
                    with self.assertRaises(ValueError):
                        calculate_bonus(50000, percentage)

    def test_employee_salary_negative(self):
        with self.assertLogs("decorators", level="INFO"):
            with self.assertRaisesRegex(ValueError, "Salary cannot be negative"):
                employee_salary(-50000)

    def test_employee_salary_invalid_bonus(self):
        with self.assertLogs("decorators", level="INFO"):
            with self.assertRaisesRegex(ValueError, "Bonus cannot be negative"):
                employee_salary(50000, bonus=-1000)

    def test_employee_salary_invalid_type(self):
        with self.assertLogs("decorators", level="INFO"):
            with self.assertRaises(TypeError):
                employee_salary("50000")

    def test_employee_salary_non_finite_values(self):
        invalid_values = [float("nan"), float("inf"), float("-inf")]

        for value in invalid_values:
            with self.subTest(value=value):
                with self.assertLogs("decorators", level="INFO"):
                    with self.assertRaisesRegex(ValueError, "Salary must be finite"):
                        employee_salary(value)

    def test_employee_salary_boolean_bonus(self):
        with self.assertLogs("decorators", level="INFO"):
            with self.assertRaisesRegex(TypeError, "Bonus must be a number"):
                employee_salary(50000, bonus=True)

    def test_employee_salary_string_bonus(self):
        with self.assertLogs("decorators", level="INFO"):
            with self.assertRaisesRegex(TypeError, "Bonus must be a number"):
                employee_salary(50000, bonus="5000")

    def test_employee_salary_non_finite_bonus(self):
        with self.assertLogs("decorators", level="INFO"):
            with self.assertRaisesRegex(ValueError, "Bonus must be finite"):
                employee_salary(50000, bonus=float("inf"))


if __name__ == "__main__":
    unittest.main()
