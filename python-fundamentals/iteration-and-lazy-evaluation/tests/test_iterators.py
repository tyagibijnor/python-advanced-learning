"""Unit tests for basic iterator behavior."""
import io
import sys
import unittest
from pathlib import Path
from contextlib import redirect_stdout

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from examples.iterators import basic_iter


class IteratorTests(unittest.TestCase):
    def test_basic_iter_prints_each_item(self):
        output = io.StringIO()

        with redirect_stdout(output):
            basic_iter(["Navneet", "Amit", "Neha"])

        self.assertEqual(output.getvalue(), "Navneet\nAmit\nNeha\n")

    def test_basic_iter_empty_sequence(self):
        output = io.StringIO()

        with redirect_stdout(output):
            basic_iter([])

        self.assertEqual(output.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
