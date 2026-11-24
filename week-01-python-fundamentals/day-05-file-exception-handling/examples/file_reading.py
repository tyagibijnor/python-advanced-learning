"""Read a text file one line at a time using a generator."""

from collections.abc import Iterator
from pathlib import Path


def file_generator(file_path: str | Path) -> Iterator[str]:
    with Path(file_path).open("r", encoding="utf-8") as file_handler:
        yield from file_handler


if __name__ == "__main__":
    sample_file = Path(__file__).resolve().parent.parent / "employees.txt"
    for line in file_generator(sample_file):
        print(line, end="")
