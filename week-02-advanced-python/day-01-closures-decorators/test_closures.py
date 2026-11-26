import unittest

from closures import make_counter, make_multiplier


class TestClosures(unittest.TestCase):

    def test_make_multiplier(self):
        double = make_multiplier(2)
        triple = make_multiplier(3)

        self.assertEqual(double(10), 20)
        self.assertEqual(triple(10), 30)

    def test_multiplier_independence(self):
        double = make_multiplier(2)
        triple = make_multiplier(3)

        self.assertEqual(double(5), 10)
        self.assertEqual(triple(5), 15)

    def test_make_counter(self):
        counter = make_counter()

        self.assertEqual(counter(), 1)
        self.assertEqual(counter(), 2)
        self.assertEqual(counter(), 3)

    def test_counter_independence(self):
        counter_one = make_counter()
        counter_two = make_counter()

        self.assertEqual(counter_one(), 1)
        self.assertEqual(counter_one(), 2)
        self.assertEqual(counter_two(), 1)


if __name__ == "__main__":
    unittest.main()
