from pathlib import Path
from collections.abc import Iterator


def file_generator(file_path: str | Path) -> Iterator[str]:
    path = Path(file_path)
    if not path.is_absolute():
        candidates = (
            path,
            Path(__file__).resolve().parent / path,
            Path(__file__).resolve().parent.parent / path,
        )
        path = next((candidate for candidate in candidates if candidate.exists()), candidates[-1])

    with path.open("r", encoding="utf-8") as file_handler:
        for line in file_handler:
            yield line


def file_writer(file_path,content):
    path = Path(file_path)
    if not path.is_absolute():
        candidates = (
            path,
            Path(__file__).resolve().parent / path,
            Path(__file__).resolve().parent.parent / path,
        )
        path = next((candidate for candidate in candidates if candidate.exists()), candidates[-1])
    
    with path.open("a", encoding="utf-8") as file_handler:
          file_handler.write(content+"\n")

if __name__ == "__main__":    
    for line in file_generator("employees.txt"):
        print(line, end="")
    file_writer("employees.txt","Deepak")
    for line in file_generator("employees.txt"):
            print(line, end="")
