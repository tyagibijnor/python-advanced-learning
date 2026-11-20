from pathlib import Path
from collections.abc import Iterator


def file_generator(file_path: str) -> Iterator[str]:
    path = Path(file_path)
    if not path.is_absolute() and not path.exists():
        path = Path(__file__).resolve().parent / path

    with path.open("r", encoding="utf-8") as file_handler:
        for line in file_handler:
            if "ERROR" in line:
                yield line


if __name__ == "__main__":
    for line in file_generator("sample.log"):
        print(line, end="")