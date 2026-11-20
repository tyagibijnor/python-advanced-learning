
"""Unit tests for generator functions."""

import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
import io
from contextlib import redirect_stdout

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from examples.generators import employee_generator, even_number, gen_number
from practical.file_generator import file_generator


class TestGenerators(unittest.TestCase):

    def test_gen_number(self):
        self.assertEqual(list(gen_number()), list(range(1, 11)))

    def test_even_number(self):
        self.assertEqual(list(even_number()), list(range(2, 51, 2)))

    def test_employee_generator_filters_and_yields_tuples(self):
        employees = [
            {"id": 101, "name": "Amit"},
            {"id": 102, "name": "Rahul"},
            {"id": 103, "name": "Neha"},
        ]

        expected = [(102, "Rahul"), (103, "Neha")]

        self.assertEqual(list(employee_generator(employees)), expected)

    def test_employee_generator_empty_input(self):
        self.assertEqual(list(employee_generator([])), [])

    def test_employee_generator_exhaustion(self):
        employees = [{"id": 102, "name": "Rahul"}]
        generator = employee_generator(employees)

        self.assertEqual(next(generator), (102, "Rahul"))

        with self.assertRaises(StopIteration):
            next(generator)

    def test_file_generator(self):
        with TemporaryDirectory() as temp_dir:
            log_file = Path(temp_dir) / "sample.log"

            log_file.write_text(
                "INFO: Application started\n"
                "ERROR: Database connection failed\n"
                "WARNING: High memory usage\n"
                "ERROR: API request failed\n",
                encoding="utf-8",
            )

            expected = [
                "ERROR: Database connection failed\n",
                "ERROR: API request failed\n",
            ]

            self.assertEqual(
                list(file_generator(str(log_file))),
                expected,
            )

    def test_file_generator_without_errors(self):
        with TemporaryDirectory() as temp_dir:
            log_file = Path(temp_dir) / "info.log"
            log_file.write_text(
                "INFO: Application started\n",
                encoding="utf-8",
            )

            self.assertEqual(list(file_generator(str(log_file))), [])

    def test_file_generator_empty_file(self):
        with TemporaryDirectory() as temp_dir:
            log_file = Path(temp_dir) / "empty.log"
            log_file.write_text("", encoding="utf-8")

            self.assertEqual(list(file_generator(str(log_file))), [])

    def test_file_generator_missing_file(self):
        with TemporaryDirectory() as temp_dir:
            missing_file = Path(temp_dir) / "missing.log"

            with self.assertRaises(FileNotFoundError):
                list(file_generator(str(missing_file)))


if __name__ == "__main__":
    unittest.main()
