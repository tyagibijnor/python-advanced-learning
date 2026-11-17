import unittest

from bonus import calculate_bonus


class BonusTests(unittest.TestCase):

    def test_valid_bonus(self):
        result = calculate_bonus(
            Amit=50000,
            Rahul=60000,
            Neha=80000
        )

        # Check total bonus is 19000
        self.assertEqual(result["total_bonus"], 19000)
        # Check Amit's bonus is 5000
        self.assertEqual(result["bonuses"]["Amit"], 5000)

    def test_empty_input(self):
        # Check that ValueError is raised
        with self.assertRaises(ValueError):
            calculate_bonus()

    def test_negative_salary(self):
        # Check that ValueError is raised
        with self.assertRaises(ValueError):
            calculate_bonus(Amit=-50000)

    def test_string_salary(self):
        with self.assertRaises(TypeError):
            calculate_bonus(Amit="50000")


    def test_boolean_salary(self):
        with self.assertRaises(TypeError):
            calculate_bonus(Amit=True)


if __name__ == "__main__":
    unittest.main()