"""Unit tests for employee bonus calculations."""

import unittest

from bonus import calculate_bonus


class BonusTests(unittest.TestCase):
    def test_valid_bonus(self):
        result = calculate_bonus(
            Amit=50000,
            Rahul=60000,
            Neha=80000,
        )

        self.assertEqual(result["total_bonus"], 19000)
        self.assertEqual(result["bonuses"]["Amit"], 5000)
        self.assertEqual(result["bonuses"]["Rahul"], 6000)
        self.assertEqual(result["bonuses"]["Neha"], 8000)

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            calculate_bonus()

    def test_negative_salary(self):
        with self.assertRaises(ValueError):
            calculate_bonus(Amit=-50000)

    def test_string_salary(self):
        with self.assertRaises(TypeError):
            calculate_bonus(Amit="50000")

    def test_boolean_salary(self):
        with self.assertRaises(TypeError):
            calculate_bonus(Amit=True)

    def test_zero_salary_is_valid(self):
        result = calculate_bonus(Amit=0)

        self.assertEqual(result["bonuses"]["Amit"], 0)
        self.assertEqual(result["total_bonus"], 0)


if __name__ == "__main__":
    unittest.main()
