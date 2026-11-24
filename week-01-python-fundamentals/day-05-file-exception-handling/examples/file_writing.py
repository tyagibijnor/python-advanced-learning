"""Append text to a file using pathlib."""

from pathlib import Path


def file_writer(file_path: str | Path, content: str) -> None:
    with Path(file_path).open("a", encoding="utf-8") as file_handler:
        file_handler.write(f"{content}\n")


if __name__ == "__main__":
    sample_file = Path(__file__).resolve().parent.parent / "employees-output.txt"
    file_writer(sample_file, "Example employee")
    print(f"Appended a line to {sample_file}")
